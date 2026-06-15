"""
Metadata Report Builder module.
"""

import pandas as pd

def build_metadata_disclaimer() -> str:
    return (
        "DIKKAT: Bu cikti offline/local research artifact metadata ve card documentation raporudur. "
        "Model deployment, canli emir, broker talimati, gercek pozisyon, resmi sertifika, "
        "production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\n"
    )

def build_research_artifact_inventory_markdown_report(summary: dict, artifact_df: pd.DataFrame | None = None) -> str:
    md = "# Research Artifact Inventory Report\n\n"
    md += build_metadata_disclaimer() + "\n"
    md += f"**Total Artifacts:** {summary.get('total_artifacts', 0)}\n\n"
    md += "## Types\n"
    for t, count in summary.get('types', {}).items():
        md += f"- {t}: {count}\n"
    return md

def build_model_dataset_cards_markdown_report(summary: dict, model_df: pd.DataFrame | None = None, dataset_df: pd.DataFrame | None = None) -> str:
    md = "# Model & Dataset Cards Report\n\n"
    md += build_metadata_disclaimer() + "\n"
    md += f"**Total Model Cards:** {summary.get('total_model_cards', 0)}\n"
    md += f"**Total Dataset Cards:** {summary.get('total_dataset_cards', 0)}\n"
    return md

def build_experiment_reproducibility_cards_markdown_report(summary: dict, experiment_df: pd.DataFrame | None = None, repro_df: pd.DataFrame | None = None) -> str:
    md = "# Experiment & Reproducibility Cards Report\n\n"
    md += build_metadata_disclaimer() + "\n"
    md += f"**Total Experiment Cards:** {summary.get('total_experiment_cards', 0)}\n"
    md += f"**Total Reproducibility Cards:** {summary.get('total_reproducibility_cards', 0)}\n"
    return md

def build_scenario_regression_cards_markdown_report(summary: dict, scenario_df: pd.DataFrame | None = None, regression_df: pd.DataFrame | None = None) -> str:
    md = "# Scenario & Regression Cards Report\n\n"
    md += build_metadata_disclaimer() + "\n"
    md += f"**Total Scenario Cards:** {summary.get('total_scenario_cards', 0)}\n"
    md += f"**Total Regression Cards:** {summary.get('total_regression_cards', 0)}\n"
    return md

def build_metadata_export_markdown_report(summary: dict, export_index_df: pd.DataFrame | None = None) -> str:
    md = "# Metadata Export Report\n\n"
    md += build_metadata_disclaimer() + "\n"
    md += f"**Total Exports:** {summary.get('total_exports', 0)}\n"
    md += f"**Local Only Confirmed:** {summary.get('local_only_confirmed', False)}\n"
    return md

def build_metadata_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    md = "# Metadata Quality Report\n\n"
    md += build_metadata_disclaimer() + "\n"
    if quality:
         md += f"**Passed:** {quality.get('passed', False)}\n"
         md += f"**Warnings:** {quality.get('warning_count', 0)}\n"
         md += f"**No Deployment Claims:** {quality.get('no_deployment_claims_confirmed', False)}\n"
         md += f"**No Investment Advice:** {quality.get('no_investment_advice_confirmed', False)}\n"

         if quality.get("forbidden_terms_found"):
             md += "\n**Forbidden Terms Found:**\n"
             for t in quality["forbidden_terms_found"]:
                 md += f"- {t}\n"
    return md

def build_metadata_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    md = "# Metadata Status Report\n\n"
    md += build_metadata_disclaimer() + "\n"
    md += f"**Status:** Metadata pipeline completed.\n"
    return md
