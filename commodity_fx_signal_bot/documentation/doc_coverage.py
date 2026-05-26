from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any

from documentation.documentation_models import (
    DocumentationCoverageItem,
    build_coverage_id,
    documentation_coverage_item_to_dict
)

EXPECTED_MODULES = [
    "data", "features", "candidates", "risk", "backtest", "validation", "ml",
    "paper", "notifications", "orchestration", "observability", "security",
    "research_reports", "report_exports", "portfolio_research", "portfolio_regime",
    "synthetic_indices", "factor_research", "meta_research", "experiments",
    "governance", "research_planning", "knowledge_base", "command_center",
    "quality_gates", "performance", "maintenance", "documentation"
]

def build_expected_documentation_matrix() -> pd.DataFrame:
    items = []
    for mod in EXPECTED_MODULES:
        items.append({
            "module_name": mod,
            "expected_doc": f"docs/MODULE_{mod.upper()}.md"
        })
    return pd.DataFrame(items)

def check_module_documentation_coverage(project_root: Path) -> pd.DataFrame:
    matrix = build_expected_documentation_matrix()
    results = []

    docs_dir = project_root / "docs"
    all_text = ""
    if docs_dir.exists():
         for p in docs_dir.rglob("*.md"):
             try:
                 with open(p, "r", encoding="utf-8") as f:
                     all_text += f.read().lower() + "\n"
             except Exception:
                 pass

    readme_path = project_root / "README.md"
    if readme_path.exists():
         try:
             with open(readme_path, "r", encoding="utf-8") as f:
                 all_text += f.read().lower() + "\n"
         except Exception:
             pass

    for _, row in matrix.iterrows():
        mod_name = row["module_name"]
        doc_exists = mod_name.lower() in all_text

        item = DocumentationCoverageItem(
            coverage_id=build_coverage_id(mod_name, row["expected_doc"]),
            module_name=mod_name,
            expected_doc=row["expected_doc"],
            doc_exists=doc_exists,
            section_exists=doc_exists,
            status="covered" if doc_exists else "missing",
            warnings=[] if doc_exists else [f"Modül {mod_name} için dokümantasyon (mention) bulunamadı."]
        )
        results.append(documentation_coverage_item_to_dict(item))

    return pd.DataFrame(results)

def check_script_documentation_coverage(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def check_output_documentation_coverage(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def build_documentation_coverage_report(project_root: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = check_module_documentation_coverage(project_root)
    summary = summarize_documentation_coverage(df)
    return df, summary

def summarize_documentation_coverage(coverage_df: pd.DataFrame) -> dict:
    if coverage_df is None or coverage_df.empty:
        return {"total_modules": 0, "covered_modules": 0, "missing_modules": 0}

    covered = len(coverage_df[coverage_df["status"] == "covered"])
    return {
        "total_modules": len(coverage_df),
        "covered_modules": covered,
        "missing_modules": len(coverage_df) - covered
    }
