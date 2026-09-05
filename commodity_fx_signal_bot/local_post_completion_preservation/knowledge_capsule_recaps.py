from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def build_knowledge_capsule_quickstart_recap(profile: LocalPostCompletionPreservationProfile) -> tuple[str, dict]:
    return "Quickstart: no advice", {"len": 1}

def build_knowledge_capsule_command_recap(profile: LocalPostCompletionPreservationProfile) -> tuple[str, dict]:
    return "Command: no advice", {"len": 1}

def build_knowledge_capsule_output_recap(profile: LocalPostCompletionPreservationProfile) -> tuple[str, dict]:
    return "Output: no advice", {"len": 1}

def build_knowledge_capsule_safety_recap(profile: LocalPostCompletionPreservationProfile) -> tuple[str, dict]:
    return "Safety: no advice", {"len": 1}

def build_knowledge_capsule_maintenance_recap(profile: LocalPostCompletionPreservationProfile) -> tuple[str, dict]:
    return "Maintenance: no advice", {"len": 1}

def build_knowledge_capsule_risk_recap(profile: LocalPostCompletionPreservationProfile) -> tuple[str, dict]:
    return "Risk: no advice", {"len": 1}

def summarize_knowledge_capsule_recaps(recaps: dict[str, str]) -> dict:
    return {"keys": list(recaps.keys())}
