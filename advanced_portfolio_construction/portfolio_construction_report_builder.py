# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Report Builder.

Generates markdown and textual reports for all Portfolio Construction contracts,
position sizing, risk budgeting, limits, guards, disabled execution checks,
readiness scores, manifests, and Phase 154 handoffs with mandatory regulatory disclaimers.
"""

from typing import Any, Dict, Optional
import pandas as pd


def build_portfolio_construction_disclaimer() -> str:
    """Return the mandatory safety and regulatory disclaimer for Phase 153."""
    return (
        "> [!CAUTION]\n"
        "> **YASAL UYARI VE GÜVENLİK BİLDİRİMİ (PHASE 153 PORTFOLIO CONSTRUCTION CONTRACT REPORT)**:\n"
        "> Bu çıktı Phase 153 Portfolio Construction, Position Sizing and Risk Budgeting sözleşme katmanı "
        "> çıktısıdır. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, portföy/sizing/risk "
        "> değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek portföy "
        "> optimizasyonu (quadratic programming, mean-variance, vb.), gerçek sermaye tahsisi (capital allocation), "
        "> hedef portföy ağırlığı üretimi, gerçek pozisyon boyutlandırma (lot, kontrat, hisse adedi), "
        "> margin/leverage uygulama, canlı risk limiti zorlama, model eğitimi/tahmini, metrik hesaplama, "
        "> web kazıma veya canlı broker API entegrasyonu kesinlikle DEĞİLDİR ve YASAKTIR.\n"
    )


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    """Helper formatting DataFrame as markdown table safely without requiring tabulate."""
    if df is None or df.empty:
        return "_No tabular records available._"
    try:
        return df.to_markdown(index=False)
    except Exception:
        return df.to_string(index=False)


def build_portfolio_construction_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for profile registry."""
    md = [
        build_portfolio_construction_disclaimer(),
        "## Portfolio Construction Profile Registry",
        f"- **Active Profile**: `{summary.get('active_profile', 'N/A')}`",
        f"- **Total Profiles**: {summary.get('total_profiles', 0)}",
        f"- **All Dry Run**: {summary.get('all_dry_run', True)}",
        f"- **All Local Only**: {summary.get('all_local_only', True)}",
        f"- **Status**: `{summary.get('status', 'PORTFOLIO_CONTRACT_READY')}`\n",
    ]
    if profile_df is not None and not profile_df.empty:
        md.append(_df_to_markdown(profile_df))
    return "\n".join(md)


def build_portfolio_construction_contracts_markdown_report(
    summary: Dict[str, Any], contracts_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for portfolio construction contracts."""
    md = [
        build_portfolio_construction_disclaimer(),
        "## Portfolio Construction Contracts",
        f"- **Active Profile**: `{summary.get('active_profile', 'N/A')}`",
        f"- **Total Contracts**: {summary.get('total_contracts', 0)}",
        f"- **Status**: `{summary.get('status', 'PORTFOLIO_CONTRACT_READY')}`\n",
    ]
    if contracts_df is not None and not contracts_df.empty:
        md.append(_df_to_markdown(contracts_df))
    return "\n".join(md)


def build_position_sizing_contracts_markdown_report(
    summary: Dict[str, Any], sizing_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for position sizing contracts."""
    md = [
        build_portfolio_construction_disclaimer(),
        "## Position Sizing Contracts",
        f"- **Active Profile**: `{summary.get('active_profile', 'N/A')}`",
        f"- **Total Sizing Models**: {summary.get('total_models', 0)}",
        f"- **Status**: `{summary.get('status', 'PORTFOLIO_CONTRACT_READY')}`\n",
    ]
    if sizing_df is not None and not sizing_df.empty:
        md.append(_df_to_markdown(sizing_df))
    return "\n".join(md)


def build_risk_budget_contracts_markdown_report(
    summary: Dict[str, Any], risk_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for risk budget contracts."""
    md = [
        build_portfolio_construction_disclaimer(),
        "## Risk Budget Contracts",
        f"- **Active Profile**: `{summary.get('active_profile', 'N/A')}`",
        f"- **Total Rules**: {summary.get('total_rules', 0)}",
        f"- **Status**: `{summary.get('status', 'PORTFOLIO_CONTRACT_READY')}`\n",
    ]
    if risk_df is not None and not risk_df.empty:
        md.append(_df_to_markdown(risk_df))
    return "\n".join(md)


def build_findings_markdown_report(
    summary: Dict[str, Any], findings_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for portfolio findings."""
    md = [
        build_portfolio_construction_disclaimer(),
        "## Portfolio Construction Findings",
        f"- **Active Profile**: `{summary.get('active_profile', 'N/A')}`",
        f"- **Total Findings**: {summary.get('total_findings', 0)}",
        f"- **Critical Count**: {summary.get('critical_count', 0)}",
        f"- **Manual Review Required Count**: {summary.get('manual_review_required_count', 0)}",
        f"- **Status**: `{summary.get('status', 'PORTFOLIO_CONTRACT_READY')}`\n",
    ]
    if findings_df is not None and not findings_df.empty:
        md.append(_df_to_markdown(findings_df))
    return "\n".join(md)


def build_readiness_score_markdown_report(
    summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for readiness score."""
    md = [
        build_portfolio_construction_disclaimer(),
        "## Portfolio Construction Readiness Score",
        f"- **Overall Score**: {summary.get('overall_score', 1.0)}",
        f"- **Classification**: `{summary.get('classification', 'portfolio_construction_contract_ready_non_production')}`",
        f"- **Meets Threshold**: {summary.get('meets_threshold', True)}",
        f"- **Status**: `{summary.get('status', 'PORTFOLIO_CONTRACT_READY')}`\n",
    ]
    if score_df is not None and not score_df.empty:
        md.append(_df_to_markdown(score_df))
    return "\n".join(md)


def build_manifest_markdown_report(
    summary: Dict[str, Any], manifest_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for master manifest."""
    md = [
        build_portfolio_construction_disclaimer(),
        "## Portfolio Construction Master Manifest",
        f"- **Manifest ID**: `{summary.get('manifest_id', 'MNF-153-001')}`",
        f"- **Current Phase**: {summary.get('current_phase', 153)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Next Phase**: {summary.get('next_phase', 154)}",
        f"- **Portfolio Constructed**: {summary.get('portfolio_constructed', False)}",
        f"- **Position Sizing Generated**: {summary.get('position_sizing_generated', False)}",
        f"- **Capital Allocation Generated**: {summary.get('capital_allocation_generated', False)}",
        f"- **Orders Generated**: {summary.get('orders_generated', False)}",
        f"- **Broker Order Sent**: {summary.get('broker_order_sent', False)}",
        f"- **Live Order Sent**: {summary.get('live_order_sent', False)}",
        f"- **Phase 154 Handoff Ready**: {summary.get('phase_154_handoff_ready', True)}",
        f"- **Status**: `{summary.get('status', 'PORTFOLIO_CONTRACT_READY')}`\n",
    ]
    if manifest_df is not None and not manifest_df.empty:
        md.append(_df_to_markdown(manifest_df))
    return "\n".join(md)


def build_phase_154_handoff_markdown_report(
    summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for Phase 154 handoff."""
    md = [
        build_portfolio_construction_disclaimer(),
        "## Phase 154 Handoff Report",
        f"- **Handoff ID**: `{summary.get('handoff_id', 'HND-153-154-001')}`",
        f"- **Source Phase**: {summary.get('source_phase', 153)}",
        f"- **Target Phase**: {summary.get('target_phase', 154)}",
        f"- **Final Goal Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Handoff Status**: `{summary.get('status', 'HANDOFF_READY')}`",
        f"- **Manual Review Required**: {summary.get('manual_review_required', True)}\n",
    ]
    if handoff_df is not None and not handoff_df.empty:
        md.append(_df_to_markdown(handoff_df))
    return "\n".join(md)
