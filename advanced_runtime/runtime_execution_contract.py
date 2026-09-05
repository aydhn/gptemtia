import pandas as pd
from .runtime_config import AdvancedRuntimeProfile
from .runtime_models import RuntimeContractItem, build_runtime_contract_id

def build_default_execution_contract_items(profile: AdvancedRuntimeProfile) -> list[RuntimeContractItem]:
    areas = [
        "config loading", "path resolution", "DataLake read/write",
        "FeatureStore read/write", "report building", "script dry-run execution",
        "validation", "quality checks", "status reports"
    ]
    items = []
    for a in areas:
        items.append(RuntimeContractItem(
            contract_id=build_runtime_contract_id("exec", a.replace(" ", "_").replace("/", "_")),
            contract_area="exec",
            contract_name=a,
            input_expectation="Valid profile",
            output_expectation="Safe execution",
            forbidden_behavior=[
                "no live trading", "no broker order", "no investment advice",
                "no scraping", "no production deployment", "no model deployment",
                "no external LLM", "no destructive file action"
            ],
            manual_review_required=False
        ))
    return items

def build_runtime_execution_contract(profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_execution_contract_items(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_runtime_execution_contract(df)

def summarize_runtime_execution_contract(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total_contracts": len(df)}
