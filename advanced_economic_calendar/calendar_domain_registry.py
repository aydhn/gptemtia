import pandas as pd
from typing import Tuple, Dict, List
from advanced_economic_calendar.calendar_provider_config import CalendarProviderProfile
from advanced_economic_calendar.calendar_provider_models import CalendarProviderDomain, build_calendar_provider_domain_id
from advanced_economic_calendar.calendar_provider_labels import list_calendar_domain_labels

def build_default_calendar_domains(profile: CalendarProviderProfile) -> List[CalendarProviderDomain]:
    domains = []
    for lbl in list_calendar_domain_labels():
        domains.append(CalendarProviderDomain(
            domain_id=build_calendar_provider_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"Domain for {lbl}",
            required_outputs=["schema", "registry"],
            warnings=[]
        ))
    return domains

def build_economic_calendar_domain_registry(profile: CalendarProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_calendar_domains(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_calendar_domains(df)
    return df, summary

def summarize_calendar_domains(df: pd.DataFrame) -> Dict:
    return {
        "total_domains": len(df),
        "domains": df["domain_label"].tolist() if not df.empty else []
    }
