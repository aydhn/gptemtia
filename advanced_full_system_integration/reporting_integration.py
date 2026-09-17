# -*- coding: utf-8 -*-
"""Phase 158: Reporting Integration Registry.

Integrates system-wide markdown, txt, json, and csv report builders with disclaimers.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile


def build_reporting_integration_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build reporting integration DataFrame and summary."""
    items = [
        {"item_id": "RPI-001", "format": "markdown", "builder": "build_markdown_reports", "disclaimer_enforced": True, "status": "INTEGRATED"},
        {"item_id": "RPI-002", "format": "text", "builder": "build_text_reports", "disclaimer_enforced": True, "status": "INTEGRATED"},
        {"item_id": "RPI-003", "format": "json", "builder": "build_json_reports", "disclaimer_enforced": True, "status": "INTEGRATED"},
        {"item_id": "RPI-004", "format": "csv", "builder": "build_csv_reports", "disclaimer_enforced": True, "status": "INTEGRATED"},
    ]
    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_formats": len(df),
        "all_disclaimers_enforced": bool(df["disclaimer_enforced"].all()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
