import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchInterfaceContract, build_research_interface_contract_id

def build_default_data_access_interface_items(profile: AdvancedResearchEngineProfile) -> list[ResearchInterfaceContract]:
    return [
        ResearchInterfaceContract(
            contract_id=build_research_interface_contract_id("data_access_interface"),
            interface_name="data_access_interface",
            input_contract="provider key, symbol universe, timeframe, local cache policy",
            output_contract="normalized data reference",
            future_phase_range="106-115",
            forbidden_behavior=['scraping', 'live broker data dependency', 'mandatory paid API call', 'raw credential output'],
            manual_review_required=True
        )
    ]

def build_data_access_interface_contract(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_data_access_interface_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_data_access_interface_contract(df)

def summarize_data_access_interface_contract(df: pd.DataFrame) -> dict:
    return {"contracts": len(df)}
