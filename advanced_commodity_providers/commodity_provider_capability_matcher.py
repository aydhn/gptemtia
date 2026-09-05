
import pandas as pd
from .commodity_provider_config import CommodityProviderProfile

def match_commodity_provider_capabilities(
    requested_data_type: str,
    requested_category: str,
    timeframe: str,
    capability_df: pd.DataFrame,
) -> pd.DataFrame:
    if capability_df.empty: return pd.DataFrame()
    def match_row(row):
        return (requested_data_type in row.get("data_types", []) and 
                requested_category in row.get("commodity_categories", []) and
                timeframe in row.get("timeframe_support", []))
    matched = capability_df[capability_df.apply(match_row, axis=1)]
    return matched

def build_commodity_provider_capability_matcher_report(profile: CommodityProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"match_status": "ok"}])
    return df, summarize_commodity_provider_capability_matcher(df)

def summarize_commodity_provider_capability_matcher(df: pd.DataFrame) -> dict:
    return {"total_matches": len(df)}
