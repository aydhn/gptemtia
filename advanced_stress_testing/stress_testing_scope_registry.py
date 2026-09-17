# -*- coding: utf-8 -*-
"""Phase 148: Stress Testing Scope Registry.

Builds and summarizes operational boundaries and negative invariants for the stress testing scope.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

SCOPE_ITEMS: List[Dict[str, Any]] = [
    {
        "scope_name": "local_offline_stress_contract_layer",
        "category": "IN_SCOPE",
        "description": "Yerel ve cevrimdisi stres senaryo sozlesmelerinin ve sok yer tutucularinin tanimlanmasi.",
        "enforced": True,
    },
    {
        "scope_name": "no_live_trading",
        "category": "OUT_OF_SCOPE",
        "description": "Gercek piyasaya emir gonderimi ve canli islem yurutulmesi kesinlikle yasaktir.",
        "enforced": True,
    },
    {
        "scope_name": "no_broker_execution",
        "category": "OUT_OF_SCOPE",
        "description": "Araci kurum API baglantisi ve emir iletimi kesinlikle engellenmistir.",
        "enforced": True,
    },
    {
        "scope_name": "no_investment_advice",
        "category": "OUT_OF_SCOPE",
        "description": "Kesin AL/SAT, pozisyon veya yatirim tavsiyesi uretilmez.",
        "enforced": True,
    },
    {
        "scope_name": "no_true_stress_execution",
        "category": "OUT_OF_SCOPE",
        "description": "Gercek stres testi calistirilmasi engellenmistir; sozlesmeler salt sema modundadir.",
        "enforced": True,
    },
    {
        "scope_name": "no_scenario_simulation_execution",
        "category": "OUT_OF_SCOPE",
        "description": "Gercek senaryo simülasyonu calistirilmasi engellenmistir.",
        "enforced": True,
    },
    {
        "scope_name": "no_monte_carlo_execution",
        "category": "OUT_OF_SCOPE",
        "description": "Monte Carlo simülasyonu bu fazda calistirilmaz; Phase 149 konusu olarak devredilir.",
        "enforced": True,
    },
    {
        "scope_name": "no_metric_calculation",
        "category": "OUT_OF_SCOPE",
        "description": "Stres PnL, VaR, ES veya drawdown gercek olarak hesaplanmaz; yalnizca yer tutucu tanimlanir.",
        "enforced": True,
    },
    {
        "scope_name": "no_model_training",
        "category": "OUT_OF_SCOPE",
        "description": "Gercek makine ogrenimi model egitimi kesinlikle engellenmistir.",
        "enforced": True,
    },
    {
        "scope_name": "no_prediction",
        "category": "OUT_OF_SCOPE",
        "description": "Tahmin veya hedef etiket uretimi kesinlikle engellenmistir.",
        "enforced": True,
    },
    {
        "scope_name": "no_deployment",
        "category": "OUT_OF_SCOPE",
        "description": "Uretim ortamina dagitim veya model kayit defterine yazim yapilmaz.",
        "enforced": True,
    },
    {
        "scope_name": "phase_149_handoff_only",
        "category": "IN_SCOPE",
        "description": "Phase 149 Monte Carlo saglamlik fazi icin teshis ve hazirlik devir paketi olusturulmasi.",
        "enforced": True,
    },
]


def build_stress_testing_scope_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry defining in-scope and out-of-scope boundaries."""
    rows: List[Dict[str, Any]] = []
    for item in SCOPE_ITEMS:
        rows.append(
            {
                "scope_name": item["scope_name"],
                "category": item["category"],
                "description": item["description"],
                "enforced": item["enforced"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_scope_items": len(df),
        "in_scope_count": int((df["category"] == "IN_SCOPE").sum()),
        "out_of_scope_count": int((df["category"] == "OUT_OF_SCOPE").sum()),
        "all_enforced": bool(df["enforced"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
