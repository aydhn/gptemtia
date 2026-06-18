import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile
from local_consistency.consistency_models import ConsistencyCheck, build_consistency_check_id


def build_default_consistency_checks(profile: LocalConsistencyProfile) -> list[ConsistencyCheck]:
    checks = [
        ConsistencyCheck(
            check_id=build_consistency_check_id("config_env_check", "config/settings.py", ".env.example"),
            check_type="config_env_check",
            check_name="Config Env Consistency",
            source_layer="config",
            target_layer="env",
            description="Ensure settings match .env.example",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("settings_docs_check", "config/settings.py", "docs"),
            check_type="settings_docs_check",
            check_name="Settings Docs Consistency",
            source_layer="config",
            target_layer="docs",
            description="Ensure settings are documented",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("paths_datalake_check", "config/paths.py", "data_lake.py"),
            check_type="paths_datalake_check",
            check_name="Paths DataLake Consistency",
            source_layer="config",
            target_layer="storage",
            description="Ensure paths have datalake methods",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("script_report_check", "scripts", "reports"),
            check_type="script_report_check",
            check_name="Script Report Consistency",
            source_layer="scripts",
            target_layer="reports",
            description="Ensure scripts produce expected reports",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("report_datalake_check", "reports", "data_lake.py"),
            check_type="report_datalake_check",
            check_name="Report DataLake Consistency",
            source_layer="reports",
            target_layer="storage",
            description="Ensure reports have datalake counterparts",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("docs_phase_log_check", "docs/PHASE_LOG.md", "scripts"),
            check_type="docs_phase_log_check",
            check_name="Docs Phase Log Consistency",
            source_layer="docs",
            target_layer="scripts",
            description="Ensure scripts are documented in phase log",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("evidence_control_check", "evidence", "control"),
            check_type="evidence_control_check",
            check_name="Evidence Control Consistency",
            source_layer="evidence",
            target_layer="control",
            description="Ensure evidence maps to controls",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("metadata_artifact_check", "metadata", "artifact"),
            check_type="metadata_artifact_check",
            check_name="Metadata Artifact Consistency",
            source_layer="metadata",
            target_layer="artifact",
            description="Ensure metadata exists for artifacts",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("graph_metadata_check", "graph", "metadata"),
            check_type="graph_metadata_check",
            check_name="Graph Metadata Consistency",
            source_layer="graph",
            target_layer="metadata",
            description="Ensure graph matches metadata",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("timeline_artifact_check", "timeline", "artifact"),
            check_type="timeline_artifact_check",
            check_name="Timeline Artifact Consistency",
            source_layer="timeline",
            target_layer="artifact",
            description="Ensure timeline matches artifacts",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("backup_packaging_secrets_check", "backup", "secrets"),
            check_type="backup_packaging_secrets_check",
            check_name="Backup Packaging Secrets Consistency",
            source_layer="backup",
            target_layer="secrets",
            description="Ensure backups and packaging respect secret boundaries",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("non_use_policy_check", "reports", "policy"),
            check_type="non_use_policy_check",
            check_name="Non-Use Policy Consistency",
            source_layer="reports",
            target_layer="policy",
            description="Ensure non-use policies are respected",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("disclaimer_check", "reports", "docs"),
            check_type="disclaimer_check",
            check_name="Disclaimer Consistency",
            source_layer="reports",
            target_layer="docs",
            description="Ensure disclaimers exist",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("safety_boundary_check", "reports", "safety"),
            check_type="safety_boundary_check",
            check_name="Safety Boundary Consistency",
            source_layer="reports",
            target_layer="safety",
            description="Ensure safety boundaries are respected",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("contradiction_check", "reports", "docs"),
            check_type="contradiction_check",
            check_name="Contradiction Check",
            source_layer="reports",
            target_layer="docs",
            description="Detect contradictions in reports and docs",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("reference_check", "reports", "docs"),
            check_type="reference_check",
            check_name="Reference Check",
            source_layer="reports",
            target_layer="docs",
            description="Detect broken or missing references",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        ),
        ConsistencyCheck(
            check_id=build_consistency_check_id("stale_reconciliation_check", "timeline", "metadata"),
            check_type="stale_reconciliation_check",
            check_name="Stale Reconciliation Check",
            source_layer="timeline",
            target_layer="metadata",
            description="Check for stale artifacts",
            expected_artifacts=[],
            status="consistency_unknown",
            warnings=[]
        )
    ]
    return checks

def consistency_checks_to_dataframe(checks: list[ConsistencyCheck]) -> pd.DataFrame:
    from local_consistency.consistency_models import consistency_check_to_dict
    return pd.DataFrame([consistency_check_to_dict(c) for c in checks])

def build_consistency_check_registry(profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    checks = build_default_consistency_checks(profile)
    df = consistency_checks_to_dataframe(checks)
    summary = {
        "total_checks": len(checks),
        "profile": profile.name,
        "warnings": []
    }
    return df, summary

def build_cross_layer_consistency_matrix(check_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    # Placeholder for matrix building logic
    matrix_df = pd.DataFrame()
    summary = {
        "total_layers": 0,
        "warnings": []
    }
    return matrix_df, summary

def summarize_consistency_check_registry(check_df: pd.DataFrame) -> dict:
    return {
        "total_checks": len(check_df) if not check_df.empty else 0
    }
