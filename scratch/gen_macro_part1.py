import os
from pathlib import Path

base_dir = Path(r"c:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia")
macro_dir = base_dir / "advanced_macro_providers"
macro_dir.mkdir(parents=True, exist_ok=True)

files = {}

files["__init__.py"] = '"""Macro Provider Layer."""\n'

files["macro_provider_config.py"] = """
from dataclasses import dataclass

@dataclass(frozen=True)
class MacroProviderProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 109
    target_final_phase: int = 160
    next_phase: int = 110
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_directional_macro_claim: bool = False
    allow_model_deployment: bool = False
    allow_production_deployment: bool = False
    allow_web_server: bool = False
    allow_dashboard: bool = False
    allow_gui_tui: bool = False
    allow_external_llm: bool = False
    allow_vector_db: bool = False
    allow_embedding_api: bool = False
    allow_web_scraping: bool = False
    allow_html_scraping: bool = False
    allow_browser_automation_scraping: bool = False
    allow_hidden_api_reverse_engineering: bool = False
    allow_paywall_bypass: bool = False
    allow_rate_limit_abuse: bool = False
    allow_required_network_call: bool = False
    allow_required_paid_api: bool = False
    allow_credential_output: bool = False
    allow_cloud_publish: bool = False
    allow_docker_push: bool = False
    allow_git_tag: bool = False
    allow_archive_creation: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    enable_rates_and_yields: bool = True
    enable_inflation: bool = True
    enable_growth: bool = True
    enable_labor: bool = True
    enable_trade_balance: bool = True
    enable_central_bank_policy: bool = True
    enable_liquidity_indicators: bool = True
    enable_risk_sentiment: bool = True
    enable_yield_curve: bool = True
    enable_dxy_placeholder: bool = True
    enable_release_metadata: bool = True
    enable_revision_policy_requirements: bool = True
    enable_frequency_unit_normalization: bool = True
    enable_manual_file_provider: bool = True
    enable_local_cache_provider: bool = True
    enable_official_api_placeholder: bool = True
    enable_licensed_provider_placeholder: bool = True
    enable_public_dataset_placeholder: bool = True
    enable_dry_run_fixture_provider: bool = True
    enable_capability_matching: bool = True
    enable_preference_resolution: bool = True
    enable_health_check: bool = True
    min_readiness_score: float = 0.45
    min_quality_score: float = 0.45
    enabled: bool = True
    notes: str = ""

def get_default_macro_provider_profile() -> MacroProviderProfile:
    return MacroProviderProfile(
        name="balanced_no_scraping_macro_provider",
        description="Phase 109 no-scraping macro provider layer için dengeli profil.",
        notes="Phase 109 no-scraping macro provider layer için dengeli profil."
    )

def get_macro_provider_profile(name: str) -> MacroProviderProfile:
    if name == "balanced_no_scraping_macro_provider":
        return get_default_macro_provider_profile()
    elif name == "strict_macro_provider_safety":
        return MacroProviderProfile(
            name="strict_macro_provider_safety",
            description="Strict safety profile",
            min_readiness_score=0.65,
            min_quality_score=0.65,
            notes="Scraping, credential output, live/broker, deployment, external API zorunluluğu, yönlü makro iddia ve yatırım tavsiyesi sınırlarını sıkı denetleyen macro provider profili."
        )
    elif name == "macro_dry_run_fixture_focus":
        return MacroProviderProfile(
            name="macro_dry_run_fixture_focus",
            description="Dry run focus",
            notes="Gerçek macro API çağrısı yapmadan macro provider contract ve dry-run fixture testlerine odaklı profil."
        )
    raise ValueError(f"Unknown profile {name}")

def list_macro_provider_profiles(enabled_only: bool = True) -> list[MacroProviderProfile]:
    return [
        get_default_macro_provider_profile(),
        get_macro_provider_profile("strict_macro_provider_safety"),
        get_macro_provider_profile("macro_dry_run_fixture_focus")
    ]

def validate_macro_provider_profiles() -> None:
    pass
"""

files["macro_provider_labels.py"] = """
def list_macro_domain_labels(): return ["macro_provider_profile_domain", "macro_provider_domain", "unknown_macro_domain"]
def list_macro_category_labels(): return ["macro_rates_and_yields", "macro_inflation", "macro_growth", "macro_labor", "macro_trade_balance", "macro_central_bank_policy", "macro_liquidity", "macro_risk_sentiment", "macro_yield_curve", "macro_currency_index", "macro_unknown_category"]
def list_macro_data_type_labels(): return ["macro_data_timeseries", "macro_data_release_metadata", "macro_data_revision_metadata", "macro_data_region_metadata", "macro_data_indicator_metadata", "macro_data_provider_metadata", "macro_data_unknown"]
def list_macro_provider_status_labels(): return ["macro_provider_ready", "macro_provider_ready_with_warnings", "macro_provider_placeholder_only", "macro_provider_missing", "macro_provider_blocked_by_no_scraping_boundary", "macro_provider_needs_manual_review", "macro_provider_unknown"]
def list_macro_risk_labels(): return ["macro_provider_critical_risk", "macro_provider_high_risk", "macro_provider_medium_risk", "macro_provider_low_risk", "macro_provider_info", "macro_provider_unknown_risk"]
def validate_macro_domain_label(label: str): pass
def validate_macro_category_label(label: str): pass
def validate_macro_data_type_label(label: str): pass
def validate_macro_provider_status(label: str): pass
def validate_macro_risk_label(label: str): pass
"""

files["macro_provider_models.py"] = """
from dataclasses import dataclass, asdict

@dataclass
class MacroProviderProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int
    target_final_phase: int
    next_phase: int
    local_only: bool
    non_production: bool
    research_only: bool
    no_scraping: bool
    status_label: str
    warnings: list[str]

@dataclass
class MacroProviderDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class MacroIndicator:
    indicator_id: str
    canonical_indicator: str
    display_name: str
    category_label: str
    region: str
    currency: str
    default_frequency: str
    unit: str
    release_lag_note: str
    revision_note: str
    status_label: str
    warnings: list[str]

@dataclass
class MacroIndicatorCategory:
    category_id: str
    category_label: str
    category_name: str
    description: str
    example_indicators: list[str]
    warnings: list[str]

@dataclass
class MacroRegionMetadata:
    region_id: str
    region_code: str
    region_name: str
    currency_code: str
    central_bank_ref: str
    notes: str
    warnings: list[str]

@dataclass
class MacroSymbolNormalizationRule:
    rule_id: str
    canonical_indicator: str
    provider_name: str
    provider_symbol_pattern: str
    normalized_symbol: str
    notes: str
    manual_review_required: bool

@dataclass
class MacroProviderCapability:
    capability_id: str
    provider_name: str
    provider_type: str
    macro_categories: list[str]
    data_types: list[str]
    frequency_support: list[str]
    region_support: list[str]
    requires_network: bool
    requires_credentials: bool
    supports_local_cache: bool
    no_scraping_compliant: bool
    status_label: str
    warnings: list[str]

@dataclass
class MacroProviderMetadata:
    provider_id: str
    provider_name: str
    provider_type: str
    description: str
    homepage_ref: str
    license_note: str
    credential_policy: str
    no_scraping_policy: str
    macro_coverage_note: str
    status_label: str
    warnings: list[str]

@dataclass
class MacroProviderRequest:
    request_id: str
    provider_name: str
    data_type: str
    indicators: list[str]
    region: str | None
    frequency: str
    start: str | None
    end: str | None
    dry_run: bool
    local_only: bool
    metadata: dict

@dataclass
class MacroProviderResponse:
    response_id: str
    request_id: str
    provider_name: str
    data_type: str
    status_label: str
    output_ref: str
    row_count: int
    schema_ref: str
    warnings: list[str]
    manual_review_required: bool

@dataclass
class MacroProviderError:
    error_id: str
    provider_name: str
    error_type: str
    message: str
    retryable: bool
    blocked_by_safety: bool
    recommendation: str

@dataclass
class MacroProviderContractItem:
    contract_id: str
    contract_area: str
    input_expectation: str
    output_expectation: str
    forbidden_behavior: list[str]
    manual_review_required: bool

@dataclass
class MacroProviderFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool

def build_macro_provider_profile_id(profile_name: str) -> str: return f"profile_{profile_name}"
def build_macro_provider_domain_id(domain_label: str) -> str: return f"domain_{domain_label}"
def build_macro_indicator_id(canonical_indicator: str, region: str) -> str: return f"ind_{canonical_indicator}_{region}"
def build_macro_category_id(category_label: str) -> str: return f"cat_{category_label}"
def build_macro_region_id(region_code: str) -> str: return f"reg_{region_code}"
def build_macro_symbol_normalization_rule_id(canonical_indicator: str, provider_name: str) -> str: return f"norm_{canonical_indicator}_{provider_name}"
def build_macro_provider_capability_id(provider_name: str, data_type: str) -> str: return f"cap_{provider_name}_{data_type}"
def build_macro_provider_metadata_id(provider_name: str) -> str: return f"meta_{provider_name}"
def build_macro_provider_request_id(provider_name: str, data_type: str, frequency: str) -> str: return f"req_{provider_name}_{data_type}_{frequency}"
def build_macro_provider_response_id(request_id: str, provider_name: str) -> str: return f"res_{request_id}_{provider_name}"
def build_macro_provider_error_id(provider_name: str, error_type: str) -> str: return f"err_{provider_name}_{error_type}"
def build_macro_provider_contract_id(contract_area: str) -> str: return f"contract_{contract_area}"
def build_macro_provider_finding_id(title: str) -> str: return f"find_{title}"
"""

files["macro_provider_profile_registry.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderProfileItem, build_macro_provider_profile_id

def build_default_macro_provider_profile_items(profile: MacroProviderProfile) -> list[MacroProviderProfileItem]:
    return [
        MacroProviderProfileItem(
            profile_id=build_macro_provider_profile_id(profile.name),
            profile_name=profile.name,
            current_phase=profile.current_phase,
            target_final_phase=profile.target_final_phase,
            next_phase=profile.next_phase,
            local_only=profile.local_only,
            non_production=profile.non_production,
            research_only=profile.research_only,
            no_scraping=True,
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]

def build_macro_provider_profile_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_provider_profile_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_provider_profile_registry(df)

def summarize_macro_provider_profile_registry(df: pd.DataFrame) -> dict:
    return {"total_profiles": len(df)}
"""

files["macro_provider_domain_registry.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroProviderDomain, build_macro_provider_domain_id

def build_default_macro_provider_domains(profile: MacroProviderProfile) -> list[MacroProviderDomain]:
    return [
        MacroProviderDomain(
            domain_id=build_macro_provider_domain_id("macro_provider_profile"),
            domain_label="macro_provider_profile_domain",
            domain_name="Macro Provider Profile",
            description="Profile configuration",
            required_outputs=[],
            warnings=[]
        )
    ]

def build_macro_provider_domain_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_provider_domains(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_provider_domains(df)

def summarize_macro_provider_domains(df: pd.DataFrame) -> dict:
    return {"total_domains": len(df)}
"""

files["macro_indicator_universe.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroIndicator, build_macro_indicator_id

def build_rates_and_yields_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return [
        MacroIndicator(
            indicator_id=build_macro_indicator_id("US_10Y_YIELD", "US"),
            canonical_indicator="US_10Y_YIELD",
            display_name="US 10 Year Yield",
            category_label="macro_rates_and_yields",
            region="US",
            currency="USD",
            default_frequency="daily",
            unit="percent",
            release_lag_note="End of day",
            revision_note="None",
            status_label="macro_provider_ready",
            warnings=[]
        ),
        MacroIndicator(
            indicator_id=build_macro_indicator_id("US_2Y_YIELD", "US"),
            canonical_indicator="US_2Y_YIELD",
            display_name="US 2 Year Yield",
            category_label="macro_rates_and_yields",
            region="US",
            currency="USD",
            default_frequency="daily",
            unit="percent",
            release_lag_note="End of day",
            revision_note="None",
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]

def build_inflation_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return [
        MacroIndicator(
            indicator_id=build_macro_indicator_id("US_CPI_YOY", "US"),
            canonical_indicator="US_CPI_YOY",
            display_name="US CPI YoY",
            category_label="macro_inflation",
            region="US",
            currency="USD",
            default_frequency="monthly",
            unit="percent",
            release_lag_note="Mid-month",
            revision_note="Frequent",
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]

def build_growth_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return []

def build_labor_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return []

def build_central_bank_policy_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return [
        MacroIndicator(
            indicator_id=build_macro_indicator_id("FED_POLICY_RATE", "US"),
            canonical_indicator="FED_POLICY_RATE",
            display_name="FED Policy Rate",
            category_label="macro_central_bank_policy",
            region="US",
            currency="USD",
            default_frequency="monthly",
            unit="percent",
            release_lag_note="FOMC dates",
            revision_note="None",
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]

def build_risk_sentiment_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return [
        MacroIndicator(
            indicator_id=build_macro_indicator_id("DXY_PLACEHOLDER", "US"),
            canonical_indicator="DXY_PLACEHOLDER",
            display_name="DXY Placeholder",
            category_label="macro_currency_index",
            region="US",
            currency="USD",
            default_frequency="daily",
            unit="index",
            release_lag_note="Realtime",
            revision_note="None",
            status_label="macro_provider_ready",
            warnings=[]
        ),
        MacroIndicator(
            indicator_id=build_macro_indicator_id("US_YIELD_CURVE_10Y2Y", "US"),
            canonical_indicator="US_YIELD_CURVE_10Y2Y",
            display_name="US Yield Curve 10Y-2Y",
            category_label="macro_yield_curve",
            region="US",
            currency="USD",
            default_frequency="daily",
            unit="percent",
            release_lag_note="EOD",
            revision_note="None",
            status_label="macro_provider_ready",
            warnings=[]
        )
    ]

def build_default_macro_indicators(profile: MacroProviderProfile) -> list[MacroIndicator]:
    return (build_rates_and_yields_indicators(profile) + build_inflation_indicators(profile) + 
            build_growth_indicators(profile) + build_labor_indicators(profile) + 
            build_central_bank_policy_indicators(profile) + build_risk_sentiment_indicators(profile))

def build_macro_indicator_universe_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_indicators(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_indicator_universe(df)

def summarize_macro_indicator_universe(df: pd.DataFrame) -> dict:
    return {"total_indicators": len(df)}
"""

files["macro_indicator_categories.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroIndicatorCategory, build_macro_category_id

def build_default_macro_indicator_categories(profile: MacroProviderProfile) -> list[MacroIndicatorCategory]:
    cats = ["rates_and_yields", "inflation", "growth", "labor", "trade_balance", "central_bank_policy", "liquidity", "risk_sentiment", "yield_curve", "currency_index"]
    return [MacroIndicatorCategory(
        category_id=build_macro_category_id(c),
        category_label=f"macro_{c}",
        category_name=c.replace("_", " ").title(),
        description=f"{c} category",
        example_indicators=[],
        warnings=[]
    ) for c in cats]

def build_macro_indicator_category_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_indicator_categories(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_indicator_categories(df)

def summarize_macro_indicator_categories(df: pd.DataFrame) -> dict:
    return {"total_categories": len(df)}
"""

files["macro_region_metadata.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroRegionMetadata, build_macro_region_id

def build_default_macro_region_metadata(profile: MacroProviderProfile) -> list[MacroRegionMetadata]:
    regions = [
        ("US", "USD", "FED", "United States"),
        ("EU", "EUR", "ECB", "Eurozone"),
        ("UK", "GBP", "BOE", "United Kingdom"),
        ("JP", "JPY", "BOJ", "Japan"),
        ("TR", "TRY", "CBRT", "Turkey"),
        ("CN", "CNY", "PBOC", "China")
    ]
    return [MacroRegionMetadata(
        region_id=build_macro_region_id(r[0]),
        region_code=r[0],
        region_name=r[3],
        currency_code=r[1],
        central_bank_ref=r[2],
        notes="",
        warnings=[]
    ) for r in regions]

def build_macro_region_country_currency_metadata_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_region_metadata(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_region_metadata(df)

def summarize_macro_region_metadata(df: pd.DataFrame) -> dict:
    return {"total_regions": len(df)}
"""

files["macro_symbol_normalization.py"] = """
import pandas as pd
from .macro_provider_config import MacroProviderProfile
from .macro_provider_models import MacroSymbolNormalizationRule, build_macro_symbol_normalization_rule_id

def build_default_macro_symbol_normalization_rules(profile: MacroProviderProfile) -> list[MacroSymbolNormalizationRule]:
    return [
        MacroSymbolNormalizationRule(
            rule_id=build_macro_symbol_normalization_rule_id("US_10Y_YIELD", "generic"),
            canonical_indicator="US_10Y_YIELD",
            provider_name="generic",
            provider_symbol_pattern="US10Y",
            normalized_symbol="US_10Y_YIELD",
            notes="",
            manual_review_required=False
        ),
        MacroSymbolNormalizationRule(
            rule_id=build_macro_symbol_normalization_rule_id("FED_POLICY_RATE", "generic"),
            canonical_indicator="FED_POLICY_RATE",
            provider_name="generic",
            provider_symbol_pattern="FEDFUNDS",
            normalized_symbol="FED_POLICY_RATE",
            notes="",
            manual_review_required=False
        )
    ]

def normalize_macro_indicator_symbol(symbol: str, provider_name: str | None = None) -> str:
    if symbol == "US10Y": return "US_10Y_YIELD"
    if symbol == "FEDFUNDS": return "FED_POLICY_RATE"
    return symbol

def denormalize_macro_indicator_symbol(canonical_indicator: str, provider_name: str) -> str:
    return canonical_indicator

def build_macro_symbol_normalization_map(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_macro_symbol_normalization_rules(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_macro_symbol_normalization(df)

def summarize_macro_symbol_normalization(df: pd.DataFrame) -> dict:
    return {"total_rules": len(df)}
"""

for fname, content in files.items():
    with open(macro_dir / fname, "w", encoding="utf-8") as f:
        f.write(content)

print("Part 1 created")
