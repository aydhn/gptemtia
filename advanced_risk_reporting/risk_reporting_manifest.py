# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Master Manifest."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingManifest


def build_risk_reporting_manifest(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Phase 155 master manifest."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    manifest = RiskReportingManifest(
        manifest_name="Phase 155 Risk Reporting, Exposure Attribution and Limit Monitoring Manifest",
        current_phase=profile.current_phase,
        target_final_phase=profile.target_final_phase,
        next_phase=profile.next_phase,
        non_signal=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
        official_approval=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        risk_report_generated=False,
        exposure_attribution_generated=False,
        limit_monitoring_executed=False,
        metric_calculated=False,
        var_calculated=False,
        expected_shortfall_calculated=False,
        exposure_calculated=False,
        limit_breach_generated=False,
        alert_generated=False,
        dashboard_generated=False,
        portfolio_adjustment_generated=False,
        rebalance_generated=False,
        orders_generated=False,
        optimizer_executed=False,
        model_training_executed=False,
        model_predict_executed=False,
        prediction_generated=False,
        target_label_generated=False,
        broker_order_sent=False,
        live_order_sent=False,
        artifact_persisted=False,
        model_registry_written=False,
        model_deployed=False,
        production_deployed=False,
        source_preserved=True,
        manual_review_required=True,
        phase_156_handoff_ready=True,
    )

    data = manifest.model_dump()
    df = pd.DataFrame([data])
    summary = {
        "manifest_name": manifest.manifest_name,
        "current_phase": manifest.current_phase,
        "next_phase": manifest.next_phase,
        "target_final_phase": manifest.target_final_phase,
        "non_signal": manifest.non_signal,
        "non_production": manifest.non_production,
        "zero_execution": True,
        "phase_156_handoff_ready": manifest.phase_156_handoff_ready,
    }
    return df, summary
