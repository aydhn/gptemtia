import pandas as pd
from evidence_governance.evidence_config import EvidenceGovernanceProfile
from evidence_governance.evidence_models import ControlEvidenceMapping, build_control_evidence_mapping_id

def build_policy_to_control_mapping(policy_df: pd.DataFrame, control_df: pd.DataFrame) -> pd.DataFrame:
    if policy_df is None or policy_df.empty or control_df is None or control_df.empty:
        return pd.DataFrame()

    mappings = []

    # We create mapping based on the controls list in policy_df, or domain match
    for _, policy in policy_df.iterrows():
        policy_controls = policy.get("controls", [])
        if not isinstance(policy_controls, list):
            policy_controls = [policy_controls]

        for _, control in control_df.iterrows():
            control_domain = control.get("control_domain")

            # Simple heuristic mapping for this offline mock
            if control_domain in policy_controls or policy.get("policy_domain") in control_domain:
                mappings.append({
                    "policy_id": policy.get("policy_id"),
                    "control_id": control.get("control_id"),
                    "mapping_type": "domain_match"
                })

    return pd.DataFrame(mappings)

def map_controls_to_evidence(control_df: pd.DataFrame, artifact_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    if control_df is None or control_df.empty or artifact_df is None or artifact_df.empty:
        return pd.DataFrame(), {"warnings": ["Missing inputs for mapping"]}

    mappings = []
    warnings = []

    for _, control in control_df.iterrows():
        control_id = control.get("control_id")
        req_labels = control.get("required_evidence_labels", [])
        if not isinstance(req_labels, list):
            req_labels = [req_labels]

        found_match = False
        for _, artifact in artifact_df.iterrows():
            art_id = artifact.get("artifact_id")
            art_label = artifact.get("artifact_label")

            if art_label in req_labels:
                strength = classify_mapping_strength(control, artifact)
                mappings.append({
                    "mapping_id": build_control_evidence_mapping_id(control_id, art_id),
                    "control_id": control_id,
                    "artifact_id": art_id,
                    "mapping_strength": strength,
                    "status": "active",
                    "evidence_path": artifact.get("relative_path", ""),
                    "warnings": []
                })
                found_match = True

        if not found_match:
            warnings.append(f"No evidence found for control {control_id}")

    mapping_df = pd.DataFrame(mappings)
    return mapping_df, {"warnings": warnings, "mapped_pairs": len(mappings)}

def classify_mapping_strength(control_row: pd.Series, artifact_row: pd.Series) -> str:
    # Basic heuristic
    art_label = artifact_row.get("artifact_label")
    req_labels = control_row.get("required_evidence_labels", [])

    if art_label in req_labels:
        # Check freshness to adjust strength potentially?
        if artifact_row.get("freshness_label") == "evidence_fresh":
            return "direct_evidence"
        else:
            return "supporting_evidence"

    return "weak_evidence"

def evaluate_control_status(control_id: str, mapping_df: pd.DataFrame, artifact_df: pd.DataFrame) -> dict:
    if mapping_df is None or mapping_df.empty:
        return {"status": "control_missing_evidence", "warnings": ["No mappings"]}

    control_maps = mapping_df[mapping_df["control_id"] == control_id]
    if control_maps.empty:
        return {"status": "control_missing_evidence", "warnings": ["No evidence mapped"]}

    # Check if any mapping is direct
    if "direct_evidence" in control_maps["mapping_strength"].values:
        return {"status": "control_evidenced", "warnings": []}

    if "supporting_evidence" in control_maps["mapping_strength"].values:
        return {"status": "control_partially_evidenced", "warnings": ["Only supporting evidence found"]}

    return {"status": "control_stale_evidence", "warnings": ["Weak or stale evidence"]}

def build_control_status_table(control_df: pd.DataFrame, mapping_df: pd.DataFrame, artifact_df: pd.DataFrame) -> pd.DataFrame:
    if control_df is None or control_df.empty:
        return pd.DataFrame()

    statuses = []
    for _, control in control_df.iterrows():
        cid = control.get("control_id")
        eval_res = evaluate_control_status(cid, mapping_df, artifact_df)

        statuses.append({
            "control_id": cid,
            "control_name": control.get("control_name"),
            "status": eval_res["status"],
            "warnings": eval_res["warnings"]
        })

    return pd.DataFrame(statuses)

def summarize_control_mapping(mapping_df: pd.DataFrame, status_df: pd.DataFrame) -> dict:
    return {
        "total_mappings": len(mapping_df) if mapping_df is not None else 0,
        "control_statuses": status_df["status"].value_counts().to_dict() if status_df is not None and "status" in status_df.columns else {}
    }
