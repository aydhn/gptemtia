# -*- coding: utf-8 -*-
"""Phase 159: Final Documentation Freeze Contracts."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    DOCUMENTATION_FREEZE_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

DOC_FREEZE_ITEMS = [
    ("architecture_doc_freeze", "docs/ARCHITECTURE.md", "Sistem mimarisi ve veri akış diyagramı dokümantasyon dondurması"),
    ("roadmap_doc_freeze", "docs/ROADMAP.md", "Faz yol haritası dondurması"),
    ("phase_log_doc_freeze", "docs/PHASE_LOG.md", "Tüm faz adımları kayıt günlüğü dondurması"),
    ("operator_manual_freeze", "docs/OPERATOR_MANUAL.md", "Operatör kullanım kılavuzu ve runbook dondurması"),
    ("analyst_handbook_freeze", "docs/ANALYST_HANDBOOK.md", "Araştırma analisti el kitabı dondurması"),
    ("safe_usage_guide_freeze", "docs/SAFE_USAGE_GUIDE.md", "Güvenli kullanım ve no-go sınırları dokümanı dondurması"),
    ("rc_checklist_freeze", "docs/RELEASE_CANDIDATE_CHECKLIST.md", "Release candidate kontrol listesi dokümanı dondurması"),
    ("final_hardening_guide_freeze", "docs/FINAL_HARDENING_GUIDE.md", "Final hardening kılavuzu dondurması"),
]


def build_final_documentation_freeze_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build documentation freeze contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for freeze_name, scope, desc in DOC_FREEZE_ITEMS:
        rows.append({
            "freeze_name": freeze_name,
            "freeze_category": "documentation",
            "target_scope": scope,
            "description": desc,
            "frozen": True,
            "actual_lock_enacted": False,
            "modifications_allowed_without_review": False,
            "domain": DOCUMENTATION_FREEZE_DOMAIN,
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
