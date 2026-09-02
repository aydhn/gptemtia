import pandas as pd

def build_simplification_disclaimer() -> str:
    return "Bu rapor offline/local modular simplification ve maintainability rehearsal ciktisidir; gercek refactor, dosya silme/tasima, production cleanup, compliance sertifikasi, canli sinyal, broker talimati, model deployment veya yatirim tavsiyesi degildir.\n"

def build_simplification_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return "# Simplification Domain Registry\n\n" + build_simplification_disclaimer()

def build_final_modular_complexity_map_markdown_report(summary: dict, complexity_df: pd.DataFrame | None = None) -> str:
    return "# Final Modular Complexity Map\n\n" + build_simplification_disclaimer()

def build_optional_slimming_plan_markdown_report(summary: dict, plan_df: pd.DataFrame | None = None) -> str:
    return "# Optional Slimming Plan\n\n" + build_simplification_disclaimer()

def build_repo_ergonomics_markdown_report(summary: dict, guide_text: str | None = None) -> str:
    return "# Repo Ergonomics\n\n" + build_simplification_disclaimer()

def build_maintainability_seed_markdown_report(summary: dict, seed_text: str | None = None) -> str:
    return "# Maintainability Seed\n\n" + build_simplification_disclaimer()

def build_simplification_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return "# Simplification Quality\n\n" + build_simplification_disclaimer()

def build_simplification_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return "# Simplification Status\n\n" + build_simplification_disclaimer()
