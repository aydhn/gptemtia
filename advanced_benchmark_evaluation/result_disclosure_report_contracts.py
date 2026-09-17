# -*- coding: utf-8 -*-
"""Phase 151: Result Disclosure Report Contracts Module.

Defines mandatory disclosure sections for all evaluation reports.
Enforces zero performance guarantees and full transparency of limitations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_RESULT_DISCLOSURE_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

RESULT_DISCLOSURES: List[Dict[str, Any]] = [
    {
        "disclosure_id": "DISC_RESEARCH_ONLY",
        "title": "Internal Research and Non-Advice Disclosure",
        "category": "legal_regulatory",
        "description": "Raporun yatırım tavsiyesi, al/sat sinyali veya onay olmadığını belirten zorunlu beyan.",
    },
    {
        "disclosure_id": "DISC_SIMULATION_LIMITATIONS",
        "title": "Simulation Realism Limitations Disclosure",
        "category": "methodological",
        "description": "Geçmiş simülasyonların gelecekteki sonuçları garanti etmeyeceğini belirten beyan.",
    },
    {
        "disclosure_id": "DISC_FRICTION_ASSUMPTIONS",
        "title": "Friction and Slippage Assumptions Disclosure",
        "category": "execution_modeling",
        "description": "Kullanılan komisyon, gecikme ve kayma modellerinin varsayımlarını açıklayan beyan.",
    },
    {
        "disclosure_id": "DISC_UNTRACKED_RISKS",
        "title": "Model Tail Risk and Black Swan Vulnerability Disclosure",
        "category": "risk_management",
        "description": "Örneklemde yer almayan aşırı kuyruk riskleri ve rejim sıçramalarına dair uyarı.",
    },
]


def build_result_disclosure_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of result disclosure contracts."""
    rows: List[Dict[str, Any]] = []

    for d in RESULT_DISCLOSURES:
        rows.append(
            {
                "disclosure_id": d["disclosure_id"],
                "title": d["title"],
                "category": d["category"],
                "description": d["description"],
                "is_mandatory": True,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_RESULT_DISCLOSURE_DOMAIN,
        "total_disclosures": len(df),
        "all_mandatory": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
