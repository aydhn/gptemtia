from portable_packaging.config_verification import (
    verify_env_example,
    verify_settings_env_alignment,
    verify_no_secrets_in_templates
)

def test_config_verification(tmp_path):
    res = verify_env_example(tmp_path)
    assert not res.passed

    df, s = verify_settings_env_alignment(tmp_path)
    assert not df.empty

    df, s = verify_no_secrets_in_templates(tmp_path)
    assert not df.empty
