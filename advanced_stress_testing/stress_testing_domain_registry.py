# -*- coding: utf-8 -*-
"""Phase 148: Stress Testing Domain Registry.

Builds and summarizes domain definitions for the stress testing contract layer.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_labels import DOMAIN_LABELS

DOMAIN_DESCRIPTIONS: Dict[str, str] = {
    "stress_testing_profile_domain": "Stres testi profili ve isletim ayarlari alani.",
    "stress_testing_domain": "Genel yerel stres testi sozlesme alani.",
    "stress_testing_scope_domain": "Stres testi arastirma ve guvenlik kapsami alani.",
    "stress_scenario_contract_domain": "Stres senaryo sozlesmeleri cekirdek alani.",
    "historical_scenario_contract_domain": "Tarihsel kriz senaryo sozlesmeleri alani.",
    "hypothetical_scenario_contract_domain": "Varsayimsal kriz senaryo sozlesmeleri alani.",
    "regime_shock_domain": "Rejim kirilma ve gecis soku sozlesmeleri alani.",
    "volatility_shock_domain": "Volatilite patlamasi ve sok sozlesmeleri alani.",
    "liquidity_shock_domain": "Likidite kurakligi ve derinlik kaybi sozlesmeleri alani.",
    "spread_widening_domain": "Spread genislemesi ve alis-satis sok sozlesmeleri alani.",
    "gap_risk_placeholder_domain": "Fiyat boslugu ve seans gecis risk yer tutucu alani.",
    "correlation_breakdown_placeholder_domain": "Korelasyon kirilmasi ve baglilik cokus yer tutucu alani.",
    "macro_shock_placeholder_domain": "Faiz, enflasyon ve makro sok yer tutucu alani.",
    "cross_asset_contagion_placeholder_domain": "Capraz varlik bulasma yer tutucu alani.",
    "execution_disruption_placeholder_domain": "Iletim aksamasi ve emir ret yer tutucu alani.",
    "transaction_cost_shock_domain": "Stres komisyon ve islem maliyet soku alani.",
    "slippage_shock_domain": "Stres kayma (slippage) soku sozlesme alani.",
    "stress_metric_placeholder_domain": "Stres performans ve risk metrik yer tutucu alani.",
    "scenario_metric_placeholder_domain": "Senaryo metrik yer tutucu alani.",
    "robustness_metric_placeholder_domain": "Saglamlik metrik yer tutucu alani.",
    "output_contract_domain": "Stres cikti sema ve sozlesme alani.",
    "dependency_domain": "Onceki faz ve altyapi bagimliliklari alani.",
    "bias_guard_domain": "Lookahead, yanlilik ve sizinti muhafizlari alani.",
    "disabled_execution_domain": "Devre disi birakilmis gercek yurutme guvenceleri alani.",
    "finding_domain": "Stres testi yonetisim bulgulari alani.",
    "readiness_score_domain": "Teshis hazirlik skoru alani.",
    "manifest_domain": "Master stres testi butunluk manifestosu alani.",
    "health_domain": "Sistem ve bagimlilik saglik denetimi alani.",
    "validation_domain": "Sozlesme dogrulama ve guvenlik denetim alani.",
    "safety_domain": "Guvenlik sinirlari, NO-GO ve SAFE-GO ilkeleri alani.",
    "phase_149_handoff_domain": "Phase 149 Monte Carlo saglamlik devir paketi alani.",
}


def build_stress_testing_domain_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of all stress testing domains."""
    rows: List[Dict[str, Any]] = []
    for domain_name in DOMAIN_LABELS:
        rows.append(
            {
                "domain_name": domain_name,
                "description": DOMAIN_DESCRIPTIONS.get(domain_name, "Stres testi alani."),
                "non_signal": True,
                "local_only": True,
                "non_production": True,
                "current_phase": profile.current_phase,
                "target_final_phase": profile.target_final_phase,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_domains": len(df),
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_local_only": bool(df["local_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
    }
    return df, summary
