from kalyke import VoIPClient


def test_initialize_with_pathlib(auth_key_filepath):
    client = VoIPClient(
        use_sandbox=True,
        auth_key_filepath=auth_key_filepath,
    )

    assert isinstance(client, VoIPClient)


def test_initialize_with_str(auth_key_filepath):
    client = VoIPClient(
        use_sandbox=True,
        auth_key_filepath=str(auth_key_filepath),
    )

    assert isinstance(client, VoIPClient)
