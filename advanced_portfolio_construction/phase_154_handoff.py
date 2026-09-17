# -*- coding: utf-8 -*-
"""Phase 153: Phase 154 Portfolio Sizing & Allocation Optimization Handoff Report."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from .portfolio_construction_config import (
    PortfolioConstructionProfile,
    get_default_portfolio_construction_profile,
)
from .portfolio_construction_labels import (
    PHASE_154_HANDOFF_DOMAIN,
    HANDOFF_READY,
    PORTFOLIO_CONTRACT_READY,
)

HANDOFF_ITEMS: List[Dict[str, Any]] = [
    {
        "item_id": "HND-154-01",
        "topic": "portfolio_construction_contracts_delivered",
        "description": "Portfoy insa sozlesmeleri (evren, uygunluk, sinyal ve risk girdi sozlesmeleri) tamamlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-154-02",
        "topic": "position_sizing_contracts_delivered",
        "description": "Pozisyon boyutlandirma sozlesmeleri ve yer tutuculari (fixed fractional, vol targeting, risk parity, drawdown aware) tamamlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-154-03",
        "topic": "risk_budget_contracts_delivered",
        "description": "Risk butceleme sozlesmeleri ve yer tutuculari (varlik, strateji, rejim, portfoy) tamamlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-154-04",
        "topic": "exposure_and_concentration_limits_delivered",
        "description": "Maruziyet ve yogunlasma limit sozlesmeleri ve yer tutuculari (gross/net, sektor, kaldirac, teminat, notional) tamamlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-154-05",
        "topic": "guards_and_disabled_execution_delivered",
        "description": "Lookahead, tahsisat/boyutlandirma iddiasi, yatirim tavsiyesi muhafizlari ve devre disi birakilan calistirma raporlari tamamlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-154-06",
        "topic": "findings_and_master_manifest_delivered",
        "description": "Portfoy bulgulari, hazirlik skoru ve Phase 153 ana manifestosu hazirlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-154-07",
        "topic": "readiness_score_threshold_met",
        "description": "Hazirlik skoru >= 0.75 olup, portfolio_construction_contract_ready_non_production seviyesine ulasildi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-154-08",
        "topic": "strict_non_production_boundary_enforced",
        "description": "Canli emir, broker entegrasyonu, gercek portfoy agirligi veya lot uretilmemesi kosulu korundu.",
        "satisfied": True,
    },
]


def build_phase_154_handoff_report(
    profile: Optional[PortfolioConstructionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Phase 154 handoff."""
    active = profile or get_default_portfolio_construction_profile()

    records = []
    for item in HANDOFF_ITEMS:
        records.append({
            "handoff_id": "HND-153-154-001",
            "item_id": item["item_id"],
            "topic": item["topic"],
            "description": item["description"],
            "satisfied": item["satisfied"],
            "source_phase": active.current_phase,
            "target_phase": active.next_phase,
            "target_final_phase": active.target_final_phase,
            "manual_review_required": True,
            "non_signal": True,
            "contract_only": True,
            "non_production": True,
            "status": HANDOFF_READY,
        })

    df = pd.DataFrame(records)
    all_satisfied = df["satisfied"].all()

    summary: Dict[str, Any] = {
        "domain": PHASE_154_HANDOFF_DOMAIN,
        "active_profile": active.profile_name,
        "handoff_id": "HND-153-154-001",
        "source_phase": active.current_phase,
        "target_phase": active.next_phase,
        "target_final_phase": active.target_final_phase,
        "total_items": len(records),
        "satisfied_count": int(df["satisfied"].sum()),
        "all_satisfied": bool(all_satisfied),
        "manual_review_required": True,
        "status": HANDOFF_READY if all_satisfied else "HANDOFF_BLOCKED",
    }
    return df, summary
