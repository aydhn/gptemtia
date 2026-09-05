import os
from pathlib import Path

base_dir = Path(r"c:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia")
macro_dir = base_dir / "advanced_macro_providers"

files = {}

files["macro_timeseries_schema.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile

def build_macro_timeseries_schema_contract(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [
        {"field": "indicator", "type": "str", "required": True},
        {"field": "timestamp", "type": "datetime", "required": True},
        {"field": "value", "type": "float", "required": True},
        {"field": "unit", "type": "str", "required": True},
        {"field": "region", "type": "str", "required": True},
        {"field": "currency", "type": "str", "required": False},
        {"field": "frequency", "type": "str", "required": True},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "retrieval_mode", "type": "str", "required": True},
        {"field": "release_reference", "type": "str", "required": False},
        {"field": "revision_status", "type": "str", "required": False},
        {"field": "data_quality_status", "type": "str", "required": False},
        {"field": "manual_review_required", "type": "bool", "required": True},
    ]
    df = pd.DataFrame(schema)
    return df, summarize_macro_timeseries_schema(df)

def summarize_macro_timeseries_schema(df: pd.DataFrame) -> dict:
    return {"total_fields": len(df)}
"""

files["macro_release_metadata_schema.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile

def build_macro_release_metadata_schema_contract(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [
        {"field": "release_id", "type": "str", "required": True},
        {"field": "indicator", "type": "str", "required": True},
        {"field": "region", "type": "str", "required": True},
        {"field": "scheduled_release_time", "type": "datetime", "required": True},
        {"field": "actual_release_time", "type": "datetime", "required": False},
        {"field": "period_reference", "type": "str", "required": True},
        {"field": "actual", "type": "float", "required": False},
        {"field": "forecast", "type": "float", "required": False},
        {"field": "previous", "type": "float", "required": False},
        {"field": "revised_previous", "type": "float", "required": False},
        {"field": "importance", "type": "str", "required": False},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "retrieval_mode", "type": "str", "required": True},
        {"field": "manual_review_required", "type": "bool", "required": True},
    ]
    df = pd.DataFrame(schema)
    return df, summarize_macro_release_metadata_schema(df)

def summarize_macro_release_metadata_schema(df: pd.DataFrame) -> dict:
    return {"total_fields": len(df)}
"""

files["macro_revision_policy_requirements.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile

def build_default_macro_revision_policy_requirements(profile: MacroProviderProfile) -> pd.DataFrame:
    reqs = [
        {"indicator_category": "macro_inflation", "revision_risk": "high", "vintage_data_needed": True, "previous_value_handling": "keep", "revised_value_handling": "append", "future_phase_owner": "Phase 113", "manual_review_required": True}
    ]
    return pd.DataFrame(reqs)

def build_macro_revision_policy_requirement_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_macro_revision_policy_requirements(profile)
    return df, summarize_macro_revision_policy_requirements(df)

def summarize_macro_revision_policy_requirements(df: pd.DataFrame) -> dict:
    return {"total_requirements": len(df)}
"""

files["macro_frequency_unit_requirements.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile

def build_default_macro_frequency_unit_requirements(profile: MacroProviderProfile) -> pd.DataFrame:
    reqs = [
        {"indicator_category": "macro_inflation", "expected_frequency": "monthly", "allowed_frequency_variants": ["quarterly"], "expected_unit": "percent", "allowed_unit_variants": ["index"], "normalization_note": "", "future_phase_owner": "Phase 113", "manual_review_required": True}
    ]
    return pd.DataFrame(reqs)

def build_macro_frequency_unit_normalization_requirement_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_macro_frequency_unit_requirements(profile)
    return df, summarize_macro_frequency_unit_requirements(df)

def summarize_macro_frequency_unit_requirements(df: pd.DataFrame) -> dict:
    return {"total_requirements": len(df)}
"""

files["macro_provider_capabilities.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderCapability, build_macro_provider_capability_id

def build_default_macro_provider_capabilities(profile: MacroProviderProfile) -> list[MacroProviderCapability]:
    caps = [
        MacroProviderCapability(
            capability_id=build_macro_provider_capability_id("macro_dry_run_fixture_provider", "timeseries"),
            provider_name="macro_dry_run_fixture_provider",
            provider_type="provider_dry_run_fixture",
            macro_categories=["macro_rates_and_yields", "macro_inflation"],
            data_types=["macro_data_timeseries", "macro_data_release_metadata"],
            frequency_support=["daily", "monthly"],
            region_support=["US", "EU"],
            requires_network=False,
            requires_credentials=False,
            supports_local_cache=True,
            no_scraping_compliant=True,
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]
    return caps

def build_macro_provider_capability_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_provider_capabilities(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_provider_capabilities(df)

def summarize_macro_provider_capabilities(df: pd.DataFrame) -> dict:
    return {"total_capabilities": len(df)}
"""

files["macro_provider_metadata.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderMetadata, build_macro_provider_metadata_id

def build_default_macro_provider_metadata(profile: MacroProviderProfile) -> list[MacroProviderMetadata]:
    meta = [
        MacroProviderMetadata(
            provider_id=build_macro_provider_metadata_id("macro_dry_run_fixture_provider"),
            provider_name="macro_dry_run_fixture_provider",
            provider_type="provider_dry_run_fixture",
            description="Dry run fixture for macro",
            homepage_ref="local://dry_run",
            license_note="local",
            credential_policy="not stored/not printed/manual configuration only",
            no_scraping_policy="compliant",
            macro_coverage_note="synthetic",
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]
    return meta

def validate_macro_provider_metadata_item(item: MacroProviderMetadata, profile: MacroProviderProfile) -> dict:
    return {"valid": True}

def build_macro_provider_metadata_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_provider_metadata(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_provider_metadata(df)

def summarize_macro_provider_metadata(df: pd.DataFrame) -> dict:
    return {"total_metadata": len(df)}
"""

files["macro_provider_request.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderRequest, build_macro_provider_request_id
from .macro_symbol_normalization import normalize_macro_indicator_symbol

def build_macro_provider_request_schema(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [{"field": "request_id", "type": "str"}]
    df = pd.DataFrame(schema)
    return df, {"total_fields": 1}

def create_macro_provider_request(
    provider_name: str,
    data_type: str,
    indicators: list[str] | None = None,
    region: str | None = None,
    frequency: str = "monthly",
    start: str | None = None,
    end: str | None = None,
    dry_run: bool = True,
    local_only: bool = True,
    metadata: dict | None = None,
) -> MacroProviderRequest:
    norm_inds = [normalize_macro_indicator_symbol(ind, provider_name) for ind in (indicators or [])]
    return MacroProviderRequest(
        request_id=build_macro_provider_request_id(provider_name, data_type, frequency),
        provider_name=provider_name,
        data_type=data_type,
        indicators=norm_inds,
        region=region,
        frequency=frequency,
        start=start,
        end=end,
        dry_run=dry_run,
        local_only=local_only,
        metadata=metadata or {}
    )

def validate_macro_provider_request(request: MacroProviderRequest, profile: MacroProviderProfile) -> dict:
    return {"valid": True}

def macro_provider_request_to_dict(request: MacroProviderRequest) -> dict:
    return vars(request)
"""

files["macro_provider_response.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderResponse, build_macro_provider_response_id

def build_macro_provider_response_schema(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [{"field": "response_id", "type": "str"}]
    df = pd.DataFrame(schema)
    return df, {"total_fields": 1}

def create_macro_provider_response(
    request_id: str,
    provider_name: str,
    data_type: str,
    status_label: str,
    output_ref: str = "",
    row_count: int = 0,
    schema_ref: str = "",
    warnings: list[str] | None = None,
    manual_review_required: bool = True,
) -> MacroProviderResponse:
    return MacroProviderResponse(
        response_id=build_macro_provider_response_id(request_id, provider_name),
        request_id=request_id,
        provider_name=provider_name,
        data_type=data_type,
        status_label=status_label,
        output_ref=output_ref,
        row_count=row_count,
        schema_ref=schema_ref,
        warnings=warnings or [],
        manual_review_required=manual_review_required
    )

def validate_macro_provider_response(response: MacroProviderResponse, profile: MacroProviderProfile) -> dict:
    return {"valid": True}

def macro_provider_response_to_dict(response: MacroProviderResponse) -> dict:
    return vars(response)
"""

files["macro_provider_errors.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderError, build_macro_provider_error_id

def build_macro_provider_error_schema(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    schema = [{"field": "error_id", "type": "str"}]
    df = pd.DataFrame(schema)
    return df, {"total_fields": 1}

def create_macro_provider_error(provider_name: str, error_type: str, message: str, retryable: bool = False, blocked_by_safety: bool = False, recommendation: str = "") -> MacroProviderError:
    return MacroProviderError(
        error_id=build_macro_provider_error_id(provider_name, error_type),
        provider_name=provider_name,
        error_type=error_type,
        message=message,
        retryable=retryable,
        blocked_by_safety=blocked_by_safety,
        recommendation=recommendation
    )

def macro_provider_error_to_dict(error: MacroProviderError) -> dict:
    return vars(error)

def summarize_macro_provider_errors(df: pd.DataFrame) -> dict:
    return {"total_errors": len(df)}
"""

for fname, content in files.items():
    with open(macro_dir / fname, "w", encoding="utf-8") as f:
        f.write(content)

print("Part 2 created")
