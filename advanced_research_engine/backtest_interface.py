import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchInterfaceContract, build_research_interface_contract_id

def build_default_backtest_interface_items(profile: AdvancedResearchEngineProfile) -> list[ResearchInterfaceContract]:
    return [
        ResearchInterfaceContract(
            contract_id=build_research_interface_contract_id("backtest_interface"),
            interface_name="backtest_interface",
            input_contract="strategy/signal research refs, cost/slippage config",
            output_contract="backtest result reference",
            future_phase_range="146-152",
            forbidden_behavior=['live trading approval', 'unrealistic guarantee'],
            manual_review_required=True
        )
    ]

def build_backtest_interface_contract(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_backtest_interface_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_backtest_interface_contract(df)

def summarize_backtest_interface_contract(df: pd.DataFrame) -> dict:
    return {"contracts": len(df)}
