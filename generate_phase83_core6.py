import os
from pathlib import Path

def generate_core6():
    base_dir = Path("commodity_fx_signal_bot/local_performance")
    
    # storage_retention.py
    (base_dir / "storage_retention.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_default_storage_retention_items(profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"item": "reports", "retention": "30 days", "warning": "Dosya silmez."}])

def build_storage_retention_rehearsal_plan(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_storage_retention_items(profile)
    return df, summarize_storage_retention_plan(df)

def summarize_storage_retention_plan(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

    # report_rotation.py
    (base_dir / "report_rotation.py").write_text("""from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_report_rotation_sections(profile: LocalPerformanceProfile) -> list[dict]:
    return [{"title": "Rotation", "content": "Manuel yapiniz. Otomatik rotation uygulamaz."}]

def build_report_rotation_rehearsal_guide(project_root: Path, profile: LocalPerformanceProfile) -> tuple[str, dict]:
    sections = build_report_rotation_sections(profile)
    text = "# Report Rotation Rehearsal Guide\\n"
    for s in sections:
        text += f"\\n## {s['title']}\\n{s['content']}\\n"
    return text, summarize_report_rotation_guide(text)

def summarize_report_rotation_guide(text: str) -> dict: return {"length": len(text)}
""", encoding="utf-8")

    # datalake_retention.py
    (base_dir / "datalake_retention.py").write_text("""from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_datalake_retention_sections(profile: LocalPerformanceProfile) -> list[dict]:
    return [{"title": "Retention", "content": "Manuel yapiniz. Hukuki saklama tavsiyesi degildir."}]

def build_datalake_retention_rehearsal_guide(project_root: Path, profile: LocalPerformanceProfile) -> tuple[str, dict]:
    sections = build_datalake_retention_sections(profile)
    text = "# DataLake Retention Rehearsal Guide\\n"
    for s in sections:
        text += f"\\n## {s['title']}\\n{s['content']}\\n"
    return text, summarize_datalake_retention_guide(text)

def summarize_datalake_retention_guide(text: str) -> dict: return {"length": len(text)}
""", encoding="utf-8")

    # performance_no_go_safe_go.py
    (base_dir / "performance_no_go_safe_go.py").write_text("""import pandas as pd
from .performance_config import LocalPerformanceProfile

def build_performance_no_go_conditions(profile: LocalPerformanceProfile) -> pd.DataFrame:
    data = [
        "real benchmark claim", "load/stress test claim", "production profiling claim",
        "cloud cost approval claim", "production capacity approval claim", "live/broker/deploy claim",
        "investment performance claim", "investment advice wording", "raw secret output",
        "file deletion/move/overwrite claim", "package publish/cloud upload claim"
    ]
    return pd.DataFrame([{"condition": c, "status": "no-go"} for c in data])

def build_performance_safe_go_conditions(profile: LocalPerformanceProfile) -> pd.DataFrame:
    data = [
        "read-only estimate reports available", "lightweight runtime profile documented",
        "heavy-output warnings documented", "retention rehearsal documented", "no benchmark executed",
        "no background monitoring", "no cloud dependency", "manual review required"
    ]
    return pd.DataFrame([{"condition": c, "status": "safe-go", "warning": "production capacity approval degildir"} for c in data])

def build_performance_no_go_safe_go_summary(profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df1 = build_performance_no_go_conditions(profile)
    df2 = build_performance_safe_go_conditions(profile)
    df = pd.concat([df1, df2], ignore_index=True)
    return df, summarize_performance_no_go_safe_go(df)

def summarize_performance_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    if summary_df is None or summary_df.empty: return {"total": 0}
    return {"total": len(summary_df), "no_go": len(summary_df[summary_df["status"]=="no-go"]), "safe_go": len(summary_df[summary_df["status"]=="safe-go"])}
""", encoding="utf-8")

if __name__ == "__main__":
    generate_core6()
    print("Core 6 generated")
