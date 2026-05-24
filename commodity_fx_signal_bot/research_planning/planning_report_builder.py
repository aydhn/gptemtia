import pandas as pd

def build_research_planning_disclaimer() -> str:
    return "\n> UYARI: Bu rapor offline research planning/backlog çıktısıdır; gerçek emir, canlı sinyal, model deployment, broker talimatı veya yatırım tavsiyesi değildir.\n"

def build_research_backlog_markdown_report(summary: dict, backlog_df: pd.DataFrame) -> str:
    md = "# Research Backlog Report\n"
    md += build_research_planning_disclaimer()
    md += f"\nTotal Tasks: {summary.get('total_tasks', 0)}\n"
    return md

def build_priority_scoring_markdown_report(summary: dict, priority_df: pd.DataFrame) -> str:
    md = "# Priority Scoring Report\n"
    md += build_research_planning_disclaimer()
    md += f"\nAverage Score: {summary.get('average_score', 0.0):.2f}\n"
    return md

def build_next_best_experiment_markdown_report(summary: dict, next_best_df: pd.DataFrame) -> str:
    md = "# Next Best Experiment Report\n"
    md += build_research_planning_disclaimer()
    md += f"\nTotal Recommendations: {summary.get('total', 0)}\n"
    return md

def build_research_debt_markdown_report(summary: dict, debt_df: pd.DataFrame) -> str:
    md = "# Research Debt Report\n"
    md += build_research_planning_disclaimer()
    md += f"\nTotal Debt Items: {summary.get('total_debt_items', 0)}\n"
    return md

def build_roadmap_health_markdown_report(summary: dict, roadmap_df: pd.DataFrame | None = None) -> str:
    md = "# Roadmap Health Report\n"
    md += build_research_planning_disclaimer()
    md += f"\nStatus: {summary.get('roadmap_status', 'Unknown')}\n"
    md += f"Health Score: {summary.get('roadmap_health_score', 0.0):.2f}\n"
    return md
