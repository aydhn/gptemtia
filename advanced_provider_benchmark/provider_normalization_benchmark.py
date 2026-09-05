from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkRecord,
    build_provider_benchmark_record_id,
)

NORMALIZATION_PROVIDERS = [
    ("advanced_fx_providers_engine", "provider_domain_fx", 0.95, "Phase 113 FX symbol normalization: uppercase standard pairs with UTC ISO timestamps", False),
    ("advanced_commodity_providers_engine", "provider_domain_commodity", 0.92, "Phase 113 Commodity symbol & unit normalization (USD/bbl, USD/oz)", False),
    ("advanced_macro_providers_engine", "provider_domain_macro", 0.90, "Phase 113 Macro indicator normalization & unit standardization (percent, index_points)", False),
    ("advanced_economic_calendar_engine", "provider_domain_calendar", 0.92, "Phase 113 Calendar event normalization & country ISO alpha-2 codes", False),
    ("advanced_news_metadata_engine", "provider_domain_news_metadata", 0.88, "Phase 113 News tag normalization: slug format and canonical taxonomy linking", False),
    ("manual_file_provider_adapter", "provider_domain_cross_domain", 0.68, "Phase 113 requires fallback field mapping for custom user schemas", True),
    ("local_cache_provider_adapter", "provider_domain_cross_domain", 0.91, "Phase 113 cached frames match canonical schema versions exactly", False),
    ("official_api_provider_placeholder", "provider_domain_cross_domain", 0.85, "Phase 113 API response adapters produce normalized target views", True),
    ("licensed_vendor_provider_placeholder", "provider_domain_cross_domain", 0.86, "Phase 113 vendor feed transformations map cleanly to canonical contracts", True),
]


def build_provider_normalization_benchmark_report(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records: List[ProviderBenchmarkRecord] = []
    for prov_name, domain, score, evidence, rev_req in NORMALIZATION_PROVIDERS:
        rec_id = build_provider_benchmark_record_id(prov_name, "metric_normalization")
        status = "benchmark_pass" if score >= profile.min_benchmark_score else "benchmark_partial"
        if rev_req:
            status = "benchmark_manual_review_required"
        records.append(
            ProviderBenchmarkRecord(
                record_id=rec_id,
                provider_name=prov_name,
                provider_domain=domain,
                metric_label="metric_normalization",
                raw_score=score,
                weighted_score=round(score * 0.15, 4),
                status_label=status,
                evidence_ref=evidence,
                limitation_note="Derived from Phase 113 normalization manifests; non-destructive views only",
                manual_review_required=rev_req,
            )
        )
    records_dict = [r.to_dict() for r in records]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_normalization_benchmark(df)
    return df, summary


def summarize_provider_normalization_benchmark(df: pd.DataFrame) -> Dict[str, Any]:
    mean_score = float(df["raw_score"].mean()) if not df.empty and "raw_score" in df.columns else 0.0
    return {
        "total_providers_evaluated": len(df),
        "mean_normalization_score": round(mean_score, 4),
        "manual_review_count": int(df["manual_review_required"].sum()) if not df.empty and "manual_review_required" in df.columns else 0,
        "current_phase": 115,
        "target_final_phase": 160,
    }
