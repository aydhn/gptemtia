import pandas as pd
from .ux_config import AnalystUXProfile

def _build_shortcut(id_: str, name: str, purpose: str, aliases: list, commands: list, outputs: list) -> dict:
    return {
        "shortcut_id": id_,
        "name": name,
        "purpose": purpose,
        "aliases": aliases,
        "commands": commands,
        "expected_outputs": outputs,
        "safety_notes": "No live execution.",
        "warnings": ["Sadece plan ve rehber üretir. Otomatik execution yapmaz."]
    }

def build_daily_offline_review_shortcut(profile: AnalystUXProfile) -> dict:
    return _build_shortcut("sh_daily_review", "Daily Offline Review", "Review end of day reports", ["status:final"], ["python -m scripts.run_final_review_status"], ["Status output"])

def build_weekly_quality_review_shortcut(profile: AnalystUXProfile) -> dict:
    return _build_shortcut("sh_weekly_quality", "Weekly Quality", "Check code quality", ["quality:check"], ["python -m scripts.run_static_safety_scan"], ["Quality output"])

def build_scenario_demo_shortcut(profile: AnalystUXProfile) -> dict:
    return _build_shortcut("sh_scenario_demo", "Scenario Demo", "Run demo scenario", ["demo:scenario"], ["python -m scripts.run_end_to_end_demo_report"], ["Demo output"])

def build_regression_check_shortcut(profile: AnalystUXProfile) -> dict:
    return _build_shortcut("sh_regression_check", "Regression Check", "Check regressions", ["regression:demo"], ["python -m scripts.run_demo_acceptance_report"], ["Regression output"])

def build_final_review_shortcut(profile: AnalystUXProfile) -> dict:
    return _build_shortcut("sh_final_review", "Final Review", "Run final review", ["report:final"], ["python -m scripts.run_final_system_review"], ["Final review output"])

def build_maintenance_review_shortcut(profile: AnalystUXProfile) -> dict:
    return _build_shortcut("sh_maintenance", "Maintenance Review", "Check maintenance status", ["report:maintenance"], ["python -m scripts.run_storage_lifecycle_report"], ["Maintenance output"])

def build_documentation_refresh_shortcut(profile: AnalystUXProfile) -> dict:
    return _build_shortcut("sh_docs_refresh", "Docs Refresh", "Refresh docs", ["docs:pack"], ["python -m scripts.run_documentation_pack_report"], ["Docs output"])

def build_default_workflow_shortcuts(profile: AnalystUXProfile) -> tuple[pd.DataFrame, dict]:
    shortcuts = [
        build_daily_offline_review_shortcut(profile),
        build_weekly_quality_review_shortcut(profile),
        build_scenario_demo_shortcut(profile),
        build_regression_check_shortcut(profile),
        build_final_review_shortcut(profile),
        build_maintenance_review_shortcut(profile),
        build_documentation_refresh_shortcut(profile)
    ]
    df = pd.DataFrame(shortcuts)
    return df, {"count": len(shortcuts)}
