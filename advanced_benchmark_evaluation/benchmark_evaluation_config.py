# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Configuration Module.

Defines the BenchmarkEvaluationProfile dataclass, pre-configured profiles,
and validation utilities enforcing strict offline/local research parameters.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(frozen=True)
class BenchmarkEvaluationProfile:
    """Configuration profile for Phase 151 Benchmark Comparison and Strategy Evaluation Reports."""

    profile_name: str
    description: str
    current_phase: int = 151
    target_final_phase: int = 160
    next_phase: int = 152
    default_language: str = "tr"
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True

    # Strict Negative Invariant Booleans
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_signal_generation: bool = False
    allow_directional_claim: bool = False
    allow_backtest_execution: bool = False
    allow_benchmark_execution: bool = False
    allow_metric_calculation: bool = False
    allow_result_claim: bool = False
    allow_performance_claim: bool = False
    allow_strategy_approval: bool = False
    allow_capital_allocation: bool = False
    allow_portfolio_construction: bool = False
    allow_position_sizing: bool = False
    allow_optimizer_execution: bool = False
    allow_model_training: bool = False
    allow_model_fit: bool = False
    allow_model_predict: bool = False
    allow_model_inference: bool = False
    allow_prediction_generation: bool = False
    allow_target_label_generation: bool = False
    allow_model_registry_write: bool = False
    allow_artifact_persistence: bool = False
    allow_model_deployment: bool = False
    allow_production_deployment: bool = False
    allow_production_approval: bool = False
    allow_broker_ready_approval: bool = False
    allow_live_trading_approval: bool = False
    allow_official_approval_claim: bool = False
    allow_production_ready_claim: bool = False
    allow_broker_ready_claim: bool = False
    allow_full_article_usage: bool = False
    allow_article_body_usage: bool = False
    allow_raw_content_usage: bool = False
    allow_scraped_html_usage: bool = False
    allow_embedding_generation: bool = False
    allow_vector_db: bool = False
    allow_web_scraping: bool = False
    allow_credential_output: bool = False
    allow_source_overwrite: bool = False
    allow_auto_destructive_cleaning: bool = False
    allow_file_deletion: bool = False
    allow_overwrite: bool = False
    allow_auto_imputation: bool = False
    allow_auto_feature_drop: bool = False

    # Evaluation Report Enablement Flags
    enable_benchmark_reports: bool = True
    enable_strategy_evaluation_reports: bool = True
    enable_summary_placeholders: bool = True
    enable_metric_placeholders: bool = True
    enable_claim_guards: bool = True
    enable_disabled_execution_reports: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_152_handoff: bool = True

    # Scoring & Storage
    min_readiness_score: float = 0.50
    save_reports: bool = True

    # Metadata Attributes
    supported_asset_classes: List[str] = field(
        default_factory=lambda: ["commodity", "fx"]
    )
    supported_benchmark_types: List[str] = field(
        default_factory=lambda: [
            "buy_and_hold",
            "cash_risk_free",
            "equal_weight_basket",
            "regime_aware_baseline",
            "cost_adjusted_baseline",
        ]
    )
    report_formats: List[str] = field(
        default_factory=lambda: ["markdown", "json", "csv", "txt"]
    )


PROFILES: Dict[str, BenchmarkEvaluationProfile] = {
    "balanced_local_benchmark_evaluation_contracts": BenchmarkEvaluationProfile(
        profile_name="balanced_local_benchmark_evaluation_contracts",
        description="Dengeli yerel benchmark karşılaştırma ve strateji değerlendirme rapor sözleşmeleri profili.",
        min_readiness_score=0.50,
    ),
    "conservative_local_benchmark_evaluation_contracts": BenchmarkEvaluationProfile(
        profile_name="conservative_local_benchmark_evaluation_contracts",
        description="Muhafazakar yerel benchmark ve strateji değerlendirme profili; daha katı iddia sınırları.",
        min_readiness_score=0.60,
    ),
    "institutional_local_benchmark_evaluation_contracts": BenchmarkEvaluationProfile(
        profile_name="institutional_local_benchmark_evaluation_contracts",
        description="Kurumsal düzeyde yerel benchmark ve strateji raporlama sözleşmeleri; tam feragatname ve bağımlılık kontrolü.",
        min_readiness_score=0.70,
    ),
}


def get_benchmark_evaluation_profile(
    name: Optional[str] = None,
) -> BenchmarkEvaluationProfile:
    """Retrieve benchmark evaluation profile by name, falling back to balanced default."""
    if not name or name not in PROFILES:
        return PROFILES["balanced_local_benchmark_evaluation_contracts"]
    return PROFILES[name]


def list_benchmark_evaluation_profiles(
    enabled_only: bool = True,
) -> List[BenchmarkEvaluationProfile]:
    """List all registered benchmark evaluation profiles."""
    return list(PROFILES.values())


def get_default_benchmark_evaluation_profile() -> BenchmarkEvaluationProfile:
    """Return the default benchmark evaluation profile."""
    return PROFILES["balanced_local_benchmark_evaluation_contracts"]


def validate_benchmark_evaluation_profiles() -> bool:
    """Validate all profiles conform to negative invariants and non-production rules."""
    for p in PROFILES.values():
        if p.current_phase != 151 or p.next_phase != 152:
            return False
        if not (p.local_only and p.non_production and p.research_only and p.dry_run_default):
            return False
        if (
            p.allow_live_trading
            or p.allow_broker_integration
            or p.allow_backtest_execution
            or p.allow_benchmark_execution
            or p.allow_metric_calculation
            or p.allow_result_claim
            or p.allow_performance_claim
            or p.allow_strategy_approval
            or p.allow_capital_allocation
            or p.allow_portfolio_construction
            or p.allow_position_sizing
            or p.allow_optimizer_execution
            or p.allow_model_training
            or p.allow_prediction_generation
        ):
            return False
    return True
