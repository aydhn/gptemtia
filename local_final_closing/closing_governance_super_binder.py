import pandas as pd
from pathlib import Path
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def build_closing_governance_super_binder_sections(project_root: Path, profile: LocalFinalClosingProfile) -> list[dict]:
    return [
        {"title": "Super-binder amacı", "content": "Super binder amacı."},
        {"title": "Bu super-binder ne değildir?", "content": "Official acceptance değildir, production approval değildir, legal/compliance proof değildir. Yatırım tavsiyesi yok."},
        {"title": "Final master terminal lock recap", "content": "Terminal lock recap."},
        {"title": "Ultimate offline project constitution recap", "content": "Constitution recap."},
        {"title": "Final non-production seal recap", "content": "Non-production seal recap."},
        {"title": "Local-only terminal archive index recap", "content": "Archive index recap."},
        {"title": "Final criteria/evidence recap", "content": "Criteria and evidence recap."},
        {"title": "Final issue/unresolved recap", "content": "Issues recap."},
        {"title": "Final checklists recap", "content": "Checklists recap."},
        {"title": "Final no-go/safe-go recap", "content": "No-go/safe-go recap."},
        {"title": "Final exception/gap/risk recap", "content": "Exception/gap/risk recap."},
        {"title": "Final readiness recap", "content": "Readiness recap."},
        {"title": "Final validation/quality recap", "content": "Validation/quality recap."},
        {"title": "Closing statement", "content": "Closing statement."},
        {"title": "Final boundary statement", "content": "Bu rapor offline/local final closing governance ve non-production seal rehearsal çıktısıdır; gerçek project lock, official constitution, official seal, official acceptance, legal/compliance approval, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."}
    ]

def build_closing_governance_super_binder(project_root: Path, profile: LocalFinalClosingProfile) -> tuple[str, dict]:
    sections = build_closing_governance_super_binder_sections(project_root, profile)
    lines = ["# Closing Governance Super-Binder\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    text = "\n".join(lines)
    return text, summarize_closing_governance_super_binder(text)

def summarize_closing_governance_super_binder(text: str) -> dict:
    return {"length": len(text)}
