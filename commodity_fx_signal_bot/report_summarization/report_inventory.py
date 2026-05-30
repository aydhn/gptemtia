import pandas as pd
from pathlib import Path
from datetime import datetime, timezone
import hashlib

from config.paths import PROJECT_ROOT, REPORTS_DIR, LAKE_DIR, DOCS_DIR
from report_summarization.summary_config import ReportSummaryProfile

def discover_summary_source_reports(project_root: Path, profile: ReportSummaryProfile) -> pd.DataFrame:
    records = []

    if profile.scan_reports_output:
        for p in REPORTS_DIR.rglob("*"):
            if p.is_file() and p.suffix in [".md", ".csv", ".txt", ".json"]:
                records.append(p)

    if profile.scan_data_lake:
        for p in LAKE_DIR.rglob("*"):
            if p.is_file() and p.suffix in [".csv", ".json", ".parquet"]:
                name = p.name.lower()
                if "report" in name or "status" in name or "quality" in name:
                    records.append(p)

    if profile.scan_docs:
        for p in DOCS_DIR.rglob("*.md"):
            if p.is_file():
                records.append(p)

    rows = []
    for p in set(records):
        try:
            stat = p.stat()
            size = stat.st_size
            if size == 0:
                continue

            module = classify_source_report_module(p)
            report_type = classify_source_report_type(p)

            rows.append({
                "source_report_id": "rep_" + hashlib.sha256(str(p.resolve()).encode("utf-8")).hexdigest()[:12],
                "source_path": str(p.relative_to(project_root)),
                "module_name": module,
                "report_type": report_type,
                "size_bytes": size,
                "modified_at_utc": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat()
            })
        except Exception:
            pass

    df = pd.DataFrame(rows)
    if not df.empty:
        df = df.sort_values(by="modified_at_utc", ascending=False).head(profile.max_reports).reset_index(drop=True)
    return df

def classify_source_report_module(path: Path) -> str:
    path_str = str(path).lower()
    modules = [
        "research_reports", "report_exports", "portfolio_research", "portfolio_regime",
        "synthetic_indices", "factor_research", "meta_research", "experiments",
        "governance", "research_planning", "knowledge_base", "command_center",
        "quality_gates", "performance", "maintenance", "documentation",
        "final_review", "scenarios", "scenario_regression", "analyst_ux",
        "report_summarization"
    ]

    for m in modules:
        if m in path_str:
            return m

    return "unknown_module"

def classify_source_report_type(path: Path) -> str:
    path_str = str(path).lower()
    if "status" in path_str: return "status_report"
    if "quality" in path_str: return "quality_report"
    if "audit" in path_str: return "audit_report"
    if "summary" in path_str: return "summary_report"
    if "scenario" in path_str: return "scenario_report"
    if "regression" in path_str: return "regression_report"
    if "finding" in path_str: return "finding_report"
    if "review" in path_str: return "review_report"
    if path.suffix == ".md": return "markdown_doc"
    return "data_report"

def read_report_text(path: Path, max_chars: int) -> tuple[str, dict]:
    try:
        if path.suffix == ".parquet":
            return "", {"status": "skipped_binary"}

        text = path.read_text(encoding="utf-8", errors="replace")

        if ".env" in str(path) or "secret" in str(path).lower():
            return "", {"status": "skipped_secret"}

        truncated = False
        if len(text) > max_chars:
            text = text[:max_chars]
            truncated = True

        return text, {"status": "success", "truncated": truncated}
    except Exception as e:
        return "", {"status": f"error: {str(e)}"}

def build_report_inventory_summary(inventory_df: pd.DataFrame) -> dict:
    if inventory_df.empty:
        return {"total_reports": 0}

    return {
        "total_reports": len(inventory_df),
        "total_size_kb": inventory_df["size_bytes"].sum() / 1024.0,
        "modules_found": inventory_df["module_name"].nunique(),
        "report_types": inventory_df["report_type"].value_counts().to_dict(),
        "latest_report": inventory_df["modified_at_utc"].max()
    }
