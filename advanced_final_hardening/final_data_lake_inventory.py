# -*- coding: utf-8 -*-
"""Phase 159: Final Data Lake Inventory.

Inventories Data Lake storage domains and paths.
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

DATA_LAKE_DOMAINS = [
    ("advanced_final_hardening", "data/lake/advanced_final_hardening/", "Phase 159 final hardening depolama alanı"),
    ("advanced_full_system_integration", "data/lake/advanced_full_system_integration/", "Phase 158 sistem entegrasyon alanı"),
    ("advanced_portfolio_acceptance", "data/lake/advanced_portfolio_acceptance/", "Phase 157 portföy kabul depolama alanı"),
    ("advanced_risk_reporting", "data/lake/advanced_risk_reporting/", "Phase 154 risk raporlama depolama alanı"),
    ("advanced_backtest_acceptance", "data/lake/advanced_backtest_acceptance/", "Phase 151 backtest kabul depolama alanı"),
    ("advanced_ml_acceptance", "data/lake/advanced_ml_acceptance/", "Phase 145 ML kabul depolama alanı"),
    ("raw_commodities", "data/lake/commodities/", "Emtia ham veri ambarı"),
    ("raw_forex", "data/lake/forex/", "Döviz ham veri ambarı"),
]


def build_final_data_lake_inventory_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build Data Lake inventory registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for dl_name, path, desc in DATA_LAKE_DOMAINS:
        rows.append({
            "item_id": f"DL-{dl_name}",
            "inventory_type": "data_lake_domain",
            "item_name": dl_name,
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
        "domain_count": len(rows),
        "all_metadata_only": bool(df["metadata_only"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
