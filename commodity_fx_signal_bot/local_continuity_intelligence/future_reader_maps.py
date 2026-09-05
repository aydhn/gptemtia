import pandas as pd
from .continuity_models import FutureReaderItem
def build_future_reader_onboarding_map(profile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([i.__dict__ for i in build_default_future_reader_items(profile)])
    return df, summarize_future_reader_map(df)
def build_future_reader_role_guide(profile) -> tuple[pd.DataFrame, dict]:
    return build_future_reader_onboarding_map(profile)
def build_future_reader_first_hour_guide(profile) -> tuple[pd.DataFrame, dict]:
    return build_future_reader_onboarding_map(profile)
def build_future_reader_first_day_guide(profile) -> tuple[pd.DataFrame, dict]:
    return build_future_reader_onboarding_map(profile)
def build_future_reader_first_week_guide(profile) -> tuple[pd.DataFrame, dict]:
    return build_future_reader_onboarding_map(profile)
def build_default_future_reader_items(profile) -> list[FutureReaderItem]:
    return [FutureReaderItem("r1", "r2", "g1", "s1", True, ["No live/broker/deploy"])]
def summarize_future_reader_map(df: pd.DataFrame) -> dict:
    return {"total": len(df)}