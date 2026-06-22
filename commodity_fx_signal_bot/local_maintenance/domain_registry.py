import pandas as pd
from typing import Tuple, List, Dict, Any

from local_maintenance.maintenance_config import LocalMaintenanceProfile
from local_maintenance.maintenance_models import MaintenanceDomain, build_maintenance_domain_id, maintenance_domain_to_dict

def build_default_maintenance_domains(profile: LocalMaintenanceProfile) -> List[MaintenanceDomain]:
    domains = [
        MaintenanceDomain(
            domain_id=build_maintenance_domain_id("Documentation Maintenance"),
            domain_name="Documentation Maintenance",
            domain_label="documentation_maintenance",
            description="Maintenance of documentation artifacts, manuals, and architecture guides.",
            owner_role="operator",
            default_cadence="refresh_monthly_manual",
            required_artifacts=["docs/ARCHITECTURE.md", "docs/OPERATOR_MANUAL.md"],
            warnings=[]
        ),
        MaintenanceDomain(
            domain_id=build_maintenance_domain_id("Tests Maintenance"),
            domain_name="Tests Maintenance",
            domain_label="tests_maintenance",
            description="Maintenance of tests and testing guidelines.",
            owner_role="maintainer",
            default_cadence="refresh_before_handoff_manual",
            required_artifacts=["tests/"],
            warnings=[]
        ),
        MaintenanceDomain(
            domain_id=build_maintenance_domain_id("Scripts Maintenance"),
            domain_name="Scripts Maintenance",
            domain_label="scripts_maintenance",
            description="Maintenance of command scripts.",
            owner_role="operator",
            default_cadence="refresh_before_handoff_manual",
            required_artifacts=["scripts/"],
            warnings=[]
        ),
        MaintenanceDomain(
            domain_id=build_maintenance_domain_id("Reports Maintenance"),
            domain_name="Reports Maintenance",
            domain_label="reports_maintenance",
            description="Maintenance of report templates and formats.",
            owner_role="analyst",
            default_cadence="refresh_monthly_manual",
            required_artifacts=["reports/"],
            warnings=[]
        ),
        MaintenanceDomain(
            domain_id=build_maintenance_domain_id("DataLake Maintenance"),
            domain_name="DataLake Maintenance",
            domain_label="datalake_maintenance",
            description="Maintenance of data lake structure and schema.",
            owner_role="operator",
            default_cadence="refresh_on_change_manual",
            required_artifacts=["data/lake/"],
            warnings=[]
        ),
        MaintenanceDomain(
            domain_id=build_maintenance_domain_id("Security Maintenance"),
            domain_name="Security Maintenance",
            domain_label="security_maintenance",
            description="Maintenance of security and secret hygiene.",
            owner_role="maintainer",
            default_cadence="refresh_monthly_manual",
            required_artifacts=["data/lake/secrets_hygiene/"],
            warnings=[]
        ),
        MaintenanceDomain(
            domain_id=build_maintenance_domain_id("Backup & Packaging Maintenance"),
            domain_name="Backup & Packaging Maintenance",
            domain_label="backup_packaging_maintenance",
            description="Maintenance of backup and packaging procedures.",
            owner_role="operator",
            default_cadence="refresh_before_handoff_manual",
            required_artifacts=["portable_bundle/"],
            warnings=[]
        ),
        MaintenanceDomain(
            domain_id=build_maintenance_domain_id("Evidence/Metadata/Graph/Timeline Maintenance"),
            domain_name="Evidence/Metadata/Graph/Timeline Maintenance",
            domain_label="evidence_metadata_graph_timeline_maintenance",
            description="Maintenance of tracking and knowledge graph items.",
            owner_role="analyst",
            default_cadence="refresh_monthly_manual",
            required_artifacts=["data/lake/evidence_governance/"],
            warnings=[]
        ),
        MaintenanceDomain(
            domain_id=build_maintenance_domain_id("Consistency & Readiness Maintenance"),
            domain_name="Consistency & Readiness Maintenance",
            domain_label="consistency_readiness_maintenance",
            description="Maintenance of cross-layer consistency and project readiness.",
            owner_role="operator",
            default_cadence="refresh_monthly_manual",
            required_artifacts=["data/lake/local_readiness/"],
            warnings=[]
        ),
        MaintenanceDomain(
            domain_id=build_maintenance_domain_id("Dependency Maintenance"),
            domain_name="Dependency Maintenance",
            domain_label="dependency_maintenance",
            description="Maintenance of software dependencies.",
            owner_role="maintainer",
            default_cadence="refresh_quarterly_manual",
            required_artifacts=["requirements.txt", "pyproject.toml"],
            warnings=[]
        ),
        MaintenanceDomain(
            domain_id=build_maintenance_domain_id("Operator Maintenance"),
            domain_name="Operator Maintenance",
            domain_label="operator_maintenance",
            description="General operator routines.",
            owner_role="operator",
            default_cadence="refresh_monthly_manual",
            required_artifacts=[],
            warnings=[]
        )
    ]
    return domains

def build_maintenance_domain_registry(profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    domains = build_default_maintenance_domains(profile)
    df = pd.DataFrame([maintenance_domain_to_dict(d) for d in domains])
    summary = summarize_maintenance_domains(df)
    return df, summary

def summarize_maintenance_domains(domain_df: pd.DataFrame) -> Dict[str, Any]:
    if domain_df is None or domain_df.empty:
        return {"total_domains": 0}

    summary = {
        "total_domains": len(domain_df),
        "domains_by_role": domain_df["owner_role"].value_counts().to_dict(),
        "domains_by_cadence": domain_df["default_cadence"].value_counts().to_dict(),
        "disclaimer": "This domain registry is not a maintenance contract."
    }
    return summary
