# -*- coding: utf-8 -*-
"""Phase 159: Release Candidate Warnings."""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    WARNING_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

STANDARD_WARNINGS = [
    ("WARN-01", "contract_only_release_candidate", "Bu sürüm adayı bir sözleşme katmanıdır; gerçek production release değildir."),
    ("WARN-02", "placeholder_only_evidence", "Tüm yedekleme ve kurtarma mekanizmaları yerel simülasyon ve sözleşme seviyesindedir."),
    ("WARN-03", "no_real_system_execution", "Sistem tam otomasyonla çalıştırılmamıştır; canlı bot işletimi kapalıdır."),
    ("WARN-04", "no_live_trading", "Canlı alım satım emirleri kesinlikle bloke edilmiştir."),
    ("WARN-05", "no_broker_execution", "Broker API entegrasyonu tamamen devre dışıdır."),
    ("WARN-06", "no_production_deployment", "Canlı sunucuya dağıtım yapılmamıştır ve onaylanmamıştır."),
    ("WARN-07", "no_release_deployment", "Harici ortama release aktarımı yapılmamıştır."),
    ("WARN-08", "no_model_registry_write", "Model registry üzerine hiçbir kayıt yazılmamıştır."),
    ("WARN-09", "no_artifact_persistence", "Hiçbir model ağırlığı diske kaydedilmemiştir."),
    ("WARN-10", "no_prediction", "Canlı tahmin veya inference yürütülmemiştir."),
    ("WARN-11", "no_signal_generation", "Hiçbir AL/SAT sinyali veya yatırım tavsiyesi üretilmemiştir."),
    ("WARN-12", "manual_review_required", "Tüm kritik adımlar için insan operatör incelemesi zorunludur."),
    ("WARN-13", "phase_160_must_remain_non_live", "Phase 160 nihai teslimatı da canlı işlem ve broker kilitlerini korumak zorundadır."),
]


def build_release_candidate_warning_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build warning registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for w_id, name, desc in STANDARD_WARNINGS:
        rows.append({
            "warning_id": w_id,
            "warning_name": name,
            "warning_text": desc,
            "is_acknowledged": True,
            "domain": WARNING_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "warning_count": len(rows),
        "all_acknowledged": bool(df["is_acknowledged"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
