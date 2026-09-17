# -*- coding: utf-8 -*-
"""Phase 159: Operator Safe Usage Protocols."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    SAFE_USAGE_PROTOCOL_DOMAIN,
    OPERATOR_RUNBOOK_CONTRACT_READY,
)

SAFE_USAGE_RULES = [
    ("SUR-01", "research_only_boundary", "Sistem yalnızca yerel akademik ve araştırma amaçlı kullanılabilir."),
    ("SUR-02", "no_live_orders", "Canlı finansal piyasalara emir iletilemez veya işlem yapılamaz."),
    ("SUR-03", "no_broker_credentials", "Broker hesap anahtarları veya şifreleri sisteme girilemez."),
    ("SUR-04", "no_financial_advice", "Üretilen hiçbir analiz veya skor yatırım tavsiyesi olarak sunulamaz."),
    ("SUR-05", "offline_first", "Sistem harici internet araması veya web scraping yapmadan yerel çalışır."),
]


def build_operator_safe_usage_protocol_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build operator safe usage protocol registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for sur_id, name, desc in SAFE_USAGE_RULES:
        rows.append({
            "protocol_id": sur_id,
            "protocol_name": name,
            "description": desc,
            "enforced": True,
            "domain": SAFE_USAGE_PROTOCOL_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": OPERATOR_RUNBOOK_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "rule_count": len(rows),
        "all_enforced": bool(df["enforced"].all()),
        "current_phase": active_profile.current_phase,
        "status": OPERATOR_RUNBOOK_CONTRACT_READY,
    }
    return df, summary
