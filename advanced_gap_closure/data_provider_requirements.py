import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile
from .gap_closure_models import DataFoundationRequirement, to_dict

def build_default_data_provider_requirements(profile: FunctionalGapClosureProfile) -> list[DataFoundationRequirement]:
    areas = ["OHLCV schema", "macro data schema", "event/calendar schema", "news metadata schema"]
    return [DataFoundationRequirement(
        requirement_id=f"req_{a}", requirement_area=a, required_for_phase=106,
        provider_relevance="high", no_scraping_constraint="yes", expected_contract="yes",
        readiness_label="data_foundation_ready", warnings=[]
    ) for a in areas]

def build_data_provider_requirements_matrix(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([to_dict(i) for i in build_default_data_provider_requirements(profile)])
    return df, summarize_data_provider_requirements(df)

def summarize_data_provider_requirements(df: pd.DataFrame) -> dict: return {"total": len(df)}
