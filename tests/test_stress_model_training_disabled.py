# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Model Training Disabled Report."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_model_training_disabled import (
    build_stress_model_training_disabled_report,
    validate_no_stress_model_training_request,
)


def test_model_training_disabled():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_model_training_disabled_report(prof)
    assert not df.empty
    assert summary["is_blocked"] is True
    assert summary["enforced"] is True
    assert summary["non_signal"] is True

    res = validate_no_stress_model_training_request("train_model")
    assert res["is_safe"] is False
