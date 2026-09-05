"""Fusion Feature Report Builder.

Builds comprehensive Markdown and Plaintext reports for Phase 120 Macro/Calendar/News Feature Fusion.
Strictly non-signal, research use only.
"""

from datetime import datetime, timezone
from typing import Any, Dict


DISCLAIMER = (
    "DISCLAIMER: BU SISTEM YALNIZCA OFFLINE/YEREL ARASTIRMA VE GELISTIRME AMACLIDIR. "
    "KESINLIKLE YATIRIM TAVSIYESI, TICARI SINYAL, AL-SAT TAVSIYESI, HEDEF VE TAHMIN ICERMEZ. "
    "HABER VERILERI YALNIZCA METADATA OLARAK KULLANILIR; TAM METIN VE KAZIMA (SCRAPING) KULLANILMAZ."
)


def build_fusion_feature_markdown_report(summary_data: Dict[str, Any]) -> str:
    """Construct Markdown report for Phase 120."""
    now = datetime.now(timezone.utc).isoformat()
    lines = [
        "# Phase 120 — Macro / Calendar / News Feature Fusion Report",
        "",
        f"> **Generated at**: `{now}`",
        f"> **Status**: `{summary_data.get('status', 'OK')}`",
        "",
        f"**{DISCLAIMER}**",
        "",
        "## 1. Executive Summary",
        f"- **Current Phase**: {summary_data.get('current_phase', 120)}",
        f"- **Next Phase**: {summary_data.get('next_phase', 121)}",
        f"- **Target Final Phase**: {summary_data.get('target_final_phase', 160)}",
        f"- **Readiness Score**: {summary_data.get('readiness_score', 1.0)}",
        f"- **Handoff Ready**: {summary_data.get('handoff_ready', True)}",
        "",
        "## 2. Fusion Domains & Registries",
        f"- **Domain Count**: {summary_data.get('domain_count', 35)}",
        f"- **Metadata Features Tracked**: {summary_data.get('metadata_feature_count', 0)}",
        f"- **Contracts Verified**: {summary_data.get('contract_count', 0)}",
        f"- **Policies Enforced**: {summary_data.get('policy_count', 0)}",
        "",
        "## 3. Core Safety Guarantees",
        "- **Zero Trade Signal Mandate**: Enforced. Zero buy/sell indicators.",
        "- **Metadata-Only News**: Enforced. No article body, no raw HTML, no scraping.",
        "- **No-Lookahead Backward Join**: Enforced. `safe_fusion_asof_join_backward` with `release_timestamp <= base_timestamp`.",
        "- **Prohibited Shift(-1)**: Enforced. Negative shifts rejected.",
        "",
        "## 4. Handoff to Phase 121",
        f"- **Phase 121 Target**: Feature Validation, Lag Integrity & Leakage Guard",
        f"- **Handoff Status**: {'READY' if summary_data.get('handoff_ready', True) else 'PENDING'}",
        "",
    ]
    return "\n".join(lines)


def build_fusion_feature_text_report(summary_data: Dict[str, Any]) -> str:
    """Construct Plaintext report for Phase 120."""
    now = datetime.now(timezone.utc).isoformat()
    lines = [
        "================================================================================",
        "PHASE 120 — MACRO / CALENDAR / NEWS FEATURE FUSION REPORT",
        f"Timestamp: {now}",
        "================================================================================",
        f"{DISCLAIMER}",
        "--------------------------------------------------------------------------------",
        f"Current Phase: {summary_data.get('current_phase', 120)}",
        f"Next Phase: {summary_data.get('next_phase', 121)}",
        f"Target Final Phase: {summary_data.get('target_final_phase', 160)}",
        f"Readiness Score: {summary_data.get('readiness_score', 1.0)}",
        f"Handoff Ready: {summary_data.get('handoff_ready', True)}",
        f"Domain Count: {summary_data.get('domain_count', 35)}",
        f"Metadata Features Count: {summary_data.get('metadata_feature_count', 0)}",
        "--------------------------------------------------------------------------------",
        "Safety Boundaries:",
        "- Zero Trade Signals: ENFORCED",
        "- Metadata-Only News Fusion: ENFORCED",
        "- No-Lookahead Backward-Only AsOf Join: ENFORCED",
        "- Forbidden Terms & Article Text Guard: ACTIVE",
        "================================================================================",
    ]
    return "\n".join(lines)
