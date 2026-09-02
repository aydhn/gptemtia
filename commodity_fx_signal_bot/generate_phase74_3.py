import os
from pathlib import Path

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

write_file('local_briefing/decision_context.py', '''
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
    
    text = "# Decision-Context Binder\\n\\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\\n\\n"
    
    for _, row in q_df.iterrows():
        text += f"## {row['question']}\\n"
        text += f"**Cevap:** {row['safe_response']}\\n"
        text += f"**Baglam:** {row['context_label']}\\n\\n"
        
    return text, {"length": len(text)}

def summarize_decision_context(matrix_df: pd.DataFrame) -> dict:
    if matrix_df is None or matrix_df.empty:
        return {"total_questions": 0}
    return {"total_questions": len(matrix_df)}
''')

write_file('local_briefing/capability_map.py', '''
from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_capability_groups(profile: LocalBriefingProfile) -> pd.DataFrame:
    groups = [
        "research reporting", "DataLake storage", "backtest/paper outputs",
        "evidence governance", "artifact metadata", "local graph", "timeline",
        "consistency", "readiness", "maintenance", "archive", "disaster recovery rehearsal",
        "training/onboarding", "briefing/communication"
    ]
    return pd.DataFrame({"capability_group": groups, "status": ["offline_ready"] * len(groups)})

def map_capabilities_to_outputs(project_root: Path, profile: LocalBriefingProfile) -> pd.DataFrame:
    df = build_capability_groups(profile)
    df["outputs"] = df["capability_group"].apply(lambda x: f"reports/output/{x.split('/')[0]}")
    return df

def build_capability_map_nontechnical(project_root: Path, profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    df = map_capabilities_to_outputs(project_root, profile)
    return df, summarize_capability_map(df)

def summarize_capability_map(capability_df: pd.DataFrame) -> dict:
    if capability_df is None or capability_df.empty:
        return {"total_capabilities": 0}
    return {"total_capabilities": len(capability_df)}
''')

write_file('local_briefing/boundary_summary.py', '''
from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_boundary_summary_table(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    boundaries = [
        ("canli emir yok", "Sistem broker'a veri gondermez"),
        ("broker entegrasyonu yok", "Broker API keyleri sisteme dahil edilmemistir"),
        ("gercek pozisyon yok", "Sadece kagit uzerinde islem yapilir"),
        ("yatirim tavsiyesi yok", "Uretilen raporlar analizdir, tavsiye degildir"),
        ("model deployment yok", "Modeller production sunucularina aktarilmaz"),
        ("production scheduler yok", "Canli operasyon tetikleyici scheduler yoktur"),
        ("background daemon yok", "Sonsuz dongude calisan trading botu yoktur"),
        ("cloud upload yok", "Veriler disariya gonderilmez"),
        ("external LLM/API yok", "Harici zeka servisi cagirisi yapilmaz"),
        ("web dashboard yok", "Lokal UI disinda web servisi yoktur"),
        ("auto-fix/destructive action yok", "Sistem kodlari otomatik degistirmez")
    ]
    df = pd.DataFrame(boundaries, columns=["boundary", "description"])
    return df, summarize_boundary_non_use("", df)

def build_boundary_non_use_summary(project_root: Path, profile: LocalBriefingProfile) -> tuple[str, dict]:
    df, summary = build_boundary_summary_table(profile)
    text = "# Boundary and Non-Use Summary\\n\\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\\n\\n"
    for _, row in df.iterrows():
        text += f"- **{row['boundary']}**: {row['description']}\\n"
    return text, summary

def summarize_boundary_non_use(text: str, boundary_df: pd.DataFrame) -> dict:
    if boundary_df is None or boundary_df.empty:
        return {"total_boundaries": 0}
    return {"total_boundaries": len(boundary_df)}
''')

write_file('local_briefing/risk_limitation_narrative.py', '''
from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_risk_limitation_table(project_root: Path, profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    risks = [
        ("offline/local scope", "Data disari acilamaz, guncellemeler manueldir"),
        ("data freshness limitations", "Veriler gercek zamanli degildir"),
        ("backtest limitations", "Gecmis performans gelecegi garanti etmez"),
        ("synthetic/demo/test limitations", "Sentetik veriler gercek piyasa krizlerini yansitmayabilir"),
        ("manual review requirement", "Otomasyon olmadan karar alinmamalidir"),
        ("dependency aging", "Lokal paketler eskiyebilir"),
        ("stale reports", "Raporlar olusturuldugu anin bilgisini icerir"),
        ("archive/DR simulation limits", "Sadece belirli senaryolar test edilmistir"),
        ("no live trading", "Canli islem kapabilitesi yoktur"),
        ("no official compliance", "Resmi uyum sertifikasi yoktur"),
        ("no investment advice", "Ciktilar tavsiye niteligi tasimaz")
    ]
    df = pd.DataFrame(risks, columns=["risk_limitation", "description"])
    return df, {"total_risks": len(df)}

def build_risk_limitation_narrative(project_root: Path, profile: LocalBriefingProfile) -> tuple[str, dict]:
    df, summary = build_risk_limitation_table(project_root, profile)
    text = "# Risk and Limitation Narrative\\n\\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\\n\\n"
    for _, row in df.iterrows():
        text += f"- **{row['risk_limitation']}**: {row['description']}\\n"
    return text, summary

def summarize_risk_limitation_narrative(text: str, risk_df: pd.DataFrame) -> dict:
    if risk_df is None or risk_df.empty:
        return {"total_risks": 0}
    return {"total_risks": len(risk_df)}
''')
