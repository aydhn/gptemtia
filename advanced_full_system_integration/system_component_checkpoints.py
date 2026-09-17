# -*- coding: utf-8 -*-
"""Phase 158: System Component Checkpoints.

Builds and validates checkpoints for all major system components.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemComponentCheckpoint


CHECKPOINTS_DATA = [
    ("CHK-001", "core_runtime", "main", "config.settings", ["scripts.run_pipeline"], ["tests.test_main"], "core_manifest", "core_validation", "core_safety"),
    ("CHK-002", "data_lake", "data.storage.data_lake", "config.settings", ["scripts.run_data_lake"], ["tests.test_data_lake"], "data_lake_manifest", "data_lake_validation", "data_lake_safety"),
    ("CHK-003", "feature_store", "ml.feature_store", "config.settings", ["scripts.run_feature_store"], ["tests.test_feature_store"], "feature_store_manifest", "feature_store_validation", "feature_store_safety"),
    ("CHK-004", "feature_factor_engine", "advanced_feature_factor_acceptance", "config.settings", ["scripts.run_feature_factor_acceptance"], ["tests.test_feature_factor_acceptance"], "feature_factor_manifest", "feature_factor_validation", "feature_factor_safety"),
    ("CHK-005", "regime_engine", "advanced_regime_acceptance", "config.settings", ["scripts.run_regime_acceptance"], ["tests.test_regime_acceptance"], "regime_manifest", "regime_validation", "regime_safety"),
    ("CHK-006", "ml_governance", "advanced_model_governance", "config.settings", ["scripts.run_model_governance"], ["tests.test_model_governance"], "ml_gov_manifest", "ml_gov_validation", "ml_gov_safety"),
    ("CHK-007", "ml_acceptance", "advanced_ml_acceptance", "config.settings", ["scripts.run_ml_acceptance"], ["tests.test_ml_acceptance"], "ml_acc_manifest", "ml_acc_validation", "ml_acc_safety"),
    ("CHK-008", "backtest_acceptance", "advanced_backtest_acceptance", "config.settings", ["scripts.run_backtest_acceptance"], ["tests.test_backtest_acceptance"], "backtest_manifest", "backtest_validation", "backtest_safety"),
    ("CHK-009", "portfolio_acceptance", "advanced_portfolio_acceptance", "config.settings", ["scripts.run_portfolio_acceptance_manifest"], ["tests.test_portfolio_acceptance_manifest"], "portfolio_manifest", "portfolio_validation", "portfolio_safety"),
    ("CHK-010", "risk_reporting", "advanced_risk_reporting", "config.settings", ["scripts.run_risk_reporting_manifest"], ["tests.test_risk_reporting_manifest"], "risk_manifest", "risk_validation", "risk_safety"),
    ("CHK-011", "portfolio_scenario_control", "advanced_portfolio_scenario_control", "config.settings", ["scripts.run_portfolio_scenario_control_manifest"], ["tests.test_portfolio_scenario_control_manifest"], "scenario_manifest", "scenario_validation", "scenario_safety"),
    ("CHK-012", "reporting_layer", "reports.report_builder", "config.settings", ["scripts.run_reports"], ["tests.test_reports"], "reporting_manifest", "reporting_validation", "reporting_safety"),
    ("CHK-013", "full_system_integration", "advanced_full_system_integration", "config.settings", ["scripts.run_system_integration_findings_manifest"], ["tests.test_full_system_integration_manifest"], "full_system_manifest", "full_system_validation", "full_system_safety"),
]


def build_system_component_checkpoint_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system component checkpoint registry DataFrame and summary."""
    items = []
    for cid, cname, emod, ecfg, escripts, etests, eman, evalr, esafe in CHECKPOINTS_DATA:
        chk = SystemComponentCheckpoint(
            checkpoint_id=cid,
            component_name=cname,
            expected_module=emod,
            expected_config=ecfg,
            expected_scripts=escripts,
            expected_tests=etests,
            expected_manifest=eman,
            expected_validation_report=evalr,
            expected_safety_boundary=esafe,
            contract_only=True,
            local_only=True,
            dry_run=True,
            non_production=True,
            manual_review_required=True,
            production_ready=False,
            broker_ready=False,
            live_ready=False,
            signal_ready=False,
        )
        items.append(chk.__dict__)

    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_checkpoints": len(df),
        "all_contract_only": bool(df["contract_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "all_production_ready_false": not bool(df["production_ready"].any()) if not df.empty else True,
        "all_broker_ready_false": not bool(df["broker_ready"].any()) if not df.empty else True,
        "all_live_ready_false": not bool(df["live_ready"].any()) if not df.empty else True,
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary


def validate_system_component_checkpoint(checkpoint: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single checkpoint dictionary against safety rules."""
    is_valid = True
    issues = []

    if checkpoint.get("production_ready", False):
        is_valid = False
        issues.append("production_ready must be False")
    if checkpoint.get("broker_ready", False):
        is_valid = False
        issues.append("broker_ready must be False")
    if checkpoint.get("live_ready", False):
        is_valid = False
        issues.append("live_ready must be False")
    if checkpoint.get("signal_ready", False):
        is_valid = False
        issues.append("signal_ready must be False")
    if not checkpoint.get("contract_only", False):
        is_valid = False
        issues.append("contract_only must be True")

    return {
        "checkpoint_id": checkpoint.get("checkpoint_id", "UNKNOWN"),
        "is_valid": is_valid,
        "issues": issues,
        "non_signal": True,
    }
