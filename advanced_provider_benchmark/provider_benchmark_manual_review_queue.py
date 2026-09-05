from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkManualReviewItem,
    build_provider_benchmark_review_id,
)
from advanced_provider_benchmark.provider_benchmark_findings import (
    build_provider_benchmark_findings_registry,
)


def build_provider_benchmark_manual_review_queue(
    findings_df: pd.DataFrame | None,
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if findings_df is None or findings_df.empty:
        findings_df, _ = build_provider_benchmark_findings_registry(profile)

    review_items: List[ProviderBenchmarkManualReviewItem] = []
    for _, row in findings_df.iterrows():
        if row.get("manual_review_required", False):
            f_id = row.get("finding_id", "find_unknown")
            p_name = row.get("provider_name", "prov_unknown")
            p_domain = row.get("provider_domain", "domain_unknown")
            reason = row.get("message", "Manual review required")
            rec = row.get("recommendation", "Conduct non-destructive documentation review")

            r_id = build_provider_benchmark_review_id(f_id)
            review_items.append(
                ProviderBenchmarkManualReviewItem(
                    review_id=r_id,
                    finding_id=f_id,
                    provider_name=p_name,
                    provider_domain=p_domain,
                    review_reason=reason,
                    suggested_action=rec,
                    destructive_action_allowed=False,
                    status_label="benchmark_manual_review_required",
                )
            )

    records_dict = [r.to_dict() for r in review_items]
    df = pd.DataFrame.from_records(records_dict)
    summary = summarize_provider_benchmark_manual_review_queue(df)
    return df, summary


def summarize_provider_benchmark_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_manual_review_items": len(df),
        "all_non_destructive": True,
        "destructive_actions_prevented": True,
        "review_providers": df["provider_name"].unique().tolist() if not df.empty and "provider_name" in df.columns else [],
        "current_phase": 115,
        "target_final_phase": 160,
    }
