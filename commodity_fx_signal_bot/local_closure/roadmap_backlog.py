
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile
from local_closure.closure_models import RoadmapItem, build_roadmap_item_id, roadmap_item_to_dict
from local_closure.closure_labels import list_roadmap_status_labels

def build_default_roadmap_items(profile: LocalClosureProfile) -> list[RoadmapItem]:
    return [
        RoadmapItem(
            roadmap_id=build_roadmap_item_id("Offline Model Training"),
            title="Offline Model Training",
            category="model research offline",
            status="roadmap_candidate",
            rationale="Gelecekte farklı algoritmalar test edilebilir.",
            prerequisites=["Feature Store update"],
            safety_boundaries=["Strict local execution", "No live connection"],
            warnings=[]
        ),
        RoadmapItem(
            roadmap_id=build_roadmap_item_id("Live Trading Connection"),
            title="Live Trading Connection",
            category="governance extensions",
            status="roadmap_blocked_by_safety",
            rationale="Canlı trade projenin offline sınırlarını ihlal eder.",
            prerequisites=[],
            safety_boundaries=["Blocked by policy"],
            warnings=["Blocked by safety restrictions"]
        )
    ]

def classify_roadmap_item_safety(item: RoadmapItem, profile: LocalClosureProfile) -> dict:
    if "live" in item.title.lower() or "broker" in item.title.lower() or "deploy" in item.title.lower():
        item.status = "roadmap_blocked_by_safety"
        item.warnings.append("Blocked by safety restrictions")
    return roadmap_item_to_dict(item)

def build_future_roadmap_backlog(project_root: Path, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_roadmap_items(profile)
    processed = [classify_roadmap_item_safety(item, profile) for item in items]
    df = pd.DataFrame(processed)
    summary = summarize_roadmap_backlog(df)
    return df, summary

def summarize_roadmap_backlog(roadmap_df: pd.DataFrame) -> dict:
    return {
        "total_items": len(roadmap_df),
        "blocked_items": len(roadmap_df[roadmap_df["status"] == "roadmap_blocked_by_safety"]) if not roadmap_df.empty else 0
    }

def export_roadmap_backlog_markdown(roadmap_df: pd.DataFrame, summary: dict) -> str:
    md = "# Future Roadmap Backlog\n\n"
    md += "> **UYARI**: Bu rapor offline/local v1.0 closure rehearsal ve final meta-review çıktısıdır; gerçek v1.0 release, production release, compliance sertifikası, resmi proje kapanışı, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"
    if roadmap_df.empty:
        md += "No items found.\n"
        return md
    for _, row in roadmap_df.iterrows():
        md += f"## {row['title']}\n"
        md += f"- **Status**: {row['status']}\n"
        md += f"- **Category**: {row['category']}\n"
        md += f"- **Rationale**: {row['rationale']}\n\n"
    return md
