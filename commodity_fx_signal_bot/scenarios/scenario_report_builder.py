"""
Markdown report builders for scenarios.
"""

import pandas as pd


def build_scenario_disclaimer() -> str:
    """Returns the mandatory disclaimer for all scenario reports."""
    return (
        "**DISCLAIMER**: Bu rapor offline controlled research scenario/demo çıktısıdır; "
        "gerçek emir, canlı sinyal, model deployment, broker talimatı, production scheduler "
        "veya yatırım tavsiyesi değildir."
    )


def build_scenario_registry_markdown_report(summary: dict, scenarios_df: pd.DataFrame = None) -> str:
    """Builds a markdown report for the scenario registry."""
    lines = [
        "# Scenario Registry Report",
        "",
        build_scenario_disclaimer(),
        "",
        "## Summary",
        f"- **Total Scenarios**: {summary.get('total_scenarios', 0)}"
    ]

    if "by_type" in summary:
        lines.append("\n### By Type")
        for k, v in summary["by_type"].items():
            lines.append(f"- {k}: {v}")

    if scenarios_df is not None and not scenarios_df.empty:
        lines.append("\n## Scenarios")
        lines.append(scenarios_df[["scenario_name", "scenario_type", "safety_label"]].to_markdown(index=False))

    return "\n".join(lines)


def build_sample_data_markdown_report(summary: dict, sample_df: pd.DataFrame = None) -> str:
    """Builds a markdown report for sample data."""
    lines = [
        "# Sample Data Builder Report",
        "",
        build_scenario_disclaimer(),
        "",
        "## Summary",
        f"- **Files Saved**: {summary.get('files_saved', 0)}",
        f"- **Output Dir**: {summary.get('output_dir', 'N/A')}",
        ""
    ]

    if sample_df is not None and not sample_df.empty:
        lines.append("## Generated Series")
        lines.append(sample_df[["series_name", "rows", "synthetic"]].to_markdown(index=False))

    return "\n".join(lines)


def build_scenario_dry_run_markdown_report(summary: dict, dry_run_df: pd.DataFrame = None) -> str:
    """Builds a markdown report for dry runs."""
    lines = [
        "# Scenario Dry Run Report",
        "",
        build_scenario_disclaimer(),
        "",
        "## Summary",
        f"- **Total Runs**: {summary.get('total_runs', 0)}",
        f"- **Passed Runs**: {summary.get('passed_runs', summary.get('passed', 0))}",
        ""
    ]

    if dry_run_df is not None and not dry_run_df.empty:
        lines.append("## Execution Results")
        # Handle columns safely if they exist
        cols_to_show = ["scenario_name", "status", "validation_passed"]
        cols = [c for c in cols_to_show if c in dry_run_df.columns]
        if cols:
            lines.append(dry_run_df[cols].to_markdown(index=False))

    return "\n".join(lines)


def build_case_study_markdown_report(summary: dict, case_df: pd.DataFrame = None) -> str:
    """Builds a markdown report for case studies."""
    lines = [
        "# Case Studies Report",
        "",
        build_scenario_disclaimer(),
        "",
        "## Summary",
        f"- **Total Case Studies**: {summary.get('total', len(case_df) if case_df is not None else 0)}",
        ""
    ]

    if case_df is not None and not case_df.empty:
        for _, row in case_df.iterrows():
            lines.append(f"### {row.get('title', 'Unknown')}")
            lines.append(f"**Objective**: {row.get('objective', '')}")
            lines.append(f"**Learning**: {row.get('expected_learning', '')}\n")

    return "\n".join(lines)


def build_demo_workflow_markdown_report(summary: dict, workflow_df: pd.DataFrame = None) -> str:
    """Builds a markdown report for demo workflows."""
    lines = [
        "# Demo Workflow Packs Report",
        "",
        build_scenario_disclaimer(),
        "",
        "## Summary",
        f"- **Total Packs**: {summary.get('total_packs', 0)}",
        ""
    ]

    if workflow_df is not None and not workflow_df.empty:
        lines.append("## Workflows")
        cols = [c for c in ["workflow_name", "scenario_type", "objective"] if c in workflow_df.columns]
        if cols:
            lines.append(workflow_df[cols].to_markdown(index=False))

    return "\n".join(lines)


def build_end_to_end_demo_markdown_report(summary: dict, plan_df: pd.DataFrame = None) -> str:
    """Builds a markdown report for end-to-end demo plan."""
    lines = [
        "# End-to-End Demo Plan Report",
        "",
        build_scenario_disclaimer(),
        "",
        "## Summary",
        f"- **Total Steps**: {summary.get('total_steps', 0)}",
        ""
    ]

    if plan_df is not None and not plan_df.empty:
        lines.append("## Execution Plan")
        lines.append(plan_df[["step", "action", "command"]].to_markdown(index=False))

    return "\n".join(lines)


def build_scenario_status_markdown_report(summary: dict, status_df: pd.DataFrame = None) -> str:
    """Builds a markdown report for scenario status."""
    lines = [
        "# Scenario Status Report",
        "",
        build_scenario_disclaimer(),
        "",
        "## Status Summary",
        f"- **Total Components**: {summary.get('total_components', 0)}",
        ""
    ]

    if status_df is not None and not status_df.empty:
        lines.append("## Components")
        lines.append(status_df.to_markdown(index=False))

    return "\n".join(lines)
