from .exceptions import ImproperlyConfigured


SANDBOX_HOST = 'api.development.push.apple.com:443'
PRODUCTION_HOST = 'api.push.apple.com:443'


class BaseClient(object):

    def __init__(self, bundle_id, use_sandbox, force_proto):
        self.bundle_id = bundle_id
        self.force_proto = force_proto
        self.host = SANDBOX_HOST if use_sandbox else PRODUCTION_HOST


class APNsClient(BaseClient):

    def __init__(self, team_id, auth_key_id, auth_key_filepath, bundle_id, use_sandbox=False, force_proto=None):

        if not auth_key_filepath:
            raise ImproperlyConfigured(
                'You must provide a path to a file containing the auth key'
            )

        try:
            with open(auth_key_filepath, 'r') as f:
                auth_key = f.read()
        except Exception as e:
            raise ImproperlyConfigured(
                'The APNS auth key file at %r is not readable: %s' % (auth_key_filepath, e)
            )

        self.team_id = team_id
        self.auth_key_id = auth_key_id
        self.auth_key = auth_key
        super(APNsClient, self).__init__(bundle_id, use_sandbox, force_proto)


class VoIPClient(BaseClient):

    def __init__(self, auth_key_filepath, bundle_id, use_sandbox=False, force_proto=None):
        super(VoIPClient, self).__init__(bundle_id, use_sandbox, force_proto)
