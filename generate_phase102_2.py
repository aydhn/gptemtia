import os

def write_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    write_file('advanced_runtime/runtime_profile_registry.py', '''import pandas as pd
from .runtime_config import AdvancedRuntimeProfile
from .runtime_models import RuntimeProfileItem, build_runtime_profile_id

def build_default_runtime_profile_items(profile: AdvancedRuntimeProfile) -> list[RuntimeProfileItem]:
    return [RuntimeProfileItem(
        profile_id=build_runtime_profile_id(profile.name),
        profile_name=profile.name,
        current_phase=profile.current_phase,
        target_final_phase=profile.target_final_phase,
        local_only=profile.local_only,
        non_production=profile.non_production,
        research_only=profile.research_only,
        status_label="runtime_ready",
        warnings=[]
    )]

def build_advanced_runtime_profile_registry(profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_runtime_profile_items(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    summary = summarize_runtime_profile_registry(df)
    return df, summary

def summarize_runtime_profile_registry(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total": len(df), "ready": len(df[df["status_label"] == "runtime_ready"])}
''')

    write_file('advanced_runtime/runtime_context.py', '''import pandas as pd
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
    text = "# Unified Runtime Context\\n\\n"
    for sec in sections:
        text += f"## {sec['title']}\\n{sec['content']}\\n\\n"
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
''')

    write_file('advanced_runtime/runtime_capabilities.py', '''import pandas as pd
from .runtime_config import AdvancedRuntimeProfile
from .runtime_models import RuntimeCapabilityItem, build_runtime_capability_id

def build_default_runtime_capabilities(profile: AdvancedRuntimeProfile) -> list[RuntimeCapabilityItem]:
    caps = [
        ("capability_settings", "settings"),
        ("capability_paths", "paths"),
        ("capability_datalake", "datalake"),
        ("capability_featurestore", "featurestore"),
        ("capability_reporting", "reporting"),
        ("capability_scripts", "scripts"),
        ("capability_tests", "tests"),
        ("capability_docs", "docs"),
        ("capability_advanced_continuation", "advanced_continuation"),
        ("capability_provider_future", "future data providers"),
        ("capability_feature_future", "future feature engine"),
        ("capability_regime_future", "future regime engine"),
        ("capability_ml_gpu_future", "future ML/GPU"),
        ("capability_backtest_future", "future backtest"),
        ("capability_portfolio_future", "future portfolio"),
        ("capability_final_integration_future", "future final integration")
    ]
    items = []
    for label, name in caps:
        items.append(RuntimeCapabilityItem(
            capability_id=build_runtime_capability_id(label),
            capability_label=label,
            capability_name=name,
            current_status="ready" if "future" not in name else "planned",
            future_phase_range="103-160",
            required_by=[],
            warnings=[]
        ))
    return items

def build_runtime_capability_registry(profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_runtime_capabilities(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_runtime_capabilities(df)

def summarize_runtime_capabilities(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total": len(df), "planned": len(df[df["current_status"] == "planned"])}
''')

if __name__ == '__main__':
    main()
