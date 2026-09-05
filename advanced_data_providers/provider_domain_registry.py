import pandas as pd
from .provider_config import DataProviderAbstractionProfile
from .provider_models import ProviderDomain, build_provider_domain_id
from dataclasses import asdict

def build_default_provider_domains(profile: DataProviderAbstractionProfile) -> list[ProviderDomain]:
    return [
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_profile_domain"),
            domain_label="provider_profile_domain",
            domain_name="Provider Profile",
            description="Profile settings.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_type_domain"),
            domain_label="provider_type_domain",
            domain_name="Provider Type",
            description="Provider types.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_capability_domain"),
            domain_label="provider_capability_domain",
            domain_name="Provider Capability",
            description="Provider capabilities.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_metadata_domain"),
            domain_label="provider_metadata_domain",
            domain_name="Provider Metadata",
            description="Provider metadata.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_request_domain"),
            domain_label="provider_request_domain",
            domain_name="Provider Request",
            description="Provider requests.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_response_domain"),
            domain_label="provider_response_domain",
            domain_name="Provider Response",
            description="Provider responses.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_error_domain"),
            domain_label="provider_error_domain",
            domain_name="Provider Error",
            description="Provider errors.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_interface_domain"),
            domain_label="provider_interface_domain",
            domain_name="Provider Interface",
            description="Provider interfaces.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_adapter_contract_domain"),
            domain_label="provider_adapter_contract_domain",
            domain_name="Provider Adapter Contract",
            description="Provider adapter contracts.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_registry_domain"),
            domain_label="provider_registry_domain",
            domain_name="Provider Registry",
            description="Provider registry.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_resolver_domain"),
            domain_label="provider_resolver_domain",
            domain_name="Provider Resolver",
            description="Provider resolvers.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_preference_domain"),
            domain_label="provider_preference_domain",
            domain_name="Provider Preference",
            description="Provider preferences.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_capability_matcher_domain"),
            domain_label="provider_capability_matcher_domain",
            domain_name="Provider Capability Matcher",
            description="Provider capability matchers.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_fixture_domain"),
            domain_label="provider_fixture_domain",
            domain_name="Provider Fixture",
            description="Provider fixtures.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_placeholder_domain"),
            domain_label="provider_placeholder_domain",
            domain_name="Provider Placeholder",
            description="Provider placeholders.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_output_schema_domain"),
            domain_label="provider_output_schema_domain",
            domain_name="Provider Output Schema",
            description="Provider output schemas.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_safety_domain"),
            domain_label="provider_safety_domain",
            domain_name="Provider Safety",
            description="Provider safety.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_health_domain"),
            domain_label="provider_health_domain",
            domain_name="Provider Health",
            description="Provider health.",
            required_outputs=[],
            warnings=[]
        ),
        ProviderDomain(
            domain_id=build_provider_domain_id("provider_quality_domain"),
            domain_label="provider_quality_domain",
            domain_name="Provider Quality",
            description="Provider quality.",
            required_outputs=[],
            warnings=[]
        )
    ]

def build_provider_domain_registry(profile: DataProviderAbstractionProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_provider_domains(profile)
    df = pd.DataFrame([asdict(item) for item in items])
    return df, summarize_provider_domains(df)

def summarize_provider_domains(df: pd.DataFrame) -> dict:
    return {"total_domains": len(df)}
