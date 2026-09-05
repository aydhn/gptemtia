import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchInterfaceContract, build_research_interface_contract_id

def build_default_ml_interface_items(profile: AdvancedResearchEngineProfile) -> list[ResearchInterfaceContract]:
    return [
        ResearchInterfaceContract(
            contract_id=build_research_interface_contract_id("ml_interface"),
            interface_name="ml_interface",
            input_contract="feature matrix, labels, walk-forward config",
            output_contract="research model result reference",
            future_phase_range="136-145",
            forbidden_behavior=['production deployment', 'live inference claim', 'guaranteed performance'],
            manual_review_required=True
        )
    ]

def build_ml_interface_contract(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_ml_interface_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_ml_interface_contract(df)

def summarize_ml_interface_contract(df: pd.DataFrame) -> dict:
    return {"contracts": len(df)}
