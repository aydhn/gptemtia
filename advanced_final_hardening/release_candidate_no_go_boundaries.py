# -*- coding: utf-8 -*-
"""Phase 159: Release Candidate NO-GO Boundaries.

Defines non-negotiable NO-GO boundaries for Release Candidate status.
Intercepts and rejects prohibited deployment, trading, and execution actions.
"""

from typing import Dict, Tuple, Union
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    RELEASE_CANDIDATE_BOUNDARY_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

RC_NO_GO_ACTIONS = [
    ("live_trading", "Canlı piyasa işlem ve emir iletimi"),
    ("broker_execution", "Broker API aracılığıyla işlem yapma"),
    ("production_deployment", "Canlı production sunucusuna yükleme"),
    ("release_deployment", "Harici release ortamına aktarma"),
    ("model_deployment", "Model servislerini canlıya alma"),
    ("investment_advice", "Yatırım tavsiyesi sunma veya sinyal önerme"),
    ("signal_generation", "Doğrudan kesin trade sinyali üretme"),
    ("order_generation", "Gerçek emir nesneleri türetme"),
    ("model_training", "Gerçek model eğitimi veya ağırlık güncelleme"),
    ("prediction", "Gerçek zamanlı model tahmini/inference"),
    ("target_label_generation", "Etiket/hedef değişken üretimi"),
    ("backtest_execution", "Gerçek zamanlı backtest simülasyonu"),
    ("benchmark_execution", "Canlı benchmark hesaplaması"),
    ("portfolio_execution", "Gerçek portföy oluşturma/yeniden dengeleme"),
    ("risk_execution", "Gerçek risk limit hesaplama çalıştırması"),
    ("scenario_execution", "Gerçek senaryo simülasyon çalıştırması"),
    ("optimizer_execution", "Optimizatör çalıştırma"),
    ("metric_calculation", "Performans metriği hesaplama"),
    ("model_registry_write", "Model registry üzerine yazma"),
    ("artifact_persistence", "Model ağırlık artifact'ı saklama"),
    ("scraping", "Web scraping ve harici veri çekme"),
    ("credential_output", "Gizli anahtar veya credential yazdırma"),
    ("source_overwrite", "Kaynak veriyi veya kodu ezme"),
    ("file_deletion", "Dosya silme"),
    ("destructive_cleaning", "Tahribatlı veri temizliği yapma"),
]


def build_release_candidate_no_go_boundary_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build release candidate NO-GO boundary registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for action, desc in RC_NO_GO_ACTIONS:
        rows.append({
            "boundary_id": f"RC-NOGO-{action}",
            "boundary_type": "no_go",
            "action_name": action,
            "policy": "STRICTLY_PROHIBITED",
            "reason": desc,
            "enforced": True,
            "domain": RELEASE_CANDIDATE_BOUNDARY_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "no_go_boundary_count": len(rows),
        "all_enforced": bool(df["enforced"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary


def validate_release_candidate_no_go_request(request: Union[Dict, str]) -> Dict:
    """Validate and intercept incoming release candidate requests against NO-GO boundaries."""
    req_text = request if isinstance(request, str) else str(request).lower()
    blocked_actions = [item[0] for item in RC_NO_GO_ACTIONS]

    matched = [act for act in blocked_actions if act in req_text]
    is_blocked = len(matched) > 0

    return {
        "request": req_text,
        "is_blocked": is_blocked,
        "matched_no_go_actions": matched,
        "policy_verdict": "BLOCKED_BY_RC_NO_GO_POLICY" if is_blocked else "CLEARED_FOR_LOCAL_INSPECTION",
        "status": "BLOCKED" if is_blocked else "CLEARED",
    }
