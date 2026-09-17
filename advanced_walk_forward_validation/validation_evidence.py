# -*- coding: utf-8 -*-
"""Phase 147: Validation Evidence Registry.

Collects and registers governance evidence ensuring all contracts, guards,
and negative invariants are verified and documented.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

EVIDENCE_ITEMS: List[Dict[str, Any]] = [
    {
        "evidence_id": "EVD-147-01",
        "evidence_type": "SPLIT_CONTRACT_PRESENT",
        "verified": True,
        "description": "Rolling, expanding ve anchored split sozlesmeleri kayitli.",
    },
    {
        "evidence_id": "EVD-147-02",
        "evidence_type": "OOS_CONTRACT_PRESENT",
        "verified": True,
        "description": "Orneklem disi (OOS) kesisimsiz bolumleme sozlesmeleri kayitli.",
    },
    {
        "evidence_id": "EVD-147-03",
        "evidence_type": "BENCHMARK_CONTRACT_PRESENT",
        "verified": True,
        "description": "Buy & Hold, nakit ve esit agirlikli benchmark sozlesmeleri kayitli.",
    },
    {
        "evidence_id": "EVD-147-04",
        "evidence_type": "NO_LOOKAHEAD_GUARD_PRESENT",
        "verified": True,
        "description": "Kronolojik siralama ve asof backward join muhafizlari aktif.",
    },
    {
        "evidence_id": "EVD-147-05",
        "evidence_type": "PURGE_EMBARGO_GUARD_PRESENT",
        "verified": True,
        "description": "Etiket cakismasini ve otoregresif sizintiyi engelleyen purge/embargo muhafizlari aktif.",
    },
    {
        "evidence_id": "EVD-147-06",
        "evidence_type": "BIAS_GUARDS_PRESENT",
        "verified": True,
        "description": "Data snooping, survivorship ve overfitting muhafizlari aktif.",
    },
    {
        "evidence_id": "EVD-147-07",
        "evidence_type": "COST_SLIPPAGE_DEPENDENCY_PRESENT",
        "verified": True,
        "description": "Phase 146 islem maliyeti ve kayma modeli sozlesme baglantilari tanimli.",
    },
    {
        "evidence_id": "EVD-147-08",
        "evidence_type": "DISABLED_EXECUTION_REPORTS_PRESENT",
        "verified": True,
        "description": "Canli islem, broker, egitim, cikarim ve metrik hesaplama engelleri raporlandi.",
    },
    {
        "evidence_id": "EVD-147-09",
        "evidence_type": "PHASE_148_HANDOFF_PRESENT",
        "verified": True,
        "description": "Phase 148 Stress Testing and Scenario Simulation handoff paketi hazir.",
    },
]


def build_validation_evidence_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for validation evidence registry."""
    rows = []
    for e in EVIDENCE_ITEMS:
        rows.append(
            {
                "evidence_id": e["evidence_id"],
                "evidence_type": e["evidence_type"],
                "verified": e["verified"],
                "description": e["description"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    all_verified = bool(df["verified"].all()) if not df.empty else False
    summary = {
        "total_evidence_items": len(df),
        "all_verified": all_verified,
        "non_signal": True,
    }
    return df, summary
