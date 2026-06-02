"""
Operational playbook logic.
"""

import pandas as pd
from datetime import datetime

from master_orchestration.master_config import MasterOrchestrationProfile
from master_orchestration.master_models import OperationalPlaybookSection, build_playbook_section_id

def build_operator_playbook_sections(profile: MasterOrchestrationProfile) -> list[OperationalPlaybookSection]:
    sections = [
        OperationalPlaybookSection(
            section_id=build_playbook_section_id("Operator Guidelines", "operator"),
            title="Operator Guidelines",
            audience="Operator",
            purpose="Daily operational tasks",
            steps=[{"step": 1, "action": "Run daily offline review"}, {"step": 2, "action": "Check system health"}],
            related_modes=["daily_offline_review_mode"],
            related_commands=["run_system_healthcheck"],
            warnings=["No live trading commands allowed."]
        )
    ]
    return sections

def build_codex_playbook_sections(profile: MasterOrchestrationProfile) -> list[OperationalPlaybookSection]:
    sections = [
        OperationalPlaybookSection(
            section_id=build_playbook_section_id("Codex Guidelines", "codex"),
            title="Codex Guidelines",
            audience="Codex",
            purpose="Development and integration tasks",
            steps=[{"step": 1, "action": "Follow documentation"}, {"step": 2, "action": "Run regression checks"}],
            related_modes=["regression_check_mode", "documentation_refresh_mode"],
            related_commands=["run_scenario_regression", "run_documentation_pack_report"],
            warnings=["Never generate code for live broker execution."]
        )
    ]
    return sections

def build_analyst_playbook_sections(profile: MasterOrchestrationProfile) -> list[OperationalPlaybookSection]:
    sections = [
        OperationalPlaybookSection(
            section_id=build_playbook_section_id("Analyst Guidelines", "analyst"),
            title="Analyst Guidelines",
            audience="Analyst",
            purpose="Signal review and summarization",
            steps=[{"step": 1, "action": "Generate executive brief"}, {"step": 2, "action": "Review scenario runs"}],
            related_modes=["summary_briefing_mode", "scenario_demo_mode"],
            related_commands=["run_executive_summary_report", "run_scenarios"],
            warnings=["Do not treat outputs as investment advice."]
        )
    ]
    return sections

def build_full_operational_playbook(profile: MasterOrchestrationProfile, mode_df: pd.DataFrame, plan_df: pd.DataFrame) -> tuple[str, dict]:
    sections = []
    sections.extend(build_operator_playbook_sections(profile))
    sections.extend(build_codex_playbook_sections(profile))
    sections.extend(build_analyst_playbook_sections(profile))

    text_lines = [
        "===========================================================",
        "FULL PROJECT OPERATIONAL PLAYBOOK",
        "===========================================================",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "UYARI: Bu playbook offline araştırma/dry-run işlemleri içindir.",
        "Canlı trading kılavuzu veya broker yönergesi değildir.",
        "Otomatik trade onayı içermez.",
        ""
    ]

    for sec in sections:
        text_lines.append(f"### {sec.title} ({sec.audience})")
        text_lines.append(f"Purpose: {sec.purpose}")
        text_lines.append("Steps:")
        for step in sec.steps:
            text_lines.append(f"  {step['step']}. {step['action']}")
        text_lines.append(f"Related Modes: {', '.join(sec.related_modes)}")
        text_lines.append(f"Related Commands: {', '.join(sec.related_commands)}")
        text_lines.append(f"Warnings: {', '.join(sec.warnings)}")
        text_lines.append("")

    summary = {
        "total_sections": len(sections),
        "audiences": list(set([s.audience for s in sections]))
    }

    return "\n".join(text_lines), summary

def operational_playbook_sections_to_dataframe(sections: list[OperationalPlaybookSection]) -> pd.DataFrame:
    if not sections:
        return pd.DataFrame()
    return pd.DataFrame([vars(s) for s in sections])
