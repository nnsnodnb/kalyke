from kalyke import LiveActivityClient


def test_initialize_with_pathlib(auth_key_filepath):
    client = LiveActivityClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM_ID",
        auth_key_id="DUMMY",
        auth_key_filepath=auth_key_filepath,
    )

    assert isinstance(client, LiveActivityClient)


def test_initialize_with_str(auth_key_filepath):
    client = LiveActivityClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM_ID",
        auth_key_id="DUMMY",
        auth_key_filepath=str(auth_key_filepath),
    )

    assert isinstance(client, LiveActivityClient)
