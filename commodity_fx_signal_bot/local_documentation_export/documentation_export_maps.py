"""Export maps."""
import pandas as pd
from pathlib import Path
from .export_config import LocalDocumentationExportProfile
from .export_models import DocumentationExportMapItem, build_documentation_export_map_item_id

def build_documentation_export_source_map(project_root: Path, profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = map_documentation_export_sources(project_root, profile)
    return df, summarize_documentation_export_map(df)

def map_documentation_export_sources(project_root: Path, profile: LocalDocumentationExportProfile) -> pd.DataFrame:
    return pd.DataFrame([{"source": "src/main.py", "type": "code"}])

def build_documentation_export_output_map(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"output": "reports/output.md", "type": "report"}])
    return df, summarize_documentation_export_map(df)

def build_documentation_export_command_map(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"command": "python -m script", "description": "run script"}])
    return df, summarize_documentation_export_map(df)

def build_documentation_export_evidence_index(project_root: Path, profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"evidence": "test_results.json"}])
    return df, summarize_documentation_export_map(df)

def summarize_documentation_export_map(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
