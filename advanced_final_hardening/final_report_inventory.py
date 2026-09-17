# -*- coding: utf-8 -*-
"""Phase 159: Final Report Inventory.

Inventories report artifact families across all phases.
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

REPORT_FAMILIES = [
    ("advanced_final_hardening", "reports/output/advanced_final_hardening/", "Final hardening ve release candidate raporları"),
    ("advanced_full_system_integration", "reports/output/advanced_full_system_integration/", "Sistem entegrasyon ve kabul provası raporları"),
    ("advanced_portfolio_acceptance", "reports/output/advanced_portfolio_acceptance/", "Portföy kabul raporları"),
    ("advanced_backtest_acceptance", "reports/output/advanced_backtest_acceptance/", "Backtest kabul raporları"),
    ("advanced_risk_reporting", "reports/output/advanced_risk_reporting/", "Risk analizi raporları"),
    ("advanced_ml_acceptance", "reports/output/advanced_ml_acceptance/", "Makine öğrenimi kabul raporları"),
]


def build_final_report_inventory_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build report inventory registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for fam_name, path, desc in REPORT_FAMILIES:
        rows.append({
            "item_id": f"REP-{fam_name}",
            "inventory_type": "report_family",
            "item_name": fam_name,
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
        "report_family_count": len(rows),
        "all_metadata_only": bool(df["metadata_only"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
