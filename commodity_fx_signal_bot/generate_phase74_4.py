import os
from pathlib import Path

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

write_file('local_briefing/milestone_narrative.py', '''
from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_milestone_table(project_root: Path, profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    milestones = [
        ("core research platform", "offline_ready"),
        ("reporting and DataLake", "offline_ready"),
        ("safety and governance", "offline_ready"),
        ("metadata/evidence", "offline_ready"),
        ("graph/timeline/consistency", "offline_ready"),
        ("readiness/maintenance/archive/DR", "offline_ready"),
        ("training/briefing", "offline_ready")
    ]
    df = pd.DataFrame(milestones, columns=["milestone_group", "status"])
    return df, summarize_milestone_narrative("", df)

def build_milestone_narrative(project_root: Path, profile: LocalBriefingProfile) -> tuple[str, dict]:
    df, summary = build_milestone_table(project_root, profile)
    text = "# Milestone Narrative\\n\\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\\n\\n"
    for _, row in df.iterrows():
        text += f"- **{row['milestone_group']}**: {row['status']} (Manual review required)\\n"
    return text, summary

def summarize_milestone_narrative(text: str, milestone_df: pd.DataFrame) -> dict:
    if milestone_df is None or milestone_df.empty:
        return {"total_milestones": 0}
    return {"total_milestones": len(milestone_df)}
''')

write_file('local_briefing/phase_evolution_narrative.py', '''
from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_phase_evolution_table(project_root: Path, profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    phases = [
        ("Phases 1-10", "Core foundation and data lake"),
        ("Phases 11-20", "Model training and backtesting pipelines"),
        ("Phases 21-30", "Governance, evidence, and security"),
        ("Phases 31-40", "Knowledge graph, timeline, readiness"),
        ("Phases 41-50", "Maintenance, archive, DR"),
        ("Phases 51-60", "ML enhancements, observability"),
        ("Phases 61-70", "Advanced training, scenario regression, synthesis"),
        ("Phases 71-74", "Training kits, Briefing, Communication")
    ]
    df = pd.DataFrame(phases, columns=["phase_group", "description"])
    return df, {"total_phases": len(df)}

def build_phase_evolution_narrative(project_root: Path, profile: LocalBriefingProfile) -> tuple[str, dict]:
    df, summary = build_phase_evolution_table(project_root, profile)
    text = "# Phase Evolution Narrative\\n\\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\\n\\n"
    for _, row in df.iterrows():
        text += f"- **{row['phase_group']}**: {row['description']}\\n"
    
    text += "\\n*Not: Bu evrim canli sistem tamamlandi iddiasi tasimaz.*"
    return text, summary

def summarize_phase_evolution_narrative(text: str, phase_df: pd.DataFrame) -> dict:
    if phase_df is None or phase_df.empty:
        return {"total_phases": 0}
    return {"total_phases": len(phase_df)}
''')

write_file('local_briefing/architecture_narrative.py', '''
from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_architecture_layer_table(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    layers = [
        ("config/settings", "Lokal yapilandirma ayarlari"),
        ("scripts", "Offline analizleri tetikleyen kodlar"),
        ("reports", "Sonuclarin insan okunabilir hale getirilmesi"),
        ("DataLake", "Tum uretilen verilerin lokal saklanmasi"),
        ("FeatureStore", "Ozniteliklerin offline depolanmasi"),
        ("evidence/metadata", "Karar destek surecleri kayitlari"),
        ("graph/timeline/consistency", "Verilerin tarihsel iliskisel kontrolu"),
        ("readiness/maintenance/archive/DR/training/briefing", "Operasyonel ve yonetimsel local scriptler")
    ]
    df = pd.DataFrame(layers, columns=["layer", "description"])
    return df, {"total_layers": len(df)}

def build_local_only_architecture_narrative(project_root: Path, profile: LocalBriefingProfile) -> tuple[str, dict]:
    df, summary = build_architecture_layer_table(profile)
    text = "# Local-Only Architecture Narrative\\n\\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\\n\\n"
    for _, row in df.iterrows():
        text += f"- **{row['layer']}**: {row['description']}\\n"
    
    text += "\\n*Not: Mimari, web, cloud veya broker baglantisi icermez.*"
    return text, summary

def summarize_architecture_narrative(text: str, layer_df: pd.DataFrame) -> dict:
    if layer_df is None or layer_df.empty:
        return {"total_layers": 0}
    return {"total_layers": len(layer_df)}
''')

write_file('local_briefing/stakeholder_faq.py', '''
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_default_stakeholder_faq(profile: LocalBriefingProfile) -> pd.DataFrame:
    faqs = [
        ("Bu sistem para kazandirir mi?", "Sistem sadece offline arastirma yapar, garantili getiri saglamaz."),
        ("Canli emir gonderiyor mu?", "Hayir, canli islem engellenmistir."),
        ("Yatirim tavsiyesi veriyor mu?", "Hayir, ciktilar tavsiye degil, analizdir."),
        ("Broker baglantisi var mi?", "Hayir, herhangi bir broker api key icermez."),
        ("Uretime hazir mi?", "Sadece offline test ortami icin hazirdir."),
        ("Neden local/offline?", "Veri guvenligi ve arastirma izolasyonu amaciyla."),
        ("Raporlari kim okumali?", "Analistler, risk yoneticileri ve proje yoneticileri."),
        ("Score'lar ne anlama gelir?", "Model ve veri kalitesini gosteren teknik metriklerdir."),
        ("Sinirliliklar neler?", "Canli islem, gercek para kullanimi ve anlik veri akisi yoktur."),
        ("Sonraki guvenli adim nedir?", "Lokal uretilen backtest sonuclarini incelemek.")
    ]
    return pd.DataFrame(faqs, columns=["question", "answer"])

def build_stakeholder_faq_registry(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_stakeholder_faq(profile)
    return df, summarize_stakeholder_faq(df)

def summarize_stakeholder_faq(faq_df: pd.DataFrame) -> dict:
    if faq_df is None or faq_df.empty:
        return {"total_faq": 0}
    return {"total_faq": len(faq_df)}
''')
