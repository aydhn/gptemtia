import pandas as pd

def build_advanced_config_disclaimer() -> str:
    return "Bu çıktı Phase 104 Advanced Config Profile System raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, production deployment, model deployment, scraping, external LLM/API çağrısı veya official approval değildir."

def build_advanced_config_profile_registry_markdown_report(summary: dict, registry_df: pd.DataFrame = None) -> str:
    return f"# Config Profile Registry\n\n{build_advanced_config_disclaimer()}\n\n" + (registry_df.to_markdown() if registry_df is not None else "No data")

def build_research_mode_preset_markdown_report(summary: dict, preset_df: pd.DataFrame = None) -> str:
    return f"# Research Mode Presets\n\n{build_advanced_config_disclaimer()}\n\n" + (preset_df.to_markdown() if preset_df is not None else "No data")

def build_composed_profile_markdown_report(summary: dict, composed_df: pd.DataFrame = None) -> str:
    return f"# Composed Profiles\n\n{build_advanced_config_disclaimer()}\n\n" + (composed_df.to_markdown() if composed_df is not None else "No data")

def build_profile_compatibility_markdown_report(summary: dict, compatibility_df: pd.DataFrame = None) -> str:
    return f"# Profile Compatibility\n\n{build_advanced_config_disclaimer()}\n\n" + (compatibility_df.to_markdown() if compatibility_df is not None else "No data")

def build_profile_validation_markdown_report(summary: dict, validation_df: pd.DataFrame = None) -> str:
    return f"# Profile Validation\n\n{build_advanced_config_disclaimer()}\n\n" + (validation_df.to_markdown() if validation_df is not None else "No data")

def build_profile_quality_markdown_report(summary: dict, quality: dict = None) -> str:
    return f"# Profile Quality\n\n{build_advanced_config_disclaimer()}\n\n" + str(quality)

def build_advanced_config_status_markdown_report(summary: dict, status_df: pd.DataFrame = None) -> str:
    return f"# Advanced Config Status\n\n{build_advanced_config_disclaimer()}\n\n" + (status_df.to_markdown() if status_df is not None else "No data")
