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
    text = "# Local-Only Architecture Narrative\n\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\n\n"
    for _, row in df.iterrows():
        text += f"- **{row['layer']}**: {row['description']}\n"
    
    text += "\n*Not: Mimari, web, cloud veya broker baglantisi icermez.*"
    return text, summary

def summarize_architecture_narrative(text: str, layer_df: pd.DataFrame) -> dict:
    if layer_df is None or layer_df.empty:
        return {"total_layers": 0}
    return {"total_layers": len(layer_df)}
