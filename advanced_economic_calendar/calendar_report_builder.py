import pandas as pd
from typing import Dict, Optional

def _md(title: str) -> str:
    return f"# {title}\n\nBu çıktı Phase 110 Economic Calendar Integration No Scraping raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, event yönü kesinlik iddiası, production deployment, model deployment, scraping, external LLM/API çağrısı, gerçek economic calendar provider API çağrısı zorunluluğu veya official approval değildir.\n\n"

def build_calendar_provider_profile_registry_markdown_report(summary: Dict, profile_df: Optional[pd.DataFrame] = None) -> str: return _md("Calendar Provider Profile Registry")
def build_calendar_domain_registry_markdown_report(summary: Dict, domain_df: Optional[pd.DataFrame] = None) -> str: return _md("Calendar Domain Registry")
def build_economic_event_universe_markdown_report(summary: Dict, event_df: Optional[pd.DataFrame] = None) -> str: return _md("Economic Event Universe")
def build_event_indicator_mapping_markdown_report(summary: Dict, mapping_df: Optional[pd.DataFrame] = None) -> str: return _md("Event Indicator Mapping")
def build_calendar_event_schema_markdown_report(summary: Dict, schema_df: Optional[pd.DataFrame] = None) -> str: return _md("Calendar Event Schema")
def build_release_event_schema_markdown_report(summary: Dict, release_df: Optional[pd.DataFrame] = None) -> str: return _md("Release Event Schema")
def build_event_surprise_requirement_markdown_report(summary: Dict, surprise_df: Optional[pd.DataFrame] = None) -> str: return _md("Event Surprise Requirements")
def build_calendar_provider_capability_markdown_report(summary: Dict, capability_df: Optional[pd.DataFrame] = None) -> str: return _md("Calendar Provider Capability")
def build_calendar_provider_registry_markdown_report(summary: Dict, registry_df: Optional[pd.DataFrame] = None) -> str: return _md("Calendar Provider Registry")
def build_calendar_contract_markdown_report(summary: Dict, contract_df: Optional[pd.DataFrame] = None) -> str: return _md("Calendar Contract")
def build_calendar_dry_run_markdown_report(summary: Dict, dry_run_df: Optional[pd.DataFrame] = None) -> str: return _md("Calendar Dry Run Fixture")
def build_calendar_safety_markdown_report(summary: Dict, safety_df: Optional[pd.DataFrame] = None) -> str: return _md("Calendar Safety Boundary")
def build_calendar_health_markdown_report(summary: Dict, health_df: Optional[pd.DataFrame] = None) -> str: return _md("Calendar Health Check")
def build_calendar_quality_markdown_report(summary: Dict, quality: Optional[Dict] = None) -> str: return _md("Calendar Quality Report")
def build_calendar_status_markdown_report(summary: Dict, status_df: Optional[pd.DataFrame] = None) -> str: return _md("Calendar Status Report")
def build_phase_111_handoff_markdown_report(summary: Dict, handoff_text: Optional[str] = None) -> str: return _md("Phase 111 News Metadata Handoff")

def build_calendar_provider_disclaimer() -> str:
    return "Bu çıktı Phase 110 Economic Calendar Integration No Scraping raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, event yönü kesinlik iddiası, production deployment, model deployment, scraping, external LLM/API çağrısı, gerçek economic calendar provider API çağrısı zorunluluğu veya official approval değildir."
