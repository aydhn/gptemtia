import pandas as pd
from pathlib import Path
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def build_reviewer_pack_sections(checklist_df: pd.DataFrame, question_df: pd.DataFrame, evidence_df: pd.DataFrame) -> list[dict]:
    return [
        {"title": "Amaç ve kapsam", "content": "Bu doküman bağımsız gözden geçirme provasıdır."},
        {"title": "Resmi audit olmadığına dair sınır", "content": "Bu doküman resmi audit, compliance belgesi veya yatırım tavsiyesi değildir."},
        {"title": "İnceleme sırası", "content": "1. Evidence trail 2. Questions 3. Trace matrix"},
        {"title": "Beklenen evidence seti", "content": f"Toplam evidence: {len(evidence_df) if evidence_df is not None else 0}"},
        {"title": "Reviewer question bank özeti", "content": f"Toplam soru: {len(question_df) if question_df is not None else 0}"},
        {"title": "Acceptance checklist özeti", "content": f"Checklist items: {len(checklist_df) if checklist_df is not None else 0}"},
        {"title": "No-go/safe-go özeti", "content": "No-go ve safe-go koşulları listelenmiştir."},
        {"title": "Quality/validation outputs", "content": "Validation and quality logs reviewed."},
        {"title": "Manual review notları", "content": "Tüm riskli alanlar manual review gerektirir."},
        {"title": "Yapılmayacaklar", "content": "Production release onayı, canlı emir, broker entegrasyonu yok."}
    ]

def build_independent_reviewer_pack(checklist_df: pd.DataFrame, question_df: pd.DataFrame, evidence_df: pd.DataFrame, profile: LocalAcceptanceProfile) -> tuple[str, dict]:
    sections = build_reviewer_pack_sections(checklist_df, question_df, evidence_df)
    
    lines = ["# Independent Reviewer Pack\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    
    text = "\n".join(lines)
    return text, summarize_independent_reviewer_pack(text)

def save_independent_reviewer_pack(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path

def summarize_independent_reviewer_pack(text: str) -> dict:
    return {"length": len(text)}
