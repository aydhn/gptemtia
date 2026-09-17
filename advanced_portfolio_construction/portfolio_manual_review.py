# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Manual Review Gates."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_MANUAL_REVIEW_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

PORTFOLIO_REVIEW_GATES: List[Dict[str, Any]] = [
    {
        "gate_id": "GATE-153-01",
        "gate_name": "portfolio_universe_and_eligibility_review_gate",
        "domain": "portfolio_construction",
        "topic": "Asset eligibility and universe specification",
        "review_requirement": "Varlik evreni ve uygunluk kurallarinin offline arastirma gereksinimleriyle tutarliligini dogrula.",
        "action_required": "Operator must confirm eligible assets before sizing placeholders are referenced.",
    },
    {
        "gate_id": "GATE-153-02",
        "gate_name": "position_sizing_models_review_gate",
        "domain": "position_sizing",
        "topic": "Position sizing methodology and risk limits",
        "review_requirement": "Volatilite hedefleme, risk paritesi ve drawdown duyarlilik sozlesmelerini dogrula.",
        "action_required": "Operator must verify mathematical bounds of sizing formulas.",
    },
    {
        "gate_id": "GATE-153-03",
        "gate_name": "risk_budgeting_governance_review_gate",
        "domain": "risk_budgeting",
        "topic": "Risk budget distribution across assets and regimes",
        "review_requirement": "Varlik, strateji ve rejim bazli risk butce paylasim sozlesmelerini dogrula.",
        "action_required": "Operator must confirm risk allocation ceiling and floor consistency.",
    },
    {
        "gate_id": "GATE-153-04",
        "gate_name": "exposure_and_concentration_limits_review_gate",
        "domain": "exposure_limits",
        "topic": "Concentration, gross/net, leverage, and margin ceilings",
        "review_requirement": "Yogunlasma ve kaldirac sinirlarinin koruyucu sozlesme standartlarina uygunlugunu dogrula.",
        "action_required": "Operator must review exposure ceilings and sector diversification constraints.",
    },
    {
        "gate_id": "GATE-153-05",
        "gate_name": "safety_and_disabled_execution_review_gate",
        "domain": "safety_governance",
        "topic": "Prohibition of live trading and real capital allocation",
        "review_requirement": "Canli emir, broker entegrasyonu ve gercek agirlik uretiminin devre disi oldugunu teyit et.",
        "action_required": "Operator sign-off certifying strict non-production and research-only compliance.",
    },
]


def build_portfolio_manual_review_gate_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of portfolio manual review gates."""
    rows = []
    for g in PORTFOLIO_REVIEW_GATES:
        rows.append({
            "gate_id": g["gate_id"],
            "gate_name": g["gate_name"],
            "domain": g["domain"],
            "topic": g["topic"],
            "review_requirement": g["review_requirement"],
            "action_required": g["action_required"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "sign_off_required": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_MANUAL_REVIEW_DOMAIN,
        "active_profile": profile.profile_name,
        "total_review_gates": len(df),
        "all_sign_off_required": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
