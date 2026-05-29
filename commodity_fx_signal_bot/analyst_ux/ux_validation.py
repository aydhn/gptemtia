import pandas as pd
from .ux_config import AnalystUXProfile

def validate_alias_registry(aliases_df: pd.DataFrame, profile: AnalystUXProfile) -> dict:
    if aliases_df.empty: return {"passed": False, "reason": "empty"}
    if not {"alias_id", "command", "safety_label"}.issubset(aliases_df.columns):
        return {"passed": False, "reason": "missing_columns"}
    blocked = aliases_df["safety_label"].str.startswith("blocked").sum()
    return {"passed": blocked == 0, "blocked_count": blocked}

def validate_intent_table(intent_df: pd.DataFrame, profile: AnalystUXProfile) -> dict:
    if intent_df.empty: return {"passed": False, "reason": "empty"}
    return {"passed": True}

def validate_command_suggestions(suggestions_df: pd.DataFrame, profile: AnalystUXProfile) -> dict:
    if suggestions_df.empty: return {"passed": False, "reason": "empty"}
    blocked = suggestions_df["safety_label"].str.startswith("blocked").sum()
    return {"passed": blocked == 0, "blocked_count": blocked}

def validate_prompt_packs(prompts_df: pd.DataFrame, profile: AnalystUXProfile) -> dict:
    if prompts_df.empty: return {"passed": False, "reason": "empty"}
    # Check if warnings contain disclaimer
    has_disclaimer = prompts_df["warnings"].apply(lambda w: "offline" in str(w).lower() or "yatırım" in str(w).lower()).all()
    return {"passed": has_disclaimer}

def validate_workflow_shortcuts(shortcuts_df: pd.DataFrame, profile: AnalystUXProfile) -> dict:
    if shortcuts_df.empty: return {"passed": False, "reason": "empty"}
    return {"passed": True}

def build_ux_validation_report(tables: dict[str, pd.DataFrame], profile: AnalystUXProfile) -> tuple[pd.DataFrame, dict]:
    results = [
        {"component": "alias_registry", **validate_alias_registry(tables.get("aliases", pd.DataFrame()), profile)},
        {"component": "intent_table", **validate_intent_table(tables.get("intents", pd.DataFrame()), profile)},
        {"component": "command_suggestions", **validate_command_suggestions(tables.get("suggestions", pd.DataFrame()), profile)},
        {"component": "prompt_packs", **validate_prompt_packs(tables.get("prompts", pd.DataFrame()), profile)},
        {"component": "workflow_shortcuts", **validate_workflow_shortcuts(tables.get("shortcuts", pd.DataFrame()), profile)}
    ]
    df = pd.DataFrame(results)
    passed = df["passed"].all() if not df.empty else False
    return df, {"passed": passed, "total": len(df), "passed_count": df["passed"].sum()}
