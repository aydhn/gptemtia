from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkRecord,
    build_provider_benchmark_record_id,
)

LICENSE_PROVIDERS = [
    ("advanced_fx_providers_engine", "provider_domain_fx", 0.95, "Open research local mock; zero external distribution claims", False),
    ("advanced_commodity_providers_engine", "provider_domain_commodity", 0.95, "Open research local mock; zero exchange feed reproduction", False),
    ("advanced_macro_providers_engine", "provider_domain_macro", 0.95, "Public domain / government statistical indicator references", False),
    ("advanced_economic_calendar_engine", "provider_domain_calendar", 0.95, "Synthetic offline event schedule; no proprietary calendar republication", False),
    ("advanced_news_metadata_engine", "provider_domain_news_metadata", 0.90, "Strict metadata-only fair-use boundary; zero full article text", False),
    ("manual_file_provider_adapter", "provider_domain_cross_domain", 0.70, "User responsibility for uploaded data licensing", True),
    ("local_cache_provider_adapter", "provider_domain_cross_domain", 0.95, "Local machine boundary; no external redistribution", False),
    ("official_api_provider_placeholder", "provider_domain_cross_domain", 0.65, "Vendor public terms require license review before live production use", True),
    ("licensed_vendor_provider_placeholder", "provider_domain_cross_domain", 0.60, "Commercial proprietary vendor terms require corporate procurement approval", True),
]


def build_provider_license_provenance_benchmark_report(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records: List[ProviderBenchmarkRecord] = []
    for prov_name, domain, score, evidence, rev_req in LICENSE_PROVIDERS:
        rec_id = build_provider_benchmark_record_id(prov_name, "metric_license_provenance")
        status = "benchmark_pass" if score >= profile.min_benchmark_score else "benchmark_partial"
        if rev_req:
            status = "benchmark_manual_review_required"
        records.append(
            ProviderBenchmarkRecord(
                record_id=rec_id,
                provider_name=prov_name,
                provider_domain=domain,
                metric_label="metric_license_provenance",
                raw_score=score,
                weighted_score=round(score * 0.05, 4),
                status_label=status,
                evidence_ref=evidence,
                limitation_note="Licensing evaluation for offline research only; not legal advice or official release",
                manual_review_required=rev_req,
            )
        )
    records_dict = [r.to_dict() for r in records]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_license_provenance_benchmark(df)
    return df, summary


def summarize_provider_license_provenance_benchmark(df: pd.DataFrame) -> Dict[str, Any]:
    mean_score = float(df["raw_score"].mean()) if not df.empty and "raw_score" in df.columns else 0.0
    return {
        "total_providers_evaluated": len(df),
        "mean_license_score": round(mean_score, 4),
        "manual_review_count": int(df["manual_review_required"].sum()) if not df.empty and "manual_review_required" in df.columns else 0,
        "current_phase": 115,
        "target_final_phase": 160,
    }
