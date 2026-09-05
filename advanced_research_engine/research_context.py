import pandas as pd
from pathlib import Path
from .research_engine_config import AdvancedResearchEngineProfile

def build_unified_research_context_sections(profile: AdvancedResearchEngineProfile) -> list[dict]:
    return [
        {"title": "Research engine amacı", "content": "Ortak araştırma motoru arayüzü."},
        {"title": "Bu research engine ne değildir?", "content": "Canlı trading, kesin AL/SAT veya broker arayüzü değildir."},
        {"title": "Phase 101-160 bağlantısı", "content": "İleri fazların temelidir."},
        {"title": "Data interface role", "content": "Veri erişimi sağlar."},
        {"title": "Feature interface role", "content": "Feature üretimi."},
        {"title": "Regime interface role", "content": "Rejim etiketleme."},
        {"title": "ML interface role", "content": "ML tahmini."},
        {"title": "Backtest interface role", "content": "Strateji backtest."},
        {"title": "Portfolio interface role", "content": "Portföy simülasyonu."},
        {"title": "Report interface role", "content": "Raporlama."},
        {"title": "Signal research interface role", "content": "Sinyal araştırması, emir değil."},
        {"title": "Safety boundary", "content": "Offline ve güvenli yapı."},
        {"title": "Phase 104 hazırlığı", "content": "Profil altyapısı."}
    ]

def build_unified_research_context(project_root: Path, profile: AdvancedResearchEngineProfile) -> tuple[str, dict]:
    sections = build_unified_research_context_sections(profile)
    text = "\n\n".join([f"## {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_unified_research_context(text)

def summarize_unified_research_context(text: str) -> dict:
    return {"length": len(text)}

def build_research_context_registry(project_root: Path, profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"context_area": "core", "context_name": "unified"}])
    return df, {"count": 1}
