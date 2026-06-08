
import pytest
from pathlib import Path
from secrets_hygiene.env_template_auditor import (
    parse_env_template,
    classify_env_variable_safety,
    audit_env_template,
    build_env_template_recommendations
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_parse_env_template(tmp_path):
    f = tmp_path / ".env.example"
    f.write_text("API_KEY=YOUR_KEY\nTEST=1")
    df = parse_env_template(f)
    assert not df.empty
    assert "variable_name" in df.columns

def test_placeholder_safe():
    safety = classify_env_variable_safety("API_KEY", "YOUR_KEY_HERE")
    assert safety["has_placeholder"]
    assert not safety["has_realistic_secret_value"]

def test_real_looking_secret_warning():
    safety = classify_env_variable_safety("API_KEY", "AKIAIOSFODNN7EXAMPLE")
    assert not safety["has_placeholder"]
    assert safety["has_realistic_secret_value"]

def test_recommendations_dataframe(tmp_path):
    f = tmp_path / ".env.example"
    f.write_text("API_KEY=AKIAIOSFODNN7EXAMPLE\n")
    profile = get_default_secrets_hygiene_profile()
    df, summary = audit_env_template(tmp_path, profile)
    recs = build_env_template_recommendations(df)
    assert not recs.empty
