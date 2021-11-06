from unittest import TestCase

from kalyke.payload import Payload, Alert


class TestAlert(TestCase):
    def test_representation(self):
        alert = Alert(
            title="this is title",
            title_localized_key="title_key",
            title_localized_args="title_args",
            subtitle="this is subtitle",
            subtitle_loc_key="subtitle_key",
            subtitle_loc_args="subtitle_args",
            body="this is body",
            body_localized_key="body_key",
            body_localized_args="body_args",
            action_localized_key="action_key",
            action="this is action",
            launch_image="launch_image.png",
        )
        result = alert.dict()

        self.assertEqual(result["title"], "this is title")
        self.assertEqual(result["title-loc-key"], "title_key")
        self.assertEqual(result["title-loc-args"], "title_args")

        self.assertEqual(result["subtitle"], "this is subtitle")
        self.assertEqual(result["subtitle-loc-key"], "subtitle_key")
        self.assertEqual(result["subtitle-loc-args"], "subtitle_args")

        self.assertEqual(result["body"], "this is body")
        self.assertEqual(result["loc-key"], "body_key")
        self.assertEqual(result["loc-args"], "body_args")

        self.assertEqual(result["action-loc-key"], "action_key")
        self.assertEqual(result["action"], "this is action")

        self.assertEqual(result["launch-image"], "launch_image.png")


class TestPayload(TestCase):
    def test_representation(self):
        payload = Payload(alert="this is alert", badge=1, sound="default")
        result = payload.dict()

        self.assertEqual(result["aps"]["alert"], "this is alert")
        self.assertEqual(result["aps"]["badge"], 1)
        self.assertEqual(result["aps"]["sound"], "default")

    def test_representation_with_payload_alert(self):
        alert = Alert(title="this is title", body="this is body")
        custom = {"custom_key": "custom value"}
        payload = Payload(
            alert=alert,
            badge=1,
            sound="default",
            content_available=True,
            mutable_content=True,
            thread_id="this_is_thread_identifier",
            category="notification_category",
            interruption_level="passive",
            relevance_score=1,
            custom=custom,
        )
        result = payload.dict()

        self.assertEqual(result["aps"]["alert"]["title"], "this is title")
        self.assertEqual(result["aps"]["alert"]["body"], "this is body")
        self.assertEqual(result["aps"]["badge"], 1)
        self.assertEqual(result["aps"]["sound"], "default")
        self.assertEqual(result["aps"]["content-available"], 1)
        self.assertEqual(result["aps"]["mutable-content"], 1)
        self.assertEqual(result["aps"]["thread-id"], "this_is_thread_identifier")
        self.assertEqual(result["aps"]["category"], "notification_category")
        self.assertEqual(result["aps"]["interruption-level"], "passive")
        self.assertEqual(result["aps"]["relevance-score"], 1)
        self.assertEqual(result["custom_key"], "custom value")

    def test_error_payload_for_invalid_interruption_level(self):
        with self.assertRaises(ValueError) as e:
            _ = Payload(interruption_level="invalid")

        self.assertEqual(
            e.exception.args[0],
            "Invalid value for interruption_level.\n"
            "Please choice from passive, active, time-sensitive or critical.\n"
            "https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel",
        )

    def test_error_payload_invalid_relevance_score(self):
        with self.assertRaises(ValueError) as e:
            _ = Payload(relevance_score=2)

        self.assertEqual(
            e.exception.args[0],
            "Invalid value for relevance_score.\n"
            "a value between 0\n"
            "https://developer.apple.com/documentation/usernotifications/unnotificationcontent/3821031-relevancescore",
        )
