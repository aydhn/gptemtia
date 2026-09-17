# -*- coding: utf-8 -*-
"""Phase 159: Final Safety Freeze Contracts."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    SAFETY_FREEZE_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

SAFETY_FREEZE_ITEMS = [
    ("no_live_trading_freeze", "execution_policy", "Canlı emir gönderiminin kesin olarak devre dışı bırakılması ve dondurulması"),
    ("no_broker_integration_freeze", "execution_policy", "Broker bağlantısının kesin olarak devre dışı bırakılması ve dondurulması"),
    ("no_signal_generation_freeze", "signal_policy", "AL/SAT sinyali veya yatırım tavsiyesi üretiminin kesin olarak engellenmesi"),
    ("no_production_deployment_freeze", "deployment_policy", "Production veya release sunucusuna aktarımın kilitlenmesi"),
    ("no_destructive_ops_freeze", "data_policy", "Kaynak veri ezme, silme ve tahribatlı işlemlerin kilitlenmesi"),
    ("no_scraping_no_secrets_freeze", "security_policy", "Web scraping ve secret/credential basımının engellenmesi"),
]


def build_final_safety_freeze_contract_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build safety freeze contract registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for freeze_name, scope, desc in SAFETY_FREEZE_ITEMS:
        rows.append({
            "freeze_name": freeze_name,
            "freeze_category": "safety",
            "target_scope": scope,
            "description": desc,
            "frozen": True,
            "actual_lock_enacted": False,
            "modifications_allowed_without_review": False,
            "domain": SAFETY_FREEZE_DOMAIN,
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
