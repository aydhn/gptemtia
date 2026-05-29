import pandas as pd
from .ux_config import AnalystUXProfile
from .ux_models import AnalystIntent, build_intent_id

def normalize_user_query(query_text: str) -> str:
    return query_text.lower().strip()

def classify_analyst_intent(query_text: str, profile: AnalystUXProfile) -> AnalystIntent:
    q = normalize_user_query(query_text)
    intent_label = "unknown_intent"
    confidence = 0.1
    matched = []
    related = []


    if any(k in q for k in ["regression", "snapshot", "golden output"]):
        intent_label = "scenario_regression_intent"
        confidence = 0.9
        matched.append("regression")
        related.append("scenario_regression")
    elif any(k in q for k in ["demo", "senaryo", "örnek akış"]):
        intent_label = "scenario_demo_intent"
        confidence = 0.8
        matched.append("demo")
        related.append("scenarios")
    elif any(k in q for k in ["durum", "status", "kontrol"]):
        intent_label = "status_check_intent"
        confidence = 0.9
        matched.append("status")
        related.append("status")
    elif any(k in q for k in ["rapor", "üret", "çalıştırılacak komut"]):

        intent_label = "report_generation_intent"
        confidence = 0.85
        matched.append("rapor")
        related.append("reporting")
    elif any(k in q for k in ["ne biliyoruz", "ara", "sorgu"]):
        intent_label = "knowledge_query_intent"
        confidence = 0.8
        matched.append("ara")
        related.append("knowledge_base")
    elif any(k in q for k in ["dokümantasyon", "rehber", "kılavuz"]):
        intent_label = "documentation_lookup_intent"
        confidence = 0.8
        matched.append("dokümantasyon")
        related.append("documentation")
    elif any(k in q for k in ["final review", "audit", "acceptance"]):
        intent_label = "final_review_intent"
        confidence = 0.9
        matched.append("final review")
        related.append("final_review")
    elif any(k in q for k in ["pytest", "quality", "ci", "hata"]):
        if "hata" in q and "troubleshoot" not in q:
            intent_label = "quality_gate_intent"
            matched.append("hata")
        else:
            intent_label = "quality_gate_intent"
            matched.append("quality")
        confidence = 0.8
        related.append("quality_gates")
    elif any(k in q for k in ["cleanup", "archive", "retention"]):
        intent_label = "maintenance_intent"
        confidence = 0.8
        matched.append("cleanup")
        related.append("maintenance")
    elif any(k in q for k in ["performans", "cache", "runtime"]):
        intent_label = "performance_intent"
        confidence = 0.8
        matched.append("performans")
        related.append("performance")
    elif any(k in q for k in ["governance", "lineage"]):
        intent_label = "governance_intent"
        confidence = 0.8
        matched.append("governance")
        related.append("governance")
    elif any(k in q for k in ["experiment", "ablation"]):
        intent_label = "experiment_intent"
        confidence = 0.8
        matched.append("experiment")
        related.append("experiments")
    elif any(k in q for k in ["backlog", "planning"]):
        intent_label = "research_planning_intent"
        confidence = 0.8
        matched.append("backlog")
        related.append("research_planning")
    elif any(k in q for k in ["troubleshoot"]):
        intent_label = "troubleshooting_intent"
        confidence = 0.8
        matched.append("troubleshoot")
        related.append("troubleshooting")

    if confidence < profile.min_intent_confidence:
        intent_label = "unknown_intent"

    return AnalystIntent(
        intent_id=build_intent_id(query_text),
        query_text=query_text,
        intent_label=intent_label,
        confidence=confidence,
        matched_keywords=matched,
        related_modules=related,
        warnings=[]
    )

def extract_query_symbols(query_text: str) -> list[str]:
    # Placeholder for symbol extraction logic (e.g. GC=F)
    if "GC=F" in query_text.upper():
        return ["GC=F"]
    return []

def extract_query_modules(query_text: str) -> list[str]:
    return classify_analyst_intent(query_text, AnalystUXProfile(name="temp", description="temp")).related_modules

def build_intent_examples() -> pd.DataFrame:
    examples = [
        {"query": "final review durumunu kontrol et", "expected_intent": "status_check_intent"},
        {"query": "GC=F için hangi offline raporları çalıştırabilirim", "expected_intent": "report_generation_intent"},
    ]
    return pd.DataFrame(examples)

def summarize_intents(intent_df: pd.DataFrame) -> dict:
    if intent_df is None or intent_df.empty: return {"count": 0}
    return {"count": len(intent_df), "intents": intent_df['intent_label'].unique().tolist()}
