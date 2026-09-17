# -*- coding: utf-8 -*-
"""Phase 159: Final Test Inventory.

Inventories key test modules across all phases.
Metadata only; does not invoke test execution.
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

TEST_INVENTORY = [
    ("test_final_hardening_config.py", "tests/test_final_hardening_config.py", "Phase 159 Konfigürasyon testleri"),
    ("test_final_hardening_labels.py", "tests/test_final_hardening_labels.py", "Phase 159 Etiket testleri"),
    ("test_final_hardening_models.py", "tests/test_final_hardening_models.py", "Phase 159 Veri modelleri testleri"),
    ("test_final_hardening_contracts.py", "tests/test_final_hardening_contracts.py", "Phase 159 Hardening sözleşmeleri testleri"),
    ("test_operator_runbook_contracts.py", "tests/test_operator_runbook_contracts.py", "Phase 159 Operatör runbook testleri"),
    ("test_release_candidate_contracts.py", "tests/test_release_candidate_contracts.py", "Phase 159 Release candidate sözleşme testleri"),
    ("test_full_system_integration_config.py", "tests/test_full_system_integration_config.py", "Phase 158 Sistem entegrasyon testleri"),
    ("test_portfolio_acceptance_config.py", "tests/test_portfolio_acceptance_config.py", "Phase 157 Portföy kabul testleri"),
    ("test_backtest_acceptance_config.py", "tests/test_backtest_acceptance_config.py", "Phase 151 Backtest kabul testleri"),
    ("test_phase_160_handoff.py", "tests/test_phase_160_handoff.py", "Phase 160 devir testleri"),
]


def build_final_test_inventory_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build test inventory registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for t_name, path, desc in TEST_INVENTORY:
        rows.append({
            "item_id": f"TST-{t_name}",
            "inventory_type": "test",
            "item_name": t_name,
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
        "test_count": len(rows),
        "all_metadata_only": bool(df["metadata_only"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
