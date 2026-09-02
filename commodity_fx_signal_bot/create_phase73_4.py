import os

with open("local_training/command_lessons.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile

def detect_forbidden_training_command_terms(command: str) -> list[str]:
    forbidden = ["buy", "sell", "live", "broker", "deploy", "daemon", "server", "delete", "rm ", "move", "overwrite", "upload", "cloud", "restore --apply", "backup --apply", "real market download", "scraping"]
    found = []
    for f in forbidden:
        if f in command.lower():
            found.append(f)
    return found

def classify_training_command_safety(command: str) -> dict:
    terms = detect_forbidden_training_command_terms(command)
    return {"is_safe": len(terms) == 0, "forbidden_terms": terms}

def build_safe_command_lesson_registry(project_root: Path, profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    commands = ["python -m scripts.run_maintenance_status", "python -m scripts.run_readiness_quality_report"]
    data = []
    for c in commands:
        data.append({"command": c, **classify_training_command_safety(c)})
    df = pd.DataFrame(data)
    return df, summarize_command_lessons(df)

def summarize_command_lessons(command_df: pd.DataFrame) -> dict:
    if command_df is None or command_df.empty: return {"count": 0}
    return {"count": len(command_df)}
''')

with open("local_training/report_lessons.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile
from .training_models import TrainingLesson, build_training_lesson_id

def build_report_reading_lesson(report_family: str, profile: LocalTrainingProfile) -> TrainingLesson:
    return TrainingLesson(
        lesson_id=build_training_lesson_id("report_training", report_family),
        lesson_name=f"Read {report_family}",
        domain_label="report_training",
        role_label="operator_role",
        objective="Learn to read report",
        steps=["Locate", "Read"],
        safe_commands=[],
        expected_outputs=["Understanding"],
        status="lesson_ready",
        warnings=["Report lesson sonuçların doğruluğunu garanti etmez.", "Yatırım tavsiyesi üretmez."]
    )

def build_report_reading_lesson_registry(project_root: Path, profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    families = ["research_reports", "quality_gates", "final_review", "scenario_regression", "master_orchestration", "secrets_hygiene", "backup_recovery", "portable_packaging", "evidence_governance", "artifact_metadata", "local_knowledge_graph", "local_timeline", "local_consistency", "local_readiness", "local_maintenance", "local_archive", "local_dr"]
    lessons = [build_report_reading_lesson(f, profile) for f in families]
    df = pd.DataFrame([l.__dict__ for l in lessons])
    return df, summarize_report_lessons(df)

def summarize_report_lessons(report_lesson_df: pd.DataFrame) -> dict:
    if report_lesson_df is None or report_lesson_df.empty: return {"count": 0}
    return {"count": len(report_lesson_df)}
''')

with open("local_training/datalake_lessons.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile
from .training_models import TrainingLesson, build_training_lesson_id

def build_datalake_domain_lesson(domain_name: str, profile: LocalTrainingProfile) -> TrainingLesson:
    return TrainingLesson(
        lesson_id=build_training_lesson_id("datalake_training", domain_name),
        lesson_name=f"Explore {domain_name}",
        domain_label="datalake_training",
        role_label="operator_role",
        objective="Navigate DataLake",
        steps=["Open folder"],
        safe_commands=[],
        expected_outputs=[],
        status="lesson_ready",
        warnings=["DataLake lesson raw data extraction değildir.", "Secret/private data okunmaz.", "Read-only navigation anlatılır."]
    )

def build_datalake_reading_lesson_registry(project_root: Path, profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([build_datalake_domain_lesson("test", profile).__dict__])
    return df, summarize_datalake_lessons(df)

def summarize_datalake_lessons(datalake_lesson_df: pd.DataFrame) -> dict:
    if datalake_lesson_df is None or datalake_lesson_df.empty: return {"count": 0}
    return {"count": len(datalake_lesson_df)}
''')

with open("local_training/cross_layer_lessons.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile
from .training_models import TrainingLesson, build_training_lesson_id

def build_cross_layer_lesson(layer_name: str, profile: LocalTrainingProfile) -> TrainingLesson:
    return TrainingLesson(
        lesson_id=build_training_lesson_id("cross_layer_training", layer_name),
        lesson_name=f"Cross layer: {layer_name}",
        domain_label="cross_layer_training",
        role_label="operator_role",
        objective="Understand cross layer",
        steps=["Review links"],
        safe_commands=[],
        expected_outputs=[],
        status="lesson_ready",
        warnings=["Cross-layer lesson canlı sistem eğitimi değildir.", "Relationship/consistency/readiness score production guarantee değildir.", "Manual review vurgusu olmalı."]
    )

def build_cross_layer_lesson_registry(project_root: Path, profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    layers = ["evidence_governance", "artifact_metadata", "local_knowledge_graph", "local_timeline", "local_consistency", "local_readiness", "local_maintenance", "local_archive", "local_dr", "local_training"]
    lessons = [build_cross_layer_lesson(l, profile) for l in layers]
    df = pd.DataFrame([l.__dict__ for l in lessons])
    return df, summarize_cross_layer_lessons(df)

def summarize_cross_layer_lessons(cross_df: pd.DataFrame) -> dict:
    if cross_df is None or cross_df.empty: return {"count": 0}
    return {"count": len(cross_df)}
''')

with open("local_training/troubleshooting_lessons.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile
from .training_models import TrainingLesson, build_training_lesson_id

def build_common_troubleshooting_lessons(profile: LocalTrainingProfile) -> list[TrainingLesson]:
    commons = ["missing output file", "missing report directory", "import error", "missing optional dependency", "empty DataFrame output", "missing DataLake save/load pair", "missing status script", "broken path reference", "stale report", "secret boundary warning", "forbidden command warning"]
    return [
        TrainingLesson(
            lesson_id=build_training_lesson_id("troubleshooting_training", c),
            lesson_name=f"Fix {c}",
            domain_label="troubleshooting_training",
            role_label="developer_role",
            objective="Troubleshoot",
            steps=["Check logs"],
            safe_commands=[],
            expected_outputs=[],
            status="lesson_ready",
            warnings=["Troubleshooting auto-fix değildir.", "Dosya silme/overwrite önermez.", "Manual review ve safe status commands odaklıdır."]
        ) for c in commons
    ]

def build_troubleshooting_lesson_registry(project_root: Path, profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    lessons = build_common_troubleshooting_lessons(profile)
    df = pd.DataFrame([l.__dict__ for l in lessons])
    return df, summarize_troubleshooting_lessons(df)

def summarize_troubleshooting_lessons(troubleshooting_df: pd.DataFrame) -> dict:
    if troubleshooting_df is None or troubleshooting_df.empty: return {"count": 0}
    return {"count": len(troubleshooting_df)}
''')
