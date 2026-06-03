"""
Backup policies configuration.
"""

import pandas as pd
from .backup_models import BackupPolicy, build_backup_policy_id, backup_policy_to_dict
from .backup_config import BackupRecoveryProfile


def build_default_backup_policies(profile: BackupRecoveryProfile) -> list[BackupPolicy]:
    return [
        BackupPolicy(
            policy_id=build_backup_policy_id("critical_source_scope"),
            scope_label="critical_source_scope",
            description="Core source code",
            include=profile.include_source,
            manifest_only=False,
            hash_required=True,
            restore_required=True,
            protected=True,
            warnings=[]
        ),
        BackupPolicy(
            policy_id=build_backup_policy_id("config_template_scope"),
            scope_label="config_template_scope",
            description="Configuration templates",
            include=profile.include_configs,
            manifest_only=False,
            hash_required=True,
            restore_required=True,
            protected=True,
            warnings=[]
        ),
        BackupPolicy(
            policy_id=build_backup_policy_id("docs_scope"),
            scope_label="docs_scope",
            description="Documentation",
            include=profile.include_docs,
            manifest_only=False,
            hash_required=True,
            restore_required=True,
            protected=False,
            warnings=[]
        ),
        BackupPolicy(
            policy_id=build_backup_policy_id("tests_scope"),
            scope_label="tests_scope",
            description="Test files",
            include=profile.include_tests,
            manifest_only=False,
            hash_required=True,
            restore_required=True,
            protected=False,
            warnings=[]
        ),
        BackupPolicy(
            policy_id=build_backup_policy_id("reports_manifest_only_scope"),
            scope_label="reports_manifest_only_scope",
            description="Reports output",
            include=profile.include_reports_manifest_only,
            manifest_only=True,
            hash_required=False,
            restore_required=False,
            protected=False,
            warnings=[]
        ),
        BackupPolicy(
            policy_id=build_backup_policy_id("data_manifest_only_scope"),
            scope_label="data_manifest_only_scope",
            description="Data Lake output",
            include=profile.include_data_manifest_only,
            manifest_only=True,
            hash_required=False,
            restore_required=False,
            protected=False,
            warnings=[]
        ),
        BackupPolicy(
            policy_id=build_backup_policy_id("excluded_secret_scope"),
            scope_label="excluded_secret_scope",
            description="Secrets and credentials",
            include=False,
            manifest_only=False,
            hash_required=False,
            restore_required=False,
            protected=True,
            warnings=["Never include secrets"]
        )
    ]

def backup_policies_to_dataframe(policies: list[BackupPolicy]) -> pd.DataFrame:
    return pd.DataFrame([backup_policy_to_dict(p) for p in policies])


def get_backup_policy_for_scope(scope_label: str, policies_df: pd.DataFrame) -> dict | None:
    if policies_df is None or policies_df.empty:
        return None
    matches = policies_df[policies_df["scope_label"] == scope_label]
    if not matches.empty:
        return matches.iloc[0].to_dict()
    return None


def apply_backup_policies_to_inventory(inventory_df: pd.DataFrame, policies_df: pd.DataFrame, profile: BackupRecoveryProfile) -> pd.DataFrame:
    df = inventory_df.copy()
    if policies_df is None or policies_df.empty:
        return df

    df["applied_policy"] = df["backup_scope"].apply(
        lambda scope: get_backup_policy_for_scope(scope, policies_df)["policy_id"] if get_backup_policy_for_scope(scope, policies_df) else "default"
    )
    return df


def summarize_backup_policies(policies_df: pd.DataFrame) -> dict:
    if policies_df is None or policies_df.empty:
        return {"status": "empty"}
    return {
        "total_policies": len(policies_df),
        "included_scopes": len(policies_df[policies_df["include"] == True]),
        "manifest_only_scopes": len(policies_df[policies_df["manifest_only"] == True])
    }
