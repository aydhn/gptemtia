import pandas as pd
from .ux_config import AnalystUXProfile
from .ux_models import AnalystIntent, SafeCommandSuggestion, build_safe_command_suggestion_id
from .intent_classifier import classify_analyst_intent

def _get_safety_label(command: str) -> str:
    cmd_lower = command.lower()
    if any(k in cmd_lower for k in ["live", "real order", "send_order"]):
        return "blocked_live_suggestion"
    if any(k in cmd_lower for k in ["broker", "endpoint", "api keys"]):
        return "blocked_broker_suggestion"
    if any(k in cmd_lower for k in ["deploy", "production scheduler"]):
        return "blocked_deploy_suggestion"
    if any(k in cmd_lower for k in ["daemon", "while true", "server"]):
        return "blocked_daemon_suggestion"
    if "dry-run" in cmd_lower or "dry_run" in cmd_lower:
        return "dry_run_only_suggestion"
    return "safe_offline_suggestion"

def map_intent_to_aliases(intent: AnalystIntent, aliases_df: pd.DataFrame, profile: AnalystUXProfile) -> pd.DataFrame:
    if aliases_df.empty: return pd.DataFrame()

    # Simple mapping based on intent to alias mapping
    # E.g. status_check_intent matches status_alias
    type_mapping = {
        "status_check_intent": "status_alias",
        "report_generation_intent": "report_alias",
        "knowledge_query_intent": "query_alias",
        "documentation_lookup_intent": "documentation_alias",
        "scenario_demo_intent": "scenario_alias",
        "scenario_regression_intent": "scenario_alias",
        "quality_gate_intent": "quality_alias",
        "maintenance_intent": "maintenance_alias"
    }
    target_type = type_mapping.get(intent.intent_label, "unknown_alias")

    mapped = aliases_df[aliases_df["alias_type"] == target_type].copy()
    if len(mapped) > profile.max_command_suggestions:
        mapped = mapped.head(profile.max_command_suggestions)
    return mapped

def build_safe_command_suggestions(query_text: str, aliases_df: pd.DataFrame, profile: AnalystUXProfile) -> tuple[pd.DataFrame, dict]:
    intent = classify_analyst_intent(query_text, profile)
    mapped_aliases = map_intent_to_aliases(intent, aliases_df, profile)

    suggestions = []
    rank = 1
    for _, row in mapped_aliases.iterrows():
        command = row["command"]
        if "<query>" in command:
            command = command.replace("<query>", query_text)

        safety = _get_safety_label(command)
        # Skip blocked in safe list
        if safety.startswith("blocked"):
            continue

        sugg = SafeCommandSuggestion(
            suggestion_id=build_safe_command_suggestion_id(query_text, command),
            query_text=query_text,
            intent_label=intent.intent_label,
            command_alias_id=row["alias_id"],
            command=command,
            description=row["description"],
            safety_label=safety,
            rank=rank,
            confidence=intent.confidence,
            warnings=[]
        )
        suggestions.append(sugg)
        rank += 1

    df = pd.DataFrame([s.__dict__ for s in suggestions])
    return df, {"intent": intent.intent_label, "count": len(suggestions)}

def rank_command_suggestions(suggestions_df: pd.DataFrame) -> pd.DataFrame:
    if suggestions_df.empty: return suggestions_df
    return suggestions_df.sort_values(by="rank")

def validate_suggestion_safety(suggestion_df: pd.DataFrame, profile: AnalystUXProfile) -> dict:
    if suggestion_df.empty: return {"passed": True, "blocked_count": 0}
    blocked_count = suggestion_df["safety_label"].str.startswith("blocked").sum()
    return {"passed": blocked_count == 0, "blocked_count": blocked_count}

def summarize_command_suggestions(suggestions_df: pd.DataFrame) -> dict:
    if suggestions_df.empty: return {"count": 0}
    return {"count": len(suggestions_df), "commands": suggestions_df["command"].tolist()}
