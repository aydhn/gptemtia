# -*- coding: utf-8 -*-
"""Phase 159: Operator NO-GO Protocols.

Defines NO-GO boundaries and request validation to intercept and block
any unauthorized execution requests (live trading, broker, orders, etc.).
"""

from typing import Dict, Tuple, Union
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    NO_GO_PROTOCOL_DOMAIN,
    OPERATOR_RUNBOOK_CONTRACT_READY,
)

NO_GO_RULES = [
    ("NOGO-01", "live_trading_request", "Canlı piyasa alım/satım işlemi talebi", "BLOCK_IMMEDIATELY"),
    ("NOGO-02", "broker_connection_request", "Broker API anahtarı veya bağlantı talebi", "BLOCK_IMMEDIATELY"),
    ("NOGO-03", "signal_issuance_request", "Kesin AL/SAT veya yönlü tavsiye üretme talebi", "BLOCK_IMMEDIATELY"),
    ("NOGO-04", "production_deploy_request", "Canlı sunucu veya release deployment talebi", "BLOCK_IMMEDIATELY"),
    ("NOGO-05", "model_inference_request", "Gerçek zamanlı model tahmini veya inference talebi", "BLOCK_IMMEDIATELY"),
    ("NOGO-06", "order_generation_request", "Gerçek emir nesnesi oluşturma talebi", "BLOCK_IMMEDIATELY"),
    ("NOGO-07", "source_overwrite_request", "Kaynak veri dosyalarını silme veya ezme talebi", "BLOCK_IMMEDIATELY"),
    ("NOGO-08", "credential_leak_request", "API anahtarı veya parola yazdırma talebi", "BLOCK_IMMEDIATELY"),
]


def build_operator_no_go_protocol_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build operator NO-GO protocol registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for rule_id, target, desc, action in NO_GO_RULES:
        rows.append({
            "protocol_id": rule_id,
            "target_request": target,
            "description": desc,
            "action": action,
            "enforced": True,
            "domain": NO_GO_PROTOCOL_DOMAIN,
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


def validate_operator_no_go_request(request: Union[Dict, str]) -> Dict:
    """Validate and intercept incoming requests against NO-GO rules."""
    req_text = request if isinstance(request, str) else str(request).lower()
    blocked_keywords = [
        "live_trading", "broker", "send_order", "real_order", "buy_signal",
        "sell_signal", "deploy_production", "release_deploy", "model_predict",
        "delete_data", "source_overwrite", "api_key"
    ]

    matched_keywords = [kw for kw in blocked_keywords if kw in req_text]
    is_blocked = len(matched_keywords) > 0

    return {
        "request": req_text,
        "is_blocked": is_blocked,
        "matched_violations": matched_keywords,
        "policy_action": "BLOCK_BY_NO_GO_POLICY" if is_blocked else "PASS_LOCAL_CHECK",
        "status": "BLOCKED" if is_blocked else "CLEARED",
    }
