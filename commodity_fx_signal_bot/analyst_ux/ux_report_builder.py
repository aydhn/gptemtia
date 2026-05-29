import pandas as pd

def build_ux_disclaimer() -> str:
    return "UYARI: Bu rapor offline analyst UX/productivity çıktısıdır; gerçek emir, canlı sinyal, model deployment, broker talimatı, production scheduler veya yatırım tavsiyesi değildir."

def build_alias_markdown_report(summary: dict, aliases_df: pd.DataFrame | None = None) -> str:
    lines = ["# Command Alias Registry Report", "", build_ux_disclaimer(), ""]
    lines.append(f"Valid Aliases: {summary.get('valid_count', 0)}")
    lines.append(f"Blocked Aliases: {summary.get('blocked_count', 0)}")
    if aliases_df is not None and not aliases_df.empty:
        lines.append("")
        lines.append(aliases_df.to_markdown(index=False))
    return "\n".join(lines)

def build_safe_command_suggestion_markdown_report(summary: dict, suggestions_df: pd.DataFrame | None = None) -> str:
    lines = ["# Safe Command Suggestions Report", "", build_ux_disclaimer(), ""]
    lines.append(f"Intent: {summary.get('intent', 'unknown')}")
    lines.append(f"Total Suggestions: {summary.get('count', 0)}")
    if suggestions_df is not None and not suggestions_df.empty:
        lines.append("")
        lines.append(suggestions_df.to_markdown(index=False))
    return "\n".join(lines)

def build_prompt_pack_markdown_report(summary: dict, prompts_df: pd.DataFrame | None = None) -> str:
    lines = ["# Prompt Pack Report", "", build_ux_disclaimer(), ""]
    lines.append(f"Total Packs: {summary.get('total_packs', 0)}")
    if prompts_df is not None and not prompts_df.empty:
        lines.append("")
        lines.append(prompts_df.to_markdown(index=False))
    return "\n".join(lines)

def build_productivity_checklist_markdown_report(summary: dict, checklist_df: pd.DataFrame | None = None) -> str:
    lines = ["# Productivity Checklist Report", "", build_ux_disclaimer(), ""]
    lines.append(f"Passed: {summary.get('passed', False)}")
    lines.append(f"Score: {summary.get('score', 0.0):.2f}")
    if checklist_df is not None and not checklist_df.empty:
        lines.append("")
        lines.append(checklist_df.to_markdown(index=False))
    return "\n".join(lines)

def build_task_board_markdown_report(summary: dict, task_df: pd.DataFrame | None = None) -> str:
    lines = ["# Analyst Task Board Report", "", build_ux_disclaimer(), ""]
    lines.append(f"Total Tasks: {summary.get('count', 0)}")
    if task_df is not None and not task_df.empty:
        lines.append("")
        lines.append(task_df.to_markdown(index=False))
    return "\n".join(lines)

def build_operator_productivity_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    lines = ["# Operator Productivity Status Report", "", build_ux_disclaimer(), ""]
    lines.append(f"Passed: {summary.get('passed', False)}")
    if status_df is not None and not status_df.empty:
        lines.append("")
        lines.append(status_df.to_markdown(index=False))
    return "\n".join(lines)
