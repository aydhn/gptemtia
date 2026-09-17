# -*- coding: utf-8 -*-
"""Phase 154: Optimization Metric Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_metric_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build general optimization metric placeholders table."""
    metrics = [
        ("objective_value_placeholder", "optimization", "Hesaplanan amac fonksiyon degeri yer tutucusu", "scalar"),
        ("expected_return_placeholder", "optimization", "Beklenen portfoy getirisi yer tutucusu", "percentage"),
        ("expected_volatility_placeholder", "optimization", "Beklenen yillik portfoy oynakligi yer tutucusu", "percentage"),
        ("sharpe_placeholder", "optimization", "Hesaplanan Sharpe orani yer tutucusu", "ratio"),
        ("cvar_placeholder", "optimization", "Hesaplanan %95 CVaR degeri yer tutucusu", "percentage"),
        ("max_drawdown_placeholder", "optimization", "Beklenen maksimum drawdown yer tutucusu", "percentage"),
        ("risk_contribution_placeholder", "optimization", "Varlik basina marjinal risk katkisi yer tutucusu", "percentage"),
        ("frontier_point_placeholder", "optimization", "Etkin sinir noktasi koordinat yer tutucusu", "coordinate"),
    ]
    records = []
    for name, domain, desc, unit in metrics:
        records.append({
            "metric_name": name,
            "metric_domain": domain,
            "formula_description": desc,
            "unit": unit,
            "is_placeholder": True,
            "actual_value": None,
            "is_calculated": False,
        })
    df = pd.DataFrame(records)
    summary = {
        "metric_count": len(records),
        "all_metrics_placeholders": True,
        "zero_metrics_calculated": True,
    }
    return df, summary
