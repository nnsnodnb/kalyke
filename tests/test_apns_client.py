from kalyke.client import APNsClient
from unittest import TestCase


class TestAPNsClient(TestCase):

    def setUp(self):
        self.client = APNsClient(team_id='TEAM_ID', auth_key_id='AUTH_KEY_ID', auth_key_filepath='',
                                 bundle_id='com.example.app', use_sandbox=True)
