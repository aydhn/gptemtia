# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Domain Registry Module.

Registers all official research, reporting, and evaluation domains with boundary definitions.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    ALL_DOMAINS,
    LABEL_BENCHMARK_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

DOMAIN_DESCRIPTIONS: Dict[str, str] = {
    "benchmark_evaluation_profile_domain": "Profil konfigürasyonları ve çalışma modu yönetişimi.",
    "benchmark_evaluation_domain": "Merkezi benchmark değerlendirme etki alanı.",
    "benchmark_evaluation_scope_domain": "Dahil edilen ve hariç tutulan araştırma kapsamları.",
    "benchmark_report_contract_domain": "Benchmark karşılaştırma raporu sözleşmeleri.",
    "strategy_evaluation_report_contract_domain": "Strateji değerlendirme raporu sözleşmeleri.",
    "benchmark_universe_report_domain": "Emtia ve FX benchmark referans evreni sözleşmeleri.",
    "benchmark_baseline_report_domain": "Pasif, nakit ve sepet temel referans stratejileri.",
    "strategy_vs_benchmark_report_domain": "Strateji ve benchmark görece karşılaştırma sözleşmeleri.",
    "cost_adjusted_evaluation_domain": "Komisyon ve finansman maliyeti düzeltilmiş değerlendirme.",
    "slippage_adjusted_evaluation_domain": "Fiyat kayması ve likidite etkisi düzeltilmiş değerlendirme.",
    "regime_aware_evaluation_domain": "Piyasa rejimlerine göre ayrıştırılmış değerlendirme.",
    "walk_forward_evaluation_domain": "Walk-forward pencerelerine dayalı değerlendirme sözleşmeleri.",
    "oos_evaluation_domain": "Örneklem dışı (OOS) kilitli dönem değerlendirme sözleşmeleri.",
    "stress_aware_evaluation_domain": "Kriz ve stres senaryolarına duyarlı değerlendirme.",
    "monte_carlo_robustness_evaluation_domain": "Monte Carlo yeniden örnekleme ve dayanıklılık değerlendirmesi.",
    "parameter_stability_evaluation_domain": "Parametre duyarlılığı ve plato kararlılığı değerlendirmesi.",
    "governance_aware_evaluation_domain": "Yönetişim ve denetim izi uyumlu raporlama.",
    "result_disclosure_domain": "Zorunlu metodolojik açıklama ve sınır bildirimleri.",
    "summary_placeholder_domain": "Hesaplanmamış özet şablonları.",
    "metric_placeholder_domain": "Hesaplanmamış performans ve risk metrik yer tutucuları.",
    "risk_summary_domain": "Kuyruk riski ve drawdown özet yer tutucuları.",
    "cost_impact_summary_domain": "Maliyet etkisi özet yer tutucuları.",
    "slippage_impact_summary_domain": "Kayma etkisi özet yer tutucuları.",
    "report_disclaimer_domain": "Yasal ve ampirik feragatname bildirimleri.",
    "claim_guard_domain": "Sonuç ve getiri iddialarını engelleyen muhafızlar.",
    "strategy_approval_guard_domain": "Strateji onayı ve sermaye tahsisini engelleyen muhafızlar.",
    "benchmark_selection_bias_guard_domain": "Benchmark seçim yanlılığı denetim muhafızları.",
    "disabled_execution_domain": "Devre dışı bırakılmış canlı ve simülasyon motorları.",
    "dependency_domain": "Yukarı akış faz bağımlılıkları sözleşmeleri.",
    "finding_domain": "Teşhis bulguları ve boşluk takibi.",
    "readiness_score_domain": "Sözleşme hazırlık ve bütünlük skoru.",
    "manifest_domain": "Master bütünlük ve kısıt manifestosu.",
    "health_domain": "Sistem sağlık kontrolü.",
    "validation_domain": "Çoklu doğrulama ve bütünlük kontrolleri.",
    "safety_domain": "NO-GO ve SAFE-GO güvenlik sınırları.",
    "phase_152_handoff_domain": "Phase 152 devir şartnamesi ve kabul hazırlığı.",
}


def build_benchmark_evaluation_domain_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of all registered evaluation domains."""
    rows: List[Dict[str, Any]] = []

    for dom in ALL_DOMAINS:
        rows.append(
            {
                "domain_name": dom,
                "description": DOMAIN_DESCRIPTIONS.get(dom, "Benchmark değerlendirme etki alanı."),
                "is_active": True,
                "contract_ready": True,
                "execution_allowed": False,
                "metric_calculation_allowed": False,
                "signal_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_benchmark_evaluation_domains(df)
    return df, summary


def summarize_benchmark_evaluation_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize domain registry status."""
    return {
        "domain": LABEL_BENCHMARK_EVALUATION_DOMAIN,
        "total_domains": len(df),
        "all_contract_ready": bool(df["contract_ready"].all()) if not df.empty else True,
        "all_execution_disabled": not bool(df["execution_allowed"].any()) if not df.empty else True,
        "all_signals_disabled": not bool(df["signal_allowed"].any()) if not df.empty else True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
