import pandas as pd
from pathlib import Path
from .runtime_config import AdvancedRuntimeProfile
from .runtime_models import RuntimeContextItem, build_runtime_context_id

def build_unified_runtime_context_sections(profile: AdvancedRuntimeProfile) -> list[dict]:
    return [
        {"title": "Runtime amacı", "content": "Phase 102 core runtime consolidation katmanını kurmak."},
        {"title": "Bu runtime ne değildir?", "content": "Canlı trading, broker, yatırım tavsiyesi, deployment değildir."},
        {"title": "Phase 101-160 bağlantısı", "content": "Advanced continuation planını gerçek runtime omurgasına bağlamak."},
        {"title": "Settings role", "content": "Core runtime yapılandırması sağlar."},
        {"title": "Paths role", "content": "Tüm dizin yollarını sağlar."},
        {"title": "DataLake role", "content": "Data storage ve retrieval sağlar."},
        {"title": "FeatureStore role", "content": "ML data preparation sağlar."},
        {"title": "Reports role", "content": "Rapor oluşturma sağlar."},
        {"title": "Scripts role", "content": "Çalıştırılabilir komutları sağlar."},
        {"title": "Tests role", "content": "Kalite güvence sağlar."},
        {"title": "Safety boundary", "content": "Sınırları çizer."},
        {"title": "Phase 103 hazırlığı", "content": "Research Engine Interface Layer için zemin."}
    ]

def build_unified_runtime_context(project_root: Path, profile: AdvancedRuntimeProfile) -> tuple[str, dict]:
    sections = build_unified_runtime_context_sections(profile)
    text = "# Unified Runtime Context\n\n"
    for sec in sections:
        text += f"## {sec['title']}\n{sec['content']}\n\n"
    return text, summarize_unified_runtime_context(text)

def summarize_unified_runtime_context(text: str) -> dict:
    return {"length": len(text), "sections": text.count("## ")}

def build_runtime_context_registry(project_root: Path, profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    sections = build_unified_runtime_context_sections(profile)
    items = []
    for sec in sections:
        items.append(RuntimeContextItem(
            context_id=build_runtime_context_id("general", sec['title'].replace(" ", "_")),
            context_area="general",
            context_name=sec['title'],
            source_ref="unified_runtime_context",
            runtime_role="documentation",
            status_label="runtime_ready",
            manual_review_required=False,
            warnings=[]
        ))
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_runtime_context_registry(df)

def summarize_runtime_context_registry(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total": len(df)}
