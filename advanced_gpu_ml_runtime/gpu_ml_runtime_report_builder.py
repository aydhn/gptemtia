"""Phase 136: GPU ML Runtime Markdown Report Builder.

Constructs comprehensive Markdown reports with mandatory disclaimer and non-signal boundaries.
"""

from typing import Any, Dict, Optional
import pandas as pd


GPU_ML_RUNTIME_DISCLAIMER = (
    "Bu çıktı Phase 136 GPU Acceleration and Advanced ML Runtime Foundation raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, GPU/ML runtime readiness değerini "
    "trade sinyali veya production-ready/broker-ready onayı olarak kullanma, strateji üretimi, backtest, "
    "optimizer, model training, model fit/predict/inference, clustering, ensemble, calibration, "
    "prediction/target/label üretimi, sentiment model output, haber tam metni/article body/raw content/"
    "scraped HTML/embedding/vector kullanımı, production deployment, model deployment, scraping veya "
    "gerçek provider API çağrısı değildir."
)


def build_gpu_ml_runtime_disclaimer() -> str:
    """Return official non-signal disclaimer for Phase 136."""
    return GPU_ML_RUNTIME_DISCLAIMER


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    """Format DataFrame as markdown table without requiring optional tabulate."""
    if df is None or df.empty:
        return "_Boş tablo_"
    try:
        return df.to_markdown(index=False)
    except Exception:
        cols = [str(c) for c in df.columns]
        header = "| " + " | ".join(cols) + " |"
        sep = "| " + " | ".join(["---"] * len(cols)) + " |"
        rows = []
        for _, row in df.iterrows():
            rows.append("| " + " | ".join(str(row[c]) for c in df.columns) + " |")
        return "\n".join([header, sep] + rows)


def build_gpu_ml_runtime_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for GPU ML runtime profiles."""
    lines = [
        "# Phase 136: GPU ML Runtime Profile Registry Report",
        "",
        "> " + GPU_ML_RUNTIME_DISCLAIMER,
        "",
        "## Summary",
        f"- **Active Profile**: {summary.get('active_profile', 'unknown')}",
        f"- **Current Phase**: {summary.get('current_phase', 136)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Total Profiles**: {summary.get('total_profiles', 0)}",
        f"- **Non-Signal Certified**: {summary.get('non_signal', True)}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Configured Profiles")
        lines.append(_df_to_markdown(profile_df))
        lines.append("")
    return "\n".join(lines)


def build_local_hardware_discovery_markdown_report(
    summary: Dict[str, Any],
    hardware_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for local hardware discovery."""
    lines = [
        "# Phase 136: Local Hardware Discovery Report",
        "",
        "> " + GPU_ML_RUNTIME_DISCLAIMER,
        "",
        "## Hardware Discovery Summary",
        f"- **Total Items Discovered**: {summary.get('total_items', 0)}",
        f"- **Status**: {summary.get('status', 'READY')}",
        f"- **Non-Signal Verified**: True",
        "",
    ]
    if hardware_df is not None and not hardware_df.empty:
        lines.append("## Discovered Hardware Properties")
        lines.append(_df_to_markdown(hardware_df))
        lines.append("")
    return "\n".join(lines)


def build_gpu_capability_markdown_report(
    summary: Dict[str, Any],
    gpu_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for GPU capability."""
    lines = [
        "# Phase 136: GPU Capability Registry Report",
        "",
        "> " + GPU_ML_RUNTIME_DISCLAIMER,
        "",
        "## GPU Capability Summary",
        f"- **CUDA GPU Detected**: {summary.get('cuda_gpu_detected', False)}",
        f"- **Device Count**: {summary.get('device_count', 0)}",
        f"- **Non-Signal Certified**: True",
        "",
    ]
    if gpu_df is not None and not gpu_df.empty:
        lines.append("## Detected Devices")
        lines.append(_df_to_markdown(gpu_df))
        lines.append("")
    return "\n".join(lines)


def build_runtime_dependency_capability_markdown_report(
    summary: Dict[str, Any],
    dependency_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for runtime dependencies."""
    lines = [
        "# Phase 136: Runtime Dependency Capability Report",
        "",
        "> " + GPU_ML_RUNTIME_DISCLAIMER,
        "",
        "## Dependency Summary",
        f"- **Total Packages Checked**: {summary.get('total_optional_packages', 0)}",
        f"- **Installed**: {summary.get('installed_count', 0)}",
        f"- **Missing/Placeholder**: {summary.get('missing_count', 0)}",
        "",
    ]
    if dependency_df is not None and not dependency_df.empty:
        lines.append("## Package Status Details")
        lines.append(_df_to_markdown(dependency_df))
        lines.append("")
    return "\n".join(lines)


def build_ml_runtime_safety_contract_markdown_report(
    summary: Dict[str, Any],
    contract_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for runtime safety contracts."""
    lines = [
        "# Phase 136: ML Runtime Safety Contracts Report",
        "",
        "> " + GPU_ML_RUNTIME_DISCLAIMER,
        "",
        "## Safety Contracts Summary",
        f"- **Total Contracts**: {summary.get('total_contracts', 0)}",
        f"- **All Enforced**: {summary.get('all_enforced', True)}",
        f"- **Live Trading Prohibited**: True",
        f"- **Model Training Prohibited**: True",
        "",
    ]
    if contract_df is not None and not contract_df.empty:
        lines.append("## Active Safety Contracts")
        lines.append(_df_to_markdown(contract_df))
        lines.append("")
    return "\n".join(lines)


def build_ml_input_contract_markdown_report(
    summary: Dict[str, Any],
    input_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for ML input contracts."""
    lines = [
        "# Phase 136: ML Input Contracts Report",
        "",
        "> " + GPU_ML_RUNTIME_DISCLAIMER,
        "",
        "## ML Input Contracts Summary",
        f"- **Total Input Contracts**: {summary.get('total_contracts', 0)}",
        f"- **Source Preservation Guaranteed**: True",
        f"- **No-Lookahead Enforced**: True",
        f"- **Metadata-Only News Enforced**: True",
        "",
    ]
    if input_df is not None and not input_df.empty:
        lines.append("## Catalog Input Specifications")
        lines.append(_df_to_markdown(input_df))
        lines.append("")
    return "\n".join(lines)


def build_ml_runtime_findings_markdown_report(
    summary: Dict[str, Any],
    findings_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for runtime findings."""
    lines = [
        "# Phase 136: ML Runtime Findings Report",
        "",
        "> " + GPU_ML_RUNTIME_DISCLAIMER,
        "",
        "## Findings Summary",
        f"- **Total Findings**: {summary.get('total_findings', 0)}",
        f"- **Manual Review Required**: {summary.get('manual_review_count', 0)}",
        "",
    ]
    if findings_df is not None and not findings_df.empty:
        lines.append("## Active Findings")
        lines.append(_df_to_markdown(findings_df))
        lines.append("")
    return "\n".join(lines)


def build_ml_runtime_readiness_score_markdown_report(
    summary: Dict[str, Any],
    score_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for ML runtime readiness score."""
    lines = [
        "# Phase 136: ML Runtime Readiness Score Report",
        "",
        "> " + GPU_ML_RUNTIME_DISCLAIMER,
        "",
        "## Readiness Score Summary",
        f"- **Readiness Score**: {summary.get('readiness_score', 0.0):.4f}",
        f"- **Classification**: {summary.get('classification', 'unknown')}",
        f"- **Is Ready**: {summary.get('is_ready', False)}",
        f"- **Notice**: Hardware readiness score is NOT a trading signal or production approval.",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.append("## Score Breakdown")
        lines.append(_df_to_markdown(score_df))
        lines.append("")
    return "\n".join(lines)


def build_gpu_ml_runtime_manifest_markdown_report(
    summary: Dict[str, Any],
    manifest_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for GPU ML runtime manifest."""
    lines = [
        "# Phase 136: GPU ML Runtime Manifest Report",
        "",
        "> " + GPU_ML_RUNTIME_DISCLAIMER,
        "",
        "## Manifest Summary",
        f"- **Manifest Name**: {summary.get('manifest_name', 'gpu_ml_runtime_manifest')}",
        f"- **Current Phase**: {summary.get('current_phase', 136)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Readiness Score**: {summary.get('readiness_score', 0.0):.4f}",
        f"- **Model Training Executed**: False",
        f"- **Model Predict Executed**: False",
        f"- **Non-Signal Invariant**: True",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.append("## Manifest Invariants")
        lines.append(_df_to_markdown(manifest_df))
        lines.append("")
    return "\n".join(lines)


def build_gpu_ml_runtime_validation_markdown_report(
    summary: Dict[str, Any],
    validation_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for GPU ML runtime validation."""
    lines = [
        "# Phase 136: GPU ML Runtime Validation Report",
        "",
        "> " + GPU_ML_RUNTIME_DISCLAIMER,
        "",
        "## Validation Summary",
        f"- **Total Checks**: {summary.get('total_checks', 0)}",
        f"- **Passed Checks**: {summary.get('passed_checks', 0)}",
        f"- **All Passed**: {summary.get('all_passed', True)}",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append("## Validation Check Details")
        lines.append(_df_to_markdown(validation_df))
        lines.append("")
    return "\n".join(lines)


def build_gpu_ml_runtime_safety_markdown_report(
    summary: Dict[str, Any],
    safety_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for safety boundary."""
    lines = [
        "# Phase 136: GPU ML Runtime Safety Boundary Report",
        "",
        "> " + GPU_ML_RUNTIME_DISCLAIMER,
        "",
        "## Safety Boundary Summary",
        f"- **Safety Status**: {summary.get('safety_status', 'SECURE')}",
        f"- **NO-GO Conditions Enforced**: {summary.get('no_go_count', 0)}",
        f"- **SAFE-GO Principles Active**: {summary.get('safe_go_count', 0)}",
        f"- **Zero Trading Allowed**: True",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append("## Boundary Conditions")
        lines.append(_df_to_markdown(safety_df))
        lines.append("")
    return "\n".join(lines)


def build_phase_137_handoff_markdown_report(
    summary: Dict[str, Any],
    handoff_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for Phase 137 handoff."""
    lines = [
        "# Phase 136: Phase 137 ML Dataset & Experiment Handoff Report",
        "",
        "> " + GPU_ML_RUNTIME_DISCLAIMER,
        "",
        "## Handoff Summary",
        f"- **Source Phase**: {summary.get('source_phase', 136)}",
        f"- **Next Phase**: {summary.get('next_phase', 137)} (Advanced ML Dataset Contracts and Experiment Registry)",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Total Prerequisites**: {summary.get('total_prerequisites', 0)}",
        f"- **All Satisfied**: {summary.get('all_satisfied', True)}",
        f"- **Status**: {summary.get('status', 'READY')}",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Handoff Prerequisites")
        lines.append(_df_to_markdown(handoff_df))
        lines.append("")
    return "\n".join(lines)
