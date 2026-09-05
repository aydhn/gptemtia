"""Tests for advanced_feature_quality_drift.feature_quality_drift_validation."""

import pandas as pd
import pytest

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
)
from advanced_feature_quality_drift.feature_quality_drift_profile_registry import (
    build_feature_quality_drift_profile_registry,
)
from advanced_feature_quality_drift.feature_quality_metric_registry import (
    build_feature_quality_metric_registry,
)
from advanced_feature_quality_drift.feature_drift_metric_registry import (
    build_feature_drift_metric_registry,
)
from advanced_feature_quality_drift.feature_quality_drift_manifest import (
    build_feature_quality_drift_manifest,
)
from advanced_feature_quality_drift.feature_quality_drift_validation import (
    FORBIDDEN_TERMS,
    validate_feature_quality_drift_profile_registry,
    validate_quality_metric_registry,
    validate_drift_metric_registry,
    validate_quality_drift_manifest,
    validate_no_forbidden_quality_drift_claims,
    build_feature_quality_drift_validation_report,
)


def test_validate_profile_registry_success():
    df, _ = build_feature_quality_drift_profile_registry()
    assert validate_feature_quality_drift_profile_registry(df) is True


def test_validate_profile_registry_failure():
    df, _ = build_feature_quality_drift_profile_registry()
    bad_df = df.copy()
    bad_df.loc[0, "current_phase"] = 999
    with pytest.raises(ValueError, match="Invalid current_phase"):
        validate_feature_quality_drift_profile_registry(bad_df)


def test_validate_quality_metric_registry_success():
    df, _ = build_feature_quality_metric_registry()
    assert validate_quality_metric_registry(df) is True


def test_validate_drift_metric_registry_success():
    df, _ = build_feature_drift_metric_registry()
    assert validate_drift_metric_registry(df) is True


def test_validate_quality_drift_manifest_success():
    df, _ = build_feature_quality_drift_manifest()
    assert validate_quality_drift_manifest(df) is True


def test_validate_no_forbidden_claims():
    assert validate_no_forbidden_quality_drift_claims(text="Harmless diagnostic description") is True

    with pytest.raises(ValueError, match="Forbidden term detected"):
        validate_no_forbidden_quality_drift_claims(text="System produces buy_signal now")

    df_clean = pd.DataFrame({"col_clean": [1, 2]})
    assert validate_no_forbidden_quality_drift_claims(df=df_clean) is True

    df_forbidden = pd.DataFrame({"auto_drop_executed": [True]})
    with pytest.raises(ValueError, match="Forbidden term detected"):
        validate_no_forbidden_quality_drift_claims(df=df_forbidden)

    summary_clean = {"status": "ok", "phase": 123}
    assert validate_no_forbidden_quality_drift_claims(summary=summary_clean) is True

    summary_bad = {"claim": "live_trading_approved"}
    with pytest.raises(ValueError, match="Forbidden term detected"):
        validate_no_forbidden_quality_drift_claims(summary=summary_bad)


def test_build_feature_quality_drift_validation_report():
    df, summary = build_feature_quality_drift_validation_report()
    assert not df.empty
    assert summary["total_validation_checks"] == 9
    assert summary["passed_checks"] == 9
    assert summary["failed_checks"] == 0
    assert summary["status"] == "diagnostic_pass"
    assert summary["current_phase"] == 123
    assert summary["next_phase"] == 124
    assert summary["non_signal"] is True
    assert summary["destructive_action_allowed"] is False
