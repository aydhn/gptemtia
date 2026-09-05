from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_models import (
    BenchmarkWeight,
    build_benchmark_weight_id,
)

# Domain weight specifications: (metric_label, provider_domain, weight, rationale, manual_review_required)
WEIGHT_SPECS = [
    # FX weights
    ("metric_coverage", "provider_domain_fx", 0.15, "Major/minor/exotic pair universe coverage is essential", False),
    ("metric_capability", "provider_domain_fx", 0.15, "OHLCV and quote streaming capability", False),
    ("metric_quality", "provider_domain_fx", 0.20, "Bid/ask sanity and anomaly filtering from Phase 112", False),
    ("metric_normalization", "provider_domain_fx", 0.15, "Canonical pair representation and uppercase enforcement", False),
    ("metric_traceability", "provider_domain_fx", 0.10, "Source to canonical transformation provenance", False),
    ("metric_license_provenance", "provider_domain_fx", 0.05, "Open research license boundary", False),
    ("metric_no_scraping_compliance", "provider_domain_fx", 0.15, "Strict zero-scraping compliance", False),
    ("metric_metadata_only_compliance", "provider_domain_fx", 0.00, "Not applicable for numerical FX data", False),
    ("metric_manual_review_load", "provider_domain_fx", 0.05, "Penalty weight for review backlogs", True),

    # Commodity weights
    ("metric_coverage", "provider_domain_commodity", 0.15, "Spot and futures contract universe coverage", False),
    ("metric_capability", "provider_domain_commodity", 0.15, "Contract roll and delivery metadata readiness", False),
    ("metric_quality", "provider_domain_commodity", 0.15, "Price boundary sanity and outlier checking", False),
    ("metric_normalization", "provider_domain_commodity", 0.15, "Unit normalization (USD/bbl, USD/oz)", False),
    ("metric_traceability", "provider_domain_commodity", 0.10, "Physical/futures dataset provenance", False),
    ("metric_license_provenance", "provider_domain_commodity", 0.05, "Exchange license terms review", True),
    ("metric_no_scraping_compliance", "provider_domain_commodity", 0.15, "Strict zero-scraping compliance", False),
    ("metric_metadata_only_compliance", "provider_domain_commodity", 0.00, "Not applicable for numerical commodity data", False),
    ("metric_manual_review_load", "provider_domain_commodity", 0.10, "Contract specifications manual review load", True),

    # Macro weights
    ("metric_coverage", "provider_domain_macro", 0.15, "Indicator universe breadth (CPI, GDP, Rates, Employment)", False),
    ("metric_capability", "provider_domain_macro", 0.15, "Frequency (monthly, quarterly) and release date capability", False),
    ("metric_quality", "provider_domain_macro", 0.15, "Historical revision integrity from Phase 112", False),
    ("metric_normalization", "provider_domain_macro", 0.20, "Canonical indicator nomenclature and unit standardization", False),
    ("metric_traceability", "provider_domain_macro", 0.10, "Statistical agency source provenance", False),
    ("metric_license_provenance", "provider_domain_macro", 0.05, "Public domain / government statistical terms", False),
    ("metric_no_scraping_compliance", "provider_domain_macro", 0.15, "Strict zero-scraping compliance", False),
    ("metric_metadata_only_compliance", "provider_domain_macro", 0.00, "Not applicable for macro data", False),
    ("metric_manual_review_load", "provider_domain_macro", 0.05, "Indicator redefinition review penalty", True),

    # Calendar weights
    ("metric_coverage", "provider_domain_calendar", 0.15, "Global economic event universe coverage", False),
    ("metric_capability", "provider_domain_calendar", 0.15, "Scheduled vs actual release timestamp tracking", False),
    ("metric_quality", "provider_domain_calendar", 0.15, "Consensus vs actual surprise precision", False),
    ("metric_normalization", "provider_domain_calendar", 0.15, "Event taxonomy and country code normalization", False),
    ("metric_traceability", "provider_domain_calendar", 0.10, "Event schedule lineage and update history", False),
    ("metric_license_provenance", "provider_domain_calendar", 0.05, "Commercial calendar redistribution restrictions", True),
    ("metric_no_scraping_compliance", "provider_domain_calendar", 0.15, "Strict zero-scraping compliance", False),
    ("metric_metadata_only_compliance", "provider_domain_calendar", 0.00, "Not applicable for economic events", False),
    ("metric_manual_review_load", "provider_domain_calendar", 0.10, "Unscheduled revision manual review penalty", True),

    # News metadata weights
    ("metric_coverage", "provider_domain_news_metadata", 0.10, "Headline and topic coverage across assets", False),
    ("metric_capability", "provider_domain_news_metadata", 0.10, "Event linking and tag extraction capability", False),
    ("metric_quality", "provider_domain_news_metadata", 0.10, "Spam/duplicate headline filtering from Phase 112", False),
    ("metric_normalization", "provider_domain_news_metadata", 0.10, "Topic tag taxonomy and uppercase asset code normalization", False),
    ("metric_traceability", "provider_domain_news_metadata", 0.10, "Source headline and publication time provenance", False),
    ("metric_license_provenance", "provider_domain_news_metadata", 0.10, "Strict copyright and distribution boundary", True),
    ("metric_no_scraping_compliance", "provider_domain_news_metadata", 0.15, "Mandatory zero-scraping compliance", False),
    ("metric_metadata_only_compliance", "provider_domain_news_metadata", 0.20, "Mandatory zero full-text article boundary", False),
    ("metric_manual_review_load", "provider_domain_news_metadata", 0.05, "Copyright flag manual review penalty", True),

    # Cross-domain weights
    ("metric_coverage", "provider_domain_cross_domain", 0.15, "Cross-asset multi-provider coverage breadth", False),
    ("metric_capability", "provider_domain_cross_domain", 0.15, "Multi-source synchronization capability", False),
    ("metric_quality", "provider_domain_cross_domain", 0.15, "Cross-dataset coherence and alignment", False),
    ("metric_normalization", "provider_domain_cross_domain", 0.15, "Universal canonical format alignment", False),
    ("metric_traceability", "provider_domain_cross_domain", 0.15, "End-to-end lineage across all assets", False),
    ("metric_license_provenance", "provider_domain_cross_domain", 0.05, "Cross-vendor licensing boundary coherence", True),
    ("metric_no_scraping_compliance", "provider_domain_cross_domain", 0.10, "Cross-system zero-scraping enforcement", False),
    ("metric_metadata_only_compliance", "provider_domain_cross_domain", 0.05, "Universal metadata-only policy adherence", False),
    ("metric_manual_review_load", "provider_domain_cross_domain", 0.05, "Cross-asset review queue load penalty", True),
]


def build_default_benchmark_weights(
    profile: ProviderBenchmarkProfile,
) -> List[BenchmarkWeight]:
    weights: List[BenchmarkWeight] = []
    for metric_label, domain, w, rationale, rev_req in WEIGHT_SPECS:
        w_id = build_benchmark_weight_id(metric_label, domain)
        weights.append(
            BenchmarkWeight(
                weight_id=w_id,
                metric_label=metric_label,
                provider_domain=domain,
                weight=w,
                rationale=rationale,
                manual_review_required=rev_req,
            )
        )
    return weights


def build_provider_benchmark_weight_registry(
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    weights = build_default_benchmark_weights(profile)
    records_dict = [w.to_dict() for w in weights]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_benchmark_weight_registry(df)
    return df, summary


def summarize_provider_benchmark_weight_registry(df: pd.DataFrame) -> Dict[str, Any]:
    domains = df["provider_domain"].unique().tolist() if "provider_domain" in df.columns else []
    sum_by_domain = {}
    if not df.empty and "provider_domain" in df.columns and "weight" in df.columns:
        for d in domains:
            sum_by_domain[d] = round(float(df[df["provider_domain"] == d]["weight"].sum()), 4)
    return {
        "total_weights": len(df),
        "domains": domains,
        "sum_by_domain": sum_by_domain,
        "current_phase": 115,
        "target_final_phase": 160,
    }
