import pandas as pd
from local_simplification.simplification_config import LocalSimplificationProfile
from local_simplification.simplification_models import SlimmingPlanItem, build_slimming_plan_item_id, slimming_plan_item_to_dict

def build_default_slimming_plan_items(profile: LocalSimplificationProfile) -> list[SlimmingPlanItem]:
    return [
        SlimmingPlanItem(
            plan_item_id=build_slimming_plan_item_id("docs_nav", "docs"),
            title="docs navigation simplification",
            category="docs",
            priority_hint="low",
            action_type="consolidate",
            dry_run_only=True,
            prerequisites=[],
            warnings=["Gercek uygulama plani degildir."]
        )
    ]

def build_optional_slimming_plan(complexity_df: pd.DataFrame, candidate_df: pd.DataFrame, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_slimming_plan_items(profile)
    df = pd.DataFrame([slimming_plan_item_to_dict(i) for i in items])
    return df, summarize_optional_slimming_plan(df)

def prioritize_slimming_plan_items(plan_df: pd.DataFrame, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return plan_df

def summarize_optional_slimming_plan(plan_df: pd.DataFrame) -> dict:
    return {"items": len(plan_df), "warnings": ["Gercek cleanup uygulamasi degildir.", "Manual review required"]}

def export_optional_slimming_plan_markdown(plan_df: pd.DataFrame, summary: dict) -> str:
    return "# Optional Slimming Plan\n\nBu bir refactor talimati degildir."
