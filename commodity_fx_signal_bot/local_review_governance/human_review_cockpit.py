from pathlib import Path
import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile
from local_review_governance.review_models import HumanReviewItem, build_human_review_item_id, human_review_item_to_dict

def build_human_review_cockpit_sections(project_root: Path, profile: LocalReviewGovernanceProfile) -> list[dict]:
    return [
        {"title": "Amac ve Kapsam", "content": "Offline/local human-review cockpit for manual review rehearsal."},
        {"title": "Bu cockpit ne degildir?", "content": "Gercek approval workflow degildir. Yatirim tavsiyesi degildir."},
        {"title": "Review Alanlari", "content": "Safety, Quality, Governance, Architecture"},
        {"title": "Ilk Okunacak Ciktilar", "content": "Index, Route Map, Status Matrix"},
        {"title": "Kritik Sinirlar", "content": "No real trading, no official sign-off."},
        {"title": "Manual Review Rotasi", "content": "Review safety first, then quality."},
        {"title": "Expert Review Rotasi", "content": "Check evidence map, then workbook."},
        {"title": "Approval Ledger Rehearsal Ozeti", "content": "Manual review required for all."},
        {"title": "Reviewer Console Ozeti", "content": "Dashboard degildir, offline console."},
        {"title": "No-Go / Safe-Go Ozeti", "content": "Safe-go if manual review complete. No real deploy."},
        {"title": "Final Boundary Statement", "content": "No legal, compliance or production approval claim."}
    ]

def build_final_local_human_review_cockpit(project_root: Path, profile: LocalReviewGovernanceProfile) -> tuple[str, dict]:
    sections = build_human_review_cockpit_sections(project_root, profile)
    lines = ["# Final Local Human-Review Cockpit\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    text = "\n".join(lines)
    summary = summarize_human_review_cockpit(text)
    return text, summary

def summarize_human_review_cockpit(text: str) -> dict:
    return {"length": len(text), "sections": text.count("## ")}

def build_human_review_cockpit_index(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    data = [{"index_id": "hr_idx_1", "name": "Cockpit Index", "path": "cockpit_index.csv", "status": "review_rehearsal_ready"}]
    df = pd.DataFrame(data)
    return df, summarize_human_review_cockpit_index(df)

def summarize_human_review_cockpit_index(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
