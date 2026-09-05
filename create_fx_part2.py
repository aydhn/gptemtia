import os

def w(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

w("advanced_fx_providers/fx_symbol_normalization.py", '''
import pandas as pd
from typing import Tuple, Dict, List, Optional
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXSymbolNormalizationRule, build_fx_symbol_normalization_rule_id
import re

def build_default_fx_symbol_normalization_rules(profile: FXProviderProfile) -> List[FXSymbolNormalizationRule]:
    return [
        FXSymbolNormalizationRule(
            rule_id=build_fx_symbol_normalization_rule_id("generic", "compact"),
            canonical_pair="generic", provider_name="generic", provider_symbol_pattern="compact",
            normalized_symbol="compact", notes="E.g. EURUSD", manual_review_required=False
        ),
        FXSymbolNormalizationRule(
            rule_id=build_fx_symbol_normalization_rule_id("generic", "slash"),
            canonical_pair="generic", provider_name="generic", provider_symbol_pattern="slash",
            normalized_symbol="slash", notes="E.g. EUR/USD", manual_review_required=False
        )
    ]

def normalize_fx_pair_symbol(symbol: str, provider_name: Optional[str] = None) -> str:
    # Basic heuristic for normalization to XXX/YYY
    symbol = symbol.strip().upper()
    symbol = re.sub(r'[^A-Z]', '', symbol)
    if len(symbol) == 6:
        return f"{symbol[:3]}/{symbol[3:]}"
    return symbol # Graceful fallback

def denormalize_fx_pair_symbol(canonical_pair: str, provider_name: str) -> str:
    # Mock denormalization for placeholder
    if provider_name == "generic_compact":
        return canonical_pair.replace("/", "")
    return canonical_pair

def build_fx_symbol_normalization_map(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_symbol_normalization_rules(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_symbol_normalization(df)

def summarize_fx_symbol_normalization(df: pd.DataFrame) -> Dict:
    return {"total_rules": len(df)}
''')

w("advanced_fx_providers/fx_quote_schema.py", '''
import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def build_fx_quote_schema_contract(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field": "pair", "type": "str", "required": True},
        {"field": "timestamp", "type": "datetime", "required": True},
        {"field": "bid", "type": "float", "required": True},
        {"field": "ask", "type": "float", "required": True},
        {"field": "mid", "type": "float", "required": False},
        {"field": "spread", "type": "float", "required": False},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "retrieval_mode", "type": "str", "required": True},
        {"field": "data_quality_status", "type": "str", "required": True},
        {"field": "manual_review_required", "type": "bool", "required": True},
    ]
    df = pd.DataFrame(schema)
    return df, summarize_fx_quote_schema(df)

def summarize_fx_quote_schema(df: pd.DataFrame) -> Dict:
    return {"total_fields": len(df), "warnings": ["Quote schema is abstract and does not represent live market data."]}
''')

w("advanced_fx_providers/fx_ohlcv_schema.py", '''
import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def build_fx_ohlcv_schema_contract(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field": "pair", "type": "str", "required": True},
        {"field": "timestamp", "type": "datetime", "required": True},
        {"field": "open", "type": "float", "required": True},
        {"field": "high", "type": "float", "required": True},
        {"field": "low", "type": "float", "required": True},
        {"field": "close", "type": "float", "required": True},
        {"field": "volume", "type": "float", "required": False},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "retrieval_mode", "type": "str", "required": True},
        {"field": "adjusted_flag", "type": "bool", "required": True},
        {"field": "data_quality_status", "type": "str", "required": True},
        {"field": "manual_review_required", "type": "bool", "required": True},
    ]
    df = pd.DataFrame(schema)
    return df, summarize_fx_ohlcv_schema(df)

def summarize_fx_ohlcv_schema(df: pd.DataFrame) -> Dict:
    return {"total_fields": len(df), "warnings": ["FX spot volume represents tick count or dealer volume; use with caution."]}
''')

w("advanced_fx_providers/fx_cross_rate_requirements.py", '''
import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def build_default_fx_cross_rate_requirements(profile: FXProviderProfile) -> pd.DataFrame:
    reqs = [
        {"target_pair": "EUR/JPY", "required_base_leg": "EUR/USD", "required_quote_leg": "USD/JPY", "cross_rate_formula_note": "EUR/USD * USD/JPY", "provider_dependency": "generic", "precision_note": "slippage not included", "manual_review_required": True},
        {"target_pair": "GBP/JPY", "required_base_leg": "GBP/USD", "required_quote_leg": "USD/JPY", "cross_rate_formula_note": "GBP/USD * USD/JPY", "provider_dependency": "generic", "precision_note": "slippage not included", "manual_review_required": True},
        {"target_pair": "EUR/GBP", "required_base_leg": "EUR/USD", "required_quote_leg": "GBP/USD", "cross_rate_formula_note": "EUR/USD / GBP/USD", "provider_dependency": "generic", "precision_note": "slippage not included", "manual_review_required": True},
        {"target_pair": "AUD/NZD", "required_base_leg": "AUD/USD", "required_quote_leg": "NZD/USD", "cross_rate_formula_note": "AUD/USD / NZD/USD", "provider_dependency": "generic", "precision_note": "slippage not included", "manual_review_required": True}
    ]
    return pd.DataFrame(reqs)

def build_fx_cross_rate_requirement_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_fx_cross_rate_requirements(profile)
    return df, summarize_fx_cross_rate_requirements(df)

def summarize_fx_cross_rate_requirements(df: pd.DataFrame) -> Dict:
    return {"total_requirements": len(df), "warnings": ["Cross-rate calculations are not investment advice or exact prices."]}
''')

w("advanced_fx_providers/fx_provider_capabilities.py", '''
import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderCapability, build_fx_provider_capability_id

def build_default_fx_provider_capabilities(profile: FXProviderProfile) -> List[FXProviderCapability]:
    caps = [
        ("fx_dry_run_fixture_provider", "provider_dry_run_fixture", ["fx_major_pair", "fx_minor_pair"], ["fx_data_ohlcv", "fx_data_quote"]),
        ("fx_manual_file_provider_placeholder", "provider_manual_file", ["fx_major_pair"], ["fx_data_ohlcv"]),
        ("fx_local_cache_provider_placeholder", "provider_local_cache", ["fx_major_pair"], ["fx_data_ohlcv"]),
        ("fx_official_api_provider_placeholder", "provider_official_api", ["fx_major_pair", "fx_minor_pair", "fx_exotic_pair"], ["fx_data_ohlcv", "fx_data_quote"]),
        ("fx_licensed_provider_placeholder", "provider_licensed", ["fx_major_pair"], ["fx_data_ohlcv"])
    ]
    return [
        FXProviderCapability(
            capability_id=build_fx_provider_capability_id(c[0], c[3][0]), provider_name=c[0], provider_type=c[1],
            pair_groups=c[2], data_types=c[3], timeframe_support=["1d", "1h", "1m"], requires_network=False,
            requires_credentials=False, supports_local_cache=True, no_scraping_compliant=True,
            status_label="fx_provider_ready", warnings=[]
        ) for c in caps
    ]

def build_fx_provider_capability_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_provider_capabilities(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_provider_capabilities(df)

def summarize_fx_provider_capabilities(df: pd.DataFrame) -> Dict:
    return {"total_capabilities": len(df)}
''')

w("advanced_fx_providers/fx_provider_metadata.py", '''
import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderMetadata, build_fx_provider_metadata_id

def build_default_fx_provider_metadata(profile: FXProviderProfile) -> List[FXProviderMetadata]:
    providers = [
        ("fx_dry_run_fixture_provider", "provider_dry_run_fixture"),
        ("fx_manual_file_provider_placeholder", "provider_manual_file"),
        ("fx_local_cache_provider_placeholder", "provider_local_cache"),
        ("fx_official_api_provider_placeholder", "provider_official_api"),
        ("fx_licensed_provider_placeholder", "provider_licensed")
    ]
    return [
        FXProviderMetadata(
            provider_id=build_fx_provider_metadata_id(p[0]), provider_name=p[0], provider_type=p[1],
            description=f"Placeholder for {p[0]}", homepage_ref="https://example.com/no-credential",
            license_note="Mock license", credential_policy="not stored/not printed/manual configuration only",
            no_scraping_policy="strict no-scraping", fx_coverage_note="Basic major pairs",
            status_label="fx_provider_ready", warnings=[]
        ) for p in providers
    ]

def validate_fx_provider_metadata_item(item: FXProviderMetadata, profile: FXProviderProfile) -> Dict:
    return {"valid": True, "errors": []}

def build_fx_provider_metadata_registry(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_fx_provider_metadata(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_fx_provider_metadata(df)

def summarize_fx_provider_metadata(df: pd.DataFrame) -> Dict:
    return {"total_metadata": len(df)}
''')

w("advanced_fx_providers/fx_provider_request.py", '''
import pandas as pd
from typing import Tuple, Dict, List, Optional
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderRequest, build_fx_provider_request_id
from .fx_symbol_normalization import normalize_fx_pair_symbol

def build_fx_provider_request_schema(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field": "request_id", "type": "str", "required": True},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "data_type", "type": "str", "required": True},
        {"field": "pairs", "type": "list[str]", "required": True},
        {"field": "timeframe", "type": "str", "required": True},
        {"field": "start", "type": "str", "required": False},
        {"field": "end", "type": "str", "required": False},
        {"field": "dry_run", "type": "bool", "required": True},
        {"field": "local_only", "type": "bool", "required": True},
        {"field": "metadata", "type": "dict", "required": False}
    ]
    return pd.DataFrame(schema), {"total_fields": len(schema)}

def create_fx_provider_request(
    provider_name: str,
    data_type: str,
    pairs: Optional[List[str]] = None,
    timeframe: str = "1d",
    start: Optional[str] = None,
    end: Optional[str] = None,
    dry_run: bool = True,
    local_only: bool = True,
    metadata: Optional[Dict] = None,
) -> FXProviderRequest:
    normalized_pairs = [normalize_fx_pair_symbol(p, provider_name) for p in (pairs or [])]
    return FXProviderRequest(
        request_id=build_fx_provider_request_id(provider_name, data_type, timeframe),
        provider_name=provider_name, data_type=data_type, pairs=normalized_pairs,
        timeframe=timeframe, start=start, end=end, dry_run=dry_run, local_only=local_only,
        metadata=metadata or {}
    )

def validate_fx_provider_request(request: FXProviderRequest, profile: FXProviderProfile) -> Dict:
    valid = request.dry_run and request.local_only
    return {"valid": valid, "errors": [] if valid else ["Must be dry_run and local_only"]}

def fx_provider_request_to_dict(request: FXProviderRequest) -> Dict:
    return request.to_dict()
''')

w("advanced_fx_providers/fx_provider_response.py", '''
import pandas as pd
from typing import Tuple, Dict, List, Optional
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderResponse, build_fx_provider_response_id

def build_fx_provider_response_schema(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field": "response_id", "type": "str", "required": True},
        {"field": "request_id", "type": "str", "required": True},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "data_type", "type": "str", "required": True},
        {"field": "status_label", "type": "str", "required": True},
        {"field": "output_ref", "type": "str", "required": True},
        {"field": "row_count", "type": "int", "required": True},
        {"field": "schema_ref", "type": "str", "required": True},
        {"field": "warnings", "type": "list[str]", "required": True},
        {"field": "manual_review_required", "type": "bool", "required": True}
    ]
    return pd.DataFrame(schema), {"total_fields": len(schema)}

def create_fx_provider_response(
    request_id: str,
    provider_name: str,
    data_type: str,
    status_label: str,
    output_ref: str = "",
    row_count: int = 0,
    schema_ref: str = "",
    warnings: Optional[List[str]] = None,
    manual_review_required: bool = True,
) -> FXProviderResponse:
    return FXProviderResponse(
        response_id=build_fx_provider_response_id(request_id, provider_name),
        request_id=request_id, provider_name=provider_name, data_type=data_type,
        status_label=status_label, output_ref=output_ref, row_count=row_count,
        schema_ref=schema_ref, warnings=warnings or [], manual_review_required=manual_review_required
    )

def validate_fx_provider_response(response: FXProviderResponse, profile: FXProviderProfile) -> Dict:
    return {"valid": True, "errors": []}

def fx_provider_response_to_dict(response: FXProviderResponse) -> Dict:
    return response.to_dict()
''')

w("advanced_fx_providers/fx_provider_errors.py", '''
import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile
from .fx_provider_models import FXProviderError, build_fx_provider_error_id

def build_fx_provider_error_schema(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    schema = [
        {"field": "error_id", "type": "str", "required": True},
        {"field": "provider_name", "type": "str", "required": True},
        {"field": "error_type", "type": "str", "required": True},
        {"field": "message", "type": "str", "required": True},
        {"field": "retryable", "type": "bool", "required": True},
        {"field": "blocked_by_safety", "type": "bool", "required": True},
        {"field": "recommendation", "type": "str", "required": True}
    ]
    df = pd.DataFrame(schema)
    return df, summarize_fx_provider_errors(df)

def create_fx_provider_error(provider_name: str, error_type: str, message: str, retryable: bool = False, blocked_by_safety: bool = False, recommendation: str = "") -> FXProviderError:
    return FXProviderError(
        error_id=build_fx_provider_error_id(provider_name, error_type),
        provider_name=provider_name, error_type=error_type, message=message,
        retryable=retryable, blocked_by_safety=blocked_by_safety, recommendation=recommendation
    )

def fx_provider_error_to_dict(error: FXProviderError) -> Dict:
    return error.to_dict()

def summarize_fx_provider_errors(df: pd.DataFrame) -> Dict:
    return {"total_fields": len(df)}
''')
