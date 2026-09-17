# -*- coding: utf-8 -*-
"""Phase 159: Final Script Inventory.

Inventories key execution and verification scripts across all phases.
Metadata only; does not execute any script.
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

SCRIPT_INVENTORY = [
    ("run_final_hardening_profile_registry.py", "scripts/run_final_hardening_profile_registry.py", "Phase 159 Profil ve kapsam kayıtları çalıştırıcısı"),
    ("run_final_hardening_contracts.py", "scripts/run_final_hardening_contracts.py", "Phase 159 Hardening sözleşmeleri çalıştırıcısı"),
    ("run_operator_runbook_contracts.py", "scripts/run_operator_runbook_contracts.py", "Phase 159 Operatör runbook sözleşmeleri çalıştırıcısı"),
    ("run_release_candidate_checklists.py", "scripts/run_release_candidate_checklists.py", "Phase 159 Release candidate kontrol listesi çalıştırıcısı"),
    ("run_final_freeze_audits.py", "scripts/run_final_freeze_audits.py", "Phase 159 Dondurma denetimleri çalıştırıcısı"),
    ("run_final_inventory_reports.py", "scripts/run_final_inventory_reports.py", "Phase 159 Sistem envanter raporları çalıştırıcısı"),
    ("run_release_candidate_boundaries.py", "scripts/run_release_candidate_boundaries.py", "Phase 159 Release candidate sınırları çalıştırıcısı"),
    ("run_release_candidate_findings_manifest.py", "scripts/run_release_candidate_findings_manifest.py", "Phase 159 Bulgular ve manifest çalıştırıcısı"),
    ("run_final_hardening_health_check.py", "scripts/run_final_hardening_health_check.py", "Phase 159 Sistem sağlık kontrolü çalıştırıcısı"),
    ("run_final_hardening_validation_report.py", "scripts/run_final_hardening_validation_report.py", "Phase 159 Doğrulama ve güvenlik raporu çalıştırıcısı"),
    ("run_release_candidate_status.py", "scripts/run_release_candidate_status.py", "Phase 159 Çıktı ve durum listeleme çalıştırıcısı"),
    ("run_full_system_integration_health_check.py", "scripts/run_full_system_integration_health_check.py", "Phase 158 Sistem entegrasyon sağlık kontrolü"),
    ("run_full_system_integration_profile_registry.py", "scripts/run_full_system_integration_profile_registry.py", "Phase 158 Profil kayıt çalıştırıcısı"),
    ("run_portfolio_acceptance_health_check.py", "scripts/run_portfolio_acceptance_health_check.py", "Phase 157 Portföy kabul sağlık kontrolü"),
    ("run_backtest_acceptance_health_check.py", "scripts/run_backtest_acceptance_health_check.py", "Phase 151 Backtest kabul sağlık kontrolü"),
]


def build_final_script_inventory_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build script inventory registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for s_name, path, desc in SCRIPT_INVENTORY:
        rows.append({
            "item_id": f"SCR-{s_name}",
            "inventory_type": "script",
            "item_name": s_name,
            "item_path_or_identifier": path,
            "description": desc,
            "metadata_only": True,
            "execution_blocked": True,
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
        "script_count": len(rows),
        "all_metadata_only": bool(df["metadata_only"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
