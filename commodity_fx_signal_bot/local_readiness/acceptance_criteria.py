import pandas as pd
from pathlib import Path
from .readiness_config import LocalReadinessProfile
from .readiness_models import AcceptanceCriterion, build_acceptance_criterion_id

def build_milestone_acceptance_criteria(profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    criteria = [
        AcceptanceCriterion(criterion_id=build_acceptance_criterion_id("readme_present", "docs"), criterion_name="README mevcut ve güncel", domain="docs", description="README.md exists.", evidence_path="README.md", status="unknown", manual_review_required=False, warnings=[]),
        AcceptanceCriterion(criterion_id=build_acceptance_criterion_id("phase_log_69", "docs"), criterion_name="PHASE_LOG Phase 69 kaydı içeriyor", domain="docs", description="PHASE_LOG updated with phase 69.", evidence_path="docs/PHASE_LOG.md", status="unknown", manual_review_required=True, warnings=[]),
        AcceptanceCriterion(criterion_id=build_acceptance_criterion_id("safe_usage_guide", "docs"), criterion_name="SAFE_USAGE_GUIDE mevcut", domain="docs", description="SAFE_USAGE_GUIDE.md exists.", evidence_path="docs/SAFE_USAGE_GUIDE.md", status="unknown", manual_review_required=False, warnings=[]),
        AcceptanceCriterion(criterion_id=build_acceptance_criterion_id("operator_manual", "docs"), criterion_name="OPERATOR_MANUAL mevcut", domain="docs", description="OPERATOR_MANUAL.md exists.", evidence_path="docs/OPERATOR_MANUAL.md", status="unknown", manual_review_required=False, warnings=[]),
        AcceptanceCriterion(criterion_id=build_acceptance_criterion_id("local_readiness_scripts", "scripts"), criterion_name="local_readiness scriptleri mevcut", domain="scripts", description="Local readiness scripts exist.", evidence_path="scripts/run_readiness_gate_registry.py", status="unknown", manual_review_required=False, warnings=[]),
        AcceptanceCriterion(criterion_id=build_acceptance_criterion_id("tests_contract", "tests"), criterion_name="tests contract mevcut", domain="tests", description="Test contract exists.", evidence_path="tests/test_local_readiness_scripts_contract.py", status="unknown", manual_review_required=False, warnings=[]),
        AcceptanceCriterion(criterion_id=build_acceptance_criterion_id("datalake_registry", "datalake"), criterion_name="DataLake save/load registry mevcut", domain="datalake", description="DataLake supports local readiness.", evidence_path="data/storage/data_lake.py", status="unknown", manual_review_required=False, warnings=[]),
        AcceptanceCriterion(criterion_id=build_acceptance_criterion_id("reports_local_readiness", "reports"), criterion_name="reports/output local_readiness dizini mevcut", domain="reports", description="Reports dir exists.", evidence_path="reports/output/local_readiness", status="unknown", manual_review_required=False, warnings=[]),
        AcceptanceCriterion(criterion_id=build_acceptance_criterion_id("non_use_policy", "security"), criterion_name="non-use policy coverage mevcut", domain="security", description="Non-use policy check.", evidence_path=None, status="unknown", manual_review_required=True, warnings=[]),
        AcceptanceCriterion(criterion_id=build_acceptance_criterion_id("no_go_registry", "handoff"), criterion_name="no-go condition registry mevcut", domain="handoff", description="No-go registry generated.", evidence_path="reports/output/local_readiness/csv/no_go_condition_registry.csv", status="unknown", manual_review_required=False, warnings=[]),
        AcceptanceCriterion(criterion_id=build_acceptance_criterion_id("handoff_manifest", "handoff"), criterion_name="handoff manifest mevcut", domain="handoff", description="Handoff manifest generated.", evidence_path="reports/output/local_readiness/json/handoff_package_manifest.json", status="unknown", manual_review_required=False, warnings=[]),
        AcceptanceCriterion(criterion_id=build_acceptance_criterion_id("final_binder", "handoff"), criterion_name="final local readiness binder mevcut", domain="handoff", description="Final binder generated.", evidence_path="reports/output/local_readiness/markdown/final_local_readiness_binder.md", status="unknown", manual_review_required=False, warnings=[])
    ]

    from .readiness_models import acceptance_criterion_to_dict
    df = pd.DataFrame([acceptance_criterion_to_dict(c) for c in criteria])
    summary = summarize_acceptance_criteria(df)
    return df, summary


def map_acceptance_criteria_to_evidence(criteria_df: pd.DataFrame, project_root: Path) -> tuple[pd.DataFrame, dict]:
    results = []
    for idx, row in criteria_df.iterrows():
        path = row["evidence_path"]
        if pd.notna(path) and str(path) != "None":
            p = project_root / str(path)
            if p.exists():
                row["status"] = "met"
            else:
                row["status"] = "not_met"
                row["warnings"].append(f"Evidence missing: {path}")
                row["manual_review_required"] = True
        else:
            row["status"] = "requires_review"
            row["manual_review_required"] = True
        results.append(row)
    df = pd.DataFrame(results)
    return df, summarize_acceptance_criteria(df)
def evaluate_acceptance_criteria(criteria_df: pd.DataFrame, evidence_df: pd.DataFrame, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    return criteria_df, summarize_acceptance_criteria(criteria_df)

def summarize_acceptance_criteria(criteria_df: pd.DataFrame) -> dict:
    total = len(criteria_df)
    met = len(criteria_df[criteria_df["status"] == "met"])
    not_met = len(criteria_df[criteria_df["status"] == "not_met"])
    return {
        "total_criteria": total,
        "met_criteria": met,
        "not_met_criteria": not_met
    }
