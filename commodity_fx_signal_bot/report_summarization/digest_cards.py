import pandas as pd
from report_summarization.summary_config import ReportSummaryProfile
from report_summarization.summary_models import BriefCard, build_brief_id

def build_research_digest_cards(summaries_df: pd.DataFrame, findings_df: pd.DataFrame, warnings_df: pd.DataFrame, profile: ReportSummaryProfile) -> tuple[pd.DataFrame, dict]:
    cards = []

    modules = summaries_df["module_name"].unique().tolist() if not summaries_df.empty and "module_name" in summaries_df else []
    for m in modules:
        cards.append(build_digest_card_for_module(m, findings_df, warnings_df))

    themes = [
        "safety", "quality", "regression", "documentation", "maintenance",
        "performance", "knowledge_base", "governance", "experiments",
        "planning", "final_review"
    ]
    for t in themes:
        cards.append(build_digest_card_for_theme(t, findings_df, warnings_df))

    df = pd.DataFrame([c.__dict__ for c in cards])
    return df, summarize_digest_cards(df)

def build_digest_card_for_module(module_name: str, findings_df: pd.DataFrame, warnings_df: pd.DataFrame) -> BriefCard:
    return BriefCard(
        brief_id=build_brief_id("research_digest", f"Module Digest: {module_name}", module_name),
        brief_type="research_digest",
        title=f"{module_name} Digest",
        module_name=module_name,
        symbol=None,
        summary=f"Digest for {module_name}",
        key_points=[],
        follow_ups=[],
        priority="low_priority",
        source_paths=[],
        warnings=[]
    )

def build_digest_card_for_theme(theme: str, findings_df: pd.DataFrame, warnings_df: pd.DataFrame) -> BriefCard:
    return BriefCard(
        brief_id=build_brief_id("research_digest", f"Theme Digest: {theme}"),
        brief_type="research_digest",
        title=f"{theme} Digest",
        module_name=None,
        symbol=None,
        summary=f"Digest for {theme}",
        key_points=[],
        follow_ups=[],
        priority="low_priority",
        source_paths=[],
        warnings=[]
    )

def summarize_digest_cards(cards_df: pd.DataFrame) -> dict:
    if cards_df.empty:
        return {"total_cards": 0}
    return {
        "total_cards": len(cards_df),
        "module_cards": len(cards_df[cards_df["module_name"].notna()]),
        "theme_cards": len(cards_df[cards_df["module_name"].isna()])
    }
