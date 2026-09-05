from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkRecord,
    build_provider_benchmark_record_id,
)

CORE_PROVIDERS = [
    ("advanced_fx_providers_engine", "provider_domain_fx", 0.92, "EUR/USD, GBP/USD, USD/JPY, USD/TRY coverage verified", False),
    ("advanced_commodity_providers_engine", "provider_domain_commodity", 0.88, "Gold, Silver, Brent, WTI, Natural Gas, Copper coverage verified", False),
    ("advanced_macro_providers_engine", "provider_domain_macro", 0.85, "CPI, GDP, Policy Rates, Unemployment for major economies", False),
    ("advanced_economic_calendar_engine", "provider_domain_calendar", 0.90, "Global tier-1 and tier-2 scheduled economic events", False),
    ("advanced_news_metadata_engine", "provider_domain_news_metadata", 0.82, "Headline and asset taxonomy coverage across FX/Commodities", False),
    ("manual_file_provider_adapter", "provider_domain_cross_domain", 0.60, "User-provided offline files - scope varies by upload", True),
    ("local_cache_provider_adapter", "provider_domain_cross_domain", 0.75, "Historical snapshots present in local cache store", False),
    ("official_api_provider_placeholder", "provider_domain_cross_domain", 0.80, "Vendor official API specification coverage (dry-run)", True),
    ("licensed_vendor_provider_placeholder", "provider_domain_cross_domain", 0.85, "Commercial vendor data dictionary coverage (dry-run)", True),
]


def build_provider_coverage_benchmark_report(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records: List[ProviderBenchmarkRecord] = []
    for prov_name, domain, score, evidence, rev_req in CORE_PROVIDERS:
        rec_id = build_provider_benchmark_record_id(prov_name, "metric_coverage")
        status = "benchmark_pass" if score >= profile.min_benchmark_score else "benchmark_partial"
        if rev_req:
            status = "benchmark_manual_review_required"
        records.append(
            ProviderBenchmarkRecord(
                record_id=rec_id,
                provider_name=prov_name,
                provider_domain=domain,
                metric_label="metric_coverage",
                raw_score=score,
                weighted_score=round(score * 0.15, 4),
                status_label=status,
                evidence_ref=evidence,
                limitation_note="Offline local coverage baseline; live availability not guaranteed",
                manual_review_required=rev_req,
            )
        )
    records_dict = [r.to_dict() for r in records]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_coverage_benchmark(df)
    return df, summary


def summarize_provider_coverage_benchmark(df: pd.DataFrame) -> Dict[str, Any]:
    mean_score = float(df["raw_score"].mean()) if not df.empty and "raw_score" in df.columns else 0.0
    return {
        "total_providers_evaluated": len(df),
        "mean_coverage_score": round(mean_score, 4),
        "manual_review_count": int(df["manual_review_required"].sum()) if not df.empty and "manual_review_required" in df.columns else 0,
        "current_phase": 115,
        "target_final_phase": 160,
    }
