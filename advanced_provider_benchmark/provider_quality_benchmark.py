from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkRecord,
    build_provider_benchmark_record_id,
)

QUALITY_PROVIDERS = [
    ("advanced_fx_providers_engine", "provider_domain_fx", 0.94, "Phase 112 FX quality rules passed: zero stale quotes, valid spreads", False),
    ("advanced_commodity_providers_engine", "provider_domain_commodity", 0.91, "Phase 112 Commodity quality rules: zero negative prices, valid OHLC", False),
    ("advanced_macro_providers_engine", "provider_domain_macro", 0.89, "Phase 112 Macro quality rules: frequency integrity and release timestamp consistency", False),
    ("advanced_economic_calendar_engine", "provider_domain_calendar", 0.93, "Phase 112 Calendar rules: consensus/actual numerical sanity", False),
    ("advanced_news_metadata_engine", "provider_domain_news_metadata", 0.87, "Phase 112 News quality rules: title freshness and duplicate slug prevention", False),
    ("manual_file_provider_adapter", "provider_domain_cross_domain", 0.70, "Phase 112 schema compliance warnings detected for unformatted headers", True),
    ("local_cache_provider_adapter", "provider_domain_cross_domain", 0.88, "Phase 112 cache integrity verified with zero data corruption", False),
    ("official_api_provider_placeholder", "provider_domain_cross_domain", 0.82, "Phase 112 mock responses conform to API payload schemas", True),
    ("licensed_vendor_provider_placeholder", "provider_domain_cross_domain", 0.85, "Phase 112 vendor contracts pass strict type validation", True),
]


def build_provider_quality_benchmark_report(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records: List[ProviderBenchmarkRecord] = []
    for prov_name, domain, score, evidence, rev_req in QUALITY_PROVIDERS:
        rec_id = build_provider_benchmark_record_id(prov_name, "metric_quality")
        status = "benchmark_pass" if score >= profile.min_benchmark_score else "benchmark_partial"
        if rev_req:
            status = "benchmark_manual_review_required"
        records.append(
            ProviderBenchmarkRecord(
                record_id=rec_id,
                provider_name=prov_name,
                provider_domain=domain,
                metric_label="metric_quality",
                raw_score=score,
                weighted_score=round(score * 0.15, 4),
                status_label=status,
                evidence_ref=evidence,
                limitation_note="Derived from Phase 112 quality findings; historical performance only",
                manual_review_required=rev_req,
            )
        )
    records_dict = [r.to_dict() for r in records]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_quality_benchmark(df)
    return df, summary


def summarize_provider_quality_benchmark(df: pd.DataFrame) -> Dict[str, Any]:
    mean_score = float(df["raw_score"].mean()) if not df.empty and "raw_score" in df.columns else 0.0
    return {
        "total_providers_evaluated": len(df),
        "mean_quality_score": round(mean_score, 4),
        "manual_review_count": int(df["manual_review_required"].sum()) if not df.empty and "manual_review_required" in df.columns else 0,
        "current_phase": 115,
        "target_final_phase": 160,
    }
