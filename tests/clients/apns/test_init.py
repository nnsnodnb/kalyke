from kalyke import ApnsClient


def test_initialize_with_pathlib(auth_key_filepath):
    client = ApnsClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM_ID",
        auth_key_id="DUMMY",
        auth_key_filepath=auth_key_filepath,
    )

    assert isinstance(client, ApnsClient)


def test_initialize_with_str(auth_key_filepath):
    client = ApnsClient(
        use_sandbox=True,
        team_id="DUMMY_TEAM_ID",
        auth_key_id="DUMMY",
        auth_key_filepath=str(auth_key_filepath),
    )

    assert isinstance(client, ApnsClient)
