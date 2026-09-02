import pandas as pd
from local_acceptance.acceptance_config import LocalAcceptanceProfile
from local_acceptance.acceptance_models import ReviewerQuestion, build_reviewer_question_id, reviewer_question_to_dict

def build_default_reviewer_questions(profile: LocalAcceptanceProfile) -> list[ReviewerQuestion]:
    qs = [
        "Sistem ne yapar?",
        "Sistem ne yapmaz?",
        "Canlı emir gönderiyor mu?",
        "Broker entegrasyonu var mı?",
        "Yatırım tavsiyesi üretiyor mu?",
        "Production release mi?",
        "Hangi evidence çıktıları var?",
        "Hangi no-go koşulları var?",
        "Hangi manual review alanları var?",
        "DataLake ve report outputs nasıl doğrulanıyor?",
        "Contract freeze ne anlama gelir?",
        "RC dry-run freeze gerçek RC midir?"
    ]
    out = []
    for q in qs:
        out.append(ReviewerQuestion(
            question_id=build_reviewer_question_id(q),
            question=q,
            domain_label="reviewer_pack_domain",
            expected_evidence=[],
            safe_answer_hint="Sistem canlı işlem yapmaz. Boundary-first.",
            response_label="reviewer_response_ready",
            warnings=["Bu soru yatırım tavsiyesi yönlendirmesi yapmaz."]
        ))
    return out

def classify_reviewer_response_label(question_row: pd.Series, profile: LocalAcceptanceProfile) -> str:
    return "reviewer_response_ready"

def build_reviewer_question_bank(profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    qs = build_default_reviewer_questions(profile)
    df = pd.DataFrame([reviewer_question_to_dict(q) for q in qs])
    return df, summarize_reviewer_questions(df)

def summarize_reviewer_questions(question_df: pd.DataFrame) -> dict:
    return {"total_questions": len(question_df)}
