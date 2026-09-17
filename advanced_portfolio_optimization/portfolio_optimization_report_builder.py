# -*- coding: utf-8 -*-
"""Phase 154: Portfolio Optimization Report Builder.

Generates safe markdown reports and statutory regulatory disclaimers.
"""

from typing import Dict, Optional
import pandas as pd


def build_portfolio_optimization_disclaimer() -> str:
    """Return statutory non-advisory and non-production disclaimer."""
    return (
        "> [!WARNING]\n"
        "> **YASAL UYARI VE GUVENLIK SINIRLARI**:\n"
        "> Bu cikti Phase 154 Portfolio Optimization and Allocation Constraints raporudur. "
        "> Canli emir, broker talimati, kesin AL/SAT, yatirim tavsiyesi, portfolio-optimization/readiness/objective/constraint "
        "> degerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gercek portfolio optimization, "
        "> solver execution, efficient frontier generation, portfolio construction, position sizing, capital allocation, "
        "> weight/allocation/rebalance/order generation, gercek metric calculation, model training, model fit/predict/inference, "
        "> dataset materialization, target/label/prediction uretimi, gercek exposure/leverage/margin/risk metric hesaplama, "
        "> performans garantisi, strategy approval, model deployment, model registry write, model artifact persistence, "
        "> scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanimi veya gercek provider API cagrisi degildir.\n"
    )


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    """Helper formatting DataFrame as markdown table safely without requiring tabulate."""
    if df is None or df.empty:
        return "_No tabular records available._"
    try:
        return df.to_markdown(index=False)
    except Exception:
        return df.to_string(index=False)


def build_portfolio_optimization_profile_markdown_report(summary: Dict, profile_df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for profiles."""
    lines = [
        "# Phase 154: Portfolio Optimization Profile Registry Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
        "## Profil Ozeti",
        f"- **Toplam Profil Sayisi**: {summary.get('profile_count', 0)}",
        f"- **Aktif Profil**: `{summary.get('active_profile', 'None')}`",
        f"- **Cevrimdisi / Yerel Mod**: {summary.get('all_profiles_local_only', True)}",
        f"- **Dry-Run Modu**: {summary.get('all_profiles_dry_run', True)}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Profil Detaylari")
        lines.append(_df_to_markdown(profile_df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_optimization_contract_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for optimization contracts."""
    lines = [
        "# Phase 154: Portfolio Optimization Contracts Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
        "## Sozlesme Ozeti",
        f"- **Tanimlanan Optimizasyon Sozlesmesi**: {summary.get('contract_count', 0)}",
        f"- **Sifir Optimizasyon Yurutmesi**: {summary.get('all_contracts_disallow_optimization', True)}",
        f"- **Sifir Agirlik Uretimi**: {summary.get('all_contracts_disallow_weight_generation', True)}",
        f"- **Manuel Inceleme Zorunlulugu**: {summary.get('manual_review_required_all', True)}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Sozlesme Detaylari")
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_optimization_objective_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for objective contracts."""
    lines = [
        "# Phase 154: Optimization Objective Contracts Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
        "## Amac Fonksiyonu Ozeti",
        f"- **Toplam Amac Fonksiyonu**: {summary.get('objective_count', 0)}",
        f"- **Yer Tutucu Modu**: {summary.get('all_objectives_placeholders', True)}",
        f"- **Sifir Hesaplama**: {summary.get('zero_objective_calculated', True)}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Amac Detaylari")
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_allocation_constraint_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for allocation constraints."""
    lines = [
        "# Phase 154: Allocation Constraint Contracts Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
        "## Tahsisat Kisitlari Ozeti",
        f"- **Toplam Kisit Sozlesmesi**: {summary.get('constraint_count', 0)}",
        f"- **Yer Tutucu Modu**: {summary.get('all_constraints_placeholders', True)}",
        f"- **Canli Uygulama Yok**: {summary.get('zero_live_enforcement', True)}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Kisit Detaylari")
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_solver_placeholder_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for solvers."""
    lines = [
        "# Phase 154: Optimization Solver Contracts Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
        f"- **Cozucu Sayisi**: {summary.get('solver_count', 0)}",
        f"- **Cozucu Calistirilmasi**: {summary.get('zero_solvers_executed', True)}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_optimization_output_contract_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for output contracts."""
    lines = [
        "# Phase 154: Optimization Output Contracts Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
    ]
    if df is not None and not df.empty:
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_optimization_metric_placeholder_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for metric placeholders."""
    lines = [
        "# Phase 154: Optimization Metric Placeholders Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
    ]
    if df is not None and not df.empty:
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_optimization_guard_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for guards."""
    lines = [
        "# Phase 154: Optimization Safety Guards Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
    ]
    if df is not None and not df.empty:
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_optimization_disabled_execution_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for disabled execution."""
    lines = [
        "# Phase 154: Disabled Execution Reports",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
    ]
    if df is not None and not df.empty:
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_optimization_findings_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for findings."""
    lines = [
        "# Phase 154: Portfolio Optimization Findings Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
    ]
    if df is not None and not df.empty:
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_optimization_readiness_score_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for readiness score."""
    lines = [
        "# Phase 154: Portfolio Optimization Readiness Score Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
        f"- **Readiness Score**: `{summary.get('readiness_score', 1.0):.4f}`",
        f"- **Classification**: `{summary.get('classification', 'portfolio_optimization_contract_ready_non_production')}`",
        f"- **Contract Ready**: `{summary.get('is_contract_ready', True)}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_optimization_manifest_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for master manifest."""
    lines = [
        "# Phase 154: Master Portfolio Optimization Manifest Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
        f"- **Current Phase**: {summary.get('current_phase', 154)}",
        f"- **Next Phase**: {summary.get('next_phase', 155)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Portfolio Optimized**: {summary.get('portfolio_optimized', False)}",
        f"- **Portfolio Weights Generated**: {summary.get('portfolio_weights_generated', False)}",
        f"- **Allocation Generated**: {summary.get('allocation_generated', False)}",
        f"- **Rebalance Generated**: {summary.get('rebalance_generated', False)}",
        f"- **Orders Generated**: {summary.get('orders_generated', False)}",
        f"- **Efficient Frontier Generated**: {summary.get('efficient_frontier_generated', False)}",
        f"- **Optimizer Executed**: {summary.get('optimizer_executed', False)}",
        f"- **Solver Executed**: {summary.get('solver_executed', False)}",
        f"- **Broker Order Sent**: {summary.get('broker_order_sent', False)}",
        f"- **Live Order Sent**: {summary.get('live_order_sent', False)}",
        f"- **Phase 155 Handoff Ready**: {summary.get('phase_155_handoff_ready', True)}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_optimization_validation_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for validation engine."""
    lines = [
        "# Phase 154: Portfolio Optimization Validation Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
    ]
    if df is not None and not df.empty:
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_optimization_safety_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for safety boundary."""
    lines = [
        "# Phase 154: Portfolio Optimization Safety Boundary Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
    ]
    if df is not None and not df.empty:
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_phase_155_handoff_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    """Generate markdown report for Phase 155 handoff."""
    lines = [
        "# Phase 154 to Phase 155: Risk Reporting, Exposure Attribution and Limit Monitoring Handoff Report",
        "",
        build_portfolio_optimization_disclaimer(),
        "",
        f"- **Devir Durumu**: `{summary.get('handoff_status', 'READY')}`",
        f"- **Tum Onkosullar Karsilandi**: `{summary.get('all_prerequisites_met', True)}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)
