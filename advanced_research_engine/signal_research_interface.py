import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchInterfaceContract, build_research_interface_contract_id

def build_default_signal_research_interface_items(profile: AdvancedResearchEngineProfile) -> list[ResearchInterfaceContract]:
    return [
        ResearchInterfaceContract(
            contract_id=build_research_interface_contract_id("signal_research_interface"),
            interface_name="signal_research_interface",
            input_contract="data/features/regime/ML/backtest/portfolio refs",
            output_contract="research-only signal candidate reference",
            future_phase_range="158-160",
            forbidden_behavior=['kesin AL/SAT', 'broker order', 'canlı emir', 'yatırım tavsiyesi'],
            manual_review_required=True
        )
    ]

def build_signal_research_interface_contract(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_signal_research_interface_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_signal_research_interface_contract(df)

def summarize_signal_research_interface_contract(df: pd.DataFrame) -> dict:
    return {"contracts": len(df)}
