import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchInterfaceContract, build_research_interface_contract_id

def build_default_report_interface_items(profile: AdvancedResearchEngineProfile) -> list[ResearchInterfaceContract]:
    return [
        ResearchInterfaceContract(
            contract_id=build_research_interface_contract_id("report_interface"),
            interface_name="report_interface",
            input_contract="research outputs",
            output_contract="markdown/txt/csv/json reports",
            future_phase_range="all",
            forbidden_behavior=['investment advice', 'final live signal'],
            manual_review_required=True
        )
    ]

def build_report_interface_contract(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_report_interface_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_report_interface_contract(df)

def summarize_report_interface_contract(df: pd.DataFrame) -> dict:
    return {"contracts": len(df)}
