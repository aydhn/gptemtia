import pandas as pd
from typing import Dict, Optional

def build_news_provider_disclaimer() -> str:
    return "Bu çıktı Phase 111 News Metadata Integration No Scraping raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, haber yönü kesinlik iddiası, sentiment sinyali, haber tam metni toplama, telifli içerik kopyalama, production deployment, model/NLP deployment, scraping, external LLM/API çağrısı, gerçek news provider API çağrısı zorunluluğu veya official approval değildir."

def _md(title: str) -> str:
    return f"# {title}\n\n{build_news_provider_disclaimer()}\n\n"

def build_news_provider_profile_registry_markdown_report(summary: Dict, profile_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Provider Profile Registry")

def build_news_domain_registry_markdown_report(summary: Dict, domain_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Domain Registry")

def build_news_source_registry_markdown_report(summary: Dict, source_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Source Registry")

def build_news_metadata_schema_markdown_report(summary: Dict, schema_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Metadata Schema Contract")

def build_news_item_reference_schema_markdown_report(summary: Dict, ref_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Item Reference Schema Contract")

def build_news_tag_registry_markdown_report(summary: Dict, tag_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Tag Registries (Asset / Macro / Commodity / FX)")

def build_news_event_linkage_markdown_report(summary: Dict, linkage_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Event Linkage Registry")

def build_news_sentiment_requirement_markdown_report(summary: Dict, sentiment_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Sentiment Placeholder Requirements")

def build_news_impact_requirement_markdown_report(summary: Dict, impact_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Impact Placeholder Requirements")

def build_news_provider_capability_markdown_report(summary: Dict, capability_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Provider Capability Registry")

def build_news_provider_registry_markdown_report(summary: Dict, registry_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Provider Registry")

def build_news_contract_markdown_report(summary: Dict, contract_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Adapter Contract")

def build_news_dry_run_markdown_report(summary: Dict, dry_run_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Dry Run Fixture Report")

def build_news_safety_markdown_report(summary: Dict, safety_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Safety Boundary")

def build_news_health_markdown_report(summary: Dict, health_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Health Check")

def build_news_quality_markdown_report(summary: Dict, quality: Optional[Dict] = None) -> str:
    return _md("News Quality Report")

def build_news_status_markdown_report(summary: Dict, status_df: Optional[pd.DataFrame] = None) -> str:
    return _md("News Provider Status Report")

def build_phase_112_handoff_markdown_report(summary: Dict, handoff_text: Optional[str] = None) -> str:
    return _md("Phase 112 Data Quality Engine Handoff Report")
