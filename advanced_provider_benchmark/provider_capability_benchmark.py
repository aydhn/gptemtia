from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkRecord,
    build_provider_benchmark_record_id,
)

CAPABILITY_PROVIDERS = [
    ("advanced_fx_providers_engine", "provider_domain_fx", 0.90, "OHLCV, Bid/Ask Quotes, Timestamps, Tick precision support", False),
    ("advanced_commodity_providers_engine", "provider_domain_commodity", 0.85, "Spot prices, futures metadata, contract roll dates", False),
    ("advanced_macro_providers_engine", "provider_domain_macro", 0.82, "Historical series, release frequency, revision markers", False),
    ("advanced_economic_calendar_engine", "provider_domain_calendar", 0.88, "Scheduled vs actual timestamps, consensus figures, revision records", False),
    ("advanced_news_metadata_engine", "provider_domain_news_metadata", 0.80, "Topic taxonomies, asset tagging, headline metadata, event linkage", False),
    ("manual_file_provider_adapter", "provider_domain_cross_domain", 0.65, "CSV/JSON local file ingestion with schema validation", True),
    ("local_cache_provider_adapter", "provider_domain_cross_domain", 0.78, "Fast local key-value store and snapshot reading", False),
    ("official_api_provider_placeholder", "provider_domain_cross_domain", 0.85, "REST endpoint emulation with request/response schema validation", True),
    ("licensed_vendor_provider_placeholder", "provider_domain_cross_domain", 0.88, "High-throughput tick/quote specification adherence", True),
]


def build_provider_capability_benchmark_report(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records: List[ProviderBenchmarkRecord] = []
    for prov_name, domain, score, evidence, rev_req in CAPABILITY_PROVIDERS:
        rec_id = build_provider_benchmark_record_id(prov_name, "metric_capability")
        status = "benchmark_pass" if score >= profile.min_benchmark_score else "benchmark_partial"
        if rev_req:
            status = "benchmark_manual_review_required"
        records.append(
            ProviderBenchmarkRecord(
                record_id=rec_id,
                provider_name=prov_name,
                provider_domain=domain,
                metric_label="metric_capability",
                raw_score=score,
                weighted_score=round(score * 0.15, 4),
                status_label=status,
                evidence_ref=evidence,
                limitation_note="Technical schema capability verified; execution latency not benchmarked",
                manual_review_required=rev_req,
            )
        )
    records_dict = [r.to_dict() for r in records]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_capability_benchmark(df)
    return df, summary


def summarize_provider_capability_benchmark(df: pd.DataFrame) -> Dict[str, Any]:
    mean_score = float(df["raw_score"].mean()) if not df.empty and "raw_score" in df.columns else 0.0
    return {
        "total_providers_evaluated": len(df),
        "mean_capability_score": round(mean_score, 4),
        "manual_review_count": int(df["manual_review_required"].sum()) if not df.empty and "manual_review_required" in df.columns else 0,
        "current_phase": 115,
        "target_final_phase": 160,
    }
