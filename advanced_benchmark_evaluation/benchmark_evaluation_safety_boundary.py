# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Safety Boundary Module.

Defines explicit NO-GO barriers and SAFE-GO principles for Phase 151.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_SAFETY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

NO_GO_CONDITIONS: List[Dict[str, str]] = [
    {"rule_id": "NOGO_01", "rule": "Canlı emir iletimi, hesap yönetimi veya piyasa işlemleri kesinlikle yasaktır."},
    {"rule_id": "NOGO_02", "rule": "Aracı kurum (broker) API entegrasyonu veya ağ çağrıları kesinlikle yasaktır."},
    {"rule_id": "NOGO_03", "rule": "Kesin al/sat sinyali veya yatırım tavsiyesi üretilemez."},
    {"rule_id": "NOGO_04", "rule": "Gerçek backtest simülasyonu veya motor yürütmesi başlatılamaz."},
    {"rule_id": "NOGO_05", "rule": "Gerçek benchmark simülasyon yürütmesi yapılamaz."},
    {"rule_id": "NOGO_06", "rule": "Gerçek Sharpe, win-rate, getiri, alpha veya drawdown hesaplanamaz."},
    {"rule_id": "NOGO_07", "rule": "Sonuç veya getiri iddiaları (result claim / performance claim) üretilemez."},
    {"rule_id": "NOGO_08", "rule": "Strateji resmi onayı (strategy approval) verilemez."},
    {"rule_id": "NOGO_09", "rule": "Sermaye tahsisi, lot büyüklüğü (position sizing) veya portföy oluşturulamaz."},
    {"rule_id": "NOGO_10", "rule": "Parametre optimizasyonu, curve-fitting veya grid search çalıştırılamaz."},
    {"rule_id": "NOGO_11", "rule": "Makine öğrenmesi model eğitimi, fit veya tahmin (prediction) üretimi yapılamaz."},
    {"rule_id": "NOGO_12", "rule": "Model artifact kaydı veya model registry yazımı yapılamaz."},
    {"rule_id": "NOGO_13", "rule": "Üretim ortamına dağıtım veya canlı servis açılamaz."},
    {"rule_id": "NOGO_14", "rule": "Haber tam metni, HTML kazıma, embedding veya NLP duygu modelleri kullanılamaz."},
    {"rule_id": "NOGO_15", "rule": "Kaynak verilerin üzerine yazma veya yıkıcı veri temizliği yapılamaz."},
]

SAFE_GO_CONDITIONS: List[Dict[str, str]] = [
    {"rule_id": "SAFEGO_01", "rule": "Yerel ve çevrimdışı benchmark karşılaştırma raporu sözleşmeleri tanımlanabilir."},
    {"rule_id": "SAFEGO_02", "rule": "Yerel ve çevrimdışı strateji değerlendirme raporu sözleşmeleri tanımlanabilir."},
    {"rule_id": "SAFEGO_03", "rule": "Hesaplanmamış performans ve risk metrik yer tutucuları oluşturulabilir."},
    {"rule_id": "SAFEGO_04", "rule": "Yasal ve ampirik rapor feragatnameleri üretilebilir."},
    {"rule_id": "SAFEGO_05", "rule": "Sonuç iddialarını ve izinsiz onayları engelleyen muhafızlar tanımlanabilir."},
    {"rule_id": "SAFEGO_06", "rule": "Devre dışı bırakılmış yürütme motorları resmi raporları oluşturulabilir."},
    {"rule_id": "SAFEGO_07", "rule": "Phase 152 Backtest Kabul Raporu için devir şartnamesi ve kabul hazırlığı yapılabilir."},
]


def build_benchmark_evaluation_no_go_conditions(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of NO-GO safety rules."""
    df = pd.DataFrame(NO_GO_CONDITIONS)
    df["status"] = "ENFORCED"
    df["non_signal"] = True
    return df, {"total_no_go": len(df), "all_enforced": True, "non_signal": True}


def build_benchmark_evaluation_safe_go_conditions(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of SAFE-GO principles."""
    df = pd.DataFrame(SAFE_GO_CONDITIONS)
    df["status"] = "ACTIVE"
    df["non_signal"] = True
    return df, {"total_safe_go": len(df), "all_active": True, "non_signal": True}


def build_benchmark_evaluation_safety_boundary(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build consolidated safety boundary report."""
    df_nogo, s_nogo = build_benchmark_evaluation_no_go_conditions(profile)
    df_safego, s_safego = build_benchmark_evaluation_safe_go_conditions(profile)

    combined = pd.concat([df_nogo, df_safego], ignore_index=True)
    summary = {
        "domain": LABEL_SAFETY_DOMAIN,
        "safety_status": "SECURE",
        "no_go_count": len(df_nogo),
        "safe_go_count": len(df_safego),
        "live_trading_prohibited": True,
        "broker_prohibited": True,
        "all_boundaries_enforced": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return combined, summary
