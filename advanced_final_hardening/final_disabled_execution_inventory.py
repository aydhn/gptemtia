# -*- coding: utf-8 -*-
"""Phase 159: Final Disabled Execution Inventory.

Explicitly inventories all blocked/disabled execution pathways across the system.
Guarantees at the registry level that no trading, broker, or real model executions occur.
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
    EXECUTION_BLOCKED_NO_LIVE_TRADING,
    EXECUTION_BLOCKED_NO_BROKER,
    EXECUTION_BLOCKED_NO_ORDER_GENERATION,
    EXECUTION_BLOCKED_NO_SIGNAL_GENERATION,
    EXECUTION_BLOCKED_NO_SYSTEM_EXECUTION,
    EXECUTION_BLOCKED_NO_END_TO_END_RUN,
    EXECUTION_BLOCKED_NO_PRODUCTION_DEPLOYMENT,
    EXECUTION_BLOCKED_NO_RELEASE_DEPLOYMENT,
    EXECUTION_BLOCKED_NO_MODEL_TRAINING,
    EXECUTION_BLOCKED_NO_PREDICTION,
    EXECUTION_BLOCKED_NO_MODEL_REGISTRY_WRITE,
    EXECUTION_BLOCKED_NO_ARTIFACT_PERSISTENCE,
)

DISABLED_ACTIONS = [
    ("live_trading", EXECUTION_BLOCKED_NO_LIVE_TRADING, "Canlı piyasa alım/satım işlemleri"),
    ("broker_integration", EXECUTION_BLOCKED_NO_BROKER, "Broker API bağlantısı ve emir iletimi"),
    ("order_generation", EXECUTION_BLOCKED_NO_ORDER_GENERATION, "Gerçek emir nesnesi oluşturma"),
    ("signal_generation", EXECUTION_BLOCKED_NO_SIGNAL_GENERATION, "Doğrudan AL/SAT trade sinyali üretimi"),
    ("system_execution", EXECUTION_BLOCKED_NO_SYSTEM_EXECUTION, "Gerçek full-system bot işletimi"),
    ("end_to_end_run", EXECUTION_BLOCKED_NO_END_TO_END_RUN, "Uçtan uca otomatik döngü çalıştırma"),
    ("production_deployment", EXECUTION_BLOCKED_NO_PRODUCTION_DEPLOYMENT, "Canlı sunucuya deploy etme"),
    ("release_deployment", EXECUTION_BLOCKED_NO_RELEASE_DEPLOYMENT, "Release adresi veya dış sunucuya aktarma"),
    ("model_training", EXECUTION_BLOCKED_NO_MODEL_TRAINING, "Gerçek zamanlı model eğitimi veya fit etme"),
    ("model_predict", EXECUTION_BLOCKED_NO_PREDICTION, "Canlı model inference ve tahmin yürütme"),
    ("model_registry_write", EXECUTION_BLOCKED_NO_MODEL_REGISTRY_WRITE, "Model registry üzerine kayıt yazma"),
    ("artifact_persistence", EXECUTION_BLOCKED_NO_ARTIFACT_PERSISTENCE, "Model ağırlık artifact'ı saklama"),
]


def build_final_disabled_execution_inventory_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build disabled execution inventory registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for action, label, desc in DISABLED_ACTIONS:
        rows.append({
            "action_name": action,
            "execution_label": label,
            "description": desc,
            "is_disabled": True,
            "bypass_allowed": False,
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
        "disabled_action_count": len(rows),
        "all_disabled": bool(df["is_disabled"].all()),
        "no_bypass_allowed": bool((~df["bypass_allowed"]).all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
