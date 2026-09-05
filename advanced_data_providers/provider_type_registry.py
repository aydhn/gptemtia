import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_models import ProviderTypeItem, build_provider_type_id
from dataclasses import asdict

def build_default_provider_types(profile: DataProviderAbstractionProfile) -> list[ProviderTypeItem]:
    return [
        ProviderTypeItem(
            provider_type_id=build_provider_type_id("provider_dry_run_fixture"),
            provider_type_label="provider_dry_run_fixture",
            provider_type_name="Dry Run Fixture",
            description="Mock provider.",
            allowed_network=False,
            requires_credentials=False,
            placeholder_only=False,
            warnings=[]
        ),
        ProviderTypeItem(
            provider_type_id=build_provider_type_id("provider_manual_file"),
            provider_type_label="provider_manual_file",
            provider_type_name="Manual File",
            description="Manual file provider.",
            allowed_network=False,
            requires_credentials=False,
            placeholder_only=True,
            warnings=[]
        ),
        ProviderTypeItem(
            provider_type_id=build_provider_type_id("provider_local_cache"),
            provider_type_label="provider_local_cache",
            provider_type_name="Local Cache",
            description="Local cache provider.",
            allowed_network=False,
            requires_credentials=False,
            placeholder_only=True,
            warnings=[]
        ),
        ProviderTypeItem(
            provider_type_id=build_provider_type_id("provider_official_api_placeholder"),
            provider_type_label="provider_official_api_placeholder",
            provider_type_name="Official API Placeholder",
            description="Official API placeholder.",
            allowed_network=False,
            requires_credentials=False,
            placeholder_only=True,
            warnings=[]
        ),
        ProviderTypeItem(
            provider_type_id=build_provider_type_id("provider_licensed_placeholder"),
            provider_type_label="provider_licensed_placeholder",
            provider_type_name="Licensed Placeholder",
            description="Licensed API placeholder.",
            allowed_network=False,
            requires_credentials=False,
            placeholder_only=True,
            warnings=[]
        ),
        ProviderTypeItem(
            provider_type_id=build_provider_type_id("provider_public_package_placeholder"),
            provider_type_label="provider_public_package_placeholder",
            provider_type_name="Public Package Placeholder",
            description="Public package placeholder.",
            allowed_network=False,
            requires_credentials=False,
            placeholder_only=True,
            warnings=[]
        ),
        ProviderTypeItem(
            provider_type_id=build_provider_type_id("provider_user_supplied_dataset"),
            provider_type_label="provider_user_supplied_dataset",
            provider_type_name="User Supplied Dataset",
            description="User supplied dataset.",
            allowed_network=False,
            requires_credentials=False,
            placeholder_only=True,
            warnings=[]
        )
    ]

def build_provider_type_registry(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_provider_types(profile)
    df = pd.DataFrame([asdict(item) for item in items])
    return df, summarize_provider_type_registry(df)

def summarize_provider_type_registry(df: pd.DataFrame) -> dict:
    return {"total_types": len(df)}
