# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Acceptance Validation."""

import pytest
import pandas as pd
from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    get_default_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_validation import (
    validate_no_forbidden_advanced_ml_acceptance_claims,
    validate_advanced_ml_acceptance_profile_registry,
    validate_advanced_ml_component_checkpoints,
    validate_advanced_ml_acceptance_manifest,
    build_advanced_ml_acceptance_validation_report,
)
from advanced_ml_acceptance.advanced_ml_acceptance_profile_registry import (
    build_advanced_ml_acceptance_profile_registry,
)
from advanced_ml_acceptance.advanced_ml_component_checkpoints import (
    build_advanced_ml_component_acceptance_checkpoint_registry,
)
from advanced_ml_acceptance.advanced_ml_acceptance_manifest import (
    build_advanced_ml_acceptance_manifest,
)


def test_validation_report():
    profile = get_default_advanced_ml_acceptance_profile()
    df, summary = build_advanced_ml_acceptance_validation_report({}, profile)
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["status"] == "PASS"


def test_validate_manifest():
    profile = get_default_advanced_ml_acceptance_profile()
    df_mnf, _ = build_advanced_ml_acceptance_manifest(profile)
    assert validate_advanced_ml_acceptance_manifest(df_mnf, profile) is True


def test_forbidden_claims_detection():
    assert validate_no_forbidden_advanced_ml_acceptance_claims(text="Clean valid string") is True

    with pytest.raises(ValueError):
        validate_no_forbidden_advanced_ml_acceptance_claims(text="We now have official approval for deployment.")

    with pytest.raises(ValueError):
        validate_no_forbidden_advanced_ml_acceptance_claims(summary={"production_ready": True})
