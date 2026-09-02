from .usability_config import LocalUsabilityProfile

def build_operator_what_to_run_first_guide(profile: LocalUsabilityProfile) -> tuple[str, dict]:
    return "Status scriptleri", {"length": 15}

def build_operator_what_not_to_run_guide(profile: LocalUsabilityProfile) -> tuple[str, dict]:
    return "Live broker scriptleri", {"length": 20}

def summarize_operator_guides(guides: dict[str, str]) -> dict:
    return {k: len(v) for k, v in guides.items()}
