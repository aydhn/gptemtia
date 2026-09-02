import os
from pathlib import Path

def generate_core5():
    base_dir = Path("commodity_fx_signal_bot/local_performance")
    
    # efficiency_planning.py
    (base_dir / "efficiency_planning.py").write_text("""from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_efficiency_planning_sections(profile: LocalPerformanceProfile) -> list[dict]:
    return [
        {"title": "Local-only efficiency principle", "content": "Hepsi offline manuel inceleme icindir."},
        {"title": "When to use lightweight mode", "content": "Kisa ve hizli incelemeler."},
        {"title": "How to reduce output review burden manually", "content": "Sadece hata icerenleri incele."},
        {"title": "How to prioritize quality/status scripts", "content": "Once bunlari calistir."},
        {"title": "How to avoid heavy reruns", "content": "Tekrar tekrar calistirmaktan kacin."},
        {"title": "How to read growth estimates", "content": "Manual rotasyon planla."},
        {"title": "How to handle retention manually", "content": "Kendin sil/arsivle."},
        {"title": "What not to do", "content": "Gercek yatirim karari alma. Otomatik silme yapma."}
    ]

def build_offline_efficiency_planning_guide(project_root: Path, profile: LocalPerformanceProfile) -> tuple[str, dict]:
    sections = build_efficiency_planning_sections(profile)
    text = "# Offline Efficiency Planning Guide\\n"
    for s in sections:
        text += f"\\n## {s['title']}\\n{s['content']}\\n"
    return text, summarize_efficiency_planning_guide(text)

def summarize_efficiency_planning_guide(text: str) -> dict: return {"length": len(text)}
""", encoding="utf-8")

    # efficiency_candidates.py
    (base_dir / "efficiency_candidates.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def detect_efficiency_candidates(project_root: Path, profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"candidate": "run status scripts before full reports", "rationale": "Saves time", "warning": "Otomatik optimizasyon degildir."}])

def build_efficiency_candidate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_efficiency_candidates(project_root, profile)
    return df, summarize_efficiency_candidates(df)

def summarize_efficiency_candidates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

    # lightweight_mode.py
    (base_dir / "lightweight_mode.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_default_lightweight_mode_recommendations(profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"recommendation": "generate quality reports selectively", "warning": "Config degistirmez."}])

def build_lightweight_mode_recommendation_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_lightweight_mode_recommendations(profile)
    return df, summarize_lightweight_mode_recommendations(df)

def summarize_lightweight_mode_recommendations(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

    # heavy_output_warnings.py
    (base_dir / "heavy_output_warnings.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def detect_heavy_output_warnings(project_root: Path, profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"warning": "review CSV indexes before markdown binders", "type": "heavy_output_warning", "note": "Dosya silme onermez."}])

def build_heavy_output_warning_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_heavy_output_warnings(project_root, profile)
    return df, summarize_heavy_output_warnings(df)

def summarize_heavy_output_warnings(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

if __name__ == "__main__":
    generate_core5()
    print("Core 5 generated")
