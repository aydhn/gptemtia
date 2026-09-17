# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Parameter Stability and Sensitivity Contracts."""

from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
from advanced_monte_carlo_robustness.parameter_stability_contracts import (
    build_parameter_stability_contract_registry,
    validate_parameter_stability_contract,
)
from advanced_monte_carlo_robustness.parameter_sensitivity_contracts import (
    build_parameter_sensitivity_contract_registry,
)
from advanced_monte_carlo_robustness.parameter_perturbation_contracts import (
    build_parameter_perturbation_contract_registry,
)
from advanced_monte_carlo_robustness.parameter_grid_stability_placeholders import (
    build_parameter_grid_stability_placeholder_registry,
)
from advanced_monte_carlo_robustness.parameter_surface_placeholders import (
    build_parameter_surface_placeholder_registry,
)
from advanced_monte_carlo_robustness.parameter_fragility_placeholders import (
    build_parameter_fragility_placeholder_registry,
)


def test_parameter_stability_contracts():
    profile = get_default_monte_carlo_profile()
    df, summary = build_parameter_stability_contract_registry(profile)
    assert not df.empty
    assert summary["total_contracts"] >= 4
    assert summary["all_valid"] is True
    assert summary["all_optimizations_disabled"] is True

    for _, row in df.iterrows():
        res = validate_parameter_stability_contract(row.to_dict())
        assert res["valid"] is True


def test_parameter_sensitivity_contracts():
    profile = get_default_monte_carlo_profile()
    df, summary = build_parameter_sensitivity_contract_registry(profile)
    assert not df.empty
    assert summary["total_contracts"] >= 3
    assert summary["all_unexecuted"] is True


def test_parameter_perturbation_contracts():
    profile = get_default_monte_carlo_profile()
    df, summary = build_parameter_perturbation_contract_registry(profile)
    assert not df.empty
    assert summary["total_contracts"] >= 3
    assert summary["all_unexecuted"] is True



def test_parameter_grid_stability_placeholders():
    profile = get_default_monte_carlo_profile()
    df, summary = build_parameter_grid_stability_placeholder_registry(profile)
    assert not df.empty
    assert summary["total_placeholders"] >= 2
    assert summary["all_unexecuted"] is True



def test_parameter_surface_placeholders():
    profile = get_default_monte_carlo_profile()
    df, summary = build_parameter_surface_placeholder_registry(profile)
    assert not df.empty
    assert summary["total_placeholders"] >= 3
    assert summary["all_unexecuted"] is True


def test_parameter_fragility_placeholders():
    profile = get_default_monte_carlo_profile()
    df, summary = build_parameter_fragility_placeholder_registry(profile)
    assert not df.empty
    assert summary["total_placeholders"] >= 3
    assert summary["all_unexecuted"] is True
