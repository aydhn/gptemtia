# -*- coding: utf-8 -*-
"""Phase 146: Realistic Backtest Report Builder.

Generates structured Markdown reports and legal disclaimers for Phase 146.
"""

from typing import Any, Dict, Optional
import pandas as pd


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    """Safe DataFrame to Markdown converter without tabulate requirement."""
    if df is None or df.empty:
        return "_No records available._\n"
    cols = [str(c) for c in df.columns]
    header = "| " + " | ".join(cols) + " |"
    separator = "| " + " | ".join(["---"] * len(cols)) + " |"
    rows = []
    for _, row in df.iterrows():
        row_str = "| " + " | ".join(str(val) for val in row.values) + " |"
        rows.append(row_str)
    return "\n".join([header, separator] + rows) + "\n"


def build_realistic_backtest_disclaimer() -> str:
    """Return strict legal and non-signal disclaimer for Phase 146."""
    return (
        "> **YASAL UYARI VE GUCLENDIRILMIS GUVENLIK SINIRI (PHASE 146)**:\n"
        "> Bu cikti Phase 146 Realistic Backtest, Transaction Cost and Slippage Modeling raporudur. "
        "Canli emir, broker talimati, kesin AL/SAT, yatirim tavsiyesi, backtest/readiness/cost/slippage "
        "degerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gercek backtest "
        "execution, walk-forward, benchmark, optimizer, stress test, Monte Carlo, gercek model training, "
        "model fit/predict/inference, dataset materialization, target/label/prediction uretimi, gercek "
        "performans garantisi, model deployment, model registry write, model artifact persistence, "
        "scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanimi "
        "veya gercek provider API cagrisi degildir.\n"
    )


def build_realistic_backtest_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for profile registry."""
    return (
        f"# Phase 146: Realistic Backtest Profiles Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Profile Summary\n"
        f"- **Active Profile**: {summary.get('active_profile')}\n"
        f"- **Total Profiles**: {summary.get('total_profiles')}\n"
        f"- **Local Only**: {summary.get('all_local_only')}\n"
        f"- **Non-Production**: {summary.get('all_non_production')}\n\n"
        f"## Registered Profiles\n\n"
        f"{_df_to_markdown(profile_df)}\n"
    )


def build_backtest_engine_contract_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for backtest engine contracts."""
    return (
        f"# Phase 146: Backtest Engine Contracts Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Engine Summary\n"
        f"- **Total Contracts**: {summary.get('total_contracts')}\n"
        f"- **All Execution Blocked**: {summary.get('all_execution_blocked')}\n"
        f"- **All Live Trading Blocked**: {summary.get('all_live_trading_blocked')}\n\n"
        f"## Engine Contracts Table\n\n"
        f"{_df_to_markdown(df)}\n"
    )


def build_order_simulation_contract_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for order simulation contracts."""
    return (
        f"# Phase 146: Order Simulation Contracts Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Simulation Summary\n"
        f"- **Total Order Types**: {summary.get('total_order_types')}\n"
        f"- **Broker Orders Blocked**: {summary.get('all_broker_orders_blocked')}\n"
        f"- **Live Orders Blocked**: {summary.get('all_live_orders_blocked')}\n\n"
        f"## Order Simulation Table\n\n"
        f"{_df_to_markdown(df)}\n"
    )


def build_transaction_cost_model_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for transaction cost models."""
    return (
        f"# Phase 146: Transaction Cost Models Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Cost Models Summary\n"
        f"- **Total Cost Models**: {summary.get('total_cost_models')}\n"
        f"- **Real Calculation Blocked**: {summary.get('all_real_calculation_blocked')}\n\n"
        f"## Cost Models Table\n\n"
        f"{_df_to_markdown(df)}\n"
    )


def build_slippage_model_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for slippage models."""
    return (
        f"# Phase 146: Slippage Models Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Slippage Models Summary\n"
        f"- **Total Slippage Models**: {summary.get('total_slippage_models')}\n"
        f"- **Zero Performance Guarantee**: {summary.get('all_zero_guarantee')}\n\n"
        f"## Slippage Models Table\n\n"
        f"{_df_to_markdown(df)}\n"
    )


def build_execution_realism_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for execution realism placeholders and assumptions."""
    return (
        f"# Phase 146: Execution Realism Assumptions Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Realism Summary\n"
        f"- **Total Assumptions**: {summary.get('total_assumptions')}\n"
        f"- **All Enforced**: {summary.get('all_enforced')}\n"
        f"- **Naive Backtest Prevented**: True\n\n"
        f"## Assumptions Table\n\n"
        f"{_df_to_markdown(df)}\n"
    )


def build_backtest_guard_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for no-lookahead and bias guards."""
    return (
        f"# Phase 146: Backtest Bias & Lookahead Guards Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Guards Summary\n"
        f"- **No-Lookahead Guard**: ACTIVE\n"
        f"- **Survivorship Guard**: ACTIVE\n"
        f"- **Data Snooping Guard**: ACTIVE\n"
        f"- **Overfitting Guard**: ACTIVE\n\n"
        f"## Guard Policies\n\n"
        f"{_df_to_markdown(df)}\n"
    )


def build_backtest_disabled_execution_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for disabled execution policies."""
    return (
        f"# Phase 146: Disabled Execution Enforcements Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Disabled Enforcements Summary\n"
        f"- **Live Trading**: DISABLED\n"
        f"- **Broker Order**: DISABLED\n"
        f"- **Optimizer**: DISABLED\n"
        f"- **Walk-Forward**: DISABLED\n"
        f"- **Model Training**: DISABLED\n"
        f"- **Prediction**: DISABLED\n\n"
        f"## Enforcement Details\n\n"
        f"{_df_to_markdown(df)}\n"
    )


def build_backtest_findings_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for findings and review queue."""
    return (
        f"# Phase 146: Backtest Findings & Review Queue Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Findings Summary\n"
        f"- **Total Findings**: {summary.get('total_findings')}\n"
        f"- **Critical Blockers**: {summary.get('critical_blockers')}\n"
        f"- **Manual Review Items**: {summary.get('manual_review_required_count')}\n\n"
        f"## Recorded Findings\n\n"
        f"{_df_to_markdown(df)}\n"
    )


def build_backtest_readiness_score_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for readiness score."""
    return (
        f"# Phase 146: Backtest Readiness Score Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Readiness Score Summary\n"
        f"- **Profile**: {summary.get('profile_name')}\n"
        f"- **Score**: {summary.get('readiness_score', 0.0):.2f} / 1.00\n"
        f"- **Classification**: {summary.get('classification')}\n"
        f"- **Meets Threshold**: {summary.get('meets_threshold')}\n"
        f"- **Production Ready**: FALSE (Contract diagnostic only)\n"
        f"- **Broker Ready**: FALSE\n\n"
        f"## Readiness Breakdown\n\n"
        f"{_df_to_markdown(df)}\n"
    )


def build_realistic_backtest_manifest_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for master manifest."""
    return (
        f"# Phase 146: Realistic Backtest Manifest Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Master Manifest Summary\n"
        f"- **Manifest ID**: {summary.get('manifest_id')}\n"
        f"- **Current Phase**: {summary.get('current_phase')}\n"
        f"- **Next Phase**: {summary.get('next_phase')}\n"
        f"- **Target Final Phase**: {summary.get('target_final_phase')}\n"
        f"- **All Invariants Valid**: {summary.get('all_invariants_valid')}\n\n"
        f"## Invariant Properties Table\n\n"
        f"{_df_to_markdown(df)}\n"
    )


def build_realistic_backtest_validation_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for validation results."""
    return (
        f"# Phase 146: Realistic Backtest Validation Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Validation Summary\n"
        f"- **Status**: {summary.get('validation_status')}\n"
        f"- **Total Checks**: {summary.get('total_checks')}\n"
        f"- **Passed Checks**: {summary.get('passed_checks')}\n"
        f"- **Forbidden Claims Found**: {summary.get('forbidden_claims_found')}\n\n"
        f"## Check Details\n\n"
        f"{_df_to_markdown(df)}\n"
    )


def build_realistic_backtest_safety_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for safety boundaries."""
    return (
        f"# Phase 146: Realistic Backtest Safety Boundaries Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Safety Boundaries Summary\n"
        f"- **Status**: {summary.get('safety_status', 'SECURE')}\n"
        f"- **NO-GO Conditions Enforced**: {summary.get('no_go_count', 34)}\n"
        f"- **SAFE-GO Principles Active**: {summary.get('safe_go_count', 12)}\n\n"
        f"## Rules Table\n\n"
        f"{_df_to_markdown(df)}\n"
    )


def build_phase_147_handoff_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for Phase 147 handoff package."""
    return (
        f"# Phase 146: Phase 147 Walk-Forward & OOS Benchmarking Handoff Report\n\n"
        f"{build_realistic_backtest_disclaimer()}\n"
        f"## Handoff Summary\n"
        f"- **Source Phase**: 146 (Realistic Backtest & Cost Modeling)\n"
        f"- **Target Next Phase**: 147 (Walk-Forward Validation & OOS Benchmarking)\n"
        f"- **Target Final Phase**: 160\n"
        f"- **Handoff Ready**: {summary.get('phase_147_handoff_ready', True)}\n"
        f"- **All Prerequisites Satisfied**: {summary.get('all_prerequisites_satisfied', True)}\n\n"
        f"## Handoff Prerequisites Table\n\n"
        f"{_df_to_markdown(df)}\n"
    )
