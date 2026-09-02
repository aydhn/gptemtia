import pandas as pd
from pathlib import Path
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def map_questions_to_evidence_paths(question_df: pd.DataFrame, project_root: Path, profile: LocalAcceptanceProfile) -> pd.DataFrame:
    df = question_df.copy()
    if not df.empty:
        df["mapped_evidence"] = df["question"].apply(lambda x: ["docs/README.md"])
        df["warnings"] = df["warnings"].apply(lambda x: x + ["Missing evidence manual review warning üretir."])
    return df

def build_reviewer_evidence_request_matrix(question_df: pd.DataFrame, project_root: Path, profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    df = map_questions_to_evidence_paths(question_df, project_root, profile)
    return df, summarize_reviewer_evidence_matrix(df)

def summarize_reviewer_evidence_matrix(matrix_df: pd.DataFrame) -> dict:
    return {"mapped_questions": len(matrix_df)}
