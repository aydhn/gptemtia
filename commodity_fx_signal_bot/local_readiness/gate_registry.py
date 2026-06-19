import pandas as pd
from pathlib import Path
from .readiness_config import LocalReadinessProfile
from .readiness_models import ReadinessGate, build_readiness_gate_id

def build_default_readiness_gates(profile: LocalReadinessProfile) -> list[ReadinessGate]:
    gates = [
        ReadinessGate(gate_id=build_readiness_gate_id("docs_gate", "docs"), gate_name="docs_gate", domain="docs", description="Documentation completeness.", required_artifacts=["README.md"], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("tests_gate", "tests"), gate_name="tests_gate", domain="tests", description="Test suite completeness.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("scripts_gate", "scripts"), gate_name="scripts_gate", domain="scripts", description="Scripts availability.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("reports_output_gate", "reports"), gate_name="reports_output_gate", domain="reports", description="Report outputs format.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("datalake_gate", "datalake"), gate_name="datalake_gate", domain="datalake", description="DataLake directories and methods.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("security_boundary_gate", "security"), gate_name="security_boundary_gate", domain="security", description="Security boundary check.", required_artifacts=[], status="gate_unknown", no_go_if_failed=True, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("secrets_hygiene_gate", "security"), gate_name="secrets_hygiene_gate", domain="security", description="Secrets hygiene check.", required_artifacts=[], status="gate_unknown", no_go_if_failed=True, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("backup_recovery_gate", "backup"), gate_name="backup_recovery_gate", domain="backup", description="Backup dry-run readiness.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("portable_packaging_gate", "packaging"), gate_name="portable_packaging_gate", domain="packaging", description="Packaging readiness.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("evidence_governance_gate", "governance"), gate_name="evidence_governance_gate", domain="governance", description="Evidence governance.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("artifact_metadata_gate", "metadata"), gate_name="artifact_metadata_gate", domain="metadata", description="Artifact metadata check.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("local_knowledge_graph_gate", "graph"), gate_name="local_knowledge_graph_gate", domain="graph", description="Knowledge graph readiness.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("local_timeline_gate", "timeline"), gate_name="local_timeline_gate", domain="timeline", description="Timeline readiness.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("local_consistency_gate", "consistency"), gate_name="local_consistency_gate", domain="consistency", description="Consistency check.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("final_review_gate", "review"), gate_name="final_review_gate", domain="review", description="Final review gate.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("scenario_regression_gate", "testing"), gate_name="scenario_regression_gate", domain="testing", description="Scenario regression check.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("master_orchestration_gate", "orchestration"), gate_name="master_orchestration_gate", domain="orchestration", description="Master orchestration check.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("operator_manual_gate", "docs"), gate_name="operator_manual_gate", domain="docs", description="Operator manual presence.", required_artifacts=["docs/OPERATOR_MANUAL.md"], status="gate_unknown", no_go_if_failed=False, warnings=[]),
        ReadinessGate(gate_id=build_readiness_gate_id("handoff_manifest_gate", "handoff"), gate_name="handoff_manifest_gate", domain="handoff", description="Handoff manifest readiness.", required_artifacts=[], status="gate_unknown", no_go_if_failed=False, warnings=[])
    ]
    return gates

def readiness_gates_to_dataframe(gates: list[ReadinessGate]) -> pd.DataFrame:
    from .readiness_models import readiness_gate_to_dict
    return pd.DataFrame([readiness_gate_to_dict(g) for g in gates])

def evaluate_readiness_gate_artifacts(gate_df: pd.DataFrame, project_root: Path, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    results = []
    for idx, row in gate_df.iterrows():
        required = row["required_artifacts"]
        missing = []
        for artifact in required:
            p = project_root / artifact
            if not p.exists():
                missing.append(artifact)

        status = row["status"]
        if missing:
            status = "gate_failed"
        else:
            status = "gate_passed"

        warnings = row["warnings"]
        if missing:
            warnings.append(f"Missing required artifacts: {missing}")

        row["status"] = status
        row["warnings"] = warnings
        results.append(row)

    df = pd.DataFrame(results)
    summary = summarize_readiness_gates(df)
    return df, summary

def build_readiness_gate_registry(project_root: Path, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    gates = build_default_readiness_gates(profile)
    gate_df = readiness_gates_to_dataframe(gates)
    return evaluate_readiness_gate_artifacts(gate_df, project_root, profile)

def summarize_readiness_gates(gate_df: pd.DataFrame) -> dict:
    total = len(gate_df)
    passed = len(gate_df[gate_df["status"].str.startswith("gate_passed")])
    failed = len(gate_df[gate_df["status"] == "gate_failed"])
    return {
        "total_gates": total,
        "passed_gates": passed,
        "failed_gates": failed
    }
