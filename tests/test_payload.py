from kalyke.payload import PayloadAlert, Payload
from unittest import TestCase


class TestPayloadAlert(TestCase):

    def test_representation(self):
        alert = PayloadAlert(
            title='this is title', title_localized_key='title_key', title_localized_args='title_args',
            subtitle='this is subtitle', subtitle_loc_key='subtitle_key', subtitle_loc_args='subtitle_args',
            body='this is body', body_localized_key='body_key', body_localized_args='body_args',
            action_localized_key='action_key', action='this is action', launch_image='launch_image.png'
        )
        result = alert.dict()

        self.assertEqual(result['title'], 'this is title')
        self.assertEqual(result['title-loc-key'], 'title_key')
        self.assertEqual(result['title-loc-args'], 'title_args')

        self.assertEqual(result['subtitle'], 'this is subtitle')
        self.assertEqual(result['subtitle-loc-key'], 'subtitle_key')
        self.assertEqual(result['subtitle-loc-args'], 'subtitle_args')

        self.assertEqual(result['body'], 'this is body')
        self.assertEqual(result['loc-key'], 'body_key')
        self.assertEqual(result['loc-args'], 'body_args')

        self.assertEqual(result['action-loc-key'], 'action_key')
        self.assertEqual(result['action'], 'this is action')

        self.assertEqual(result['launch-image'], 'launch_image.png')


class TestPayload(TestCase):

    def test_representation(self):
        payload = Payload(alert='this is alert', badge=1, sound='default')
        result = payload.dict()

        self.assertEqual(result['aps']['alert'], 'this is alert')
        self.assertEqual(result['aps']['badge'], 1)
        self.assertEqual(result['aps']['sound'], 'default')

    def test_representation_with_payload_alert(self):
        alert = PayloadAlert(title='this is title', body='this is body')
        custom = {'custom_key': 'custom value'}
        payload = Payload(
            alert=alert, badge=1, sound='default', content_available=True, mutable_content=True,
            thread_id='this_is_thread_identifier', category='notification_category', url_args='url_arguments',
            custom=custom
        )
        result = payload.dict()

        self.assertEqual(result['aps']['alert']['title'], 'this is title')
        self.assertEqual(result['aps']['alert']['body'], 'this is body')
        self.assertEqual(result['aps']['badge'], 1)
        self.assertEqual(result['aps']['sound'], 'default')
        self.assertEqual(result['aps']['content-available'], 1)
        self.assertEqual(result['aps']['mutable-content'], 1)
        self.assertEqual(result['aps']['thread-id'], 'this_is_thread_identifier')
        self.assertEqual(result['aps']['category'], 'notification_category')
        self.assertEqual(result['aps']['url-args'], 'url_arguments')
        self.assertEqual(result['custom_key'], 'custom value')
