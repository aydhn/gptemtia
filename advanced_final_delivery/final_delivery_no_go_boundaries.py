# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery No-Go Boundaries.

Builds and validates no-go boundary rules strictly prohibiting unsafe actions
including live trading, broker execution, model training, prediction, and deployment.
"""

from typing import Dict, Tuple, Union
import re
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_BOUNDARY_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

NO_GO_RULES = [
    ("live_trading", "Canli emir gonderimi, canli borsa islemleri ve gercek alim-satim"),
    ("broker_execution", "Broker API baglantisi ve emir iletim altyapisi"),
    ("production_deployment", "Uretim ortamina resmi onay ve otomatik dagitim"),
    ("release_deployment", "Release candidate paketini canliya dagitma"),
    ("model_deployment", "Modeli uretim API'sine veya servisine dagitma"),
    ("investment_advice", "Yatirim tavsiyesi, kesin AL/SAT veya pozisyon onerisi"),
    ("signal_generation", "Trade sinyali veya yonlu gosterge uretimi"),
    ("order_generation", "Alis/satis emri veya portfoy agirligi degisimi"),
    ("model_training", "Gercek model fit, train ve hiperparametre egitimi"),
    ("prediction", "Gercek model inference, predict ve cikarim uretimi"),
    ("target_label_generation", "Hedef etiket veya ileriye donuk getiri uretimi"),
    ("backtest_execution", "Gercek backtest veya benchmark simülasyonu"),
    ("benchmark_execution", "Gercek referans strateji karsilastirmasi"),
    ("portfolio_execution", "Gercek portfoy insasi ve sermaye tahsisi"),
    ("risk_execution", "Gercek risk raporlama ve limit izleme"),
    ("scenario_execution", "Gercek portfoy senaryo testi ve drawdown kontrolu"),
    ("optimizer_execution", "Gercek matematiksel portfoy optimizasyonu"),
    ("metric_calculation", "Gercek performans ve risk metrigi hesaplama"),
    ("model_registry_write", "Model registry'ye model kaydetme"),
    ("artifact_persistence", "Model agirlik veya binary artifact kaydetme"),
    ("scraping", "Web kazima, HTML indirme ve paywall asma"),
    ("credential_output", "API key, token, gizli anahtar ve secret yazdirma"),
    ("source_overwrite", "Kaynak veri dosyalarini ezme veya degistirme"),
    ("file_deletion", "Proje veya kaynak dosyalarini silme"),
    ("destructive_cleaning", "Yikici veri temizligi veya otomatik sutun dusurme"),
]


def build_final_delivery_no_go_boundary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build no-go boundary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for r_name, desc in NO_GO_RULES:
        rows.append({
            "rule_name": r_name,
            "description": desc,
            "strictly_prohibited": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_BOUNDARY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "no_go_rule_count": len(rows),
        "all_strictly_prohibited": bool(df["strictly_prohibited"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def validate_final_delivery_no_go_request(request: Union[dict, str]) -> dict:
    """Validate a request against no-go rules. Rejects any prohibited action."""
    text = ""
    if isinstance(request, dict):
        text = " ".join(str(v) for v in request.values())
    else:
        text = str(request)

    text_lower = text.lower()
    prohibited_matches = []

    prohibited_patterns = [
        r"\blive[_\s-]?trad",
        r"\bbroker[_\s-]?exec",
        r"\bbroker[_\s-]?order",
        r"\bdeploy",
        r"\bpredict",
        r"\btrain\b",
        r"\bfit\b",
        r"\binference\b",
        r"\bmodel[_\s-]?registry[_\s-]?write\b",
        r"\bartifact[_\s-]?persist\b",
        r"\bscrap",
        r"\bcredential",
        r"\bapi[_\s-]?key",
        r"\bsecret\b",
        r"\btoken\b",
        r"\boverwrite",
        r"\bdelet",
        r"\bdestructive",
        r"\bbacktest\b",
        r"\boptimiz",
        r"\bportfoli[_\s-]?exec",
        r"\brisk[_\s-]?exec",
        r"\bscenar[_\s-]?exec",
    ]

    for pat in prohibited_patterns:
        if re.search(pat, text_lower):
            prohibited_matches.append(pat)

    is_safe = len(prohibited_matches) == 0
    return {
        "is_safe": is_safe,
        "prohibited_matches": prohibited_matches,
        "message": "Request blocked by NO-GO policy" if not is_safe else "Request passes NO-GO policy",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if is_safe else "BLOCKED_BY_NO_GO_POLICY",
    }
