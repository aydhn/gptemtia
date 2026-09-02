import pandas as pd
from .training_config import LocalTrainingProfile

def build_daily_curriculum_items(day_number: int, profile: LocalTrainingProfile) -> list[dict]:
    plan = {
        1: "proje amacı, sınırlar, safe usage",
        2: "kurulum, config, docs",
        3: "reports/output ve DataLake okuma",
        4: "evidence, metadata, graph, timeline",
        5: "consistency, readiness, maintenance",
        6: "archive, DR, training materials",
        7: "assessment dry-run ve manual review"
    }
    return [{"day": day_number, "topic": plan.get(day_number, "Review")}]

def build_first_week_operator_curriculum(profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    data = []
    for d in range(1, 8):
        data.extend(build_daily_curriculum_items(d, profile))
    df = pd.DataFrame(data)
    df["warnings"] = "Curriculum sertifika değildir. Assessment dry-run canlı operasyon yetkisi vermez. Yatırım tavsiyesi yok."
    return df, summarize_first_week_curriculum(df)

def summarize_first_week_curriculum(curriculum_df: pd.DataFrame) -> dict:
    if curriculum_df is None or curriculum_df.empty: return {"count": 0}
    return {"count": len(curriculum_df)}
