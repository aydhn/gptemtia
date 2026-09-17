# -*- coding: utf-8 -*-
"""Unit tests for Phase 144 Governance Dependencies, Guards, Lineage, and Linkage."""

import pytest
from advanced_model_governance.model_governance_config import get_model_governance_profile
from advanced_model_governance.governance_dataset_contract_dependencies import (
    build_governance_dataset_contract_dependency_registry,
)
from advanced_model_governance.governance_baseline_model_dependencies import (
    build_governance_baseline_model_dependency_registry,
)
from advanced_model_governance.governance_gpu_training_dependencies import (
    build_governance_gpu_training_dependency_registry,
)
from advanced_model_governance.governance_ensemble_dependencies import (
    build_governance_ensemble_dependency_registry,
)
from advanced_model_governance.governance_calibration_uncertainty_dependencies import (
    build_governance_calibration_uncertainty_dependency_registry,
)
from advanced_model_governance.governance_drift_dependencies import (
    build_governance_drift_dependency_registry,
)
from advanced_model_governance.governance_explainability_dependencies import (
    build_governance_explainability_dependency_registry,
)
from advanced_model_governance.governance_no_lookahead_guards import (
    build_governance_no_lookahead_guard_registry,
    validate_governance_no_lookahead_columns,
)
from advanced_model_governance.governance_metadata_only_news_guards import (
    build_governance_metadata_only_news_guard_registry,
)
from advanced_model_governance.governance_source_preservation_guards import (
    build_governance_source_preservation_guard_registry,
)
from advanced_model_governance.governance_forbidden_column_policies import (
    build_governance_forbidden_column_policy_registry,
    validate_governance_forbidden_columns,
)
from advanced_model_governance.governance_lineage import (
    build_governance_lineage_registry,
)
from advanced_model_governance.governance_experiment_linkage import (
    build_governance_experiment_linkage_registry,
)


def test_governance_dependencies():
    prof = get_model_governance_profile()
    deps = [
        build_governance_dataset_contract_dependency_registry(prof),
        build_governance_baseline_model_dependency_registry(prof),
        build_governance_gpu_training_dependency_registry(prof),
        build_governance_ensemble_dependency_registry(prof),
        build_governance_calibration_uncertainty_dependency_registry(prof),
        build_governance_drift_dependency_registry(prof),
        build_governance_explainability_dependency_registry(prof),
    ]
    assert len(deps) == 7
    for df, summary in deps:
        assert len(df) >= 1
        assert "status" in df.columns
        assert (df["status"] == "SATISFIED").all()
        assert summary["all_satisfied"] is True


def test_governance_guards():
    prof = get_model_governance_profile()
    g_nl_df, nl_sum = build_governance_no_lookahead_guard_registry(prof)
    assert len(g_nl_df) >= 3
    assert (g_nl_df["is_enforced"] == True).all()
    assert nl_sum["all_enforced"] is True

    val_res = validate_governance_no_lookahead_columns(["price_close", "future_return"])
    assert val_res["is_valid"] is False
    assert "future_return" in val_res["violations"]

    g_mn_df, _ = build_governance_metadata_only_news_guard_registry(prof)
    assert len(g_mn_df) >= 3
    assert (g_mn_df["is_enforced"] == True).all()

    g_sp_df, _ = build_governance_source_preservation_guard_registry(prof)
    assert len(g_sp_df) >= 3
    assert (g_sp_df["is_enforced"] == True).all()

    g_fc_df, fc_sum = build_governance_forbidden_column_policy_registry(prof)
    assert len(g_fc_df) >= 5
    assert (g_fc_df["is_strictly_enforced"] == True).all()
    assert fc_sum["all_strictly_enforced"] is True

    fc_val = validate_governance_forbidden_columns(["signal", "volume"])
    assert fc_val["is_valid"] is False
    assert "signal" in fc_val["violations"]


def test_governance_lineage_and_linkage():
    prof = get_model_governance_profile()
    lin_df, lin_sum = build_governance_lineage_registry(prof)
    assert len(lin_df) >= 4
    assert lin_sum["total_lineage_nodes"] >= 4

    lnk_df, lnk_sum = build_governance_experiment_linkage_registry(prof)
    assert len(lnk_df) >= 4
    assert lnk_sum["total_linkages"] >= 4
