import pandas as pd
from pathlib import Path
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def build_non_production_seal_sections(profile: LocalFinalClosingProfile) -> list[dict]:
    return [
        {"title": "Non-production seal amacı", "content": "Non-production seal rehearsal amacı."},
        {"title": "Bu seal ne değildir?", "content": "Bu seal official seal değildir. Official production approval, legal sign-off, compliance approval, broker readiness, live trading approval, release approval, build attestation, investment advice, official acceptance değildir."},
        {"title": "Criteria overview", "content": "Criteria for seal rehearsal."},
        {"title": "Boundary overview", "content": "Boundary of seal rehearsal."},
        {"title": "Non-seal statement", "content": "This is a non-seal statement."},
        {"title": "Limitation overview", "content": "Limitations overview."},
        {"title": "Manual review ledger overview", "content": "Manual review ledger."},
        {"title": "No-go/safe-go recap", "content": "No-go/safe-go recap."},
        {"title": "Final boundary statement", "content": "Bu rapor offline/local final closing governance ve non-production seal rehearsal çıktısıdır; gerçek project lock, official constitution, official seal, official acceptance, legal/compliance approval, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."}
    ]

def build_final_non_production_seal_rehearsal(project_root: Path, profile: LocalFinalClosingProfile) -> tuple[str, dict]:
    sections = build_non_production_seal_sections(profile)
    lines = ["# Final Non-Production Seal Rehearsal\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    text = "\n".join(lines)
    return text, summarize_non_production_seal(text)

def summarize_non_production_seal(text: str) -> dict:
    return {"length": len(text)}
