import pandas as pd
from typing import Tuple, Dict
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile

def build_calendar_no_go_conditions(profile: CalendarProviderProfile) -> pd.DataFrame:
    no_go = [
        "live trading", "broker integration", "real order", "exact buy/sell instruction",
        "investment advice", "event directional certainty claim", "model deployment",
        "production deployment", "web server/dashboard", "external LLM/vector/embedding",
        "web scraping", "HTML scraping", "browser automation scraping", "hidden API reverse engineering",
        "paywall bypass", "rate limit abuse", "credential output", "required paid API lock-in",
        "cloud publish", "Docker push", "git tag", "archive creation", "destructive file action",
        "official approval wording"
    ]
    return pd.DataFrame([{"condition": c, "type": "no-go"} for c in no_go])

def build_calendar_safe_go_conditions(profile: CalendarProviderProfile) -> pd.DataFrame:
    safe_go = [
        "local/offline economic calendar abstraction", "calendar dry-run fixture",
        "calendar manual file placeholder", "calendar local cache placeholder",
        "calendar official API placeholder without network call",
        "calendar licensed provider placeholder without credential",
        "calendar public dataset placeholder without network call",
        "economic event universe registry", "event indicator mapping",
        "calendar event schema contract", "release event schema contract",
        "surprise/time/revision requirements documentation", "calendar capability matching",
        "manual review", "no broker/no live/no advice/no deploy/no scraping"
    ]
    return pd.DataFrame([{"condition": c, "type": "safe-go"} for c in safe_go])

def build_calendar_safety_boundary(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.concat([build_calendar_no_go_conditions(profile), build_calendar_safe_go_conditions(profile)])
    summary = summarize_calendar_safety_boundary(df)
    return df, summary

def summarize_calendar_safety_boundary(df: pd.DataFrame) -> Dict:
    return {
        "total_boundaries": len(df)
    }
