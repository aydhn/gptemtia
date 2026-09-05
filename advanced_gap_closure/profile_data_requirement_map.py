import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_research_profile_to_data_requirement_map(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    reqs = [{"profile": "major_fx_pairs", "req": "FX provider requirement"}, {"profile": "precious_metals", "req": "commodities provider requirement"}]
    df = pd.DataFrame(reqs)
    return df, summarize_profile_data_requirement_map(df)

def summarize_profile_data_requirement_map(df: pd.DataFrame) -> dict: return {"total": len(df)}
