"""Fusion Feature Orchestration Pipeline.

Orchestrates Phase 120 Macro/Calendar/News Feature Fusion workflows, safety validation,
matrix manifests, and Phase 121 handoff generation.
Strictly non-signal, research use only.
"""

from datetime import datetime, timezone
from typing import Any, Dict, Optional
import pandas as pd
from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_fusion.fusion_feature_config import get_fusion_feature_profile
from advanced_feature_fusion.fusion_feature_profile_registry import get_fusion_feature_profiles_summary
from advanced_feature_fusion.fusion_feature_domain_registry import get_fusion_feature_domains_summary
from advanced_feature_fusion.fusion_feature_metadata_registry import (
    get_fusion_feature_metadata_registry,
    get_fusion_feature_metadata_summary,
)
from advanced_feature_fusion.fusion_feature_matrix import build_fusion_feature_matrix
from advanced_feature_fusion.fusion_feature_validation_rules import run_all_fusion_feature_validation_rules
from advanced_feature_fusion.fusion_quality_handoff import assess_fusion_quality_handoff
from advanced_feature_fusion.fusion_feature_report_builder import (
    build_fusion_feature_markdown_report,
    build_fusion_feature_text_report,
)


def _generate_synthetic_test_data() -> Dict[str, pd.DataFrame]:
    """Generate minimal safe synthetic test dataframes for dry-run verification."""
    times = pd.date_range("2025-01-01 10:00:00", periods=5, freq="h", tz="UTC")
    base_df = pd.DataFrame({
        "timestamp": times,
        "asset_id": ["XAUUSD"] * 5,
        "price_close": [2600.0, 2605.0, 2602.0, 2610.0, 2608.0],
        "feature_volatility": [0.012, 0.014, 0.011, 0.015, 0.013],
    })

    macro_df = pd.DataFrame({
        "macro_indicator_id": ["US_CPI"] * 5,
        "macro_release_timestamp": times,
        "macro_value": [3.1, 3.1, 3.1, 3.2, 3.2],
    })

    calendar_df = pd.DataFrame({
        "event_id": ["EVT_FOMC"] * 5,
        "calendar_release_timestamp": times,
        "actual_value": [5.25, 5.25, 5.25, 5.25, 5.00],
        "forecast_value": [5.25, 5.25, 5.25, 5.25, 5.00],
    })

    news_metadata_df = pd.DataFrame({
        "news_id": [f"N_{i}" for i in range(5)],
        "news_published_timestamp": times,
        "news_topic": ["central_bank"] * 5,
        "news_asset_tags": ["USD,XAU"] * 5,
        "news_macro_tags": ["rate,inflation"] * 5,
    })

    return {
        "base_df": base_df,
        "macro_df": macro_df,
        "calendar_df": calendar_df,
        "news_metadata_df": news_metadata_df,
    }


def run_fusion_feature_pipeline(
    profile_name: Optional[str] = None,
    dry_run: bool = True,
    data_lake: Optional[DataLake] = None,
    base_df: Optional[pd.DataFrame] = None,
    macro_df: Optional[pd.DataFrame] = None,
    calendar_df: Optional[pd.DataFrame] = None,
    news_metadata_df: Optional[pd.DataFrame] = None,
) -> Dict[str, Any]:
    """Execute complete Phase 120 feature fusion pipeline."""
    settings = get_settings()
    prof_name = profile_name or getattr(settings, "default_fusion_feature_profile", "balanced_local_macro_calendar_news_fusion")
    profile = get_fusion_feature_profile(prof_name)
    dl = data_lake or DataLake()

    # Prepare inputs
    if base_df is None:
        synthetic = _generate_synthetic_test_data()
        b_df = synthetic["base_df"]
        m_df = synthetic["macro_df"]
        c_df = synthetic["calendar_df"]
        n_df = synthetic["news_metadata_df"]
    else:
        b_df = base_df
        m_df = macro_df
        c_df = calendar_df
        n_df = news_metadata_df

    # 1. Build matrix
    matrix_df, manifest = build_fusion_feature_matrix(
        base_df=b_df,
        macro_df=m_df,
        calendar_df=c_df,
        news_metadata_df=n_df,
        matrix_id=f"matrix_p120_{profile.profile_name}",
        profile_name=profile.profile_name,
    )

    # 2. Validation
    findings = run_all_fusion_feature_validation_rules(matrix_df)

    # 3. Quality & Handoff
    handoff = assess_fusion_quality_handoff(manifest=manifest, findings=findings)

    # 4. Reports & Storage
    summary_data = {
        "status": "HEALTHY" if handoff["handoff_ready"] else "DEGRADED",
        "current_phase": 120,
        "next_phase": 121,
        "target_final_phase": 160,
        "profile_name": profile.profile_name,
        "readiness_score": handoff["readiness_score"],
        "handoff_ready": handoff["handoff_ready"],
        "domain_count": get_fusion_feature_domains_summary()["total_domains"],
        "metadata_feature_count": get_fusion_feature_metadata_summary()["total_features"],
        "contract_count": 5,
        "policy_count": 5,
        "matrix_rows": manifest.total_rows,
        "matrix_columns": manifest.total_columns,
        "findings_count": len(findings),
        "executed_at": datetime.now(timezone.utc).isoformat(),
    }

    # Save to data lake
    dl.save_fusion_feature_profile_registry(get_fusion_feature_profiles_summary())
    dl.save_fusion_feature_domain_registry(get_fusion_feature_domains_summary())
    dl.save_fusion_feature_matrix_manifest(manifest.to_dict())
    dl.save_fusion_quality_handoff(handoff)

    # Save reports
    md_content = build_fusion_feature_markdown_report(summary_data)
    txt_content = build_fusion_feature_text_report(summary_data)
    dl.save_fusion_feature_report_markdown(md_content)
    dl.save_fusion_feature_report_text(txt_content)

    return {
        "manifest": manifest.to_dict(),
        "handoff": handoff,
        "summary": summary_data,
        "findings": [f.to_dict() for f in findings],
    }
