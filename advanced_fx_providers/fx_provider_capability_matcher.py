import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def match_fx_provider_capabilities(
    requested_data_type: str,
    requested_pair_group: str,
    timeframe: str,
    capability_df: pd.DataFrame,
) -> pd.DataFrame:
    # mock matcher logic
    if capability_df.empty:
        return pd.DataFrame()
    return capability_df.copy()

def build_fx_provider_capability_matcher_report(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    data = [{"match_test": "ohlcv_major", "status": "success"}]
    df = pd.DataFrame(data)
    return df, summarize_fx_provider_capability_matcher(df)

def summarize_fx_provider_capability_matcher(df: pd.DataFrame) -> Dict:
    return {"matched": len(df)}
