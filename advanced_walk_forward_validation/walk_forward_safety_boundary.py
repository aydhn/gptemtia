# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Safety Boundary.

Defines NO-GO and SAFE-GO operational matrices ensuring non-production,
non-executing research safety boundaries.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

NO_GO_CONDITIONS: List[Dict[str, Any]] = [
    {"rule_id": "NG-147-01", "name": "live_trading_prohibition", "description": "Canli hesap veya gercek sermaye ile islem yapilamaz."},
    {"rule_id": "NG-147-02", "name": "broker_execution_prohibition", "description": "Broker API uzerinden emir iletimi yapilamaz."},
    {"rule_id": "NG-147-03", "name": "investment_advice_prohibition", "description": "Yatirim tavsiyesi veya varlik alim-satim onerisi uretilemez."},
    {"rule_id": "NG-147-04", "name": "signal_generation_prohibition", "description": "Kesin AL/SAT veya pozisyon sinyali uretilemez."},
    {"rule_id": "NG-147-05", "name": "optimizer_execution_prohibition", "description": "Hiperparametre veya strateji optimizasyonu calistirilamaz."},
    {"rule_id": "NG-147-06", "name": "walk_forward_execution_prohibition", "description": "Gercek walk-forward backtest dongusu kosturulamaz."},
    {"rule_id": "NG-147-07", "name": "benchmark_execution_prohibition", "description": "Gercek benchmark strateji calistirmasi yapilamaz."},
    {"rule_id": "NG-147-08", "name": "metric_calculation_prohibition", "description": "Gercek Sharpe, alfa, beta veya getiri metrigi hesaplanamaz."},
    {"rule_id": "NG-147-09", "name": "model_training_inference_prohibition", "description": "Gercek model egitimi (fit) veya cikarim (predict) calistirilamaz."},
    {"rule_id": "NG-147-10", "name": "target_label_generation_prohibition", "description": "Gelecek getiri veya hedef etiket uretilemez."},
    {"rule_id": "NG-147-11", "name": "model_registry_write_prohibition", "description": "Model registry veya artifact deposuna kayit yapilamaz."},
    {"rule_id": "NG-147-12", "name": "deployment_prohibition", "description": "Production veya canli ortama dagitim yapilamaz."},
    {"rule_id": "NG-147-13", "name": "performance_guarantee_prohibition", "description": "Gelecek performans veya kazanc garantisi iddia edilemez."},
    {"rule_id": "NG-147-14", "name": "scraping_credential_overwrite_prohibition", "description": "Web scraping, credential basilmasi veya dosya uzerine yazma yapilamaz."},
]

SAFE_GO_CONDITIONS: List[Dict[str, Any]] = [
    {"rule_id": "SG-147-01", "name": "local_offline_split_contract_generation", "description": "Yerel ve cevrimdisi walk-forward bolum sozlesmeleri olusturulabilir."},
    {"rule_id": "SG-147-02", "name": "oos_split_contract_definition", "description": "Orneklem disi kesisimsiz OOS test sinirlari tanimlanabilir."},
    {"rule_id": "SG-147-03", "name": "benchmark_contract_definition", "description": "Buy & Hold, nakit ve esit agirlikli referans sozlesmeleri kayit altina alinabilir."},
    {"rule_id": "SG-147-04", "name": "purge_embargo_metadata_specification", "description": "Sizinti onleyici purge ve embargo metadata kurallari tanimlanabilir."},
    {"rule_id": "SG-147-05", "name": "validation_metric_placeholder_definition", "description": "Metrik formulleri hesaplama calistirilmadan yer tutucu olarak sunulabilir."},
    {"rule_id": "SG-147-06", "name": "no_lookahead_and_bias_guard_enforcement", "description": "Zaman serisi ve bias muhafizlari aktif sekilde denetim yapabilir."},
    {"rule_id": "SG-147-07", "name": "phase_148_handoff_preparation", "description": "Phase 148 Stress Testing and Scenario Simulation icin guvenli gecis paketi hazirlanabilir."},
]


def build_walk_forward_no_go_conditions(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of NO-GO conditions."""
    rows = []
    for ng in NO_GO_CONDITIONS:
        rows.append(
            {
                "rule_id": ng["rule_id"],
                "name": ng["name"],
                "description": ng["description"],
                "is_enforced": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    return df, {"total_no_go": len(df), "all_enforced": True, "non_signal": True}


def build_walk_forward_safe_go_conditions(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of SAFE-GO conditions."""
    rows = []
    for sg in SAFE_GO_CONDITIONS:
        rows.append(
            {
                "rule_id": sg["rule_id"],
                "name": sg["name"],
                "description": sg["description"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    return df, {"total_safe_go": len(df), "all_active": True, "non_signal": True}


def build_walk_forward_safety_boundary(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build combined safety boundary DataFrame."""
    df_no, s_no = build_walk_forward_no_go_conditions(profile)
    df_safe, s_safe = build_walk_forward_safe_go_conditions(profile)
    summary = {
        "no_go_count": s_no["total_no_go"],
        "safe_go_count": s_safe["total_safe_go"],
        "all_enforced": True,
        "safety_status": "SECURE",
        "non_signal": True,
    }
    return df_no, summary
