import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchInterfaceContract, build_research_interface_contract_id

def build_default_portfolio_interface_items(profile: AdvancedResearchEngineProfile) -> list[ResearchInterfaceContract]:
    return [
        ResearchInterfaceContract(
            contract_id=build_research_interface_contract_id("portfolio_interface"),
            interface_name="portfolio_interface",
            input_contract="candidate signals, risk budget, constraints",
            output_contract="portfolio simulation reference",
            future_phase_range="153-157",
            forbidden_behavior=['real portfolio order', 'broker instruction'],
            manual_review_required=True
        )
    ]

def build_portfolio_interface_contract(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_portfolio_interface_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_portfolio_interface_contract(df)

def summarize_portfolio_interface_contract(df: pd.DataFrame) -> dict:
    return {"contracts": len(df)}
