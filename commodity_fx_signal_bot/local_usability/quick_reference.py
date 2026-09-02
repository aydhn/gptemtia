from .usability_config import LocalUsabilityProfile

def build_quick_reference_sections(profile: LocalUsabilityProfile) -> list[dict]:
    return [{"title": "Quick Ref", "content": "No live broker."}]

def build_usability_quick_reference_card(profile: LocalUsabilityProfile) -> tuple[str, dict]:
    sections = build_quick_reference_sections(profile)
    return "No live broker.", {"sections": len(sections)}

def summarize_quick_reference_card(text: str) -> dict:
    return {"length": len(text)}
