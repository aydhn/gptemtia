import pandas as pd
from pathlib import Path
from .packaging_config import LocalDistributionPackagingProfile

def build_packaging_governance_binder_sections(project_root: Path, profile: LocalDistributionPackagingProfile) -> list[dict]:
    return [
        {"title": "Packaging governance amaci", "content": "Governance of local packaging."},
        {"title": "Bu binder ne degildir?", "content": "Official packaging policy degildir."},
        {"title": "Distribution bundle recap", "content": "Recap"},
        {"title": "Portable docs recap", "content": "Recap"},
        {"title": "Release folder manifest recap", "content": "Recap"},
        {"title": "ZIP-map recap", "content": "Recap"},
        {"title": "Criteria/evidence recap", "content": "Recap"},
        {"title": "Issue/unresolved recap", "content": "Recap"},
        {"title": "Handoff checklist recap", "content": "Recap"},
        {"title": "Source/output/command maps recap", "content": "Recap"},
        {"title": "No-go/safe-go recap", "content": "Recap"},
        {"title": "Exceptions/gaps/risks recap", "content": "Recap"},
        {"title": "Final boundary statement", "content": "Not investment advice."}
    ]

def build_final_packaging_governance_binder(project_root: Path, profile: LocalDistributionPackagingProfile) -> tuple[str, dict]:
    sections = build_packaging_governance_binder_sections(project_root, profile)
    text = "\n\n".join([f"## {s['title']}\n{s['content']}" for s in sections])
    text = f"# Final Packaging Governance Binder\n\n{text}"
    return text, summarize_packaging_governance_binder(text)

def summarize_packaging_governance_binder(text: str) -> dict:
    return {"status": "generated", "length": len(text)}
