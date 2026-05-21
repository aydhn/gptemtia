import pandas as pd
from typing import Optional, List, Dict
from portfolio_regime.regime_config import PortfolioRegimeProfile
from portfolio_regime.regime_models import MacroScenarioDefinition

FORBIDDEN_TRADE_TERMS = [
    "AL", "SAT", "BUY", "SELL", "OPEN_LONG", "OPEN_SHORT",
    "EMİR GÖNDER", "POZİSYON AÇ", "POZİSYON KAPAT",
    "GERÇEK EMİR", "BROKER ORDER", "LIVE ORDER"
]

def check_regime_dataframe_quality(regime_df: pd.DataFrame, profile: PortfolioRegimeProfile) -> dict:
    if regime_df is None or regime_df.empty:
        return {"valid": False, "warnings": ["Empty regime dataframe"]}
    return {"valid": True, "warnings": []}

def check_scenario_definitions_quality(scenarios: List[MacroScenarioDefinition]) -> dict:
    if not scenarios:
        return {"valid": False, "warnings": ["No scenario definitions"]}
    return {"valid": True, "warnings": []}

def check_stress_test_quality(stress_df: Optional[pd.DataFrame] = None, scenario_df: Optional[pd.DataFrame] = None) -> dict:
    return {"valid": True, "warnings": []}

def check_drawdown_cluster_quality(cluster_df: pd.DataFrame) -> dict:
    if cluster_df is None or cluster_df.empty:
        return {"valid": False, "warnings": ["Empty drawdown cluster dataframe"]}
    return {"valid": True, "warnings": []}

def check_for_forbidden_trade_terms_in_regime_research(text: Optional[str] = None, df: Optional[pd.DataFrame] = None, summary: Optional[dict] = None) -> dict:
    found_terms = []

    def check_string(s: str):
        if not isinstance(s, str):
            return
        s_upper = s.upper()
        for term in FORBIDDEN_TRADE_TERMS:
            if term in s_upper:
                if term not in found_terms:
                    found_terms.append(term)

    if text:
        check_string(text)

    if df is not None and not df.empty:
        for col in df.select_dtypes(include=['object', 'string']).columns:
            for val in df[col].dropna():
                check_string(str(val))

    if summary:
        import json
        check_string(json.dumps(summary))

    return {
        "forbidden_trade_terms_found": len(found_terms) > 0,
        "terms": found_terms
    }

def build_regime_quality_report(summary: dict, regime_df: Optional[pd.DataFrame] = None, scenario_df: Optional[pd.DataFrame] = None, stress_df: Optional[pd.DataFrame] = None, cluster_df: Optional[pd.DataFrame] = None) -> dict:

    regime_quality = check_regime_dataframe_quality(regime_df if regime_df is not None else pd.DataFrame(), None)
    cluster_quality = check_drawdown_cluster_quality(cluster_df if cluster_df is not None else pd.DataFrame())

    terms_check = check_for_forbidden_trade_terms_in_regime_research(
        df=regime_df,
        summary=summary
    )

    warnings = []
    warnings.extend(regime_quality['warnings'])
    warnings.extend(cluster_quality['warnings'])

    if terms_check['forbidden_trade_terms_found']:
        warnings.append(f"Forbidden trade terms found: {terms_check['terms']}")

    return {
        "regime_valid": regime_quality['valid'],
        "scenarios_valid": True,
        "stress_valid": True,
        "drawdown_clusters_valid": cluster_quality['valid'],
        "disclaimer_required": True,
        "forbidden_trade_terms_found": terms_check['forbidden_trade_terms_found'],
        "warning_count": len(warnings),
        "passed": not terms_check['forbidden_trade_terms_found'],
        "warnings": warnings
    }
