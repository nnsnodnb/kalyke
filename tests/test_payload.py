from kalyke.payload import PayloadAlert, Payload
from unittest import TestCase


class TestPayloadAlert(TestCase):

    def test_representation(self):
        alert = PayloadAlert(title='this is title', body='this is body')
        result = alert.dict()

        self.assertEqual(result['title'], 'this is title')
        self.assertEqual(result['body'], 'this is body')


class TestPayload(TestCase):

    def test_representation(self):
        payload = Payload(alert='this is alert', badge=1, sound='default')
        result = payload.dict()

        self.assertEqual(result['aps']['alert'], 'this is alert')
        self.assertEqual(result['aps']['badge'], 1)
        self.assertEqual(result['aps']['sound'], 'default')

    def test_representation_with_payload_alert(self):
        alert = PayloadAlert(title='this is title', body='this is body')
        payload = Payload(alert=alert, badge=1, sound='default', mutable_content=True)
        result = payload.dict()

        self.assertEqual(result['aps']['alert']['title'], 'this is title')
        self.assertEqual(result['aps']['alert']['body'], 'this is body')
        self.assertEqual(result['aps']['badge'], 1)
        self.assertEqual(result['aps']['sound'], 'default')
        self.assertEqual(result['aps']['mutable-content'], 1)
