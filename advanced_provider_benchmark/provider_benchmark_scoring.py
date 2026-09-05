from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkScore,
    build_provider_benchmark_score_id,
)
from advanced_provider_benchmark.provider_benchmark_weight_registry import (
    build_provider_benchmark_weight_registry,
)

EVALUATED_PROVIDERS = [
    ("advanced_fx_providers_engine", "provider_domain_fx", 0.94, 0.92, 0.95, 0.96, 0.94, 1.0, 0.0),
    ("advanced_commodity_providers_engine", "provider_domain_commodity", 0.90, 0.88, 0.92, 0.93, 0.91, 1.0, 0.0),
    ("advanced_macro_providers_engine", "provider_domain_macro", 0.88, 0.85, 0.90, 0.92, 0.91, 1.0, 0.0),
    ("advanced_economic_calendar_engine", "provider_domain_calendar", 0.92, 0.89, 0.94, 0.93, 0.93, 1.0, 0.0),
    ("advanced_news_metadata_engine", "provider_domain_news_metadata", 0.85, 0.83, 0.88, 0.89, 0.90, 1.0, 0.0),
    ("manual_file_provider_adapter", "provider_domain_cross_domain", 0.60, 0.65, 0.70, 0.68, 0.72, 0.95, 0.15),
    ("local_cache_provider_adapter", "provider_domain_cross_domain", 0.75, 0.78, 0.88, 0.91, 0.93, 1.0, 0.0),
    ("official_api_provider_placeholder", "provider_domain_cross_domain", 0.80, 0.85, 0.82, 0.85, 0.82, 1.0, 0.10),
    ("licensed_vendor_provider_placeholder", "provider_domain_cross_domain", 0.85, 0.88, 0.85, 0.86, 0.84, 1.0, 0.12),
]


def classify_provider_benchmark_score(score: float, profile: ProviderBenchmarkProfile) -> str:
    if score >= 0.85:
        return "benchmark_pass"
    elif score >= profile.min_benchmark_score:
        return "benchmark_pass_with_warnings"
    else:
        return "benchmark_partial"


def calculate_provider_benchmark_score(
    records_df: pd.DataFrame,
    provider_name: str,
    provider_domain: str,
    weights_df: pd.DataFrame,
    profile: ProviderBenchmarkProfile,
) -> ProviderBenchmarkScore:
    # Default scores if not present in records_df
    cov = 0.85
    cap = 0.85
    qual = 0.85
    norm = 0.85
    trace = 0.85
    comp = 1.0
    penalty = 0.0

    if records_df is not None and not records_df.empty and "provider_name" in records_df.columns:
        p_rows = records_df[records_df["provider_name"] == provider_name]
        if not p_rows.empty:
            for _, row in p_rows.iterrows():
                m = row.get("metric_label", "")
                val = float(row.get("raw_score", 0.85))
                if m == "metric_coverage":
                    cov = val
                elif m == "metric_capability":
                    cap = val
                elif m == "metric_quality":
                    qual = val
                elif m == "metric_normalization":
                    norm = val
                elif m == "metric_traceability":
                    trace = val
                elif m in ("metric_no_scraping_compliance", "metric_metadata_only_compliance"):
                    comp = min(comp, val)
                elif m == "metric_manual_review_load":
                    penalty = round(max(0.0, 1.0 - val) * 0.15, 4)

    raw_total = (cov * 0.15) + (cap * 0.15) + (qual * 0.20) + (norm * 0.15) + (trace * 0.15) + (comp * 0.20) - penalty
    total_score = max(0.0, min(1.0, round(raw_total, 4)))
    status = classify_provider_benchmark_score(total_score, profile)
    score_id = build_provider_benchmark_score_id(provider_name, provider_domain)

    return ProviderBenchmarkScore(
        score_id=score_id,
        provider_name=provider_name,
        provider_domain=provider_domain,
        total_score=total_score,
        coverage_score=round(cov, 4),
        capability_score=round(cap, 4),
        quality_score=round(qual, 4),
        normalization_score=round(norm, 4),
        traceability_score=round(trace, 4),
        compliance_score=round(comp, 4),
        manual_review_penalty=round(penalty, 4),
        status_label=status,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        notes="Offline comparative diagnostic benchmark score; not a trading signal or approval",
    )


def build_provider_benchmark_score_report(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    weights_df, _ = build_provider_benchmark_weight_registry(profile)
    scores: List[ProviderBenchmarkScore] = []
    for prov_name, domain, cov, cap, qual, norm, trace, comp, penalty in EVALUATED_PROVIDERS:
        raw_total = (cov * 0.15) + (cap * 0.15) + (qual * 0.20) + (norm * 0.15) + (trace * 0.15) + (comp * 0.20) - penalty
        total_score = max(0.0, min(1.0, round(raw_total, 4)))
        status = classify_provider_benchmark_score(total_score, profile)
        score_id = build_provider_benchmark_score_id(prov_name, domain)
        scores.append(
            ProviderBenchmarkScore(
                score_id=score_id,
                provider_name=prov_name,
                provider_domain=domain,
                total_score=total_score,
                coverage_score=round(cov, 4),
                capability_score=round(cap, 4),
                quality_score=round(qual, 4),
                normalization_score=round(norm, 4),
                traceability_score=round(trace, 4),
                compliance_score=round(comp, 4),
                manual_review_penalty=round(penalty, 4),
                status_label=status,
                official_approval=False,
                production_ready=False,
                broker_ready=False,
                notes="Offline comparative diagnostic benchmark score; not a trading signal or approval",
            )
        )
    records_dict = [s.to_dict() for s in scores]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_benchmark_scores(df)
    return df, summary


def summarize_provider_benchmark_scores(df: pd.DataFrame) -> Dict[str, Any]:
    mean_score = float(df["total_score"].mean()) if not df.empty and "total_score" in df.columns else 0.0
    return {
        "total_providers_scored": len(df),
        "mean_benchmark_score": round(mean_score, 4),
        "max_benchmark_score": float(df["total_score"].max()) if not df.empty and "total_score" in df.columns else 0.0,
        "min_benchmark_score": float(df["total_score"].min()) if not df.empty and "total_score" in df.columns else 0.0,
        "official_approval_guarantee": False,
        "production_ready_guarantee": False,
        "broker_ready_guarantee": False,
        "trade_signal_disclaimer": "Benchmark scores must NEVER be used as buy/sell signals",
        "current_phase": 115,
        "target_final_phase": 160,
    }
