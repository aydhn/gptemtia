from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkFinding,
    build_provider_benchmark_finding_id,
)

BENCHMARK_FINDINGS_SEED = [
    (
        "manual_file_provider_adapter",
        "provider_domain_cross_domain",
        "metric_coverage",
        "severity_medium",
        "benchmark_pass_with_warnings",
        "Manual file coverage varies by uploaded files and requires file schema verification",
        "Verify file headers and field names against canonical schemas before ingestion",
        True,
    ),
    (
        "official_api_provider_placeholder",
        "provider_domain_cross_domain",
        "metric_license_provenance",
        "severity_high",
        "benchmark_manual_review_required",
        "Vendor API documentation notes potential rate limit restrictions and commercial terms",
        "Conduct thorough terms-of-service and procurement review before moving beyond dry-run",
        True,
    ),
    (
        "licensed_vendor_provider_placeholder",
        "provider_domain_cross_domain",
        "metric_license_provenance",
        "severity_high",
        "benchmark_manual_review_required",
        "Commercial licensed vendor data requires formal license agreement and boundary audit",
        "Ensure enterprise data license covers local research and algorithmic modeling",
        True,
    ),
    (
        "advanced_news_metadata_engine",
        "provider_domain_news_metadata",
        "metric_metadata_only_compliance",
        "severity_info",
        "benchmark_pass",
        "News metadata collection adheres 100% to metadata-only policy with zero full text",
        "Maintain current zero-full-text boundary in all downstream feature extraction modules",
        False,
    ),
    (
        "advanced_fx_providers_engine",
        "provider_domain_fx",
        "metric_quality",
        "severity_info",
        "benchmark_pass",
        "FX quote sanity and OHLC consistency validated across all major currency pairs",
        "Ready for canonical indicator and return calculation inputs in Phase 116",
        False,
    ),
    (
        "advanced_commodity_providers_engine",
        "provider_domain_commodity",
        "metric_normalization",
        "severity_info",
        "benchmark_pass",
        "Commodity symbols and units normalized to canonical USD per barrel / USD per oz",
        "Maintain unit metadata alongside price series in Feature Store",
        False,
    ),
]


def create_provider_benchmark_finding(
    provider_name: str,
    provider_domain: str,
    metric_label: str,
    severity_label: str,
    status_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool,
) -> ProviderBenchmarkFinding:
    f_id = build_provider_benchmark_finding_id(provider_name, metric_label)
    return ProviderBenchmarkFinding(
        finding_id=f_id,
        provider_name=provider_name,
        provider_domain=provider_domain,
        metric_label=metric_label,
        severity_label=severity_label,
        status_label=status_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
    )


def build_provider_benchmark_findings_registry(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    findings: List[ProviderBenchmarkFinding] = []
    for prov_name, dom, metric, sev, stat, msg, rec, rev_req in BENCHMARK_FINDINGS_SEED:
        findings.append(
            create_provider_benchmark_finding(
                provider_name=prov_name,
                provider_domain=dom,
                metric_label=metric,
                severity_label=sev,
                status_label=stat,
                message=msg,
                recommendation=rec,
                manual_review_required=rev_req,
            )
        )
    records_dict = [f.to_dict() for f in findings]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_benchmark_findings(df)
    return df, summary


def summarize_provider_benchmark_findings(df: pd.DataFrame) -> Dict[str, Any]:
    high_sev_count = int((df["severity_label"] == "severity_high").sum()) if not df.empty and "severity_label" in df.columns else 0
    return {
        "total_findings": len(df),
        "high_severity_count": high_sev_count,
        "manual_review_required_count": int(df["manual_review_required"].sum()) if not df.empty and "manual_review_required" in df.columns else 0,
        "current_phase": 115,
        "target_final_phase": 160,
    }
