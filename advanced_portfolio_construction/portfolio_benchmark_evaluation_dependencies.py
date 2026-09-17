# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Benchmark Evaluation Dependencies."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    DEPENDENCY_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


BENCHMARK_DEPENDENCIES = [
    {"dep_id": "DEP_BENCHMARK_EVAL_151", "component": "Phase 151 Benchmark Evaluation", "source_module": "advanced_benchmark_evaluation", "status": "SATISFIED", "description": "Gosterge karsilastirma ve goreceli basarim cercevesi."},
    {"dep_id": "DEP_BENCHMARK_BUY_HOLD", "component": "Buy & Hold Benchmark", "source_module": "advanced_benchmark_evaluation", "status": "SATISFIED", "description": "Pasif uzun vadeli tutma karsilastirma sozlesmesi."},
    {"dep_id": "DEP_BENCHMARK_60_40", "component": "60/40 Commodity/FX Benchmark", "source_module": "advanced_benchmark_evaluation", "status": "SATISFIED", "description": "Sabit agirlikli coklu varlik referansi."},
    {"dep_id": "DEP_BENCHMARK_EQUAL_WEIGHT", "component": "Equal Weight Universe Benchmark", "source_module": "advanced_benchmark_evaluation", "status": "SATISFIED", "description": "Esit agirlikli evren karsilastirma referansi."},
]


def build_portfolio_benchmark_evaluation_dependency_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for benchmark evaluation dependencies."""
    rows = []
    for d in BENCHMARK_DEPENDENCIES:
        rows.append({
            "dep_id": d["dep_id"],
            "component": d["component"],
            "source_module": d["source_module"],
            "status": d["status"],
            "description": d["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "non_signal": True,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": DEPENDENCY_DOMAIN,
        "active_profile": profile.profile_name,
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
