# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Domain Registry.

Registers and summarizes all governance and evaluation domains for Phase 157.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    PORTFOLIO_ACCEPTANCE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_PROFILE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_SCOPE_DOMAIN,
    COMPONENT_REGISTRY_DOMAIN,
    COMPONENT_CHECKPOINT_DOMAIN,
    PHASE_153_PORTFOLIO_CONSTRUCTION_ACCEPTANCE_DOMAIN,
    PHASE_154_PORTFOLIO_OPTIMIZATION_ACCEPTANCE_DOMAIN,
    PHASE_155_RISK_REPORTING_ACCEPTANCE_DOMAIN,
    PHASE_156_PORTFOLIO_SCENARIO_CONTROL_ACCEPTANCE_DOMAIN,
    DEPENDENCY_ACCEPTANCE_DOMAIN,
    VALIDATION_EVIDENCE_DOMAIN,
    SAFETY_BOUNDARY_DOMAIN,
    NON_PRODUCTION_BOUNDARY_DOMAIN,
    MANUAL_REVIEW_GATE_DOMAIN,
    GO_NO_GO_BOUNDARY_DOMAIN,
    BLOCKER_DOMAIN,
    GAP_DOMAIN,
    WARNING_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_158_HANDOFF_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

DOMAINS = [
    (PORTFOLIO_ACCEPTANCE_PROFILE_DOMAIN, "Yonetisim profili domaini"),
    (PORTFOLIO_ACCEPTANCE_DOMAIN, "Portfolio kabul ana domaini"),
    (PORTFOLIO_ACCEPTANCE_SCOPE_DOMAIN, "Portfolio kabul kapsami domaini"),
    (COMPONENT_REGISTRY_DOMAIN, "Bilesen kayit domaini"),
    (COMPONENT_CHECKPOINT_DOMAIN, "Bilesen kontrol noktasi domaini"),
    (PHASE_153_PORTFOLIO_CONSTRUCTION_ACCEPTANCE_DOMAIN, "Phase 153 Portfoy insasi kabul domaini"),
    (PHASE_154_PORTFOLIO_OPTIMIZATION_ACCEPTANCE_DOMAIN, "Phase 154 Portfoy optimizasyonu kabul domaini"),
    (PHASE_155_RISK_REPORTING_ACCEPTANCE_DOMAIN, "Phase 155 Risk raporlama kabul domaini"),
    (PHASE_156_PORTFOLIO_SCENARIO_CONTROL_ACCEPTANCE_DOMAIN, "Phase 156 Senaryo testi ve drawdown kontrol kabul domaini"),
    (DEPENDENCY_ACCEPTANCE_DOMAIN, "Bagimlilik kabul domaini"),
    (VALIDATION_EVIDENCE_DOMAIN, "Dogrulama kaniti domaini"),
    (SAFETY_BOUNDARY_DOMAIN, "Guvenlik siniri domaini"),
    (NON_PRODUCTION_BOUNDARY_DOMAIN, "Non-production siniri domaini"),
    (MANUAL_REVIEW_GATE_DOMAIN, "Manuel inceleme kapisi domaini"),
    (GO_NO_GO_BOUNDARY_DOMAIN, "Go/No-go sinir domaini"),
    (BLOCKER_DOMAIN, "Bloklayici domaini"),
    (GAP_DOMAIN, "Bosluk domaini"),
    (WARNING_DOMAIN, "Uyari domaini"),
    (FINDING_DOMAIN, "Bulgular domaini"),
    (READINESS_SCORE_DOMAIN, "Hazirlik skoru domaini"),
    (MANIFEST_DOMAIN, "Manifest domaini"),
    (HEALTH_DOMAIN, "Saglik denetimi domaini"),
    (VALIDATION_DOMAIN, "Dogrulama raporu domaini"),
    (SAFETY_DOMAIN, "Guvenlik raporu domaini"),
    (PHASE_158_HANDOFF_DOMAIN, "Phase 158 Devir domaini"),
]


def build_portfolio_acceptance_domain_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of portfolio acceptance domains."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for domain_name, desc in DOMAINS:
        records.append({
            "domain_name": domain_name,
            "description": desc,
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = {
        "domain": PORTFOLIO_ACCEPTANCE_DOMAIN,
        "total_domains": len(df),
        "status": PORTFOLIO_ACCEPTANCE_READY,
    }
    return df, summary
