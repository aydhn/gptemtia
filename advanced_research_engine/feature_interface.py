import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchInterfaceContract, build_research_interface_contract_id

def build_default_feature_interface_items(profile: AdvancedResearchEngineProfile) -> list[ResearchInterfaceContract]:
    return [
        ResearchInterfaceContract(
            contract_id=build_research_interface_contract_id("feature_interface"),
            interface_name="feature_interface",
            input_contract="normalized data reference, feature profile",
            output_contract="feature matrix reference",
            future_phase_range="116-125",
            forbidden_behavior=['data leakage', 'lookahead', 'live signal claim'],
            manual_review_required=True
        )
    ]

def build_feature_interface_contract(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_feature_interface_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_feature_interface_contract(df)

def summarize_feature_interface_contract(df: pd.DataFrame) -> dict:
    return {"contracts": len(df)}
