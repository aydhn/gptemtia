# -*- coding: utf-8 -*-
"""Phase 159: Final Manifest Freeze Contracts."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    MANIFEST_FREEZE_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

MANIFEST_FREEZE_ITEMS = [
    ("system_integration_manifest_freeze", "data/lake/advanced_full_system_integration/manifest", "Phase 158 sistem entegrasyon manifesti dondurması"),
    ("release_candidate_manifest_freeze", "data/lake/advanced_final_hardening/manifest", "Phase 159 release candidate manifesti dondurması"),
    ("portfolio_acceptance_manifest_freeze", "data/lake/advanced_portfolio_acceptance/manifest", "Phase 157 portföy kabul manifesti dondurması"),
    ("ml_acceptance_manifest_freeze", "data/lake/advanced_ml_acceptance/manifest", "Phase 145 makine öğrenimi kabul manifesti dondurması"),
]


def build_final_manifest_freeze_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build manifest freeze contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for freeze_name, scope, desc in MANIFEST_FREEZE_ITEMS:
        rows.append({
            "freeze_name": freeze_name,
            "freeze_category": "manifest",
            "target_scope": scope,
            "description": desc,
            "frozen": True,
            "actual_lock_enacted": False,
            "modifications_allowed_without_review": False,
            "domain": MANIFEST_FREEZE_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "freeze_item_count": len(rows),
        "current_phase": active_profile.current_phase,
        "all_frozen": bool(df["frozen"].all()),
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
