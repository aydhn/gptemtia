from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_models import (
    BenchmarkMetric,
    build_benchmark_metric_id,
)

METRIC_SPECS = [
    (
        "metric_coverage",
        "Asset and Universe Coverage",
        "Breadth and depth of supported symbols, pairs, indicators, and events",
        "higher_is_better",
        "Diagnostic metric; does not certify completeness or live availability",
        False,
    ),
    (
        "metric_capability",
        "Technical Capabilities",
        "Presence of quote, OHLCV, tick, timestamp granularity, and metadata feeds",
        "higher_is_better",
        "Diagnostic metric; does not imply broker execution or latency guarantees",
        False,
    ),
    (
        "metric_quality",
        "Data Quality Integrity",
        "Absence of stale, missing, duplicate, or outlier anomalies from Phase 112",
        "higher_is_better",
        "Diagnostic metric; historical quality does not guarantee future reliability",
        False,
    ),
    (
        "metric_normalization",
        "Schema & Normalization Adherence",
        "Conformity to canonical schema, uppercase tokens, and UTC time from Phase 113",
        "higher_is_better",
        "Diagnostic metric; normalization is non-destructive and source-preserving",
        False,
    ),
    (
        "metric_traceability",
        "Lineage and Traceability",
        "Completeness of source-to-canonical transformation audit trail from Phase 114",
        "higher_is_better",
        "Diagnostic metric; internal auditability evaluation only",
        False,
    ),
    (
        "metric_license_provenance",
        "License and Redistribution Boundary",
        "Adherence to open research, offline usage, and non-commercial boundaries",
        "higher_is_better",
        "Requires manual review for proprietary vendor contracts",
        True,
    ),
    (
        "metric_no_scraping_compliance",
        "Strict No-Scraping Compliance",
        "100% adherence to zero web scraping, zero HTML parsing, zero bot automation",
        "higher_is_better",
        "Mandatory binary/fractional compliance filter; non-compliant providers rejected",
        False,
    ),
    (
        "metric_metadata_only_compliance",
        "Metadata-Only & Zero Full Text",
        "Strict verification that no full article texts or copyrighted news bodies are gathered",
        "higher_is_better",
        "Mandatory for news metadata providers; protects against copyright infringement",
        False,
    ),
    (
        "metric_manual_review_load",
        "Manual Review Burden",
        "Volume of outstanding non-destructive manual review items required for safety",
        "lower_is_better",
        "High review load requires operational attention before feature ingestion",
        True,
    ),
    (
        "metric_cross_domain_consistency",
        "Cross-Domain Alignment",
        "Consistency of cross-asset entity mappings (FX, commodities, macro, news tags)",
        "higher_is_better",
        "Diagnostic metric; cross-asset alignment supports multi-factor research",
        False,
    ),
    (
        "metric_unknown",
        "Unknown Metric Fallback",
        "Fallback category for unclassified benchmark measurements",
        "neutral",
        "Fallback record only",
        True,
    ),
]


def build_default_benchmark_metrics(
    profile: ProviderBenchmarkProfile,
) -> List[BenchmarkMetric]:
    metrics: List[BenchmarkMetric] = []
    for label, name, desc, direction, note, rev_req in METRIC_SPECS:
        m_id = build_benchmark_metric_id(label)
        metrics.append(
            BenchmarkMetric(
                metric_id=m_id,
                metric_label=label,
                metric_name=name,
                description=desc,
                score_direction=direction,
                safe_usage_note=note,
                manual_review_required=rev_req,
            )
        )
    return metrics


def build_provider_benchmark_metric_registry(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    metrics = build_default_benchmark_metrics(profile)
    records_dict = [m.to_dict() for m in metrics]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_benchmark_metric_registry(df)
    return df, summary


def summarize_provider_benchmark_metric_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_metrics": len(df),
        "metric_labels": df["metric_label"].tolist() if "metric_label" in df.columns else [],
        "manual_review_metrics_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "current_phase": 115,
        "target_final_phase": 160,
    }
