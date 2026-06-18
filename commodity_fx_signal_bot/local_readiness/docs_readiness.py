import pandas as pd
from pathlib import Path
from .readiness_config import LocalReadinessProfile

REQUIRED_DOCS = [
    "README.md",
    "docs/ARCHITECTURE.md",
    "docs/PHASE_LOG.md",
    "docs/OPERATOR_MANUAL.md",
    "docs/ANALYST_HANDBOOK.md",
    "docs/CODEX_AGENT_GUIDE.md",
    "docs/SAFE_USAGE_GUIDE.md",
    "docs/INSTALLATION.md",
    "docs/CONFIGURATION.md"
]

def build_documentation_readiness_report(project_root: Path, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    df = check_required_docs(project_root)
    return df, summarize_docs_readiness(df)

def check_required_docs(project_root: Path) -> pd.DataFrame:
    results = []
    for doc in REQUIRED_DOCS:
        p = project_root / doc
        results.append({
            "doc_path": doc,
            "exists": p.exists()
        })
    return pd.DataFrame(results)

def check_docs_contain_non_use_policy(project_root: Path) -> pd.DataFrame:
    # stub
    return pd.DataFrame([{"doc_path": "README.md", "has_policy": True}])

def check_docs_contain_phase69_entry(project_root: Path) -> pd.DataFrame:
    # stub
    return pd.DataFrame([{"doc_path": "docs/PHASE_LOG.md", "has_phase69": True}])

def summarize_docs_readiness(docs_df: pd.DataFrame) -> dict:
    return {
        "total_docs": len(docs_df),
        "existing_docs": len(docs_df[docs_df["exists"] == True])
    }
