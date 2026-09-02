from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile
from .briefing_models import DecisionQuestion, build_decision_question_id

def build_decision_question_registry(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    questions = [
        ("Bu platform hangi amacla kullanilabilir?", "Offline arastirma", "decision_context_informational"),
        ("Canli trade yapiyor mu?", "Hayir, kesinlikle engellenmistir", "decision_context_no_go_related"),
        ("Yatirim tavsiyesi uretir mi?", "Hayir, uretilenler analizdir", "decision_context_no_go_related"),
        ("Uretim ortamina hazir mi?", "Hayir, offline test asamasindadir", "decision_context_no_go_related"),
        ("Hangi ciktilar karar destek niteligindedir?", "Raporlar ve metadata", "decision_context_informational"),
        ("Hangi alanlar manuel review gerektirir?", "Tum islem kararlari", "decision_context_manual_review"),
        ("Paydaslar hangi raporlari okumali?", "Executive Summary ve One-Pager", "decision_context_informational"),
        ("Sonraki guvenli gelistirme adimi nedir?", "Local model tuning", "decision_context_safe_next_step"),
        ("Hangi no-go kosullari var?", "Harici cloud/LLM kullanimi veya broker entegrasyonu", "decision_context_no_go_related")
    ]
    
    out = []
    for q, a, label in questions:
        out.append(DecisionQuestion(
            question_id=build_decision_question_id(q),
            question=q,
            context_label=label,
            evidence_sources=["DataLake", "Reports"],
            safe_response=a,
            warnings=["Yatirim karari uretmez"]
        ))
        
    df = pd.DataFrame([vars(x) for x in out])
    return df, summarize_decision_context(df)

def build_decision_context_matrix(question_df: pd.DataFrame, profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    df = question_df.copy()
    df["action"] = df["context_label"].apply(lambda x: "Review" if "manual_review" in x else "Inform")
    return df, {"rows": len(df)}

def build_decision_context_binder(project_root: Path, profile: LocalBriefingProfile) -> tuple[str, dict]:
    q_df, _ = build_decision_question_registry(profile)
    
    text = "# Decision-Context Binder\n\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\n\n"
    
    for _, row in q_df.iterrows():
        text += f"## {row['question']}\n"
        text += f"**Cevap:** {row['safe_response']}\n"
        text += f"**Baglam:** {row['context_label']}\n\n"
        
    return text, {"length": len(text)}

def summarize_decision_context(matrix_df: pd.DataFrame) -> dict:
    if matrix_df is None or matrix_df.empty:
        return {"total_questions": 0}
    return {"total_questions": len(matrix_df)}
