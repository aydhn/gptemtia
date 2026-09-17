# -*- coding: utf-8 -*-
"""Phase 159: Operator Incident Response Placeholders.

Defines placeholder definitions for incident response protocols.
Contract/documentation only; does not hook into live alerting or monitoring.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    OPERATOR_PROTOCOL_DOMAIN,
    OPERATOR_RUNBOOK_CONTRACT_READY,
)

INCIDENTS = [
    ("INC-01", "live_trading_attempt_detected", "Yetkisiz canlı emir çağrısı teşebbüsü tespiti", "Immediate block and log"),
    ("INC-02", "broker_key_present_in_env", "Ortam değişkeninde gerçek broker API key varlığı tespiti", "Immediate halt and warning"),
    ("INC-03", "data_corruption_detected", "DataLake CSV dosyasında bozulma veya erişim hatası", "Run health check and rebuild"),
]


def build_operator_incident_response_placeholder_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build incident response placeholder registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for inc_id, name, desc, action in INCIDENTS:
        rows.append({
            "incident_id": inc_id,
            "incident_name": name,
            "description": desc,
            "recommended_action": action,
            "is_live_alert": False,
            "domain": OPERATOR_PROTOCOL_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": OPERATOR_RUNBOOK_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "incident_count": len(rows),
        "is_live_alert": bool(df["is_live_alert"].any()),
        "current_phase": active_profile.current_phase,
        "status": OPERATOR_RUNBOOK_CONTRACT_READY,
    }
    return df, summary
