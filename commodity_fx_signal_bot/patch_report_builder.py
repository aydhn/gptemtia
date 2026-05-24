import re
from pathlib import Path

# Add the new functions to reports/report_builder.py
file_path = Path("reports/report_builder.py")
content = file_path.read_text()

if "build_research_backlog_text_report" not in content:
    append_text = """

# Phase 48: Research Planning
def build_research_backlog_text_report(summary: dict, backlog_df: pd.DataFrame | None = None) -> str:
    from research_planning.planning_report_builder import build_research_planning_disclaimer
    text = "=== Research Backlog Report ===\\n"
    text += build_research_planning_disclaimer()
    text += f"Total Tasks: {summary.get('total_tasks', 0)}\\n"
    return text

def build_priority_scoring_text_report(summary: dict, priority_df: pd.DataFrame | None = None) -> str:
    from research_planning.planning_report_builder import build_research_planning_disclaimer
    text = "=== Priority Scoring Report ===\\n"
    text += build_research_planning_disclaimer()
    text += f"Average Score: {summary.get('average_score', 0.0):.2f}\\n"
    return text

def build_next_best_experiment_text_report(summary: dict, next_best_df: pd.DataFrame | None = None) -> str:
    from research_planning.planning_report_builder import build_research_planning_disclaimer
    text = "=== Next Best Experiment Report ===\\n"
    text += build_research_planning_disclaimer()
    text += f"Total Recommendations: {summary.get('total', 0)}\\n"
    return text

def build_research_debt_text_report(summary: dict, debt_df: pd.DataFrame | None = None) -> str:
    from research_planning.planning_report_builder import build_research_planning_disclaimer
    text = "=== Research Debt Report ===\\n"
    text += build_research_planning_disclaimer()
    text += f"Total Debt Items: {summary.get('total_debt_items', 0)}\\n"
    return text

def build_roadmap_health_text_report(summary: dict, roadmap_snapshot: dict | None = None) -> str:
    from research_planning.planning_report_builder import build_research_planning_disclaimer
    text = "=== Roadmap Health Report ===\\n"
    text += build_research_planning_disclaimer()
    text += f"Status: {summary.get('roadmap_status', 'Unknown')}\\n"
    text += f"Health Score: {summary.get('roadmap_health_score', 0.0):.2f}\\n"
    return text

def build_research_planning_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    from research_planning.planning_report_builder import build_research_planning_disclaimer
    text = "=== Research Planning Status Report ===\\n"
    text += build_research_planning_disclaimer()
    text += f"Total Files: {summary.get('total_files', 0)}\\n"
    return text
"""
    content += append_text
    file_path.write_text(content)
    print("Updated reports/report_builder.py")
