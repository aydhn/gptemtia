import pandas as pd


def build_consistency_check_registry_markdown_report(summary: dict, check_df: pd.DataFrame | None = None) -> str:
    return "# Consistency Check Registry\n" + build_consistency_disclaimer()

def build_cross_layer_consistency_matrix_markdown_report(summary: dict, matrix_df: pd.DataFrame | None = None) -> str:
    return "# Cross-Layer Consistency Matrix\n" + build_consistency_disclaimer()

def build_contradiction_detection_markdown_report(summary: dict, contradiction_df: pd.DataFrame | None = None) -> str:
    return "# Contradiction Detection\n" + build_consistency_disclaimer()

def build_stale_reconciliation_markdown_report(summary: dict, plan_df: pd.DataFrame | None = None) -> str:
    return "# Stale Artifact Reconciliation Plan\n" + build_consistency_disclaimer()

def build_system_coherence_markdown_report(summary: dict, score_df: pd.DataFrame | None = None, findings_df: pd.DataFrame | None = None) -> str:
    return "# System Coherence Report\n" + build_consistency_disclaimer()

def build_consistency_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return "# Consistency Quality Report\n" + build_consistency_disclaimer()

def build_consistency_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return "# Consistency Status Report\n" + build_consistency_disclaimer()

def build_consistency_disclaimer() -> str:
    return "> Bu rapor offline/local consistency ve system coherence çıktısıdır; canlı sinyal, broker talimatı, model deployment, production scheduler, resmi compliance onayı veya yatırım tavsiyesi değildir. Bulgular dry-run denetim ve manuel reconciliation planlama amaçlıdır.\n"
