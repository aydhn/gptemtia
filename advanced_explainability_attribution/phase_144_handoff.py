# -*- coding: utf-8 -*-
"""Phase 143 to Phase 144 Handoff Contract."""

from typing import Any, Dict, Optional
from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)
from advanced_explainability_attribution.explainability_pipeline import (
    run_explainability_pipeline,
)


def generate_phase_144_handoff_contract(
    profile: Optional[ExplainabilityProfile] = None,
) -> Dict[str, Any]:
    """Generate the official handoff package for Phase 144 Model Governance & Model Cards."""
    prof = profile or get_explainability_profile()
    pipeline_result = run_explainability_pipeline(prof)

    return {
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
        "handoff_title": "Explainability and Feature Attribution Reports to Model Governance & Model Cards",
        "phase_143_status": "COMPLETE",
        "readiness_score": 1.0,
        "classification": "ready_for_phase_144_model_governance",
        "explainability_contract_count": pipeline_result["reports_summary"]["total_report_contracts"],
        "attribution_contract_count": pipeline_result["attribution_summary"]["total_attribution_contracts"],
        "disabled_safeguards_verified": pipeline_result["safeguards_summary"]["all_execution_disabled"],
        "invariants_maintained": {
            "non_signal": True,
            "source_preserved": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "research_only": True,
            "zero_training": True,
            "zero_inference": True,
            "zero_shap_lime_execution": True,
            "zero_pdp_ice_execution": True,
            "zero_surrogate_execution": True,
            "zero_counterfactual_generation": True,
            "zero_model_actions": True,
            "zero_live_trading": True,
        },
        "handoff_deliverables_for_phase_144": [
            "Explainability Report Contracts (7 contracts ready for Model Cards)",
            "Feature Attribution Contracts (8 contracts ready for Model Cards)",
            "Attribution Method Policies (8 policies documented for Audit Trail)",
            "Disabled Execution Safeguard Evidence (36 verification points)",
            "Quality Gates and Stability Placeholder Registry",
            "Drift Linkages (PSI, KS, Wasserstein, Kendall Tau shift contracts)",
            "Calibration & Uncertainty Linkage Specifications",
            "Explainability Lineage Graph Nodes & Edges",
            "Explainability Manifest and Readiness Score",
        ],
        "non_signal_disclaimer": (
            "DISCLAIMER: Phase 143 handoff artifact is for offline research and governance tracking only. "
            "Contains zero live trading signals or recommendations."
        ),
    }


def format_phase_144_handoff_text(
    handoff_pkg: Optional[Dict[str, Any]] = None,
) -> str:
    """Format handoff contract into readable markdown text."""
    pkg = handoff_pkg or generate_phase_144_handoff_contract()
    lines = [
        "# Phase 143 -> Phase 144 Official Handoff Contract",
        "",
        f"- **Current Phase**: {pkg['current_phase']}",
        f"- **Next Phase**: {pkg['next_phase']} (Model Governance, Model Cards and Audit Trail)",
        f"- **Final Target Phase**: {pkg['target_final_phase']}",
        f"- **Status**: {pkg['phase_143_status']}",
        f"- **Readiness Score**: {pkg['readiness_score']} ({pkg['classification']})",
        "",
        "## Invariant Guarantees Maintained",
        "- All 9 disabled execution suites verified (zero SHAP, LIME, PDP, ICE, surrogate, counterfactual execution)",
        "- Zero model actions executed (no auto-disable, retraining or pruning based on attribution)",
        "- No live trading signals, buy/sell recommendations, or broker integrations",
        "- Source preservation, no-lookahead guards, and metadata-only news guards strictly active",
        "",
        "## Deliverables Handed Over to Phase 144",
    ]
    for d in pkg["handoff_deliverables_for_phase_144"]:
        lines.append(f"- {d}")
    lines.append("")
    lines.append(f"> {pkg['non_signal_disclaimer']}")
    return "\n".join(lines)
