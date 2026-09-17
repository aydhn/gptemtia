# -*- coding: utf-8 -*-
"""Phase 142: Model Drift Domain Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)
from advanced_model_drift_monitoring.model_drift_labels import (
    MODEL_DRIFT_DOMAIN_LABELS,
)


def build_model_drift_domain_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all model drift domains."""
    prof = profile or get_model_drift_profile()
    rows = []
    for domain in MODEL_DRIFT_DOMAIN_LABELS:
        if domain == "unknown_model_drift_domain":
            continue

        category = "governance"
        if "monitoring_contract" in domain:
            category = "monitoring_contracts"
        elif "linkage" in domain:
            category = "linkage_contracts"
        elif "window" in domain:
            category = "window_policies"
        elif "threshold" in domain or "segment" in domain or "schedule" in domain:
            category = "policies_and_schedules"
        elif "metric" in domain or "psi" in domain or "ks" in domain or "divergence" in domain or "wasserstein" in domain or "missingness" in domain or "categorical" in domain or "numerical" in domain:
            category = "metric_placeholders"
        elif "disabled" in domain:
            category = "disabled_executions"
        elif "guard" in domain or "policy" in domain:
            category = "safety_guards"
        elif "dependency" in domain:
            category = "dependencies"
        elif "placeholder" in domain:
            category = "placeholders"

        rows.append(
            {
                "domain_name": domain,
                "domain_category": category,
                "current_phase": prof.current_phase,
                "target_final_phase": prof.target_final_phase,
                "next_phase": prof.next_phase,
                "zero_execution_enforced": True,
                "non_signal": True,
                "dry_run_only": True,
                "status": "REGISTERED",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_model_drift_domains(df)
    return df, summary


def summarize_model_drift_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize domain registry DataFrame."""
    total_domains = len(df)
    categories = df["domain_category"].unique().tolist() if not df.empty else []
    return {
        "total_domains": total_domains,
        "categories": categories,
        "all_zero_execution": bool(df["zero_execution_enforced"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_dry_run_only": bool(df["dry_run_only"].all()) if not df.empty else True,
    }


def validate_domain_label(domain_name: str) -> bool:
    """Validate if a domain name exists in the registered domains."""
    return any(d[0] == domain_name for d in MODEL_DRIFT_MONITORING_DOMAINS)

