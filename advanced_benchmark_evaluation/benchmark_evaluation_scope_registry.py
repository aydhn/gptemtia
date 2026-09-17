# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Scope Registry Module.

Delineates included research evaluation scopes from strictly excluded operational scopes.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_BENCHMARK_EVALUATION_SCOPE_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

INCLUDED_SCOPES: List[Dict[str, str]] = [
    {
        "scope_id": "SCOPE_INC_01",
        "scope_type": "INCLUDED",
        "scope_name": "benchmark_comparison_reporting_contracts",
        "description": "Benchmark karşılaştırma raporu sözleşme şablonları ve metaveri yapıları.",
    },
    {
        "scope_id": "SCOPE_INC_02",
        "scope_type": "INCLUDED",
        "scope_name": "strategy_evaluation_reporting_contracts",
        "description": "Strateji değerlendirme raporu sözleşme şablonları ve metodolojik bildirimler.",
    },
    {
        "scope_id": "SCOPE_INC_03",
        "scope_type": "INCLUDED",
        "scope_name": "benchmark_universe_and_baseline_definitions",
        "description": "Emtia ve FX varlık sınıfları için pasif, nakit ve sepet baseline sözleşmeleri.",
    },
    {
        "scope_id": "SCOPE_INC_04",
        "scope_type": "INCLUDED",
        "scope_name": "cost_and_slippage_adjusted_contracts",
        "description": "Komisyon, taşıma maliyeti ve kayma etkisi düzeltmeli rapor sözleşmeleri.",
    },
    {
        "scope_id": "SCOPE_INC_05",
        "scope_type": "INCLUDED",
        "scope_name": "regime_and_scenario_aware_evaluation",
        "description": "Piyasa rejimleri, stres senaryoları ve Monte Carlo dayanıklılığına duyarlı rapor şablonları.",
    },
    {
        "scope_id": "SCOPE_INC_06",
        "scope_type": "INCLUDED",
        "scope_name": "uncalculated_metric_placeholders",
        "description": "Gerçek değer üretmeyen, formül ve rol odaklı performans/risk yer tutucuları.",
    },
    {
        "scope_id": "SCOPE_INC_07",
        "scope_type": "INCLUDED",
        "scope_name": "claim_and_approval_boundaries",
        "description": "Performans iddiası, strateji onayı ve sermaye tahsisini engelleyen güvenlik kuralları.",
    },
    {
        "scope_id": "SCOPE_INC_08",
        "scope_type": "INCLUDED",
        "scope_name": "phase_152_handoff_contracts",
        "description": "Phase 152 Backtest Acceptance Report devir şartnamesi ve kabul hazırlığı.",
    },
]

EXCLUDED_SCOPES: List[Dict[str, str]] = [
    {
        "scope_id": "SCOPE_EXC_01",
        "scope_type": "EXCLUDED",
        "scope_name": "live_trading_and_order_dispatch",
        "description": "Canlı emir iletimi, gerçek para yönetimi veya piyasa işlemleri.",
    },
    {
        "scope_id": "SCOPE_EXC_02",
        "scope_type": "EXCLUDED",
        "scope_name": "broker_api_integration",
        "description": "Aracı kurum API bağlantısı veya hesap yönetimi entegrasyonu.",
    },
    {
        "scope_id": "SCOPE_EXC_03",
        "scope_type": "EXCLUDED",
        "scope_name": "real_backtest_execution",
        "description": "Gerçek simülasyon veya backtest motoru yürütmesi.",
    },
    {
        "scope_id": "SCOPE_EXC_04",
        "scope_type": "EXCLUDED",
        "scope_name": "real_metric_calculation",
        "description": "Gerçek Sharpe, getiri, alpha, beta, drawdown veya kazanma oranı hesaplaması.",
    },
    {
        "scope_id": "SCOPE_EXC_05",
        "scope_type": "EXCLUDED",
        "scope_name": "strategy_approval_and_capital_allocation",
        "description": "Strateji resmi onayı, portföy oluşturma veya sermaye tahsisi.",
    },
    {
        "scope_id": "SCOPE_EXC_06",
        "scope_type": "EXCLUDED",
        "scope_name": "model_training_and_inference",
        "description": "Gerçek makine öğrenmesi eğitimi, model fit veya tahmin üretimi.",
    },
    {
        "scope_id": "SCOPE_EXC_07",
        "scope_type": "EXCLUDED",
        "scope_name": "parameter_optimization_sweeps",
        "description": "Optimizasyon taraması, curve fitting veya parametre avcılığı.",
    },
    {
        "scope_id": "SCOPE_EXC_08",
        "scope_type": "EXCLUDED",
        "scope_name": "signal_generation_and_recommendation",
        "description": "Al/Sat sinyali, yatırım tavsiyesi veya yönlü pozisyon önerisi.",
    },
]


def build_benchmark_evaluation_scope_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of included and excluded evaluation scopes."""
    rows: List[Dict[str, Any]] = []

    for item in INCLUDED_SCOPES + EXCLUDED_SCOPES:
        is_inc = item["scope_type"] == "INCLUDED"
        rows.append(
            {
                "scope_id": item["scope_id"],
                "scope_type": item["scope_type"],
                "scope_name": item["scope_name"],
                "description": item["description"],
                "is_permitted": is_inc,
                "is_blocked": not is_inc,
                "status": STATUS_EVALUATION_CONTRACT_READY,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_benchmark_evaluation_scopes(df)
    return df, summary


def summarize_benchmark_evaluation_scopes(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize scope registry status."""
    inc_count = int((df["scope_type"] == "INCLUDED").sum()) if not df.empty else 0
    exc_count = int((df["scope_type"] == "EXCLUDED").sum()) if not df.empty else 0
    return {
        "domain": LABEL_BENCHMARK_EVALUATION_SCOPE_DOMAIN,
        "total_scopes": len(df),
        "included_scopes_count": inc_count,
        "excluded_scopes_count": exc_count,
        "all_excluded_blocked": bool(df[df["scope_type"] == "EXCLUDED"]["is_blocked"].all()) if exc_count > 0 else True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
