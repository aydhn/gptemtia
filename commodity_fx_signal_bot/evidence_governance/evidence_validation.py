import pandas as pd
from evidence_governance.evidence_config import EvidenceGovernanceProfile

def validate_evidence_artifacts(artifact_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> dict:
    if artifact_df is None or artifact_df.empty:
        return {"passed": False, "warnings": ["No artifacts to validate"]}

    warnings = []
    if "artifact_id" not in artifact_df.columns:
        warnings.append("Missing artifact_id")
    if "relative_path" not in artifact_df.columns:
        warnings.append("Missing relative_path")

    return {"passed": len(warnings) == 0, "warnings": warnings}

def validate_policy_control_mapping(policy_df: pd.DataFrame, control_df: pd.DataFrame, mapping_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> dict:
    warnings = []
    if policy_df is None or control_df is None or mapping_df is None:
        return {"passed": False, "warnings": ["Missing mapping DataFrames"]}

    if mapping_df.empty:
        warnings.append("Mapping is empty (graceful warning)")

    return {"passed": True, "warnings": warnings}

def validate_traceability_matrix(trace_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> dict:
    warnings = []
    if trace_df is None or trace_df.empty:
        warnings.append("Traceability matrix is empty")
    return {"passed": len(warnings) == 0, "warnings": warnings}

def validate_evidence_packs(pack_tables: dict[str, pd.DataFrame], profile: EvidenceGovernanceProfile) -> dict:
    warnings = []
    for name, df in pack_tables.items():
        if df is None or df.empty:
            warnings.append(f"Pack {name} is empty")
    return {"passed": True, "warnings": warnings}

def validate_no_official_compliance_claims(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    # A generic function to check for forbidden terms across inputs
    from evidence_governance.evidence_quality import check_for_forbidden_terms_in_evidence
    return check_for_forbidden_terms_in_evidence(text, df, summary)

def build_evidence_validation_report(tables: dict[str, pd.DataFrame], profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    res = []

    art_val = validate_evidence_artifacts(tables.get("artifact_inventory"), profile)
    res.append({"component": "artifacts", "passed": art_val["passed"], "warnings": len(art_val["warnings"])})

    pol_val = validate_policy_control_mapping(tables.get("policy_registry"), tables.get("control_registry"), tables.get("policy_control_mapping"), profile)
    res.append({"component": "mappings", "passed": pol_val["passed"], "warnings": len(pol_val["warnings"])})

    return pd.DataFrame(res), {"overall_passed": all(r["passed"] for r in res)}
