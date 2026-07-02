import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile
from .archive_models import RetentionPolicyItem, build_retention_policy_id, retention_policy_item_to_dict

def classify_retention_label_for_domain(domain_label: str) -> str:
    if domain_label in ["documentation_archive", "report_archive", "datalake_archive", "cross_layer_archive"]:
        return "retain_long_term_manual"
    elif domain_label in ["security_archive", "backup_packaging_archive", "operator_archive"]:
        return "retain_medium_term_manual"
    elif domain_label in ["test_archive"]:
        return "retain_short_term_manual"
    elif domain_label in ["unknown_archive"]:
        return "exclude_from_archive"
    return "retain_until_next_review_manual"

def build_retention_policy_for_domain(domain_row: pd.Series, profile: LocalArchiveProfile) -> RetentionPolicyItem:
    label = domain_row.get("domain_label", "unknown")
    retention = classify_retention_label_for_domain(label)
    return RetentionPolicyItem(
        policy_id=build_retention_policy_id(label, retention),
        domain_label=label,
        retention_label=retention,
        review_interval_days=profile.retention_review_days,
        rationale=f"Default rule for {label}",
        manual_review_required=True,
        warnings=["Not an official legal retention policy"]
    )

def build_retention_policy_registry(domain_df: pd.DataFrame, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    policies = []
    if not domain_df.empty:
        for _, row in domain_df.iterrows():
            policies.append(build_retention_policy_for_domain(row, profile))
    df = pd.DataFrame([retention_policy_item_to_dict(p) for p in policies])
    return df, summarize_retention_policy(df)

def summarize_retention_policy(policy_df: pd.DataFrame) -> Dict:
    if policy_df.empty: return {"total_policies": 0}
    long_term = int((policy_df['retention_label'] == 'retain_long_term_manual').sum()) if 'retention_label' in policy_df.columns else 0
    return {
        "total_policies": len(policy_df),
        "long_term_policies": long_term,
        "notice": "Retention policies are guidelines for manual review, not automated deletion rules."
    }
