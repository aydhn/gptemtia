# -*- coding: utf-8 -*-
"""Phase 158: System Manual Review Gates.

Defines 10 mandatory human operator review gates across all integrated subsystems.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemManualReviewItem

REVIEW_GATES = [
    ("MRG-158-001", "data_pipeline_integration_review_gate", "Data Ingestion & Integrity Review", "Verify that raw data feeds and providers adhere to no-leakage and metadata-only rules.", "Review data contracts and verify zero scraping.", "PENDING_REVIEW"),
    ("MRG-158-002", "feature_factor_integration_review_gate", "Feature & Factor Quality Review", "Verify that features and factors have no lookahead bias and are non-signal.", "Inspect factor distributions and missingness.", "PENDING_REVIEW"),
    ("MRG-158-003", "regime_integration_review_gate", "Regime Engine & Transitions Review", "Verify regime definitions, stability, and absence of target labels.", "Review transition matrices and stability metrics.", "PENDING_REVIEW"),
    ("MRG-158-004", "ml_governance_review_gate", "ML Governance & Model Cards Review", "Verify that all model metadata, calibration, and drift checks are non-executing.", "Inspect model cards and explainability attribution.", "PENDING_REVIEW"),
    ("MRG-158-005", "backtest_acceptance_review_gate", "Backtest Acceptance Layer Review", "Verify realistic slippage, transaction cost modeling, and OOS validation.", "Review walk-forward and Monte Carlo robustness summaries.", "PENDING_REVIEW"),
    ("MRG-158-006", "portfolio_acceptance_review_gate", "Portfolio Acceptance Block Review", "Verify portfolio construction and optimization constraints.", "Review weight allocation bounds and diversification.", "PENDING_REVIEW"),
    ("MRG-158-007", "risk_reporting_review_gate", "Risk Limits & Exposure Attribution Review", "Verify risk exposure attribution and limit monitoring contracts.", "Inspect risk budget allocations and limit warnings.", "PENDING_REVIEW"),
    ("MRG-158-008", "scenario_control_review_gate", "Scenario Testing & Drawdown Control Review", "Verify stress scenarios, historical shocks, and drawdown controls.", "Review derisking triggers and recovery simulations.", "PENDING_REVIEW"),
    ("MRG-158-009", "reporting_docs_review_gate", "Reporting Layer & Documentation Review", "Verify that reports contain all mandatory disclaimers and warnings.", "Inspect markdown and txt reports for compliance.", "PENDING_REVIEW"),
    ("MRG-158-010", "phase_159_release_candidate_review_gate", "Phase 159 Release Candidate Review Gate", "Final human gate before proceeding to Phase 159 Release Candidate preparation.", "Confirm all 9 preceding gates are verified.", "PENDING_REVIEW"),
]


def build_system_manual_review_gate_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system manual review gate registry DataFrame and summary."""
    items = []
    for mid, gname, title, desc, action, status in REVIEW_GATES:
        item = SystemManualReviewItem(
            item_id=mid,
            gate_name=gname,
            title=title,
            description=desc,
            action_required=action,
            status=status,
        )
        items.append(item.__dict__)

    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_review_gates": len(df),
        "pending_review_count": int((df["status"] == "PENDING_REVIEW").sum()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
