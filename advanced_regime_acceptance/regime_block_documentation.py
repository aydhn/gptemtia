"""Phase 135: Regime Block Documentation Audit Report.

Verifies the presence and integrity of all required markdown documentation files.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    ACCEPTANCE_PASS,
    REGIME_BLOCK_DOCUMENTATION_DOMAIN,
)


DOCUMENTATION_FILES: List[str] = [
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


def build_regime_block_documentation_report(
    project_root: Optional[Path] = None,
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Audit project documentation files for existence and size."""
    root = project_root or Path(".")
    active = profile or get_regime_acceptance_profile()

    rows = []
    for rel_path in DOCUMENTATION_FILES:
        target = root / rel_path
        exists = target.is_file()
        size_bytes = target.stat().st_size if exists else 0
        rows.append({
            "doc_path": rel_path,
            "exists": exists,
            "size_bytes": size_bytes,
            "non_signal": True,
            "status_label": ACCEPTANCE_PASS if exists and size_bytes > 0 else "acceptance_fail",
        })

    df = pd.DataFrame(rows)
    all_exist = bool(df["exists"].all())
    summary: Dict[str, Any] = {
        "domain": REGIME_BLOCK_DOCUMENTATION_DOMAIN,
        "active_profile": active.profile_name,
        "total_docs": len(df),
        "docs_existing": int(df["exists"].sum()),
        "all_exist": all_exist,
        "non_signal": True,
        "status": "READY" if all_exist else "INCOMPLETE",
    }
    return df, summary


def summarize_regime_block_documentation(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize documentation audit DataFrame."""
    return {
        "total_docs": len(df),
        "all_exist": bool(df["exists"].all()) if not df.empty and "exists" in df.columns else False,
        "non_signal": True,
    }
