
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile
from local_closure.closure_models import LessonLearnedItem, build_lesson_learned_id, lesson_learned_item_to_dict

def build_default_lessons_learned(profile: LocalClosureProfile) -> list[LessonLearnedItem]:
    return [
        LessonLearnedItem(
            lesson_id=build_lesson_learned_id("Data Lake Ayrımı"),
            lesson_title="Data Lake Ayrımı",
            category="architecture",
            observation="Veri depolama ile raporlama ayrılmalı.",
            implication="Daha kolay test edilebilirlik.",
            recommendation="Klasör yapısını strict tut.",
            warnings=[]
        ),
        LessonLearnedItem(
            lesson_id=build_lesson_learned_id("Safety First"),
            lesson_title="Safety First",
            category="safety",
            observation="Canlı işlem kazalarına karşı önlem şart.",
            implication="Her faza non-use eklenmeli.",
            recommendation="Dry-run default olmalı.",
            warnings=[]
        )
    ]

def build_lessons_learned_compendium(project_root: Path, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    lessons = build_default_lessons_learned(profile)
    df = pd.DataFrame([lesson_learned_item_to_dict(l) for l in lessons])
    summary = summarize_lessons_learned(df)
    return df, summary

def summarize_lessons_learned(lesson_df: pd.DataFrame) -> dict:
    return {
        "total_lessons": len(lesson_df),
        "categories": lesson_df["category"].nunique() if not lesson_df.empty else 0
    }

def export_lessons_learned_markdown(lesson_df: pd.DataFrame, summary: dict) -> str:
    md = "# Lessons Learned Compendium\n\n"
    md += "> **UYARI**: Bu rapor offline/local v1.0 closure rehearsal ve final meta-review çıktısıdır; gerçek v1.0 release, production release, compliance sertifikası, resmi proje kapanışı, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"
    if lesson_df.empty:
        md += "No lessons found.\n"
        return md
    for _, row in lesson_df.iterrows():
        md += f"## {row['lesson_title']}\n"
        md += f"- **Category**: {row['category']}\n"
        md += f"- **Observation**: {row['observation']}\n"
        md += f"- **Implication**: {row['implication']}\n"
        md += f"- **Recommendation**: {row['recommendation']}\n\n"
    return md
