import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_models import ProviderContractItem, build_provider_contract_id
from dataclasses import asdict

def build_default_provider_adapter_contract_items(profile: DataProviderAbstractionProfile) -> list[ProviderContractItem]:
    forbidden_behavior = [
        "no scraping",
        "no browser automation",
        "no hidden API reverse engineering",
        "no paywall bypass",
        "no credential output",
        "no broker/live/order",
        "no investment advice",
        "no deployment",
        "no destructive file action"
    ]
    
    return [
        ProviderContractItem(
            contract_id=build_provider_contract_id("metadata_contract"),
            contract_area="metadata",
            input_expectation="None",
            output_expectation="ProviderMetadata",
            forbidden_behavior=forbidden_behavior,
            manual_review_required=True
        ),
        ProviderContractItem(
            contract_id=build_provider_contract_id("capability_contract"),
            contract_area="capability",
            input_expectation="None",
            output_expectation="list[ProviderCapability]",
            forbidden_behavior=forbidden_behavior,
            manual_review_required=True
        ),
        ProviderContractItem(
            contract_id=build_provider_contract_id("request_validation_contract"),
            contract_area="request_validation",
            input_expectation="ProviderRequest",
            output_expectation="dict with valid flag",
            forbidden_behavior=forbidden_behavior,
            manual_review_required=True
        ),
        ProviderContractItem(
            contract_id=build_provider_contract_id("fetch_response_contract"),
            contract_area="fetch_response",
            input_expectation="ProviderRequest",
            output_expectation="ProviderResponse",
            forbidden_behavior=forbidden_behavior,
            manual_review_required=True
        )
    ]

def build_provider_adapter_contract(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_provider_adapter_contract_items(profile)
    df = pd.DataFrame([asdict(item) for item in items])
    return df, summarize_provider_adapter_contract(df)

def summarize_provider_adapter_contract(df: pd.DataFrame) -> dict:
    return {"total_contracts": len(df)}
