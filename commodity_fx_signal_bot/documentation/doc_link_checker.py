import re
from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any

from documentation.documentation_models import (
    DocumentationLinkCheck,
    build_link_check_id,
    documentation_link_check_to_dict
)

def extract_markdown_links(text: str) -> list[dict]:
    links = []
    pattern = r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)'
    for match in re.finditer(pattern, text):
        links.append({
            "text": match.group(1),
            "target": match.group(2)
        })
    return links

def check_local_markdown_link(source_path: Path, target: str, project_root: Path) -> DocumentationLinkCheck:
    if target.startswith("http://") or target.startswith("https://") or target.startswith("mailto:"):
        return DocumentationLinkCheck(
            link_id=build_link_check_id(str(source_path), target),
            source_doc=str(source_path.name),
            target=target,
            link_type="external",
            exists=True,
            status="ok",
            warnings=[]
        )

    path_part = target.split("#")[0]
    if not path_part:
        return DocumentationLinkCheck(
            link_id=build_link_check_id(str(source_path), target),
            source_doc=str(source_path.name),
            target=target,
            link_type="anchor",
            exists=True,
            status="ok",
            warnings=[]
        )

    try:
        resolved_path = (source_path.parent / path_part).resolve()
        exists = resolved_path.exists()
    except Exception:
        exists = False

    return DocumentationLinkCheck(
        link_id=build_link_check_id(str(source_path), target),
        source_doc=str(source_path.name),
        target=target,
        link_type="local_file",
        exists=exists,
        status="ok" if exists else "broken",
        warnings=[] if exists else [f"Kırık link: {target}"]
    )

def check_document_links(path: Path, project_root: Path) -> list[DocumentationLinkCheck]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception:
        return []

    extracted = extract_markdown_links(text)
    checks = []
    for link in extracted:
        checks.append(check_local_markdown_link(path, link["target"], project_root))
    return checks

def build_documentation_link_check_report(project_root: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    all_checks = []

    docs_dir = project_root / "docs"
    if docs_dir.exists():
        for path in docs_dir.rglob("*.md"):
            all_checks.extend(check_document_links(path, project_root))

    readme_path = project_root / "README.md"
    if readme_path.exists():
        all_checks.extend(check_document_links(readme_path, project_root))

    if not all_checks:
        return pd.DataFrame(columns=[
            "link_id", "source_doc", "target", "link_type", "exists", "status", "warnings"
        ]), {"total_links": 0, "broken_links": 0}

    df = pd.DataFrame([documentation_link_check_to_dict(c) for c in all_checks])
    summary = summarize_link_checks(df)
    return df, summary

def summarize_link_checks(link_df: pd.DataFrame) -> dict:
    if link_df is None or link_df.empty:
        return {"total_links": 0, "broken_links": 0, "external_links": 0}

    return {
        "total_links": len(link_df),
        "broken_links": len(link_df[link_df["status"] == "broken"]),
        "external_links": len(link_df[link_df["link_type"] == "external"])
    }
