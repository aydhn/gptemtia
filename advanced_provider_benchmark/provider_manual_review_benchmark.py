from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkRecord,
    build_provider_benchmark_record_id,
)

MANUAL_REVIEW_PROVIDERS = [
    ("advanced_fx_providers_engine", "provider_domain_fx", 0.95, "Low manual review load (deterministic offline fixtures)", False),
    ("advanced_commodity_providers_engine", "provider_domain_commodity", 0.90, "Low manual review load (futures roll calendar checked)", False),
    ("advanced_macro_providers_engine", "provider_domain_macro", 0.92, "Low manual review load (standard macro taxonomy)", False),
    ("advanced_economic_calendar_engine", "provider_domain_calendar", 0.88, "Moderate review load for non-standard surprise revisions", False),
    ("advanced_news_metadata_engine", "provider_domain_news_metadata", 0.85, "Moderate review load for new topic tag taxonomy mapping", False),
    ("manual_file_provider_adapter", "provider_domain_cross_domain", 0.50, "High manual review load: schema inspection required for custom user uploads", True),
    ("local_cache_provider_adapter", "provider_domain_cross_domain", 0.95, "Low manual review load: cache hit validation automated", False),
    ("official_api_provider_placeholder", "provider_domain_cross_domain", 0.60, "High review load: API key policy and vendor documentation review", True),
    ("licensed_vendor_provider_placeholder", "provider_domain_cross_domain", 0.55, "High review load: commercial contract and licensing review needed", True),
]


def build_provider_manual_review_benchmark_report(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records: List[ProviderBenchmarkRecord] = []
    for prov_name, domain, score, evidence, rev_req in MANUAL_REVIEW_PROVIDERS:
        rec_id = build_provider_benchmark_record_id(prov_name, "metric_manual_review_load")
        status = "benchmark_pass" if score >= profile.min_benchmark_score else "benchmark_partial"
        if rev_req:
            status = "benchmark_manual_review_required"
        records.append(
            ProviderBenchmarkRecord(
                record_id=rec_id,
                provider_name=prov_name,
                provider_domain=domain,
                metric_label="metric_manual_review_load",
                raw_score=score,
                weighted_score=round(score * 0.05, 4),
                status_label=status,
                evidence_ref=evidence,
                limitation_note="Manual review evaluations are strictly non-destructive; no automated file modifications",
                manual_review_required=rev_req,
            )
        )
    records_dict = [r.to_dict() for r in records]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_manual_review_benchmark(df)
    return df, summary


def summarize_provider_manual_review_benchmark(df: pd.DataFrame) -> Dict[str, Any]:
    mean_score = float(df["raw_score"].mean()) if not df.empty and "raw_score" in df.columns else 0.0
    return {
        "total_providers_evaluated": len(df),
        "mean_manual_review_efficiency_score": round(mean_score, 4),
        "manual_review_required_count": int(df["manual_review_required"].sum()) if not df.empty and "manual_review_required" in df.columns else 0,
        "destructive_action_allowed": False,
        "current_phase": 115,
        "target_final_phase": 160,
    }
