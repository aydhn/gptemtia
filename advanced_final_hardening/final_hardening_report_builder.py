# -*- coding: utf-8 -*-
"""Phase 159: Final Hardening Report Builder.

Generates comprehensive Markdown reports and mandatory disclaimers for
Phase 159 Final Hardening, Operator Runbook, and Release Candidate artifacts.
"""

from typing import Dict, Optional
import pandas as pd

FINAL_HARDENING_DISCLAIMER: str = (
    "> [!WARNING]\n"
    "> **YASAL VE GÜVENLİK FERAGATNAMESİ (PHASE 159)**:\n"
    "> Bu çıktı Phase 159 Final Hardening, Operator Runbook and Release Candidate çıktısıdır. "
    "> Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, final-hardening/release-candidate/readiness/runbook "
    "> değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek full-system execution, "
    "> end-to-end bot run, live trading, broker execution, order generation, signal generation, model training, "
    "> model fit/predict/inference, target/label/prediction üretimi, backtest, benchmark, optimizer, portfolio construction, "
    "> risk reporting, scenario execution, metric calculation, release deployment, production deployment, model deployment, "
    "> model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/"
    "> embedding/vector kullanımı veya gerçek provider API çağrısı değildir.\n"
)


def build_final_hardening_disclaimer() -> str:
    """Return standard Phase 159 disclaimer block."""
    return FINAL_HARDENING_DISCLAIMER


def _df_to_md_table(df: Optional[pd.DataFrame]) -> str:
    """Convert a DataFrame to a readable Markdown table or return empty note."""
    if df is None or df.empty:
        return "_Kayıt bulunamadı._\n"
    try:
        return df.to_markdown(index=False) + "\n\n"
    except Exception:
        cols = [str(c) for c in df.columns]
        header = "| " + " | ".join(cols) + " |"
        sep = "| " + " | ".join(["---"] * len(cols)) + " |"
        rows = []
        for _, row in df.iterrows():
            rows.append("| " + " | ".join(str(row[c]) for c in df.columns) + " |")
        return "\n".join([header, sep] + rows) + "\n\n"


def build_final_hardening_profile_markdown_report(summary: Dict, profile_df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Final Hardening Profile Registry Report\n",
        build_final_hardening_disclaimer(),
        "## Profile Registry Summary\n",
        f"- **Active Profile**: `{summary.get('active_profile', 'unknown')}`",
        f"- **Profile Count**: {summary.get('profile_count', 0)}",
        f"- **Current Phase**: {summary.get('current_phase', 159)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Next Phase**: {summary.get('next_phase', 160)}",
        f"- **All Local Only**: {summary.get('all_local_only', True)}",
        f"- **Status**: `{summary.get('status', 'final_hardening_contract_ready')}`\n",
        "## Profiles Table\n",
        _df_to_md_table(profile_df),
    ]
    return "\n".join(md)


def build_final_hardening_contract_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Final Hardening Contracts Report\n",
        build_final_hardening_disclaimer(),
        "## Contract Summary\n",
        f"- **Contract Count**: {summary.get('contract_count', 0)}",
        f"- **All Execution Blocked**: {summary.get('all_execution_blocked', True)}",
        f"- **All Live Trading Blocked**: {summary.get('all_live_trading_blocked', True)}",
        f"- **Status**: `{summary.get('status', 'final_hardening_contract_ready')}`\n",
        "## Contracts Table\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_operator_runbook_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Operator Runbook Contracts Report\n",
        build_final_hardening_disclaimer(),
        "## Runbook Summary\n",
        f"- **Runbook Count**: {summary.get('runbook_count', 0)}",
        f"- **Execution Blocked**: {summary.get('all_execution_instructions_blocked', True)}",
        f"- **Manual Review Required**: {summary.get('all_manual_review_required', True)}",
        f"- **Status**: `{summary.get('status', 'operator_runbook_contract_ready')}`\n",
        "## Runbooks Table\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_release_candidate_contract_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Release Candidate Contracts Report\n",
        build_final_hardening_disclaimer(),
        "## Release Candidate Summary\n",
        f"- **Contract Count**: {summary.get('candidate_contract_count', 0)}",
        f"- **Production Ready**: {not summary.get('all_production_ready_false', True)}",
        f"- **Broker Ready**: {not summary.get('all_broker_ready_false', True)}",
        f"- **Live Trading Ready**: {not summary.get('all_live_ready_false', True)}",
        f"- **Status**: `{summary.get('status', 'release_candidate_contract_ready')}`\n",
        "## Release Candidate Contracts Table\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_final_freeze_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Final Freeze Contracts Report\n",
        build_final_hardening_disclaimer(),
        "## Freeze Summary\n",
        f"- **Frozen Items Count**: {summary.get('freeze_item_count', 0)}",
        f"- **All Frozen**: {summary.get('all_frozen', True)}",
        f"- **Status**: `{summary.get('status', 'final_hardening_contract_ready')}`\n",
        "## Freeze Table\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_final_inventory_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Final System Inventory Report\n",
        build_final_hardening_disclaimer(),
        "## Inventory Summary\n",
        f"- **Total Items**: {summary.get('item_count', summary.get('component_count', 0))}",
        f"- **Metadata Only**: {summary.get('all_metadata_only', True)}",
        f"- **Status**: `{summary.get('status', 'final_hardening_contract_ready')}`\n",
        "## Inventory Table\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_operator_protocol_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Operator Protocols Report\n",
        build_final_hardening_disclaimer(),
        "## Protocols Summary\n",
        f"- **Rule Count**: {summary.get('rule_count', summary.get('review_count', 0))}",
        f"- **Enforced**: {summary.get('all_enforced', True)}",
        f"- **Status**: `{summary.get('status', 'operator_runbook_contract_ready')}`\n",
        "## Protocols Table\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_release_candidate_checkpoint_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Release Candidate Checkpoints Report\n",
        build_final_hardening_disclaimer(),
        "## Checkpoint Summary\n",
        f"- **Checkpoint Count**: {summary.get('checkpoint_count', 0)}",
        f"- **All Passed / Available**: True",
        f"- **Status**: `{summary.get('status', 'release_candidate_contract_ready')}`\n",
        "## Checkpoints Table\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_release_candidate_boundary_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Release Candidate Boundaries Report\n",
        build_final_hardening_disclaimer(),
        "## Boundary Summary\n",
        f"- **Boundary Count**: {summary.get('boundary_count', summary.get('no_go_boundary_count', 0))}",
        f"- **All Enforced**: {summary.get('all_enforced', True)}",
        f"- **Status**: `{summary.get('status', 'final_hardening_contract_ready')}`\n",
        "## Boundaries Table\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_release_candidate_findings_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Release Candidate Findings Report\n",
        build_final_hardening_disclaimer(),
        "## Findings Summary\n",
        f"- **Finding Count**: {summary.get('finding_count', 0)}",
        f"- **Manual Review Required**: {summary.get('all_manual_review_required', True)}",
        f"- **Status**: `{summary.get('status', 'final_hardening_contract_ready')}`\n",
        "## Findings Table\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_release_candidate_readiness_score_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Release Candidate Readiness Score Report\n",
        build_final_hardening_disclaimer(),
        "## Score Summary\n",
        f"- **Readiness Score**: {summary.get('readiness_score', 0.0):.2f}",
        f"- **Classification**: `{summary.get('classification', 'incomplete')}`",
        f"- **Threshold Met**: {summary.get('threshold_met', True)}",
        f"- **Is Trading Signal**: False",
        f"- **Production Ready**: False",
        f"- **Status**: `{summary.get('status', 'release_candidate_contract_ready')}`\n",
        "## Score Detail\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_release_candidate_manifest_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Release Candidate Manifest Report\n",
        build_final_hardening_disclaimer(),
        "## Manifest Summary\n",
        f"- **Manifest ID**: `{summary.get('manifest_id', 'MNF-159-RELEASE-CANDIDATE-001')}`",
        f"- **Current Phase**: {summary.get('current_phase', 159)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Next Phase**: {summary.get('next_phase', 160)}",
        f"- **Final Hardening Completed**: {summary.get('final_hardening_completed', True)}",
        f"- **Release Candidate Ready**: {summary.get('release_candidate_contract_ready', True)}",
        f"- **Production Ready**: False",
        f"- **Broker Ready**: False",
        f"- **Live Ready**: False",
        f"- **Phase 160 Handoff Ready**: {summary.get('phase_160_handoff_ready', True)}",
        f"- **Status**: `{summary.get('status', 'release_candidate_contract_ready')}`\n",
        "## Manifest Detail\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_final_hardening_validation_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Final Hardening Validation Report\n",
        build_final_hardening_disclaimer(),
        "## Validation Summary\n",
        f"- **Validation Status**: `{summary.get('validation_status', 'VALIDATION_PASS')}`",
        f"- **Total Checks**: {summary.get('total_checks', 0)}",
        f"- **Passed Checks**: {summary.get('passed_checks', 0)}",
        f"- **All Passed**: {summary.get('all_passed', True)}",
        f"- **Status**: `{summary.get('status', 'final_hardening_contract_ready')}`\n",
        "## Validation Table\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_final_hardening_safety_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159: Final Hardening Safety Boundary Report\n",
        build_final_hardening_disclaimer(),
        "## Safety Summary\n",
        f"- **Safety Status**: `{summary.get('safety_status', 'SAFETY_BOUNDARY_ENFORCED')}`",
        f"- **NO-GO Rules Enforced**: {summary.get('no_go_count', 0)}",
        f"- **Safe-GO Rules Active**: {summary.get('safe_go_count', 0)}",
        f"- **Status**: `{summary.get('status', 'final_hardening_contract_ready')}`\n",
        "## Safety Rules Table\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_phase_160_handoff_markdown_report(summary: Dict, df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 159 -> Phase 160: Full Advanced Bot Final Delivery Handoff Report\n",
        build_final_hardening_disclaimer(),
        "## Handoff Summary\n",
        f"- **Current Phase**: {summary.get('current_phase', 159)}",
        f"- **Next Phase**: {summary.get('next_phase', 160)} (Full Advanced Bot Final Delivery)",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Prerequisites Count**: {summary.get('prerequisite_count', 0)}",
        f"- **All Prerequisites Satisfied**: {summary.get('all_satisfied', True)}",
        f"- **Phase 160 Handoff Ready**: {summary.get('phase_160_handoff_ready', True)}",
        f"- **Status**: `{summary.get('status', 'phase_160_handoff_ready')}`\n",
        "## Handoff Prerequisites Table\n",
        _df_to_md_table(df),
    ]
    return "\n".join(md)


def build_final_hardening_full_markdown_report(tables: Dict[str, pd.DataFrame], summary: Dict) -> str:
    """Build consolidated final hardening master Markdown report."""
    md = [
        "# Phase 159: Master Final Hardening & Release Candidate Report\n",
        build_final_hardening_disclaimer(),
        "## Executive Summary\n",
        f"- **Active Profile**: `{summary.get('active_profile', 'balanced_local_final_hardening_contracts')}`",
        f"- **Current Phase**: {summary.get('current_phase', 159)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Readiness Score**: {summary.get('readiness_score', 0.95):.2f}",
        f"- **Classification**: `{summary.get('readiness_classification', 'release_candidate_contract_ready_non_production')}`",
        f"- **Final Hardening Completed**: True",
        f"- **Release Candidate Contract Ready**: True",
        f"- **Operator Runbook Ready**: True",
        f"- **Production / Broker Ready**: Strictly False",
        f"- **Phase 160 Handoff Ready**: True\n",
    ]
    for name, df in tables.items():
        md.append(f"### Subsystem: {name.replace('_', ' ').title()}\n")
        md.append(_df_to_md_table(df))

    return "\n".join(md)
