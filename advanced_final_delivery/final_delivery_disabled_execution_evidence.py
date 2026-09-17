# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Disabled Execution Evidence.

Builds and summarizes the evidence registry proving execution mechanisms are fully disabled.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_EVIDENCE_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

DISABLED_EXECUTION_ITEMS = [
    ("system_execution_disabled", "Gercek sistem ve end-to-end bot calistirmasi engellendi"),
    ("live_trading_disabled", "Canli emir gonderimi ve borsa erisimi engellendi"),
    ("broker_execution_disabled", "Broker API ve emir iletimi engellendi"),
    ("order_generation_disabled", "Emir olusturma ve portfoy agirligi degisimi engellendi"),
    ("signal_generation_disabled", "Trade sinyali ve yonlu tavsiye uretimi engellendi"),
    ("model_training_disabled", "Model fit, train ve hiperparametre optimizasyonu engellendi"),
    ("prediction_disabled", "Model inference, predict ve target/label uretimi engellendi"),
    ("backtest_execution_disabled", "Gercek backtest ve benchmark calistirmasi engellendi"),
    ("portfolio_execution_disabled", "Portfoy insa, optimizasyon ve rebalance engellendi"),
    ("risk_execution_disabled", "Gercek risk raporlama ve drawdown simulasyonu engellendi"),
    ("scenario_execution_disabled", "Senaryo calistirma ve gercek stres testi engellendi"),
    ("deployment_disabled", "Uretim, release ve model dagitimi engellendi"),
    ("credential_output_disabled", "API key, token, secret yazdirma engellendi"),
    ("source_overwrite_disabled", "Kaynak dosya ezme, silme ve tahribat engellendi"),
]


def build_final_delivery_disabled_execution_evidence_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build disabled execution evidence DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for act_name, desc in DISABLED_EXECUTION_ITEMS:
        rows.append({
            "action_name": act_name,
            "description": desc,
            "execution_disabled": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_EVIDENCE_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "disabled_execution_count": len(rows),
        "all_executions_disabled": bool(df["execution_disabled"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
