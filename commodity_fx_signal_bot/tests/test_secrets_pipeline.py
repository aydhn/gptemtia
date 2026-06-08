
import pytest
from pathlib import Path
import pandas as pd
from unittest.mock import MagicMock
from config.settings import Settings
from secrets_hygiene.secrets_pipeline import SecretsHygienePipeline
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_secrets_pipeline_sensitive_file():
    dl = MagicMock()
    s = Settings()
    s.secrets_hygiene_enabled = True
    profile = get_default_secrets_hygiene_profile()
    pipeline = SecretsHygienePipeline(dl, s, Path("."), profile)

    tables, summary = pipeline.build_sensitive_file_scan_report(save=True)
    assert "inventory" in tables
    assert dl.save_sensitive_file_inventory.called

def test_secrets_pipeline_env_template():
    dl = MagicMock()
    s = Settings()
    profile = get_default_secrets_hygiene_profile()
    pipeline = SecretsHygienePipeline(dl, s, Path("."), profile)

    df, summary = pipeline.build_env_template_audit_report(save=True)
    assert dl.save_env_template_audit.called

def test_secrets_pipeline_boundary():
    dl = MagicMock()
    s = Settings()
    profile = get_default_secrets_hygiene_profile()
    pipeline = SecretsHygienePipeline(dl, s, Path("."), profile)

    df, summary = pipeline.build_credential_boundary_report(save=True)
    assert dl.save_credential_boundary_report.called

def test_secrets_pipeline_private_data():
    dl = MagicMock()
    s = Settings()
    profile = get_default_secrets_hygiene_profile()
    pipeline = SecretsHygienePipeline(dl, s, Path("."), profile)

    df, summary = pipeline.build_private_data_protection_report(save=True)
    assert dl.save_private_data_protection_report.called

def test_secrets_pipeline_remediation():
    dl = MagicMock()
    s = Settings()
    profile = get_default_secrets_hygiene_profile()
    pipeline = SecretsHygienePipeline(dl, s, Path("."), profile)

    df, summary = pipeline.build_secret_remediation_report(save=True)
    assert dl.save_secret_remediation_recommendations.called
