import pandas as pd
from .runtime_config import AdvancedRuntimeProfile

def build_default_runtime_commands(profile: AdvancedRuntimeProfile) -> pd.DataFrame:
    commands = [
        "python -m scripts.run_advanced_roadmap_registry",
        "python -m scripts.run_post_mvp_functional_reopen",
        "python -m scripts.run_phase_1_100_output_audit",
        "python -m scripts.run_mvp_to_advanced_gap_register",
        "python -m scripts.run_functional_continuation_layer",
        "python -m scripts.run_advanced_continuation_quality_report",
        "python -m scripts.run_advanced_runtime_profile_registry",
        "python -m scripts.run_unified_runtime_context",
        "python -m scripts.run_runtime_contracts",
        "python -m scripts.run_runtime_health_check",
        "python -m scripts.run_runtime_quality_report",
        "python -m scripts.run_runtime_status"
    ]
    data = [{"command": cmd, "safe": True} for cmd in commands]
    return pd.DataFrame(data)

def build_runtime_dry_run_command_contract(profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_runtime_commands(profile)
    return df, summarize_runtime_command_contract(df)

def summarize_runtime_command_contract(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total_commands": len(df)}
