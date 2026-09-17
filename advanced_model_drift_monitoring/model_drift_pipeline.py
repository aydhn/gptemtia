"""Model Drift Monitoring Pipeline Orchestrator for Phase 142.

Coordinates the 10-stage execution of non-executing drift contracts,
upstream linkages, window and threshold policies, disabled execution safeguards,
findings generation, and report persistence.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

from advanced_model_drift_monitoring.model_drift_config import get_model_drift_profile
from advanced_model_drift_monitoring.model_drift_domain_registry import (
    build_model_drift_domain_registry,
)
from advanced_model_drift_monitoring.model_drift_models import (
    ModelDriftMonitoringManifest,
)
from advanced_model_drift_monitoring.model_drift_monitoring_manifest import (
    build_model_drift_monitoring_manifest,
    summarize_model_drift_monitoring_manifest,
    validate_model_drift_monitoring_manifest,
)
from advanced_model_drift_monitoring.model_drift_profile_registry import (
    build_model_drift_profile_registry,
)
from advanced_model_drift_monitoring.model_drift_report_builder import (
    build_model_drift_markdown_report,
    build_model_drift_text_summary,
)


def run_model_drift_monitoring_pipeline(
    profile_name: str = "balanced_local_model_drift_contracts",
    save: bool = False,
) -> Dict[str, Any]:
    """Executes the 10-stage drift monitoring contract pipeline."""
    # Stage 1: Load Profile & Domains
    profile = get_model_drift_profile(profile_name)
    profiles_registry = build_model_drift_profile_registry()
    domains_registry = build_model_drift_domain_registry()

    # Stage 2 to 8: Assembled via build_model_drift_monitoring_manifest
    manifest = build_model_drift_monitoring_manifest(profile_name=profile_name)

    # Stage 9: Validation
    val_res = validate_model_drift_monitoring_manifest(manifest)
    summary = summarize_model_drift_monitoring_manifest(manifest)
    md_report = build_model_drift_markdown_report(manifest)
    text_summary = build_model_drift_text_summary(manifest)

    saved_files = []
    if save:
        timestamp_str = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        report_dir = Path("reports/output/advanced_model_drift_monitoring")

        report_dir.mkdir(parents=True, exist_ok=True)

        # Save Markdown Report
        md_path = report_dir / f"model_drift_monitoring_report_{timestamp_str}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_report)
        saved_files.append(str(md_path))

        # Save Manifest JSON
        json_path = report_dir / f"model_drift_manifest_{timestamp_str}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(asdict(manifest), f, indent=2, default=str)
        saved_files.append(str(json_path))

    return {
        "status": "success" if val_res["valid"] else "validation_failed",
        "phase": 142,
        "profile": profile_name,
        "manifest_id": manifest.manifest_id,
        "validation": val_res,
        "summary": summary,
        "text_summary": text_summary,
        "saved_files": saved_files,
        "next_phase": 143,
    }
