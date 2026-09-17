# -*- coding: utf-8 -*-
"""Phase 159: Final Feature Store Inventory.

Inventories Feature Store accessor methods and interfaces.
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

FEATURE_STORE_INTERFACES = [
    ("final_hardening_accessors", "ml/feature_store.py:load_final_hardening_*", "Phase 159 final hardening okuma arayüzleri"),
    ("full_system_integration_accessors", "ml/feature_store.py:load_full_system_integration_*", "Phase 158 sistem entegrasyon okuma arayüzleri"),
    ("portfolio_acceptance_accessors", "ml/feature_store.py:load_portfolio_acceptance_*", "Phase 157 portföy kabul okuma arayüzleri"),
    ("backtest_acceptance_accessors", "ml/feature_store.py:load_backtest_acceptance_*", "Phase 151 backtest okuma arayüzleri"),
    ("ml_acceptance_accessors", "ml/feature_store.py:load_ml_acceptance_*", "Phase 145 ML kabul okuma arayüzleri"),
]


def build_final_feature_store_inventory_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build Feature Store inventory registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for iface_name, path, desc in FEATURE_STORE_INTERFACES:
        rows.append({
            "item_id": f"FS-{iface_name}",
            "inventory_type": "feature_store_interface",
            "item_name": iface_name,
            "item_path_or_identifier": path,
            "description": desc,
            "metadata_only": True,
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
        "interface_count": len(rows),
        "all_metadata_only": bool(df["metadata_only"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
