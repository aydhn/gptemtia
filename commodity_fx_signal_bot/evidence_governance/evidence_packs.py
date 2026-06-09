import pandas as pd
from evidence_governance.evidence_config import EvidenceGovernanceProfile

def build_evidence_pack(pack_name: str, artifact_df: pd.DataFrame, mapping_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df is None or artifact_df.empty:
        return pd.DataFrame(), {"warnings": ["No artifacts to pack"]}

    # filter artifacts by matching the pack name loosely
    target_label = pack_name.lower().replace(" ", "_")
    if not target_label.endswith("_evidence"):
        target_label += "_evidence"

    pack_df = artifact_df[artifact_df["artifact_label"] == target_label]

    return pack_df, {"pack_size": len(pack_df)}

def build_safety_evidence_pack(artifact_df: pd.DataFrame, mapping_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    return build_evidence_pack("safety", artifact_df, mapping_df, profile)

def build_secrets_hygiene_evidence_pack(artifact_df: pd.DataFrame, mapping_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    return build_evidence_pack("secrets_hygiene", artifact_df, mapping_df, profile)

def build_backup_recovery_evidence_pack(artifact_df: pd.DataFrame, mapping_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    return build_evidence_pack("backup_recovery", artifact_df, mapping_df, profile)

def build_portable_packaging_evidence_pack(artifact_df: pd.DataFrame, mapping_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    return build_evidence_pack("packaging", artifact_df, mapping_df, profile)

def build_quality_gate_evidence_pack(artifact_df: pd.DataFrame, mapping_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    return build_evidence_pack("quality", artifact_df, mapping_df, profile)

def build_scenario_regression_evidence_pack(artifact_df: pd.DataFrame, mapping_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    return build_evidence_pack("scenario_regression", artifact_df, mapping_df, profile)

def build_final_review_evidence_pack(artifact_df: pd.DataFrame, mapping_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    return build_evidence_pack("final_review", artifact_df, mapping_df, profile)

def build_documentation_evidence_pack(artifact_df: pd.DataFrame, mapping_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    return build_evidence_pack("documentation", artifact_df, mapping_df, profile)

def build_master_orchestration_evidence_pack(artifact_df: pd.DataFrame, mapping_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    return build_evidence_pack("master_orchestration", artifact_df, mapping_df, profile)
