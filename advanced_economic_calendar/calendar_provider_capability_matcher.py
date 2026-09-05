import pandas as pd
from typing import Tuple, Dict
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile

def match_calendar_provider_capabilities(
    requested_data_type: str,
    requested_event_category: str,
    requested_region: str,
    capability_df: pd.DataFrame,
) -> pd.DataFrame:
    if capability_df.empty:
        return pd.DataFrame()
        
    def is_match(row):
        cat_match = requested_event_category in row.get("event_categories", [])
        type_match = requested_data_type in row.get("data_types", [])
        reg_match = requested_region in row.get("region_support", []) or "GLOBAL" in row.get("region_support", [])
        return cat_match and type_match and reg_match
        
    mask = capability_df.apply(is_match, axis=1)
    return capability_df[mask]

def build_calendar_provider_capability_matcher_report(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    from advanced_economic_calendar.calendar_provider_capabilities import build_calendar_provider_capability_registry
    df, _ = build_calendar_provider_capability_registry(profile)
    
    scenarios = [
        ("calendar_data_release_event", "event_inflation", "US"),
        ("calendar_data_event_schedule", "event_central_bank_policy", "EU")
    ]
    
    results = []
    for s in scenarios:
        match_df = match_calendar_provider_capabilities(s[0], s[1], s[2], df)
        results.append({
            "requested_data_type": s[0],
            "requested_event_category": s[1],
            "requested_region": s[2],
            "matched_providers": match_df["provider_name"].tolist() if not match_df.empty else []
        })
        
    res_df = pd.DataFrame(results)
    summary = summarize_calendar_provider_capability_matcher(res_df)
    return res_df, summary

def summarize_calendar_provider_capability_matcher(df: pd.DataFrame) -> Dict:
    return {
        "total_matches": len(df)
    }
