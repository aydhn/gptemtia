import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchEngineDomain, build_research_engine_domain_id

def build_default_research_engine_domains(profile: AdvancedResearchEngineProfile) -> list[ResearchEngineDomain]:
    domains = [
        "research_engine_profile_domain", "research_engine_context_domain", "research_request_domain",
        "research_result_domain", "research_interface_domain", "data_access_interface_domain",
        "feature_interface_domain", "regime_interface_domain", "ml_interface_domain",
        "backtest_interface_domain", "portfolio_interface_domain", "report_interface_domain",
        "signal_research_interface_domain", "research_gateway_domain", "research_safety_domain",
        "research_quality_domain"
    ]
    return [
        ResearchEngineDomain(
            domain_id=build_research_engine_domain_id(d),
            domain_label=d,
            domain_name=d.replace('_', ' ').title(),
            description=f"{d} module domain",
            required_outputs=[f"{d}_output"],
            warnings=[]
        ) for d in domains
    ]

def build_research_engine_domain_registry(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_research_engine_domains(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_research_engine_domains(df)
    return df, summary

def summarize_research_engine_domains(df: pd.DataFrame) -> dict:
    return {"total_domains": len(df)}
