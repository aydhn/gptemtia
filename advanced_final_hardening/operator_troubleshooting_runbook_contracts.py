# -*- coding: utf-8 -*-
"""Phase 159: Operator Troubleshooting Runbook Contracts."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    TROUBLESHOOTING_DOMAIN,
    OPERATOR_RUNBOOK_CONTRACT_READY,
)

TROUBLESHOOTING_SCENARIOS = [
    ("missing_lake_directory", "Dizin eksikliği", "config/paths.py:ensure_project_directories() fonksiyonunu çağırarak dizinleri oluşturun."),
    ("validation_failure", "Doğrulama hatası", "Hata veren sözleşme satırını inceleyin; yasaklı bayrak veya eksik parametreyi düzeltin."),
    ("live_trading_attempt", "Canlı işlem talebi", "İşlem politikası gereği engellendi. config/settings.py içinde allow_live_trading=False kalmalıdır."),
    ("broker_integration_attempt", "Broker API talebi", "İşlem politikası gereği engellendi. Broker anahtarları eklenemez, simülasyon salt yerel kalmalıdır."),
    ("low_readiness_score", "Düşük hazır oluş skoru", "Blocker ve gap kayıtlarını inceleyin; eksik rapor veya dokümantasyonu tamamlayın."),
]


def build_operator_troubleshooting_runbook_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build operator troubleshooting runbook contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for sc_id, issue, solution in TROUBLESHOOTING_SCENARIOS:
        rows.append({
            "scenario_id": sc_id,
            "issue_title": issue,
            "recommended_action": solution,
            "requires_destructive_action": False,
            "domain": TROUBLESHOOTING_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": OPERATOR_RUNBOOK_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "scenario_count": len(rows),
        "no_destructive_action": bool((~df["requires_destructive_action"]).all()),
        "current_phase": active_profile.current_phase,
        "status": OPERATOR_RUNBOOK_CONTRACT_READY,
    }
    return df, summary
