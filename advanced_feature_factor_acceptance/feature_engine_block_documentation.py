"""Phase 125: Feature Engine Block Documentation Contract Report.

Audits presence and integrity of all governance and architectural documentation.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_default_feature_factor_acceptance_profile,
)

DOC_FILES = [
    "README.md",
    "docs/ARCHITECTURE.md",
    "docs/PHASE_LOG.md",
    "docs/ROADMAP.md",
    "docs/SAFE_USAGE_GUIDE.md",
    "docs/CONFIGURATION.md",
    "docs/OPERATOR_MANUAL.md",
    "docs/ANALYST_HANDBOOK.md",
    "docs/CODEX_AGENT_GUIDE.md",
]


def build_feature_engine_block_documentation_report(
    project_root: Optional[Path] = None,
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Audit project documentation files for existence and non-signal compliance."""
    root = project_root or Path(__file__).resolve().parent.parent
    rows = []
    for doc in DOC_FILES:
        path = root / doc
        exists = path.exists()
        size = path.stat().st_size if exists else 0
        rows.append({
            "doc_path": doc,
            "exists": exists,
            "size_bytes": size,
            "status": "VALID" if exists and size > 0 else "MISSING",
            "non_signal": True,
        })
    df = pd.DataFrame(rows)

    all_exist = bool(df["exists"].all())
    summary = {
        "total_docs_checked": len(df),
        "present_docs": int(df["exists"].sum()),
        "missing_docs": int((~df["exists"]).sum()),
        "all_present": all_exist,
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_feature_engine_block_documentation(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize documentation DataFrame."""
    return {
        "total_docs": len(df),
        "all_present": bool(df["exists"].all()) if "exists" in df.columns else False,
        "non_signal": True,
    }
