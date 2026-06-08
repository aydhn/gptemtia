
import pytest
from pathlib import Path
from secrets_hygiene.gitignore_auditor import (
    build_required_gitignore_patterns,
    audit_gitignore_hygiene,
    build_gitignore_recommendations
)

def test_required_gitignore_patterns():
    patterns = build_required_gitignore_patterns()
    assert ".env" in patterns
    assert "!.env.example" in patterns

def test_gitignore_audit(tmp_path):
    f = tmp_path / ".gitignore"
    f.write_text(".env\n*.log\n")
    df, summary = audit_gitignore_hygiene(tmp_path)
    assert not df.empty

def test_recommendations(tmp_path):
    f = tmp_path / ".gitignore"
    f.write_text(".env\n")
    df, _ = audit_gitignore_hygiene(tmp_path)
    recs = build_gitignore_recommendations(df)
    assert not recs.empty
