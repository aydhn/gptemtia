import pandas as pd
from typing import Optional

def build_experiment_disclaimer() -> str:
    return (
        "**DISCLAIMER**: Bu çıktı offline experiment tracking/research versioning raporudur. "
        "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, otomatik trade onayı "
        "veya yatırım tavsiyesi değildir.\n\n"
    )

def build_hypothesis_registry_markdown_report(summary: dict, hypothesis_df: pd.DataFrame) -> str:
    md = "# Research Hypothesis Registry\n\n"
    md += build_experiment_disclaimer()

    md += "## Summary\n"
    md += f"- Total Hypotheses: {summary.get('total_hypotheses', 0)}\n"
    md += "\n"

    if not hypothesis_df.empty:
        md += "## Hypothesis List\n"
        # We only output a few columns for brevity in markdown
        cols = ["hypothesis_id", "title", "target_module", "hypothesis_status"]
        if all(c in hypothesis_df.columns for c in cols):
            md += hypothesis_df[cols].to_markdown(index=False)
        else:
            md += hypothesis_df.to_markdown(index=False)

    return md

def build_experiment_tracking_markdown_report(summary: dict, run_df: Optional[pd.DataFrame] = None) -> str:
    md = "# Experiment Tracking Report\n\n"
    md += build_experiment_disclaimer()

    md += "## Summary\n"
    md += f"- Notes: {summary.get('notes', 'No notes.')}\n\n"

    if run_df is not None and not run_df.empty:
        md += "## Run List\n"
        md += run_df.to_markdown(index=False)

    return md

def build_research_version_markdown_report(summary: dict, version_df: Optional[pd.DataFrame] = None) -> str:
    md = "# Research Version Record\n\n"
    md += build_experiment_disclaimer()

    md += "## Summary\n"
    for k, v in summary.items():
        if isinstance(v, dict):
            md += f"- {k}:\n"
            for sub_k, sub_v in v.items():
                md += f"  - {sub_k}: {sub_v}\n"
        else:
            md += f"- {k}: {v}\n"
    md += "\n"

    if version_df is not None and not version_df.empty:
        md += "## Version Records\n"
        md += version_df.to_markdown(index=False)

    return md

def build_ablation_study_markdown_report(summary: dict, ablation_df: Optional[pd.DataFrame] = None) -> str:
    md = "# Ablation Study Results\n\n"
    md += build_experiment_disclaimer()

    md += "## Summary\n"
    md += f"- Total Studies: {summary.get('total_studies', 0)}\n"
    md += f"- Metrics Analyzed: {', '.join(summary.get('metrics_analyzed', []))}\n\n"

    if ablation_df is not None and not ablation_df.empty:
        md += "## Ablation Table\n"
        md += ablation_df.to_markdown(index=False)

    return md

def build_experiment_comparison_markdown_report(summary: dict, comparison_df: Optional[pd.DataFrame] = None) -> str:
    md = "# Experiment Comparison\n\n"
    md += build_experiment_disclaimer()

    md += "## Summary\n"
    md += f"- Total Comparisons: {summary.get('total_comparisons', 0)}\n\n"

    if comparison_df is not None and not comparison_df.empty:
        md += "## Comparison Table\n"
        md += comparison_df.to_markdown(index=False)

    return md

def build_experiment_leaderboard_markdown_report(summary: dict, leaderboard_df: Optional[pd.DataFrame] = None) -> str:
    md = "# Experiment Leaderboard\n\n"
    md += build_experiment_disclaimer()

    md += "## Summary\n"
    md += f"- Total Runs Evaluated: {summary.get('total_runs', 0)}\n"
    md += f"- Top Score: {summary.get('top_score', 'N/A')}\n"
    md += "\n"

    if leaderboard_df is not None and not leaderboard_df.empty:
        md += "## Leaderboard Table\n"
        md += leaderboard_df.to_markdown(index=False)

    return md
