# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Monte Carlo Resampling Placeholders."""

from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
from advanced_monte_carlo_robustness.residual_resampling_placeholders import (
    build_residual_resampling_placeholder_registry,
)
from advanced_monte_carlo_robustness.noise_injection_placeholders import (
    build_noise_injection_placeholder_registry,
)
from advanced_monte_carlo_robustness.path_perturbation_placeholders import (
    build_path_perturbation_placeholder_registry,
)


def test_residual_resampling_placeholders():
    profile = get_default_monte_carlo_profile()
    df, summary = build_residual_resampling_placeholder_registry(profile)
    assert not df.empty
    assert summary["total_placeholders"] >= 3
    assert summary["all_unexecuted"] is True


def test_noise_injection_placeholders():
    profile = get_default_monte_carlo_profile()
    df, summary = build_noise_injection_placeholder_registry(profile)
    assert not df.empty
    assert summary["total_placeholders"] >= 3
    assert summary["all_unexecuted"] is True


def test_path_perturbation_placeholders():
    profile = get_default_monte_carlo_profile()
    df, summary = build_path_perturbation_placeholder_registry(profile)
    assert not df.empty
    assert summary["total_placeholders"] >= 3
    assert summary["all_unexecuted"] is True
