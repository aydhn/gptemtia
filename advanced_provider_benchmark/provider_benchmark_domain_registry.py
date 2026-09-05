from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_labels import BENCHMARK_DOMAIN_LABELS
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkDomain,
    build_provider_benchmark_domain_id,
)

DOMAIN_METADATA = {
    "provider_benchmark_profile_domain": ("Provider Benchmark Profile Domain", "Configuration profiles for local provider benchmarking", ["profile_registry"]),
    "provider_benchmark_domain": ("Provider Benchmark Master Domain", "Master provider benchmark abstraction and registries", ["domain_registry"]),
    "benchmark_metric_domain": ("Benchmark Metric Domain", "Metrics registry for provider capability and quality", ["metric_registry"]),
    "benchmark_weight_domain": ("Benchmark Weight Domain", "Weight specifications for multi-metric aggregation", ["weight_registry"]),
    "coverage_benchmark_domain": ("Coverage Benchmark Domain", "Assessment of asset/symbol/indicator coverage breadth", ["coverage_report"]),
    "capability_benchmark_domain": ("Capability Benchmark Domain", "Assessment of technical timeseries/quote/event capabilities", ["capability_report"]),
    "quality_benchmark_domain": ("Quality Benchmark Domain", "Evaluation of data quality findings and clean rates", ["quality_report"]),
    "normalization_benchmark_domain": ("Normalization Benchmark Domain", "Canonical schema conformance and normalization adherence", ["normalization_report"]),
    "traceability_benchmark_domain": ("Traceability Benchmark Domain", "Provenance and audit trail traceability evaluation", ["traceability_report"]),
    "license_provenance_benchmark_domain": ("License & Provenance Benchmark Domain", "Licensing terms and redistribution limitations", ["license_report"]),
    "no_scraping_compliance_domain": ("No-Scraping Compliance Domain", "Strict verification of zero web scraping boundaries", ["no_scraping_report"]),
    "metadata_only_compliance_domain": ("Metadata-Only Compliance Domain", "Zero full-text article extraction validation", ["metadata_only_report"]),
    "manual_review_benchmark_domain": ("Manual Review Benchmark Domain", "Evaluation of manual review queue load and non-destructive action", ["manual_review_report"]),
    "fx_provider_benchmark_domain": ("FX Provider Benchmark Domain", "FX specific pair coverage, quote sanity and OHLCV readiness", ["fx_benchmark_report"]),
    "commodity_provider_benchmark_domain": ("Commodity Provider Benchmark Domain", "Commodity spot/futures contract and roll metadata readiness", ["commodity_benchmark_report"]),
    "macro_provider_benchmark_domain": ("Macro Provider Benchmark Domain", "Macroeconomic indicator universe and revision metadata", ["macro_benchmark_report"]),
    "calendar_provider_benchmark_domain": ("Calendar Provider Benchmark Domain", "Economic calendar event universe and release timestamp precision", ["calendar_benchmark_report"]),
    "news_metadata_provider_benchmark_domain": ("News Metadata Provider Benchmark Domain", "News headline/topic taxonomy and event linkage without full text", ["news_benchmark_report"]),
    "cross_domain_provider_benchmark_domain": ("Cross-Domain Provider Benchmark Domain", "Cross-asset alignment and symbol-tag consistency", ["cross_domain_report"]),
    "benchmark_scoring_domain": ("Benchmark Scoring Domain", "Non-trading comparative diagnostic score calculation", ["score_report"]),
    "provider_ranking_research_domain": ("Provider Ranking Research Domain", "Offline research ranking matrix (strictly non-approval)", ["ranking_report"]),
    "benchmark_finding_domain": ("Benchmark Finding Domain", "Registry of benchmark observations and limitations", ["findings_registry"]),
    "benchmark_manual_review_domain": ("Benchmark Manual Review Domain", "Non-destructive manual review queue for benchmark gaps", ["manual_review_queue"]),
    "benchmark_health_domain": ("Benchmark Health Domain", "Subsystem readiness and component availability verification", ["health_check"]),
    "benchmark_validation_domain": ("Benchmark Validation Domain", "Integrity validation and forbidden claims enforcement", ["validation_report"]),
    "benchmark_safety_domain": ("Benchmark Safety Domain", "Strict safety boundaries, No-Go rules and Safe-Go conditions", ["safety_boundary"]),
    "phase_116_handoff_domain": ("Phase 116 Handoff Domain", "Data readiness delivery for indicator/feature/factor engine", ["phase_116_handoff"]),
    "unknown_benchmark_domain": ("Unknown Benchmark Domain", "Fallback domain for unclassified benchmark records", ["unknown_report"]),
}


def build_default_provider_benchmark_domains(
    profile: ProviderBenchmarkProfile,
) -> List[ProviderBenchmarkDomain]:
    domains: List[ProviderBenchmarkDomain] = []
    for label in BENCHMARK_DOMAIN_LABELS:
        name, desc, req_outputs = DOMAIN_METADATA.get(
            label,
            (label.replace("_", " ").title(), f"Benchmark domain for {label}", ["generic_output"]),
        )
        d_id = build_provider_benchmark_domain_id(label)
        domains.append(
            ProviderBenchmarkDomain(
                domain_id=d_id,
                domain_label=label,
                domain_name=name,
                description=desc,
                required_outputs=req_outputs,
                warnings=[],
            )
        )
    return domains


def build_provider_benchmark_domain_registry(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    domains = build_default_provider_benchmark_domains(profile)
    records_dict = [d.to_dict() for d in domains]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_benchmark_domain_registry(df)
    return df, summary


def summarize_provider_benchmark_domain_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_domains": len(df),
        "domain_labels": df["domain_label"].tolist() if "domain_label" in df.columns else [],
        "current_phase": 115,
        "target_final_phase": 160,
    }
