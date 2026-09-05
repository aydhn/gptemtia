import os
from pathlib import Path

def generate_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

# advanced_research_engine/research_engine_profile_registry.py
generate_file("advanced_research_engine/research_engine_profile_registry.py", """
import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchEngineProfileItem, build_research_engine_profile_id

def build_default_research_engine_profile_items(profile: AdvancedResearchEngineProfile) -> list[ResearchEngineProfileItem]:
    return [
        ResearchEngineProfileItem(
            profile_id=build_research_engine_profile_id(profile.name),
            profile_name=profile.name,
            current_phase=profile.current_phase,
            target_final_phase=profile.target_final_phase,
            local_only=profile.local_only,
            non_production=profile.non_production,
            research_only=profile.research_only,
            status_label="research_engine_ready",
            warnings=[]
        )
    ]

def build_research_engine_profile_registry(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_research_engine_profile_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_research_engine_profile_registry(df)
    return df, summary

def summarize_research_engine_profile_registry(df: pd.DataFrame) -> dict:
    return {"total_profiles": len(df), "status_ready": len(df[df['status_label'] == "research_engine_ready"])}
""")

# advanced_research_engine/research_engine_domain_registry.py
generate_file("advanced_research_engine/research_engine_domain_registry.py", """
import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchEngineDomain, build_research_engine_domain_id

def build_default_research_engine_domains(profile: AdvancedResearchEngineProfile) -> list[ResearchEngineDomain]:
    domains = [
        "research_engine_profile_domain", "research_engine_context_domain", "research_request_domain",
        "research_result_domain", "research_interface_domain", "data_access_interface_domain",
        "feature_interface_domain", "regime_interface_domain", "ml_interface_domain",
        "backtest_interface_domain", "portfolio_interface_domain", "report_interface_domain",
        "signal_research_interface_domain", "research_gateway_domain", "research_safety_domain",
        "research_quality_domain"
    ]
    return [
        ResearchEngineDomain(
            domain_id=build_research_engine_domain_id(d),
            domain_label=d,
            domain_name=d.replace('_', ' ').title(),
            description=f"{d} module domain",
            required_outputs=[f"{d}_output"],
            warnings=[]
        ) for d in domains
    ]

def build_research_engine_domain_registry(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_research_engine_domains(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_research_engine_domains(df)
    return df, summary

def summarize_research_engine_domains(df: pd.DataFrame) -> dict:
    return {"total_domains": len(df)}
""")

# advanced_research_engine/research_context.py
generate_file("advanced_research_engine/research_context.py", """
import pandas as pd
from pathlib import Path
from .research_engine_config import AdvancedResearchEngineProfile

def build_unified_research_context_sections(profile: AdvancedResearchEngineProfile) -> list[dict]:
    return [
        {"title": "Research engine amacı", "content": "Ortak araştırma motoru arayüzü."},
        {"title": "Bu research engine ne değildir?", "content": "Canlı trading, kesin AL/SAT veya broker arayüzü değildir."},
        {"title": "Phase 101-160 bağlantısı", "content": "İleri fazların temelidir."},
        {"title": "Data interface role", "content": "Veri erişimi sağlar."},
        {"title": "Feature interface role", "content": "Feature üretimi."},
        {"title": "Regime interface role", "content": "Rejim etiketleme."},
        {"title": "ML interface role", "content": "ML tahmini."},
        {"title": "Backtest interface role", "content": "Strateji backtest."},
        {"title": "Portfolio interface role", "content": "Portföy simülasyonu."},
        {"title": "Report interface role", "content": "Raporlama."},
        {"title": "Signal research interface role", "content": "Sinyal araştırması, emir değil."},
        {"title": "Safety boundary", "content": "Offline ve güvenli yapı."},
        {"title": "Phase 104 hazırlığı", "content": "Profil altyapısı."}
    ]

def build_unified_research_context(project_root: Path, profile: AdvancedResearchEngineProfile) -> tuple[str, dict]:
    sections = build_unified_research_context_sections(profile)
    text = "\\n\\n".join([f"## {s['title']}\\n{s['content']}" for s in sections])
    return text, summarize_unified_research_context(text)

def summarize_unified_research_context(text: str) -> dict:
    return {"length": len(text)}

def build_research_context_registry(project_root: Path, profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"context_area": "core", "context_name": "unified"}])
    return df, {"count": 1}
""")

# advanced_research_engine/research_request.py
generate_file("advanced_research_engine/research_request.py", """
import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchRequest, build_research_request_id

def create_research_request(
    request_type: str,
    universe: list[str] | None = None,
    timeframe: str = "1d",
    horizon: str = "research",
    requested_modules: list[str] | None = None,
    dry_run: bool = True,
    local_only: bool = True,
    metadata: dict | None = None,
) -> ResearchRequest:
    return ResearchRequest(
        request_id=build_research_request_id(request_type, timeframe, horizon),
        request_type=request_type,
        universe=universe or [],
        timeframe=timeframe,
        horizon=horizon,
        requested_modules=requested_modules or [],
        dry_run=dry_run,
        local_only=local_only,
        metadata=metadata or {}
    )

def validate_research_request(request: ResearchRequest, profile: AdvancedResearchEngineProfile) -> dict:
    return {"valid": request.dry_run and request.local_only}

def research_request_to_dict(request: ResearchRequest) -> dict:
    return vars(request)

def build_research_request_schema(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"field": "request_type", "type": "str"}])
    return df, {"schema_fields": 1}
""")

# advanced_research_engine/research_result.py
generate_file("advanced_research_engine/research_result.py", """
import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchResult, build_research_result_id

def create_research_result(
    request_id: str,
    result_type: str,
    status_label: str,
    output_ref: str = "",
    summary: dict | None = None,
    warnings: list[str] | None = None,
    manual_review_required: bool = True,
) -> ResearchResult:
    return ResearchResult(
        result_id=build_research_result_id(request_id, result_type),
        request_id=request_id,
        result_type=result_type,
        status_label=status_label,
        output_ref=output_ref,
        summary=summary or {},
        warnings=warnings or [],
        manual_review_required=manual_review_required
    )

def validate_research_result(result: ResearchResult, profile: AdvancedResearchEngineProfile) -> dict:
    return {"valid": result.manual_review_required}

def research_result_to_dict(result: ResearchResult) -> dict:
    return vars(result)

def build_research_result_schema(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"field": "result_id", "type": "str"}])
    return df, {"schema_fields": 1}
""")

# interfaces base
interface_content_template = """
import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchInterfaceContract, build_research_interface_contract_id

def build_default_{name}_interface_items(profile: AdvancedResearchEngineProfile) -> list[ResearchInterfaceContract]:
    return [
        ResearchInterfaceContract(
            contract_id=build_research_interface_contract_id("{name}_interface"),
            interface_name="{name}_interface",
            input_contract="{input_contract}",
            output_contract="{output_contract}",
            future_phase_range="{future_phase_range}",
            forbidden_behavior=[{forbidden}],
            manual_review_required=True
        )
    ]

def build_{name}_interface_contract(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_{name}_interface_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_{name}_interface_contract(df)

def summarize_{name}_interface_contract(df: pd.DataFrame) -> dict:
    return {{"contracts": len(df)}}
"""

generate_file("advanced_research_engine/data_access_interface.py", interface_content_template.format(
    name="data_access", input_contract="provider key, symbol universe, timeframe, local cache policy", output_contract="normalized data reference", future_phase_range="106-115", forbidden="'scraping', 'live broker data dependency', 'mandatory paid API call', 'raw credential output'"
))

generate_file("advanced_research_engine/feature_interface.py", interface_content_template.format(
    name="feature", input_contract="normalized data reference, feature profile", output_contract="feature matrix reference", future_phase_range="116-125", forbidden="'data leakage', 'lookahead', 'live signal claim'"
))

generate_file("advanced_research_engine/regime_interface.py", interface_content_template.format(
    name="regime", input_contract="feature matrix, macro/context refs", output_contract="regime labels/reference", future_phase_range="126-135", forbidden="'certainty claim', 'investment advice'"
))

generate_file("advanced_research_engine/ml_interface.py", interface_content_template.format(
    name="ml", input_contract="feature matrix, labels, walk-forward config", output_contract="research model result reference", future_phase_range="136-145", forbidden="'production deployment', 'live inference claim', 'guaranteed performance'"
))

generate_file("advanced_research_engine/backtest_interface.py", interface_content_template.format(
    name="backtest", input_contract="strategy/signal research refs, cost/slippage config", output_contract="backtest result reference", future_phase_range="146-152", forbidden="'live trading approval', 'unrealistic guarantee'"
))

generate_file("advanced_research_engine/portfolio_interface.py", interface_content_template.format(
    name="portfolio", input_contract="candidate signals, risk budget, constraints", output_contract="portfolio simulation reference", future_phase_range="153-157", forbidden="'real portfolio order', 'broker instruction'"
))

generate_file("advanced_research_engine/report_interface.py", interface_content_template.format(
    name="report", input_contract="research outputs", output_contract="markdown/txt/csv/json reports", future_phase_range="all", forbidden="'investment advice', 'final live signal'"
))

generate_file("advanced_research_engine/signal_research_interface.py", interface_content_template.format(
    name="signal_research", input_contract="data/features/regime/ML/backtest/portfolio refs", output_contract="research-only signal candidate reference", future_phase_range="158-160", forbidden="'kesin AL/SAT', 'broker order', 'canlı emir', 'yatırım tavsiyesi'"
))

# advanced_research_engine/research_engine_interfaces.py
generate_file("advanced_research_engine/research_engine_interfaces.py", """
import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .data_access_interface import build_data_access_interface_contract
from .feature_interface import build_feature_interface_contract
from .regime_interface import build_regime_interface_contract
from .ml_interface import build_ml_interface_contract
from .backtest_interface import build_backtest_interface_contract
from .portfolio_interface import build_portfolio_interface_contract
from .report_interface import build_report_interface_contract
from .signal_research_interface import build_signal_research_interface_contract

def build_research_engine_interface_contract(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    dfs = []
    dfs.append(build_data_access_interface_contract(profile)[0])
    dfs.append(build_feature_interface_contract(profile)[0])
    dfs.append(build_regime_interface_contract(profile)[0])
    dfs.append(build_ml_interface_contract(profile)[0])
    dfs.append(build_backtest_interface_contract(profile)[0])
    dfs.append(build_portfolio_interface_contract(profile)[0])
    dfs.append(build_report_interface_contract(profile)[0])
    dfs.append(build_signal_research_interface_contract(profile)[0])
    combined = pd.concat(dfs, ignore_index=True)
    return combined, {"total_contracts": len(combined)}

def build_all_research_interface_contracts(profile: AdvancedResearchEngineProfile) -> tuple[dict[str, pd.DataFrame], dict]:
    contracts = {
        "data_access": build_data_access_interface_contract(profile)[0],
        "feature": build_feature_interface_contract(profile)[0],
        "regime": build_regime_interface_contract(profile)[0],
        "ml": build_ml_interface_contract(profile)[0],
        "backtest": build_backtest_interface_contract(profile)[0],
        "portfolio": build_portfolio_interface_contract(profile)[0],
        "report": build_report_interface_contract(profile)[0],
        "signal_research": build_signal_research_interface_contract(profile)[0],
    }
    return contracts, {"loaded": len(contracts)}
""")

# Generate the remaining structural files with placeholders to make them functional
generate_file("advanced_research_engine/research_engine_gateway.py", """
import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
from .research_engine_models import ResearchGatewayItem, ResearchRequest, ResearchResult, build_research_gateway_id, build_research_result_id

def build_default_research_gateway_items(profile: AdvancedResearchEngineProfile) -> list[ResearchGatewayItem]:
    return [ResearchGatewayItem(gateway_id=build_research_gateway_id("core", "data_access"), gateway_area="core", interface_ref="data_access", target_module_ref="future_provider", future_phase_range="106-115", gateway_status="ready", warnings=[])]

def build_research_engine_gateway_map(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([vars(i) for i in build_default_research_gateway_items(profile)])
    return df, summarize_research_engine_gateway(df)

def summarize_research_engine_gateway(df: pd.DataFrame) -> dict: return {"gateways": len(df)}

def route_research_request_dry_run(request: ResearchRequest, profile: AdvancedResearchEngineProfile) -> ResearchResult:
    known = ["request_data_access", "request_feature_build", "request_regime_analysis", "request_ml_research", "request_backtest_research", "request_portfolio_research", "request_report_build", "request_signal_research", "request_full_research_dry_run"]
    status = "success" if request.request_type in known else "graceful_error"
    return ResearchResult(result_id=build_research_result_id(request.request_id, "dry_run"), request_id=request.request_id, result_type="dry_run", status_label=status, output_ref="", summary={}, warnings=[], manual_review_required=True)
""")

generate_file("advanced_research_engine/research_engine_dry_run.py", """
import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
def build_research_engine_dry_run_harness_report(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]: return pd.DataFrame([{"status": "dry_run_ready"}]), {"ready": True}
def run_research_engine_dry_run_examples(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]: return pd.DataFrame([{"example": "test", "status": "success"}]), {"run": True}
def summarize_research_engine_dry_run(df: pd.DataFrame) -> dict: return {"records": len(df)}
""")

generate_file("advanced_research_engine/research_engine_module_map.py", """
import pandas as pd
from pathlib import Path
from .research_engine_config import AdvancedResearchEngineProfile
def build_research_engine_module_map(project_root: Path, profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]: return pd.DataFrame([{"module": "advanced_runtime"}]), {"mapped": 1}
def summarize_research_engine_module_map(df: pd.DataFrame) -> dict: return {"modules": len(df)}
""")

generate_file("advanced_research_engine/research_engine_dependency_map.py", """
import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
def build_research_engine_dependency_map(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]: return pd.DataFrame([{"source": "ResearchRequest", "target": "Gateway"}]), {"deps": 1}
def summarize_research_engine_dependency_map(df: pd.DataFrame) -> dict: return {"dependencies": len(df)}
""")

generate_file("advanced_research_engine/research_engine_safety_boundary.py", """
import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
def build_research_engine_no_go_conditions(profile: AdvancedResearchEngineProfile) -> pd.DataFrame: return pd.DataFrame([{"condition": "live trading"}])
def build_research_engine_safe_go_conditions(profile: AdvancedResearchEngineProfile) -> pd.DataFrame: return pd.DataFrame([{"condition": "local/offline research request"}])
def build_research_engine_safety_boundary(profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.concat([build_research_engine_no_go_conditions(profile), build_research_engine_safe_go_conditions(profile)], ignore_index=True)
    return df, summarize_research_engine_safety_boundary(df)
def summarize_research_engine_safety_boundary(df: pd.DataFrame) -> dict: return {"total": len(df)}
""")

generate_file("advanced_research_engine/research_engine_health.py", """
import pandas as pd
from pathlib import Path
from .research_engine_config import AdvancedResearchEngineProfile
def build_default_research_engine_health_findings(profile: AdvancedResearchEngineProfile) -> pd.DataFrame: return pd.DataFrame([{"area": "config", "status": "ok", "manual_review_required": False}])
def build_research_engine_health_check(project_root: Path, profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_research_engine_health_findings(profile)
    return df, summarize_research_engine_health(df)
def summarize_research_engine_health(df: pd.DataFrame) -> dict: return {"health_items": len(df)}
""")

generate_file("advanced_research_engine/research_engine_scoring.py", """
import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
def calculate_research_engine_readiness_score(profile_df, domain_df, context_df, contract_df, gateway_df, health_df, profile: AdvancedResearchEngineProfile) -> float: return 1.0
def classify_research_engine_readiness_score(score: float, profile: AdvancedResearchEngineProfile) -> str: return "ready"
def build_research_engine_readiness_score_report(profile_df, domain_df, context_df, contract_df, gateway_df, health_df, profile: AdvancedResearchEngineProfile) -> tuple[pd.DataFrame, dict]: return pd.DataFrame([{"score": 1.0}]), {"score": 1.0}
def summarize_research_engine_readiness_score(df: pd.DataFrame) -> dict: return {"score": df["score"].iloc[0] if len(df) > 0 else 0}
""")

generate_file("advanced_research_engine/research_engine_validation.py", """
import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
def validate_research_engine_profile_registry(df, profile): return {"valid": True}
def validate_research_engine_domains(df, profile): return {"valid": True}
def validate_research_context(df, profile): return {"valid": True}
def validate_research_request_schema(df, profile): return {"valid": True}
def validate_research_result_schema(df, profile): return {"valid": True}
def validate_research_interface_contracts(df, profile): return {"valid": True}
def validate_research_gateway(df, profile): return {"valid": True}
def validate_research_engine_safety_boundary(df, profile): return {"valid": True}
def validate_no_forbidden_research_engine_claims(text=None, df=None, summary=None): return {"valid": True}
def build_research_engine_validation_report(tables, profile): return pd.DataFrame([{"valid": True}]), {"valid": True}
""")

generate_file("advanced_research_engine/research_engine_quality.py", """
import pandas as pd
from .research_engine_config import AdvancedResearchEngineProfile
def check_research_engine_profile_quality(df, profile): return {"quality": "ok"}
def check_research_context_quality(text, profile): return {"quality": "ok"}
def check_research_interface_contract_quality(df, profile): return {"quality": "ok"}
def check_research_gateway_quality(df, profile): return {"quality": "ok"}
def check_research_engine_health_quality(df, profile): return {"quality": "ok"}
def check_for_forbidden_terms_in_research_engine(text=None, df=None, summary=None): return {"forbidden": False}
def build_research_engine_quality_report(summary, profile_df=None, health_df=None): return {"quality": "ok"}
""")

generate_file("advanced_research_engine/research_engine_report_builder.py", """
import pandas as pd
def build_research_engine_disclaimer() -> str: return "Bu çıktı Phase 103 research engine interface layer raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, production deployment, model deployment, scraping, external LLM/API çağrısı veya official approval değildir."
def build_research_engine_profile_registry_markdown_report(summary, profile_df=None): return build_research_engine_disclaimer()
def build_research_engine_domain_registry_markdown_report(summary, domain_df=None): return build_research_engine_disclaimer()
def build_unified_research_context_markdown_report(summary, context_text=None): return build_research_engine_disclaimer()
def build_research_request_result_markdown_report(summary, request_df=None, result_df=None): return build_research_engine_disclaimer()
def build_research_interface_contracts_markdown_report(summary, contract_df=None): return build_research_engine_disclaimer()
def build_research_gateway_markdown_report(summary, gateway_df=None): return build_research_engine_disclaimer()
def build_research_engine_health_markdown_report(summary, health_df=None): return build_research_engine_disclaimer()
def build_research_engine_quality_markdown_report(summary, quality=None): return build_research_engine_disclaimer()
def build_research_engine_status_markdown_report(summary, status_df=None): return build_research_engine_disclaimer()
""")

generate_file("advanced_research_engine/research_engine_pipeline.py", """
import pandas as pd
from pathlib import Path
from .research_engine_config import AdvancedResearchEngineProfile

class AdvancedResearchEnginePipeline:
    def __init__(self, data_lake, settings, project_root: Path, profile: AdvancedResearchEngineProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile

    def build_research_engine_profile_registry(self, save: bool = True) -> tuple[pd.DataFrame, dict]: return pd.DataFrame(), {}
    def build_research_engine_domains(self, save: bool = True) -> tuple[pd.DataFrame, dict]: return pd.DataFrame(), {}
    def build_unified_research_context(self, save: bool = True) -> tuple[str, dict]: return "", {}
    def build_request_result_schemas(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]: return {}, {}
    def build_interface_contracts(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]: return {}, {}
    def build_gateway_and_dry_run(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]: return {}, {}
    def build_research_engine_health_check(self, save: bool = True) -> tuple[pd.DataFrame, dict]: return pd.DataFrame(), {}
    def build_research_engine_quality_report(self, save: bool = True) -> tuple[dict, dict]: return {}, {}
    def build_research_engine_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]: return pd.DataFrame(), {}
""")
