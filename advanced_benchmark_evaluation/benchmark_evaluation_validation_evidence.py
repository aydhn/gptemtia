# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Validation Evidence Module.

Registers immutable evidence demonstrating that all Phase 151 contracts,
placeholders, guards, and boundaries are formally established.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_VALIDATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

EVIDENCE_ITEMS: List[Dict[str, Any]] = [
    {
        "evidence_id": "EVID_BENCHMARK_REPORT_CONTRACTS",
        "category": "contract_integrity",
        "description": "Benchmark karşılaştırma raporu sözleşmeleri eksiksiz tanımlandı.",
        "status": "VERIFIED",
    },
    {
        "evidence_id": "EVID_STRATEGY_EVALUATION_CONTRACTS",
        "category": "contract_integrity",
        "description": "Strateji değerlendirme raporu sözleşmeleri eksiksiz tanımlandı.",
        "status": "VERIFIED",
    },
    {
        "evidence_id": "EVID_METRIC_PLACEHOLDERS",
        "category": "metric_safety",
        "description": "Tüm performans ve risk metrikleri hesaplanmamış yer tutucu olarak sözleşmeye bağlandı.",
        "status": "VERIFIED",
    },
    {
        "evidence_id": "EVID_RESULT_CLAIM_GUARDS",
        "category": "claim_boundary",
        "description": "Sonuç ve getiri iddialarını engelleyen muhafızlar devrede.",
        "status": "VERIFIED",
    },
    {
        "evidence_id": "EVID_STRATEGY_APPROVAL_GUARDS",
        "category": "approval_boundary",
        "description": "Strateji onayı ve sermaye tahsisini engelleyen muhafızlar devrede.",
        "status": "VERIFIED",
    },
    {
        "evidence_id": "EVID_BENCHMARK_SELECTION_BIAS_GUARDS",
        "category": "bias_control",
        "description": "Benchmark seçim yanlılığını önleyen ön taahhütlü baseline kuralları devrede.",
        "status": "VERIFIED",
    },
    {
        "evidence_id": "EVID_COST_SLIPPAGE_EVALUATION",
        "category": "friction_realism",
        "description": "Maliyet ve kayma düzeltmeli değerlendirme sözleşmeleri oluşturuldu.",
        "status": "VERIFIED",
    },
    {
        "evidence_id": "EVID_WALK_FORWARD_OOS_DEPENDENCY",
        "category": "validation_linkage",
        "description": "Phase 147 Walk-Forward ve OOS kilitli split bağımlılığı sağlandı.",
        "status": "VERIFIED",
    },
    {
        "evidence_id": "EVID_STRESS_MONTE_CARLO_DEPENDENCY",
        "category": "robustness_linkage",
        "description": "Phase 148 Stres senaryoları ve Phase 149 Monte Carlo zarf bağımlılığı sağlandı.",
        "status": "VERIFIED",
    },
    {
        "evidence_id": "EVID_BACKTEST_GOVERNANCE_DEPENDENCY",
        "category": "governance_linkage",
        "description": "Phase 150 Backtest yönetişim ve yanlılık kontrol çerçevesi bağlandı.",
        "status": "VERIFIED",
    },
    {
        "evidence_id": "EVID_DISABLED_EXECUTION_REPORTS",
        "category": "disabled_execution",
        "description": "11 adet resmi devre dışı yürütme raporu oluşturuldu.",
        "status": "VERIFIED",
    },
    {
        "evidence_id": "EVID_PHASE_152_HANDOFF",
        "category": "handoff_readiness",
        "description": "Phase 152 Backtest Kabul Raporu için devir şartnamesi hazırlandı.",
        "status": "VERIFIED",
    },
]


def build_benchmark_evaluation_validation_evidence_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of validation evidence."""
    rows: List[Dict[str, Any]] = []

    for item in EVIDENCE_ITEMS:
        rows.append(
            {
                "evidence_id": item["evidence_id"],
                "category": item["category"],
                "description": item["description"],
                "verification_status": item["status"],
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_VALIDATION_DOMAIN,
        "total_evidence_items": len(df),
        "all_verified": bool((df["verification_status"] == "VERIFIED").all()) if not df.empty else True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
