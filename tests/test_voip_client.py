from kalyke.client import VoIPClient
from unittest import TestCase


class TestVoIPClient(TestCase):

    def setUp(self):
        self.client = VoIPClient(auth_key_filepath='', bundle_id='com.example.app', use_sandbox=True)
