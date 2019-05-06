from contextlib import closing
from hyper import HTTP20Connection
from .exceptions import ImproperlyConfigured, PayloadTooLarge

import json
import jwt
import ssl
import time
import uuid


SANDBOX_HOST = 'api.development.push.apple.com:443'
PRODUCTION_HOST = 'api.push.apple.com:443'


class BaseClient(object):

    max_notification_size = 4 * 1024  # 4096 bytes

    def __init__(self, auth_key_filepath, bundle_id, use_sandbox, force_proto):
        if not auth_key_filepath:
            raise ImproperlyConfigured(
                'You must provide a path to a file containing the auth key'
            )

        self.auth_key = self._create_auth_key(auth_key_filepath)
        self.bundle_id = bundle_id
        self.force_proto = force_proto
        self.host = SANDBOX_HOST if use_sandbox else PRODUCTION_HOST

    def send_message(self, registration_id, alert, **kwargs):
        return self._send_message(registration_id, alert, **kwargs)

    def _send_message(self, registration_id, alert, identifier=None, expiration=None, priority=10,
                      connection=None, auth_token=None, bundle_id=None, topic=None):
        if not (topic or bundle_id or self.bundle_id):
            raise ImproperlyConfigured(
                'You must provide your bundle_id if you do not specify a topic'
            )

        # FIXME: APNS Support
        obj = alert if isinstance(alert, dict) else {}
        json_data = json.dumps(obj, separators=(',', ':'), sort_keys=True).encode('utf-8')

        if len(json_data) > self.max_notification_size:
            raise PayloadTooLarge(f'Notification body cannot exceed {self.max_notification_size} bytes')

        expiration_time = expiration if expiration is not None else int(time.time()) + 2592000

        if not topic:
            topic = bundle_id if bundle_id else self.bundle_id

        headers = {
            'apns-expiration': str(expiration_time),
            'apns-priority': str(priority),
            'apns-topic': topic
        }

        auth_token = auth_token or self._create_token()
        if auth_token:
            headers['authorization'] = f'bearer {auth_token}'

        if not identifier:
            identifier = uuid.uuid4()
        headers['apns-id'] = str(identifier)

        if connection:
            self._send_notification_request(connection, registration_id, json_data, headers)
        else:
            with closing(self._create_connection()) as connection:
                self._send_notification_request(connection, registration_id, json_data, headers)

    def _send_notification_request(self, connection, registration_id, body, headers):
        connection.request(
            'POST', f'/3/device/{registration_id}', body, headers
        )
        response = connection.get_response()

    def _create_auth_key(self, auth_key_filepath):
        raise NotImplementedError()

    def _create_token(self):
        raise NotImplementedError()

    def _create_connection(self):
        raise NotImplementedError()


class APNsClient(BaseClient):

    def __init__(self, team_id, auth_key_id, auth_key_filepath, bundle_id, use_sandbox=False, force_proto=None):
        self.team_id = team_id
        self.auth_key_id = auth_key_id
        super().__init__(auth_key_filepath, bundle_id, use_sandbox, force_proto)

    def _create_auth_key(self, auth_key_filepath):
        try:
            with open(auth_key_filepath, 'r') as f:
                auth_key = f.read()
        except Exception as e:
            raise ImproperlyConfigured(
                'The APNS auth key file at %r is not readable: %s' % (auth_key_filepath, e)
            )
        return auth_key

    def _create_token(self):
        token = jwt.encode(
            {
                'iss': self.team_id,
                'iat': time.time()
            },
            self.auth_key,
            algorithm='ES256',
            headers={
                'alg': 'ES256',
                'kid': self.auth_key_id,
            }
        )
        return token.decode('ascii')

    def _create_connection(self):
        return HTTP20Connection(self.host, force_proto=self.force_proto)


class VoIPClient(BaseClient):

    max_notification_size = 5 * 1024  # 5120 bytes

    def __init__(self, auth_key_filepath, bundle_id, use_sandbox=False, force_proto='h2'):
        if not bundle_id.endswith('.voip'):
            bundle_id += '.voip'
        super().__init__(auth_key_filepath, bundle_id, use_sandbox, force_proto)

    def _create_auth_key(self, auth_key_filepath):
        # TODO: Validate X509
        return auth_key_filepath

    def _create_token(self):
        return None

    def _create_connection(self):
        ssl_context = ssl.create_default_context()
        ssl_context.load_cert_chain(self.auth_key)
        return HTTP20Connection(self.host, ssl_context=ssl_context, force_proto=self.force_proto)
