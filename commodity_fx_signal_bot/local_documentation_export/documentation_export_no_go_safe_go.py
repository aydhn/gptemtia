"""No-go / safe-go boundaries."""
import pandas as pd
from .export_config import LocalDocumentationExportProfile

def build_documentation_export_no_go_safe_go_summary(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    no_go = build_documentation_export_no_go_conditions(profile)
    safe_go = build_documentation_export_safe_go_conditions(profile)
    df = pd.concat([no_go, safe_go], ignore_index=True)
    return df, summarize_documentation_export_no_go_safe_go(df)

def build_documentation_export_no_go_conditions(profile: LocalDocumentationExportProfile) -> pd.DataFrame:
    conditions = [
        "real static site deploy claim",
        "web server claim",
        "web dashboard claim",
        "GUI/TUI claim",
        "PDF binary generated claim",
        "browser automation claim",
        "presentation deck generated claim",
        "slides generated claim",
        "cloud docs/hosting/CDN claim",
        "package publish claim",
        "docker build/push claim",
        "git tag claim",
        "cloud upload claim",
        "deployment claim",
        "official documentation release claim",
        "legal/compliance approval claim",
        "production approval claim",
        "broker readiness claim",
        "live trading claim",
        "investment advice wording",
        "model deployment claim",
        "telemetry claim",
        "external LLM/API claim",
        "vector/embedding claim",
        "raw secret output",
        "file deletion/move/overwrite claim"
    ]
    return pd.DataFrame([{"condition": c, "type": "no-go"} for c in conditions])

def build_documentation_export_safe_go_conditions(profile: LocalDocumentationExportProfile) -> pd.DataFrame:
    conditions = [
        "static site export rehearsal documented",
        "offline HTML pack documented",
        "printable binder documented",
        "PDF-ready docs documented",
        "presentation-freeze documented",
        "source/output/command maps available",
        "route/role maps available",
        "no real deploy/hosting/dashboard/PDF/slides/live/broker/advice",
        "manual review required"
    ]
    return pd.DataFrame([{"condition": c, "type": "safe-go"} for c in conditions])

def summarize_documentation_export_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"total": len(summary_df)}
