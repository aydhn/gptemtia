import pandas as pd
from pathlib import Path
from evidence_governance.evidence_config import EvidenceGovernanceProfile

def build_governance_evidence_export_manifest(policy_df: pd.DataFrame, control_df: pd.DataFrame, artifact_df: pd.DataFrame, trace_df: pd.DataFrame, gap_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> dict:
    return {
        "export_metadata": {
            "profile_name": profile.name,
            "local_only": True,
            "official_compliance_claim": False,
            "cloud_upload": False
        },
        "contents": {
            "policies_count": len(policy_df) if policy_df is not None else 0,
            "controls_count": len(control_df) if control_df is not None else 0,
            "artifacts_count": len(artifact_df) if artifact_df is not None else 0,
            "trace_links_count": len(trace_df) if trace_df is not None else 0,
            "gaps_count": len(gap_df) if gap_df is not None else 0
        }
    }

def build_local_evidence_export_index(artifact_df: pd.DataFrame, pack_tables: dict[str, pd.DataFrame], profile: EvidenceGovernanceProfile) -> pd.DataFrame:
    if artifact_df is None or artifact_df.empty:
        return pd.DataFrame()

    index_data = []
    for _, art in artifact_df.iterrows():
        label = art.get("artifact_label")
        # determine which pack it belongs to
        pack_name = "unknown_pack"
        for p_name, p_df in pack_tables.items():
            if p_df is not None and not p_df.empty and art.get("artifact_id") in p_df["artifact_id"].values:
                pack_name = p_name
                break

        index_data.append({
            "artifact_id": art.get("artifact_id"),
            "relative_path": art.get("relative_path"),
            "pack_name": pack_name,
            "export_ready": "export_ready_local"
        })

    return pd.DataFrame(index_data)

def validate_evidence_export_safety(export_manifest: dict, export_index_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> dict:
    warnings = []
    passed = True

    if export_manifest.get("export_metadata", {}).get("cloud_upload") is True:
        passed = False
        warnings.append("Export manifest indicates cloud upload, which is forbidden.")

    if export_manifest.get("export_metadata", {}).get("official_compliance_claim") is True:
        passed = False
        warnings.append("Export manifest indicates official compliance claim, which is forbidden.")

    return {"passed": passed, "warnings": warnings}

def save_governance_evidence_export_manifest(manifest: dict, output_path: Path) -> Path:
    import json
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=4)
    return output_path

def summarize_governance_evidence_export(manifest: dict, export_index_df: pd.DataFrame) -> dict:
    return {
        "export_ready_items": len(export_index_df) if export_index_df is not None else 0,
        "is_safe_local_only": manifest.get("export_metadata", {}).get("local_only", False)
    }
