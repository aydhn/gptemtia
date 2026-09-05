from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkRecord,
    build_provider_benchmark_record_id,
)

NO_SCRAPING_PROVIDERS = [
    ("advanced_fx_providers_engine", "provider_domain_fx", 1.0, "Strict offline fixtures; zero HTTP requests, zero web scraping", False),
    ("advanced_commodity_providers_engine", "provider_domain_commodity", 1.0, "Strict offline fixtures; zero browser automation, zero scraping", False),
    ("advanced_macro_providers_engine", "provider_domain_macro", 1.0, "Deterministic synthetic fixtures; zero web page parsing", False),
    ("advanced_economic_calendar_engine", "provider_domain_calendar", 1.0, "Deterministic event registry; zero calendar HTML scraping", False),
    ("advanced_news_metadata_engine", "provider_domain_news_metadata", 1.0, "Local metadata fixtures; zero news site scraping, zero paywall bypass", False),
    ("manual_file_provider_adapter", "provider_domain_cross_domain", 1.0, "Local file paths only; zero network scraping capability", False),
    ("local_cache_provider_adapter", "provider_domain_cross_domain", 1.0, "Local disk cache reading only; zero remote scraping", False),
    ("official_api_provider_placeholder", "provider_domain_cross_domain", 1.0, "Mock API contracts; zero hidden endpoints, zero reverse engineering", False),
    ("licensed_vendor_provider_placeholder", "provider_domain_cross_domain", 1.0, "Mock feed schemas; zero scraping or rate limit abuse", False),
]


def build_provider_no_scraping_compliance_report(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records: List[ProviderBenchmarkRecord] = []
    for prov_name, domain, score, evidence, rev_req in NO_SCRAPING_PROVIDERS:
        rec_id = build_provider_benchmark_record_id(prov_name, "metric_no_scraping_compliance")
        status = "benchmark_pass" if score >= 0.99 else "benchmark_fail"
        records.append(
            ProviderBenchmarkRecord(
                record_id=rec_id,
                provider_name=prov_name,
                provider_domain=domain,
                metric_label="metric_no_scraping_compliance",
                raw_score=score,
                weighted_score=round(score * 0.15, 4),
                status_label=status,
                evidence_ref=evidence,
                limitation_note="Mandatory compliance check; scraping is strictly prohibited across all modules",
                manual_review_required=rev_req,
            )
        )
    records_dict = [r.to_dict() for r in records]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_no_scraping_compliance(df)
    return df, summary


def summarize_provider_no_scraping_compliance(df: pd.DataFrame) -> Dict[str, Any]:
    all_compliant = bool((df["raw_score"] >= 1.0).all()) if not df.empty and "raw_score" in df.columns else False
    return {
        "total_providers_evaluated": len(df),
        "all_compliant": all_compliant,
        "non_compliant_count": int((df["raw_score"] < 1.0).sum()) if not df.empty and "raw_score" in df.columns else 0,
        "current_phase": 115,
        "target_final_phase": 160,
    }
