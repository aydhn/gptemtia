"""Retention Policies for offline maintenance."""
import pandas as pd
from typing import List, Optional, Dict

from maintenance.maintenance_config import MaintenanceProfile
from maintenance.maintenance_models import RetentionPolicy, build_retention_policy_id

def build_default_retention_policies(profile: MaintenanceProfile) -> List[RetentionPolicy]:
    policies = [
        RetentionPolicy(
            policy_id=build_retention_policy_id("raw_data_retention"),
            retention_category="raw_data_retention",
            description="Raw data files downloaded from external sources.",
            keep_days=None,
            keep_latest_n=None,
            protected=True,
            archive_before_cleanup=False,
            dry_run_only=True,
            warnings=[]
        ),
        RetentionPolicy(
            policy_id=build_retention_policy_id("processed_data_retention"),
            retention_category="processed_data_retention",
            description="Processed features and ML ready data.",
            keep_days=365,
            keep_latest_n=None,
            protected=False,
            archive_before_cleanup=True,
            dry_run_only=True,
            warnings=[]
        ),
        RetentionPolicy(
            policy_id=build_retention_policy_id("report_retention"),
            retention_category="report_retention",
            description="Generated research and signal reports.",
            keep_days=90,
            keep_latest_n=profile.keep_latest_n_reports,
            protected=False,
            archive_before_cleanup=False,
            dry_run_only=True,
            warnings=[]
        ),
        RetentionPolicy(
            policy_id=build_retention_policy_id("quality_report_retention"),
            retention_category="quality_report_retention",
            description="Quality gate reports.",
            keep_days=profile.keep_quality_reports_days,
            keep_latest_n=20,
            protected=False,
            archive_before_cleanup=False,
            dry_run_only=True,
            warnings=[]
        ),
        RetentionPolicy(
            policy_id=build_retention_policy_id("governance_retention"),
            retention_category="governance_retention",
            description="Governance artifacts and lineages.",
            keep_days=profile.keep_governance_reports_days,
            keep_latest_n=20,
            protected=False,
            archive_before_cleanup=False,
            dry_run_only=True,
            warnings=[]
        ),
        RetentionPolicy(
            policy_id=build_retention_policy_id("experiment_retention"),
            retention_category="experiment_retention",
            description="Experiment tracking data and manifests.",
            keep_days=profile.keep_experiment_manifests_days,
            keep_latest_n=50,
            protected=False,
            archive_before_cleanup=False,
            dry_run_only=True,
            warnings=[]
        ),
        RetentionPolicy(
            policy_id=build_retention_policy_id("knowledge_base_retention"),
            retention_category="knowledge_base_retention",
            description="Vector index caches and text chunks.",
            keep_days=profile.keep_knowledge_index_days,
            keep_latest_n=5,
            protected=False,
            archive_before_cleanup=False,
            dry_run_only=True,
            warnings=[]
        ),
        RetentionPolicy(
            policy_id=build_retention_policy_id("cache_retention"),
            retention_category="cache_retention",
            description="Short term pandas and calculation caches.",
            keep_days=profile.keep_cache_days,
            keep_latest_n=None,
            protected=False,
            archive_before_cleanup=False,
            dry_run_only=True,
            warnings=[]
        ),
        RetentionPolicy(
            policy_id=build_retention_policy_id("checkpoint_retention"),
            retention_category="checkpoint_retention",
            description="State recovery checkpoints.",
            keep_days=profile.keep_checkpoints_days,
            keep_latest_n=None,
            protected=False,
            archive_before_cleanup=False,
            dry_run_only=True,
            warnings=[]
        ),
        RetentionPolicy(
            policy_id=build_retention_policy_id("log_retention"),
            retention_category="log_retention",
            description="System execution logs.",
            keep_days=30,
            keep_latest_n=profile.keep_latest_n_runs,
            protected=False,
            archive_before_cleanup=False,
            dry_run_only=True,
            warnings=[]
        )
    ]
    return policies

def retention_policies_to_dataframe(policies: List[RetentionPolicy]) -> pd.DataFrame:
    return pd.DataFrame([p.__dict__ for p in policies])

def get_policy_for_category(retention_category: str, policies: List[RetentionPolicy]) -> Optional[RetentionPolicy]:
    for p in policies:
        if p.retention_category == retention_category:
            return p
    return None

def apply_retention_policy_to_inventory(inventory_df: pd.DataFrame, policies_df: pd.DataFrame, profile: MaintenanceProfile) -> pd.DataFrame:
    if inventory_df.empty:
        return inventory_df

    df = inventory_df.copy()

    def determine_lifecycle(row):
        if row.get("protected"):
            return "protected_artifact"

        policy_row = policies_df[policies_df["retention_category"] == row.get("retention_category")]
        if policy_row.empty:
            return "unknown_lifecycle"

        policy = policy_row.iloc[0]

        if policy.get("protected"):
            return "protected_artifact"

        age_days = row.get("age_days")
        keep_days = policy.get("keep_days")

        if pd.isna(age_days) or pd.isna(keep_days):
            return "active_artifact"

        if age_days > keep_days:
            if policy.get("archive_before_cleanup"):
                return "archive_candidate"
            return "cleanup_candidate"

        return "active_artifact"

    df["lifecycle_label"] = df.apply(determine_lifecycle, axis=1)
    return df

def summarize_retention_policies(policies_df: pd.DataFrame) -> Dict:
    return {
        "total_policies": len(policies_df),
        "protected_policies": int(policies_df["protected"].sum()) if not policies_df.empty else 0
    }
