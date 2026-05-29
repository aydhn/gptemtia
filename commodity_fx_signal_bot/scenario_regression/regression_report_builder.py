import pandas as pd

def build_regression_disclaimer() -> str:
    return (
        "*** WARNING / UYARI ***\n"
        "Bu rapor offline scenario regression/deterministic replay çıktısıdır; "
        "gerçek emir, canlı sinyal, model deployment, broker talimatı, production scheduler "
        "veya yatırım tavsiyesi değildir.\n"
        "Golden outputlar gerçek piyasa performansı referansı değildir.\n"
        "Snapshot diffler yatırım sinyali değildir.\n"
        "Demo acceptance production acceptance değildir.\n"
        "***\n\n"
    )

def build_regression_registry_markdown_report(summary: dict, regression_df: pd.DataFrame | None = None) -> str:
    md = build_regression_disclaimer()
    md += "# Scenario Regression Registry Report\n\n"
    md += f"Total definitions: {summary.get('total_definitions', 0)}\n\n"
    if regression_df is not None and not regression_df.empty:
        md += regression_df.head(10).to_markdown() + "\n"
    return md

def build_golden_output_markdown_report(summary: dict, golden_df: pd.DataFrame | None = None) -> str:
    md = build_regression_disclaimer()
    md += "# Golden Output Report\n\n"
    md += f"Total golden outputs: {summary.get('total_golden_outputs', 0)}\n\n"
    if golden_df is not None and not golden_df.empty:
        md += golden_df.head(10).to_markdown() + "\n"
    return md

def build_snapshot_comparison_markdown_report(summary: dict, diff_df: pd.DataFrame | None = None) -> str:
    md = build_regression_disclaimer()
    md += "# Snapshot Comparison Report\n\n"
    md += f"Total diffs: {summary.get('total_diffs', 0)}\n\n"
    if diff_df is not None and not diff_df.empty:
        md += diff_df.head(10).to_markdown() + "\n"
    return md

def build_deterministic_replay_markdown_report(summary: dict, replay_df: pd.DataFrame | None = None) -> str:
    md = build_regression_disclaimer()
    md += "# Deterministic Replay Report\n\n"
    md += f"Total replays: {summary.get('total_replays', 0)}\n\n"
    if replay_df is not None and not replay_df.empty:
        md += replay_df.head(10).to_markdown() + "\n"
    return md

def build_demo_acceptance_markdown_report(summary: dict, acceptance_df: pd.DataFrame | None = None) -> str:
    md = build_regression_disclaimer()
    md += "# Demo Acceptance Report\n\n"
    md += f"Score: {summary.get('score', 0)}\n"
    md += f"Label: {summary.get('label', 'unknown')}\n\n"
    if acceptance_df is not None and not acceptance_df.empty:
        md += acceptance_df.to_markdown() + "\n"
    return md

def build_regression_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    md = build_regression_disclaimer()
    md += "# Scenario Regression Status\n\n"
    if status_df is not None and not status_df.empty:
        md += status_df.to_markdown() + "\n"
    return md
