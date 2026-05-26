from pathlib import Path
import pandas as pd
from typing import Optional

from documentation.documentation_models import (
    DocumentationRecord,
    build_doc_id,
    estimate_word_count,
    count_markdown_headings,
    documentation_record_to_dict
)
from documentation.documentation_labels import validate_document_type

def discover_documentation_files(project_root: Path) -> pd.DataFrame:
    records = []

    # Check root README
    readme_path = project_root / "README.md"
    if readme_path.exists():
        records.append(build_documentation_record(readme_path, project_root))

    # Check docs dir
    docs_dir = project_root / "docs"
    if docs_dir.exists():
        for path in docs_dir.rglob("*.md"):
            records.append(build_documentation_record(path, project_root))

    # Check reports/output
    reports_dir = project_root / "reports" / "output"
    if reports_dir.exists():
        for path in reports_dir.rglob("*.md"):
            records.append(build_documentation_record(path, project_root))
        for path in reports_dir.rglob("*.txt"):
            records.append(build_documentation_record(path, project_root))

    if not records:
        return pd.DataFrame(columns=[
            "doc_id", "title", "document_type", "audience", "path",
            "relative_path", "status", "word_count", "heading_count",
            "has_disclaimer", "safety_label", "warnings"
        ])

    return pd.DataFrame([documentation_record_to_dict(r) for r in records])

def classify_document_type(path: Path) -> str:
    name_lower = path.name.lower()
    if "user_guide" in name_lower:
        return "user_guide_doc"
    elif "operator_manual" in name_lower:
        return "operator_manual_doc"
    elif "analyst_handbook" in name_lower:
        return "analyst_handbook_doc"
    elif "developer_guide" in name_lower:
        return "developer_guide_doc"
    elif "codex_agent_guide" in name_lower:
        return "codex_agent_guide_doc"
    elif "safe_usage" in name_lower:
        return "safe_usage_guide_doc"
    elif "troubleshooting" in name_lower:
        return "troubleshooting_doc"
    elif "faq" in name_lower:
        return "faq_doc"
    elif "glossary" in name_lower:
        return "glossary_doc"
    elif "module_map" in name_lower:
        return "module_map_doc"
    elif "script_reference" in name_lower:
        return "script_reference_doc"
    elif "output_reference" in name_lower:
        return "output_reference_doc"
    elif "architecture" in name_lower:
        return "architecture_doc"
    elif "phase_log" in name_lower:
        return "phase_log_doc"
    elif "reference" in name_lower:
        return "generated_reference_doc"
    return "unknown_doc"

def infer_document_audience(path: Path, text: Optional[str] = None) -> str:
    doc_type = classify_document_type(path)
    if doc_type == "user_guide_doc":
        return "user_audience"
    elif doc_type == "operator_manual_doc":
        return "operator_audience"
    elif doc_type == "analyst_handbook_doc":
        return "analyst_audience"
    elif doc_type in ["developer_guide_doc", "architecture_doc", "module_map_doc", "script_reference_doc"]:
        return "developer_audience"
    elif doc_type == "codex_agent_guide_doc":
        return "codex_agent_audience"
    return "unknown_audience"

def build_documentation_record(path: Path, project_root: Path) -> DocumentationRecord:
    try:
        relative_path = str(path.relative_to(project_root))
    except ValueError:
        relative_path = str(path)

    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception:
        text = ""

    doc_type = classify_document_type(path)
    audience = infer_document_audience(path, text)

    warnings = []
    has_disclaimer = "offline/local" in text.lower() or "yatırım tavsiyesi değildir" in text.lower() or "canlı emir" in text.lower()

    if not has_disclaimer and path.suffix == ".md" and not path.name.lower().startswith("readme"):
         warnings.append("Disclaimer bulunamadı.")

    title = path.stem.replace("_", " ").title()
    if text:
        first_line = text.split('\n')[0].strip()
        if first_line.startswith('# '):
            title = first_line[2:].strip()

    return DocumentationRecord(
        doc_id=build_doc_id(relative_path),
        title=title,
        document_type=doc_type,
        audience=audience,
        path=str(path),
        relative_path=relative_path,
        status="doc_complete" if len(text) > 50 else "doc_incomplete",
        word_count=estimate_word_count(text),
        heading_count=count_markdown_headings(text),
        has_disclaimer=has_disclaimer,
        safety_label="safety_language_ok" if has_disclaimer else "missing_disclaimer",
        warnings=warnings
    )

def summarize_documentation_inventory(docs_df: pd.DataFrame) -> dict:
    if docs_df is None or docs_df.empty:
        return {
            "total_documents": 0,
            "document_types": {},
            "audiences": {},
            "total_words": 0,
            "missing_disclaimers": 0
        }

    return {
        "total_documents": len(docs_df),
        "document_types": docs_df["document_type"].value_counts().to_dict(),
        "audiences": docs_df["audience"].value_counts().to_dict(),
        "total_words": int(docs_df["word_count"].sum()) if "word_count" in docs_df.columns else 0,
        "missing_disclaimers": len(docs_df[docs_df["has_disclaimer"] == False]) if "has_disclaimer" in docs_df.columns else 0
    }
