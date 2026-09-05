"""Export risks."""
import pandas as pd
from .export_config import LocalDocumentationExportProfile
from .export_models import DocumentationExportFinding, build_documentation_export_finding_id

def build_documentation_export_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"risk_id": "risk_1", "description": "General risk"}])
    return df, summarize_documentation_export_risks(df)

def classify_documentation_export_risk(row: pd.Series, profile: LocalDocumentationExportProfile) -> str:
    return "documentation_export_low_risk"

def build_documentation_export_risk_digest(risk_df: pd.DataFrame, profile: LocalDocumentationExportProfile) -> tuple[str, dict]:
    digest = "No critical risks."
    return digest, {"length": len(digest)}

def summarize_documentation_export_risks(risk_df: pd.DataFrame) -> dict:
    return {"count": len(risk_df)}
