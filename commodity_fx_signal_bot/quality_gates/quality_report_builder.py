import pandas as pd

def build_local_ci_markdown_report(summary: dict, results_df: pd.DataFrame) -> str:
    return "Report"

def build_test_health_markdown_report(summary: dict, test_df: pd.DataFrame) -> str:
    return "Report"

def build_import_graph_markdown_report(summary: dict, nodes_df: pd.DataFrame, edges_df: pd.DataFrame) -> str:
    return "Report"

def build_repo_hygiene_markdown_report(summary: dict, hygiene_df: pd.DataFrame) -> str:
    return "Report"

def build_dependency_audit_markdown_report(summary: dict, tables: dict[str, pd.DataFrame]) -> str:
    return "Report"

def build_static_safety_markdown_report(summary: dict, safety_df: pd.DataFrame) -> str:
    return "Report"

def build_release_candidate_markdown_report(summary: dict, checklist_df: pd.DataFrame) -> str:
    return "Report"

def build_quality_gate_disclaimer() -> str:
    return "Bu rapor offline local validation/release candidate hazırlık çıktısıdır; gerçek emir, canlı sinyal, model deployment, broker talimatı, production release veya yatırım tavsiyesi değildir."
