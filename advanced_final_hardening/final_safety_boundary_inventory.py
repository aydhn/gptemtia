# -*- coding: utf-8 -*-
"""Phase 159: Final Safety Boundary Inventory.

Inventories active safety policies and boundary rules protecting the system.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    INVENTORY_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

SAFETY_BOUNDARIES = [
    ("SB-01", "no_live_trading_boundary", "Canlı emir ve işlem engelleme sınırı", "CRITICAL"),
    ("SB-02", "no_broker_boundary", "Broker entegrasyonu engelleme sınırı", "CRITICAL"),
    ("SB-03", "no_signals_boundary", "Trade tavsiyesi ve sinyal engelleme sınırı", "CRITICAL"),
    ("SB-04", "no_deploy_boundary", "Canlıya aktarım engelleme sınırı", "CRITICAL"),
    ("SB-05", "source_preservation_boundary", "Kaynak kod ve veriyi koruma sınırı", "HIGH"),
    ("SB-06", "no_scraping_boundary", "Web kazıma ve harici istek engelleme sınırı", "HIGH"),
    ("SB-07", "no_credential_boundary", "Kimlik ve anahtar sızıntısı engelleme sınırı", "CRITICAL"),
]


def build_final_safety_boundary_inventory_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build safety boundary inventory registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for sb_id, name, desc, sev in SAFETY_BOUNDARIES:
        rows.append({
            "boundary_id": sb_id,
            "boundary_name": name,
            "description": desc,
            "severity": sev,
            "enforced": True,
            "domain": INVENTORY_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "boundary_count": len(rows),
        "all_enforced": bool(df["enforced"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
