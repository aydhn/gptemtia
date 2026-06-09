import pandas as pd

def build_evidence_traceability_matrix(policy_df: pd.DataFrame, control_df: pd.DataFrame, mapping_df: pd.DataFrame, artifact_df: pd.DataFrame) -> pd.DataFrame:
    # Build trace linking policy -> control -> artifact
    if policy_df is None or policy_df.empty or control_df is None or control_df.empty:
        return pd.DataFrame()

    # Dummy structure for now
    trace = []

    # We will iterate through mappings
    if mapping_df is not None and not mapping_df.empty:
        for _, mapping in mapping_df.iterrows():
            cid = mapping.get("control_id")
            aid = mapping.get("artifact_id")

            # Find control
            ctrl_row = control_df[control_df["control_id"] == cid]
            if ctrl_row.empty:
                continue
            ctrl = ctrl_row.iloc[0]

            # Find artifact
            art_row = artifact_df[artifact_df["artifact_id"] == aid]
            art = art_row.iloc[0] if not art_row.empty else None

            # Find policies linked to this control domain
            for _, pol in policy_df.iterrows():
                p_controls = pol.get("controls", [])
                if not isinstance(p_controls, list):
                    p_controls = [p_controls]

                if ctrl.get("control_domain") in p_controls or pol.get("policy_domain") in ctrl.get("control_domain"):
                    trace.append({
                        "policy_id": pol.get("policy_id"),
                        "policy_name": pol.get("policy_name"),
                        "control_id": cid,
                        "control_name": ctrl.get("control_name"),
                        "control_domain": ctrl.get("control_domain"),
                        "control_status": mapping.get("status", "control_unknown"),
                        "artifact_id": aid,
                        "evidence_path": art.get("relative_path") if art is not None else "missing",
                        "artifact_label": art.get("artifact_label") if art is not None else "missing",
                        "freshness_label": art.get("freshness_label") if art is not None else "missing",
                        "mapping_strength": mapping.get("mapping_strength"),
                        "warnings": []
                    })

    return pd.DataFrame(trace)

def build_policy_traceability_matrix(policy_df: pd.DataFrame, control_df: pd.DataFrame) -> pd.DataFrame:
    # Just policies and controls
    from evidence_governance.control_mapping import build_policy_to_control_mapping
    return build_policy_to_control_mapping(policy_df, control_df)

def build_artifact_traceability_matrix(artifact_df: pd.DataFrame, mapping_df: pd.DataFrame) -> pd.DataFrame:
    # Just artifacts and controls
    if artifact_df is None or mapping_df is None or mapping_df.empty:
        return pd.DataFrame()

    merged = pd.merge(artifact_df, mapping_df, on="artifact_id", how="left")
    return merged

def summarize_traceability_matrix(trace_df: pd.DataFrame) -> dict:
    if trace_df is None or trace_df.empty:
        return {"total_trace_links": 0}

    return {
        "total_trace_links": len(trace_df),
        "unique_policies_traced": trace_df["policy_id"].nunique() if "policy_id" in trace_df.columns else 0,
        "unique_controls_traced": trace_df["control_id"].nunique() if "control_id" in trace_df.columns else 0,
        "unique_artifacts_traced": trace_df["artifact_id"].nunique() if "artifact_id" in trace_df.columns else 0
    }
