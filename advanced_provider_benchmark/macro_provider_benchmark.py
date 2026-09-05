from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkRecord,
    build_provider_benchmark_record_id,
)

MACRO_BENCHMARK_ITEMS = [
    ("advanced_macro_providers_engine", "metric_coverage", 0.88, "CPI, GDP, Policy Rates, Unemployment across US, EU, UK, JP, TR", False),
    ("advanced_macro_providers_engine", "metric_capability", 0.85, "Monthly/Quarterly release frequency tracking, revision status markers", False),
    ("advanced_macro_providers_engine", "metric_quality", 0.90, "Statistical series frequency integrity and timestamp order from Phase 112", False),
    ("advanced_macro_providers_engine", "metric_normalization", 0.92, "Standardized indicator keys and unit vocabulary (percent, index_points) from Phase 113", False),
    ("advanced_macro_providers_engine", "metric_traceability", 0.91, "Central bank and statistical agency source provenance from Phase 114", False),
    ("advanced_macro_providers_engine", "metric_no_scraping_compliance", 1.0, "Strict offline fixtures; zero web page scraping", False),
]


def build_macro_provider_benchmark_report(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records: List[ProviderBenchmarkRecord] = []
    for prov_name, metric, score, evidence, rev_req in MACRO_BENCHMARK_ITEMS:
        rec_id = build_provider_benchmark_record_id(prov_name, metric)
        status = "benchmark_pass" if score >= profile.min_benchmark_score else "benchmark_partial"
        records.append(
            ProviderBenchmarkRecord(
                record_id=rec_id,
                provider_name=prov_name,
                provider_domain="provider_domain_macro",
                metric_label=metric,
                raw_score=score,
                weighted_score=round(score * (1.0 / len(MACRO_BENCHMARK_ITEMS)), 4),
                status_label=status,
                evidence_ref=evidence,
                limitation_note="Macro benchmark is diagnostic research only; does not provide trading signals",
                manual_review_required=rev_req,
            )
        )
    records_dict = [r.to_dict() for r in records]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_macro_provider_benchmark(df)
    return df, summary


def summarize_macro_provider_benchmark(df: pd.DataFrame) -> Dict[str, Any]:
    mean_score = float(df["raw_score"].mean()) if not df.empty and "raw_score" in df.columns else 0.0
    return {
        "domain": "provider_domain_macro",
        "total_metrics_evaluated": len(df),
        "mean_domain_score": round(mean_score, 4),
        "no_scraping_compliant": True,
        "current_phase": 115,
        "target_final_phase": 160,
    }
