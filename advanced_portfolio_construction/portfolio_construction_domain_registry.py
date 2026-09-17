# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Domain Registry."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_CONSTRUCTION_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
    PORTFOLIO_CONSTRUCTION_PROFILE_DOMAIN,
    PORTFOLIO_CONTRACT_DOMAIN,
    PORTFOLIO_UNIVERSE_DOMAIN,
    ASSET_ELIGIBILITY_DOMAIN,
    SIGNAL_INPUT_DOMAIN,
    RISK_INPUT_DOMAIN,
    DEPENDENCY_DOMAIN,
    POSITION_SIZING_DOMAIN,
    RISK_BUDGET_DOMAIN,
    EXPOSURE_LIMIT_DOMAIN,
    CONCENTRATION_LIMIT_DOMAIN,
    OUTPUT_CONTRACT_DOMAIN,
    METRIC_PLACEHOLDER_DOMAIN,
    CLAIM_GUARD_DOMAIN,
    DISABLED_EXECUTION_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_154_HANDOFF_DOMAIN,
)


DOMAINS = [
    {"domain_name": PORTFOLIO_CONSTRUCTION_PROFILE_DOMAIN, "category": "configuration", "description": "Profile and configuration registry domain"},
    {"domain_name": PORTFOLIO_CONTRACT_DOMAIN, "category": "contracts", "description": "Portfolio construction contracts domain"},
    {"domain_name": PORTFOLIO_UNIVERSE_DOMAIN, "category": "universe", "description": "Portfolio universe definition domain"},
    {"domain_name": ASSET_ELIGIBILITY_DOMAIN, "category": "eligibility", "description": "Asset eligibility contract domain"},
    {"domain_name": SIGNAL_INPUT_DOMAIN, "category": "inputs", "description": "Signal inputs metadata contract domain"},
    {"domain_name": RISK_INPUT_DOMAIN, "category": "inputs", "description": "Risk inputs metadata contract domain"},
    {"domain_name": DEPENDENCY_DOMAIN, "category": "governance", "description": "Upstream phases and system dependencies domain"},
    {"domain_name": POSITION_SIZING_DOMAIN, "category": "sizing", "description": "Position sizing contracts and placeholders domain"},
    {"domain_name": RISK_BUDGET_DOMAIN, "category": "risk_budget", "description": "Risk budgeting contracts and placeholders domain"},
    {"domain_name": EXPOSURE_LIMIT_DOMAIN, "category": "limits", "description": "Exposure limit contracts domain"},
    {"domain_name": CONCENTRATION_LIMIT_DOMAIN, "category": "limits", "description": "Concentration limit contracts domain"},
    {"domain_name": OUTPUT_CONTRACT_DOMAIN, "category": "outputs", "description": "Output schema and contract enforcement domain"},
    {"domain_name": METRIC_PLACEHOLDER_DOMAIN, "category": "metrics", "description": "Metric calculation placeholder metadata domain"},
    {"domain_name": CLAIM_GUARD_DOMAIN, "category": "safety", "description": "Safety guards and claim boundaries domain"},
    {"domain_name": DISABLED_EXECUTION_DOMAIN, "category": "safety", "description": "Disabled execution reports domain"},
    {"domain_name": FINDING_DOMAIN, "category": "governance", "description": "Findings and review queue domain"},
    {"domain_name": READINESS_SCORE_DOMAIN, "category": "governance", "description": "Readiness scoring domain"},
    {"domain_name": MANIFEST_DOMAIN, "category": "manifest", "description": "Master manifest domain"},
    {"domain_name": HEALTH_DOMAIN, "category": "diagnostics", "description": "Health check domain"},
    {"domain_name": VALIDATION_DOMAIN, "category": "validation", "description": "Validation checks domain"},
    {"domain_name": SAFETY_DOMAIN, "category": "safety", "description": "Safety boundary domain"},
    {"domain_name": PHASE_154_HANDOFF_DOMAIN, "category": "handoff", "description": "Phase 154 handoff domain"},
]


def build_portfolio_construction_domain_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for portfolio construction domains."""
    rows = []
    for d in DOMAINS:
        rows.append({
            "domain_name": d["domain_name"],
            "category": d["category"],
            "description": d["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "non_signal": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_CONSTRUCTION_DOMAIN,
        "active_profile": profile.profile_name,
        "total_domains": len(df),
        "all_contract_only": True,
        "all_non_production": True,
        "all_non_signal": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def summarize_portfolio_construction_domains(df: pd.DataFrame) -> Dict:
    """Summarize portfolio construction domains."""
    return {
        "total_domains": len(df),
        "domains": df["domain_name"].tolist() if not df.empty else [],
        "non_signal": True,
    }
