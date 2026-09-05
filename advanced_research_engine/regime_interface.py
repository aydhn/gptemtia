import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchInterfaceContract, build_research_interface_contract_id

def build_default_regime_interface_items(profile: AdvancedResearchEngineProfile) -> list[ResearchInterfaceContract]:
    return [
        ResearchInterfaceContract(
            contract_id=build_research_interface_contract_id("regime_interface"),
            interface_name="regime_interface",
            input_contract="feature matrix, macro/context refs",
            output_contract="regime labels/reference",
            future_phase_range="126-135",
            forbidden_behavior=['certainty claim', 'investment advice'],
            manual_review_required=True
        )
    ]

def build_regime_interface_contract(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_regime_interface_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_regime_interface_contract(df)

def summarize_regime_interface_contract(df: pd.DataFrame) -> dict:
    return {"contracts": len(df)}
