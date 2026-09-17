# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Validation Engine."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from .portfolio_construction_config import (
    PortfolioConstructionProfile,
    get_default_portfolio_construction_profile,
    validate_portfolio_construction_profiles,
)
from .portfolio_construction_labels import (
    PORTFOLIO_VALIDATION_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)
from .portfolio_construction_manifest import build_portfolio_construction_manifest
from .portfolio_readiness_scoring import build_portfolio_readiness_score_report


def validate_portfolio_construction_invariants(
    profile: Optional[PortfolioConstructionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Validate all Phase 153 governance and safety invariants."""
    active = profile or get_default_portfolio_construction_profile()

    checks: List[Dict[str, Any]] = [
        {
            "check_id": "VAL-153-01",
            "name": "Profile Configurations Validity",
            "condition": validate_portfolio_construction_profiles(),
            "description": "Tum profil yapilandirmalarinin kurallara uygun oldugunu dogrular.",
        },
        {
            "check_id": "VAL-153-02",
            "name": "Offline Contract Boundary",
            "condition": active.local_only and active.non_production and active.research_only,
            "description": "Sistemin sadece yerel/offline ve arastirma amaciyla calistigini dogrular.",
        },
        {
            "check_id": "VAL-153-03",
            "name": "Live Execution Prohibited",
            "condition": not active.allow_live_trading and not active.allow_broker_integration,
            "description": "Canli emir iletimi ve broker entegrasyonunun kesin olarak kapal oldugunu dogrular.",
        },
        {
            "check_id": "VAL-153-04",
            "name": "Real Optimization Prohibited",
            "condition": not active.allow_optimizer_execution and not active.allow_capital_allocation,
            "description": "Gercek portfoy optimizasyonu ve sermaye tahsisinin kapal oldugunu dogrular.",
        },
        {
            "check_id": "VAL-153-05",
            "name": "Real Lot Sizing Prohibited",
            "condition": not active.allow_position_sizing,
            "description": "Gercek lot ve adet boyutlandirmasinin uretilmedigini dogrular.",
        },
        {
            "check_id": "VAL-153-06",
            "name": "Phase Boundary Alignment",
            "condition": active.current_phase == 153 and active.target_final_phase == 160 and active.next_phase == 154,
            "description": "Faz numaralarinin (153 -> 154 -> 160) dogru tanimlandigini dogrular.",
        },
    ]

    rows = []
    for c in checks:
        rows.append({
            "check_id": c["check_id"],
            "name": c["name"],
            "condition_met": c["condition"],
            "description": c["description"],
            "current_phase": active.current_phase,
            "contract_only": True,
            "non_production": True,
            "status": "PASS" if c["condition"] else "FAIL",
        })

    df = pd.DataFrame(rows)
    all_passed = df["condition_met"].all()

    summary: Dict[str, Any] = {
        "domain": PORTFOLIO_VALIDATION_DOMAIN,
        "active_profile": active.profile_name,
        "total_checks": len(records) if "records" in locals() else len(rows),
        "passed_count": int(df["condition_met"].sum()),
        "all_passed": bool(all_passed),
        "status": PORTFOLIO_CONTRACT_READY if all_passed else "VALIDATION_FAILED",
    }
    return df, summary
