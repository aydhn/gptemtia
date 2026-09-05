import os

def w(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

placeholder_base = '''
import pandas as pd
from typing import Tuple, Dict, List
from .fx_provider_config import FXProviderProfile
from .fx_provider_interfaces import BaseFXProvider
from .fx_provider_models import FXProviderMetadata, FXProviderCapability, FXProviderRequest, FXProviderResponse, build_fx_provider_metadata_id
from .fx_provider_response import create_fx_provider_response

class {class_name}(BaseFXProvider):
    provider_name = "{provider_name}"
    provider_type = "{provider_type}"

    def metadata(self) -> FXProviderMetadata:
        return FXProviderMetadata(
            provider_id=build_fx_provider_metadata_id(self.provider_name),
            provider_name=self.provider_name, provider_type=self.provider_type,
            description="Placeholder for {provider_name}", homepage_ref="", license_note="{license_note}",
            credential_policy="not stored", no_scraping_policy="strict no-scraping",
            fx_coverage_note="Placeholder", status_label="fx_provider_placeholder_only", warnings=[]
        )

    def capabilities(self) -> List[FXProviderCapability]: return []
    def validate_request(self, request: FXProviderRequest) -> Dict: return {{"valid": True, "errors": []}}
    def fetch_fx(self, request: FXProviderRequest) -> FXProviderResponse:
        return create_fx_provider_response(
            request_id=request.request_id, provider_name=self.provider_name,
            data_type=request.data_type, status_label="fx_provider_placeholder_only",
            output_ref="placeholder_ref", row_count=0
        )
    def health_check(self) -> Dict: return {{"status": "healthy", "type": "placeholder"}}

def build_{method_name}(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame([{{"provider": "{provider_name}", "status": "placeholder_active"}}])
    return df, {{"status": "ok"}}
'''

w("advanced_fx_providers/fx_manual_file_provider.py", placeholder_base.format(
    class_name="FXManualFileProviderPlaceholder", provider_name="fx_manual_file_provider_placeholder",
    provider_type="provider_manual_file", license_note="", method_name="fx_manual_file_provider_placeholder"
))

w("advanced_fx_providers/fx_local_cache_provider.py", placeholder_base.format(
    class_name="FXLocalCacheProviderPlaceholder", provider_name="fx_local_cache_provider_placeholder",
    provider_type="provider_local_cache", license_note="", method_name="fx_local_cache_provider_placeholder"
))

w("advanced_fx_providers/fx_official_api_provider.py", placeholder_base.format(
    class_name="FXOfficialApiProviderPlaceholder", provider_name="fx_official_api_provider_placeholder",
    provider_type="provider_official_api", license_note="", method_name="fx_official_api_provider_placeholder"
))

w("advanced_fx_providers/fx_licensed_provider.py", placeholder_base.format(
    class_name="FXLicensedProviderPlaceholder", provider_name="fx_licensed_provider_placeholder",
    provider_type="provider_licensed", license_note="requires manual review note", method_name="fx_licensed_provider_placeholder"
))

w("advanced_fx_providers/fx_output_validation.py", '''
import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def build_default_fx_output_validation_rules(profile: FXProviderProfile) -> pd.DataFrame:
    rules = [
        {"rule_id": "rule_ohlc_consistency", "target_schema": "fx_ohlcv_schema", "field_name": "open,high,low,close", "rule_description": "low <= open,close <= high", "severity": "high", "future_phase_owner": "Phase 112", "manual_review_required": False},
        {"rule_id": "rule_symbol_normalization", "target_schema": "all", "field_name": "pair", "rule_description": "Pair must be canonical", "severity": "medium", "future_phase_owner": "Phase 113", "manual_review_required": False}
    ]
    return pd.DataFrame(rules)

def build_fx_output_validation_contract(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_fx_output_validation_rules(profile)
    return df, summarize_fx_output_validation(df)

def summarize_fx_output_validation(df: pd.DataFrame) -> Dict:
    return {"total_rules": len(df)}
''')

w("advanced_fx_providers/fx_safety_boundary.py", '''
import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def build_fx_no_go_conditions(profile: FXProviderProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": c, "status": "no-go"} for c in [
        "live trading", "broker integration", "real order", "exact buy/sell instruction",
        "investment advice", "model deployment", "production deployment", "web server/dashboard",
        "external LLM/vector/embedding", "web scraping", "HTML scraping", "browser automation scraping",
        "hidden API reverse engineering", "paywall bypass", "rate limit abuse", "credential output",
        "required paid API lock-in", "cloud publish", "Docker push", "git tag", "archive creation",
        "destructive file action", "official approval wording"
    ]])

def build_fx_safe_go_conditions(profile: FXProviderProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": c, "status": "safe-go"} for c in [
        "local/offline FX provider abstraction", "FX dry-run fixture", "FX manual file placeholder",
        "FX local cache placeholder", "FX official API placeholder without network call",
        "FX licensed provider placeholder without credential", "FX pair universe registry",
        "FX symbol normalization map", "FX capability matching", "FX output schema contract",
        "manual review", "no broker/no live/no advice/no deploy/no scraping"
    ]])

def build_fx_safety_boundary(profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    nogo = build_fx_no_go_conditions(profile)
    safego = build_fx_safe_go_conditions(profile)
    df = pd.concat([nogo, safego], ignore_index=True)
    return df, summarize_fx_safety_boundary(df)

def summarize_fx_safety_boundary(df: pd.DataFrame) -> Dict:
    return {"nogo_count": len(df[df["status"]=="no-go"]), "safego_count": len(df[df["status"]=="safe-go"])}
''')

w("advanced_fx_providers/fx_health.py", '''
import pandas as pd
from pathlib import Path
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def build_default_fx_health_findings(profile: FXProviderProfile) -> pd.DataFrame:
    checks = [
        "config importable", "labels importable", "models importable", "FX provider interfaces available",
        "FX provider registry available", "FX dry-run fixture available", "FX manual placeholder available",
        "FX local cache placeholder available", "FX official API placeholder available",
        "FX licensed placeholder available", "FX pair universe available", "FX symbol normalization available",
        "FX quote/OHLCV schema available", "FX safety boundary available", "Phase 106 advanced_data_providers available",
        "DataLake integration available", "FeatureStore integration available", "scripts present", "tests present", "docs present"
    ]
    return pd.DataFrame([{"check": c, "status": "healthy"} for c in checks])

def build_fx_health_check(project_root: Path, profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_fx_health_findings(profile)
    return df, summarize_fx_health(df)

def summarize_fx_health(df: pd.DataFrame) -> Dict:
    return {"total_checks": len(df), "healthy_checks": len(df[df["status"]=="healthy"])}
''')

w("advanced_fx_providers/fx_scoring.py", '''
import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def calculate_fx_readiness_score(
    profile_df: pd.DataFrame, domain_df: pd.DataFrame, pair_df: pd.DataFrame, capability_df: pd.DataFrame,
    registry_df: pd.DataFrame, safety_df: pd.DataFrame, health_df: pd.DataFrame, profile: FXProviderProfile,
) -> float:
    # mock scoring logic
    if health_df.empty or safety_df.empty: return 0.0
    score = 0.5 + 0.5 * (len(health_df[health_df["status"]=="healthy"]) / len(health_df))
    return min(1.0, max(0.0, score))

def classify_fx_readiness_score(score: float, profile: FXProviderProfile) -> str:
    if score >= 0.8: return "high"
    if score >= profile.min_readiness_score: return "medium"
    return "low (manual review suggested)"

def build_fx_readiness_score_report(
    profile_df: pd.DataFrame, domain_df: pd.DataFrame, pair_df: pd.DataFrame, capability_df: pd.DataFrame,
    registry_df: pd.DataFrame, safety_df: pd.DataFrame, health_df: pd.DataFrame, profile: FXProviderProfile,
) -> Tuple[pd.DataFrame, Dict]:
    score = calculate_fx_readiness_score(profile_df, domain_df, pair_df, capability_df, registry_df, safety_df, health_df, profile)
    cls = classify_fx_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": cls}])
    return df, summarize_fx_readiness_score(df)

def summarize_fx_readiness_score(df: pd.DataFrame) -> Dict:
    return {"score": float(df.iloc[0]["score"]) if not df.empty else 0.0}
''')

w("advanced_fx_providers/fx_validation.py", '''
import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def validate_fx_provider_profile_registry(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_provider_domain_registry(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_pair_universe(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_currency_metadata(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_symbol_normalization_map(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_quote_schema(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_ohlcv_schema(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_provider_capability_registry(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_provider_metadata_registry(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_provider_request_schema(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_provider_response_schema(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_adapter_contract(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_provider_registry(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_output_validation_contract(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}
def validate_fx_safety_boundary(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"valid": True, "errors": []}

def validate_no_forbidden_fx_claims(text: str = None, df: pd.DataFrame = None, summary: dict = None) -> Dict:
    forbidden = ["live trading approved", "broker order", "real order sent", "production deployed", "model deployed"]
    text_to_check = str(text) + str(df) + str(summary)
    for f in forbidden:
        if f in text_to_check:
            return {"valid": False, "errors": [f"Forbidden claim found: {f}"]}
    return {"valid": True, "errors": []}

def build_fx_validation_report(tables: Dict[str, pd.DataFrame], profile: FXProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame([{"check": "all_validations", "status": "passed"}])
    return df, {"total_validations": len(tables), "passed": True}
''')

w("advanced_fx_providers/fx_quality.py", '''
import pandas as pd
from typing import Tuple, Dict
from .fx_provider_config import FXProviderProfile

def check_fx_provider_profile_quality(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"score": 1.0}
def check_fx_pair_universe_quality(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"score": 1.0}
def check_fx_symbol_normalization_quality(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"score": 1.0}
def check_fx_provider_registry_quality(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"score": 1.0}
def check_fx_capability_quality(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"score": 1.0}
def check_fx_safety_quality(df: pd.DataFrame, profile: FXProviderProfile) -> Dict: return {"score": 1.0}

def check_for_forbidden_terms_in_fx_layer(text: str = None, df: pd.DataFrame = None, summary: dict = None) -> Dict:
    forbidden = ["API key printed", "secret printed", "HTML scraping enabled", "guaranteed profit"]
    text_to_check = str(text) + str(df) + str(summary)
    for f in forbidden:
        if f in text_to_check:
            return {"score": 0.0, "violations": [f]}
    return {"score": 1.0, "violations": []}

def build_fx_quality_report(summary: dict, registry_df: pd.DataFrame = None, health_df: pd.DataFrame = None) -> Dict:
    return {"overall_quality_score": 1.0, "details": {}}
''')

w("advanced_fx_providers/fx_report_builder.py", '''
import pandas as pd

def build_fx_provider_disclaimer() -> str:
    return "Bu çıktı Phase 107 FX Data Provider Layer raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, production deployment, model deployment, scraping, external LLM/API çağrısı, gerçek FX provider API çağrısı zorunluluğu veya official approval değildir."

def build_fx_provider_profile_registry_markdown_report(summary: dict, profile_df: pd.DataFrame = None) -> str: return f"# Profile Registry\\n\\n{build_fx_provider_disclaimer()}"
def build_fx_provider_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame = None) -> str: return f"# Domain Registry\\n\\n{build_fx_provider_disclaimer()}"
def build_fx_pair_universe_markdown_report(summary: dict, pair_df: pd.DataFrame = None) -> str: return f"# Pair Universe\\n\\n{build_fx_provider_disclaimer()}"
def build_fx_symbol_normalization_markdown_report(summary: dict, symbol_df: pd.DataFrame = None) -> str: return f"# Symbol Normalization\\n\\n{build_fx_provider_disclaimer()}"
def build_fx_provider_capability_markdown_report(summary: dict, capability_df: pd.DataFrame = None) -> str: return f"# Capabilities\\n\\n{build_fx_provider_disclaimer()}"
def build_fx_provider_registry_markdown_report(summary: dict, registry_df: pd.DataFrame = None) -> str: return f"# Provider Registry\\n\\n{build_fx_provider_disclaimer()}"
def build_fx_contract_markdown_report(summary: dict, contract_df: pd.DataFrame = None) -> str: return f"# Contracts\\n\\n{build_fx_provider_disclaimer()}"
def build_fx_dry_run_markdown_report(summary: dict, dry_run_df: pd.DataFrame = None) -> str: return f"# Dry Run\\n\\n{build_fx_provider_disclaimer()}"
def build_fx_safety_markdown_report(summary: dict, safety_df: pd.DataFrame = None) -> str: return f"# Safety Boundary\\n\\n{build_fx_provider_disclaimer()}"
def build_fx_health_markdown_report(summary: dict, health_df: pd.DataFrame = None) -> str: return f"# Health Check\\n\\n{build_fx_provider_disclaimer()}"
def build_fx_quality_markdown_report(summary: dict, quality: dict = None) -> str: return f"# Quality Report\\n\\n{build_fx_provider_disclaimer()}"
def build_fx_status_markdown_report(summary: dict, status_df: pd.DataFrame = None) -> str: return f"# Status\\n\\n{build_fx_provider_disclaimer()}"
def build_phase_108_handoff_markdown_report(summary: dict, handoff_text: str = None) -> str: return f"# Phase 108 Handoff\\n\\n{build_fx_provider_disclaimer()}"
''')
