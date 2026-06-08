
import pytest
import pandas as pd
from pathlib import Path
from secrets_hygiene.secrets_runbook import (
    build_secret_hygiene_runbook_sections,
    build_secret_hygiene_runbook,
    build_secret_incident_manual_review_section
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_runbook_sections():
    df = pd.DataFrame()
    sections = build_secret_hygiene_runbook_sections(df, df)
    assert len(sections) > 0

def test_runbook_build():
    profile = get_default_secrets_hygiene_profile()
    df = pd.DataFrame()
    text, summary = build_secret_hygiene_runbook(df, df, profile)
    assert "Secrets Hygiene Runbook" in text
    assert "cloud vault" not in text.lower()

def test_incident_manual_review():
    text = build_secret_incident_manual_review_section(pd.DataFrame())
    assert "rotate" in text.lower()
