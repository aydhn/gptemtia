from .completion_config import LocalProjectCompletionProfile

def build_final_safe_usage_recap(profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    text = "Safe usage: Local run only. No investment advice."
    return text, {"note": "Recap is not official sign-off."}

def build_final_no_go_safe_go_recap(profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    text = "No-go: Live trading. Safe-go: Offline tests."
    return text, {"note": "Recap is not official sign-off."}

def build_final_architecture_recap(profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    text = "Architecture is offline local."
    return text, {"note": "Recap is not official sign-off."}

def build_final_quality_recap(profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    text = "Quality is local rehearsal level."
    return text, {"note": "Recap is not official sign-off."}

def build_final_safety_boundary_recap(profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    text = "Safety boundary: Local filesystem."
    return text, {"note": "Recap is not official sign-off."}

def build_final_maintenance_recap(profile: LocalProjectCompletionProfile) -> tuple[str, dict]:
    text = "Maintenance is local."
    return text, {"note": "Recap is not official sign-off."}

def summarize_final_recaps(recaps: dict[str, str]) -> dict:
    return {"recaps": len(recaps), "note": "Recaps have boundary statements."}
