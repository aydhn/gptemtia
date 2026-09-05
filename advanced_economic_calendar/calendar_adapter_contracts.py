import pandas as pd
from typing import Tuple, Dict, List
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_models import CalendarProviderContractItem, build_calendar_provider_contract_id

def build_default_calendar_adapter_contract_items(profile: CalendarProviderProfile) -> List[CalendarProviderContractItem]:
    forbidden = [
        "no scraping", "no browser automation", "no hidden API reverse engineering",
        "no paywall bypass", "no credential output", "no broker/live/order",
        "no investment advice", "no event directional claim", "no deployment",
        "no destructive file action"
    ]
    areas = [
        "Calendar metadata contract", "Calendar capability contract", "Economic event normalization contract",
        "Calendar request validation contract", "Calendar fetch response contract", "Calendar error handling contract",
        "Calendar manual file contract", "Calendar local cache contract", "Calendar official API placeholder contract",
        "Calendar licensed placeholder contract", "Calendar public dataset placeholder contract",
        "Calendar dry-run fixture contract", "Calendar event schema contract", "Release event schema contract",
        "Event surprise requirement contract", "Event time normalization requirement contract",
        "Event revision handling requirement contract", "Calendar output validation contract", "Calendar safety contract"
    ]
    
    return [CalendarProviderContractItem(
        contract_id=build_calendar_provider_contract_id(a),
        contract_area=a,
        input_expectation="Valid configuration and models",
        output_expectation="Strict compliance with safe guidelines",
        forbidden_behavior=forbidden,
        manual_review_required=True
    ) for a in areas]

def build_calendar_adapter_contract(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_calendar_adapter_contract_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_calendar_adapter_contract(df)
    return df, summary

def summarize_calendar_adapter_contract(df: pd.DataFrame) -> Dict:
    return {
        "total_contracts": len(df)
    }
