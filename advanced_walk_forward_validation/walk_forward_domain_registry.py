# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Domain Registry.

Registers and organizes domain areas for walk-forward validation and out-of-sample benchmarking.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile
from advanced_walk_forward_validation.walk_forward_labels import DOMAIN_LABELS

DOMAIN_SPECS: List[Dict[str, Any]] = [
    {
        "domain_name": "walk_forward_profile_domain",
        "category": "CONFIGURATION",
        "description": "Walk-forward profil yonetimi ve guvenlik parametreleri.",
    },
    {
        "domain_name": "walk_forward_domain",
        "category": "VALIDATION",
        "description": "Zaman serisi walk-forward dogrulama cercevesi sozlesmeleri.",
    },
    {
        "domain_name": "walk_forward_scope_domain",
        "category": "SCOPE",
        "description": "Faz 147 kapsam belirleme ve yetki sinirlari.",
    },
    {
        "domain_name": "split_contract_domain",
        "category": "SPLIT",
        "description": "Veri bolumleme sozlesmeleri ve pencere yonetimi.",
    },
    {
        "domain_name": "rolling_window_contract_domain",
        "category": "SPLIT",
        "description": "Sabit uzunluklu kayan pencere dogrulama sozlesmeleri.",
    },
    {
        "domain_name": "expanding_window_contract_domain",
        "category": "SPLIT",
        "description": "Genisleyen pencere dogrulama sozlesmeleri.",
    },
    {
        "domain_name": "anchored_window_contract_domain",
        "category": "SPLIT",
        "description": "Sabit baslangicli pencere bolumleme sozlesmeleri.",
    },
    {
        "domain_name": "purged_walk_forward_contract_domain",
        "category": "SPLIT",
        "description": "Etiket cakismasini onleyen purged walk-forward sozlesmeleri.",
    },
    {
        "domain_name": "embargo_policy_domain",
        "category": "SPLIT",
        "description": "Test sonrasi sizinti onleyici embargo politikalari.",
    },
    {
        "domain_name": "train_validation_test_split_domain",
        "category": "SPLIT",
        "description": "Egitim, dogrulama ve test bolum sozlesmeleri.",
    },
    {
        "domain_name": "out_of_sample_split_domain",
        "category": "SPLIT",
        "description": "Orneklem disi (OOS) bolumleme sozlesmeleri.",
    },
    {
        "domain_name": "holdout_period_domain",
        "category": "SPLIT",
        "description": "Korumali holdout donemi sozlesmeleri.",
    },
    {
        "domain_name": "temporal_split_boundary_domain",
        "category": "SPLIT",
        "description": "Zaman eksenli bolumleme sinirlari.",
    },
    {
        "domain_name": "regime_aware_split_domain",
        "category": "SPLIT",
        "description": "Piyasa rejimine duyarli bolumleme sozlesmeleri.",
    },
    {
        "domain_name": "cross_asset_oos_split_domain",
        "category": "SPLIT",
        "description": "Varliklar arasi OOS bolumleme sozlesmeleri.",
    },
    {
        "domain_name": "walk_forward_fold_domain",
        "category": "SPLIT",
        "description": "Walk-forward katman (fold) tanimlari.",
    },
    {
        "domain_name": "walk_forward_schedule_placeholder_domain",
        "category": "SPLIT",
        "description": "Yeniden egitebilme / guncelleme zamanlama yer tutuculari.",
    },
    {
        "domain_name": "benchmark_contract_domain",
        "category": "BENCHMARK",
        "description": "Karsilastirmali benchmark sozlesmeleri.",
    },
    {
        "domain_name": "benchmark_universe_domain",
        "category": "BENCHMARK",
        "description": "Benchmark varlik evreni sozlesmeleri.",
    },
    {
        "domain_name": "benchmark_baseline_domain",
        "category": "BENCHMARK",
        "description": "Temel benchmark strateji sozlesmeleri.",
    },
    {
        "domain_name": "benchmark_comparison_domain",
        "category": "BENCHMARK",
        "description": "Benchmark karsilastirma arayuzleri.",
    },
    {
        "domain_name": "benchmark_placeholder_domain",
        "category": "BENCHMARK",
        "description": "Pasif, nakit, buy & hold ve esit agirlikli benchmark yer tutuculari.",
    },
    {
        "domain_name": "benchmark_metric_placeholder_domain",
        "category": "METRICS",
        "description": "Alfa, beta, bilgi orani ve izleme hatasi metrik yer tutuculari.",
    },
    {
        "domain_name": "validation_metric_placeholder_domain",
        "category": "METRICS",
        "description": "OOS Sharpe, drawdown, calmar, win-rate metrik yer tutuculari.",
    },
    {
        "domain_name": "output_contract_domain",
        "category": "CONTRACTS",
        "description": "Rapor ve cikti format sozlesmeleri.",
    },
    {
        "domain_name": "validation_evidence_domain",
        "category": "GOVERNANCE",
        "description": "Dogrulama kanit ve izlenebilirlik kayitlari.",
    },
    {
        "domain_name": "dependency_domain",
        "category": "DEPENDENCY",
        "description": "Phase 1-146 moduler bagimliliklari.",
    },
    {
        "domain_name": "bias_guard_domain",
        "category": "GOVERNANCE",
        "description": "Lookahead, data snooping ve survivorship muhafizlari.",
    },
    {
        "domain_name": "disabled_execution_domain",
        "category": "GOVERNANCE",
        "description": "Kesin olarak engellenmis calistirma yollari.",
    },
    {
        "domain_name": "finding_domain",
        "category": "AUDIT",
        "description": "Dogrulama bulgulari ve aksiyon kayitlari.",
    },
    {
        "domain_name": "readiness_score_domain",
        "category": "AUDIT",
        "description": "Sistem hazirlik skoru olcumu.",
    },
    {
        "domain_name": "manifest_domain",
        "category": "MANIFEST",
        "description": "Faz 147 master manifest kaydi.",
    },
    {
        "domain_name": "health_domain",
        "category": "HEALTH",
        "description": "Sistem saglik ve ortam kontrolleri.",
    },
    {
        "domain_name": "validation_domain",
        "category": "VALIDATION",
        "description": "Kurallara uygunluk dogrulama raporu.",
    },
    {
        "domain_name": "safety_domain",
        "category": "SAFETY",
        "description": "Guvenlik sinirlari, NO-GO ve SAFE-GO kurallari.",
    },
    {
        "domain_name": "phase_148_handoff_domain",
        "category": "HANDOFF",
        "description": "Phase 148 Stress Testing and Scenario Simulation gecis paketi.",
    },
]


def build_walk_forward_domain_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for walk-forward domain registry."""
    rows = []
    for d in DOMAIN_SPECS:
        rows.append(
            {
                "domain_name": d["domain_name"],
                "category": d["category"],
                "description": d["description"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_walk_forward_domains(df)
    return df, summary


def summarize_walk_forward_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize walk-forward domain registry."""
    categories = list(df["category"].unique()) if not df.empty else []
    return {
        "total_domains": len(df),
        "categories": categories,
        "total_categories": len(categories),
        "non_signal": True,
    }
