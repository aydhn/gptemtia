import pandas as pd
from portfolio_research.portfolio_config import PortfolioResearchProfile
from portfolio_research.portfolio_models import VirtualBasketDefinition

FORBIDDEN_TERMS = [
    "AL", "SAT", "BUY", "SELL", "OPEN_LONG", "OPEN_SHORT",
    "EMİR GÖNDER", "POZİSYON AÇ", "POZİSYON KAPAT",
    "GERÇEK EMİR", "BROKER ORDER", "LIVE ORDER"
]

def check_returns_matrix_quality(returns_df: pd.DataFrame, profile: PortfolioResearchProfile) -> dict:
    if returns_df.empty:
        return {"valid": False, "warnings": ["Returns matrix is empty."]}

    warnings = []
    if len(returns_df.columns) < profile.min_symbols:
        warnings.append(f"Insufficient symbols in returns matrix ({len(returns_df.columns)} < {profile.min_symbols}).")

    if len(returns_df) < profile.min_observations:
        warnings.append(f"Insufficient observations in returns matrix ({len(returns_df)} < {profile.min_observations}).")

    return {
        "valid": len(warnings) == 0,
        "symbol_count": len(returns_df.columns),
        "observation_count": len(returns_df),
        "warnings": warnings
    }

def check_correlation_matrix_quality(corr_df: pd.DataFrame) -> dict:
    if corr_df.empty:
        return {"valid": False, "warnings": ["Correlation matrix is empty."]}

    warnings = []
    if corr_df.isnull().values.any():
        warnings.append("Correlation matrix contains NaNs.")

    return {
        "valid": len(warnings) == 0,
        "warnings": warnings
    }

def check_basket_definitions_quality(baskets: list[VirtualBasketDefinition], profile: PortfolioResearchProfile) -> dict:
    if not baskets:
        return {"valid": False, "warnings": ["No baskets defined."]}

    warnings = []
    for basket in baskets:
        if not basket.symbols:
            warnings.append(f"Basket {basket.basket_id} has no symbols.")
        elif len(basket.symbols) > profile.max_basket_symbols:
            warnings.append(f"Basket {basket.basket_id} exceeds max symbols limit.")

        weight_sum = sum(basket.weights.values())
        if abs(weight_sum - 1.0) > 0.01 and weight_sum != 0:
            warnings.append(f"Basket {basket.basket_id} weights do not sum to 1.0 (Sum: {weight_sum}).")

    return {
        "valid": len(warnings) == 0,
        "basket_count": len(baskets),
        "warnings": warnings
    }

def check_basket_performance_quality(performance_df: pd.DataFrame) -> dict:
    if performance_df.empty:
        return {"valid": False, "warnings": ["Performance dataframe is empty."]}

    warnings = []
    if 'total_return_pct' not in performance_df.columns:
        warnings.append("Missing 'total_return_pct' in performance dataframe.")

    return {
        "valid": len(warnings) == 0,
        "warnings": warnings
    }

def check_for_forbidden_trade_terms_in_portfolio_research(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    found_terms = set()

    def _check_string(s):
        if not isinstance(s, str):
            return
        s_upper = s.upper()
        for term in FORBIDDEN_TERMS:
            if term in s_upper:
                import re
                if re.search(r'\b' + re.escape(term) + r'\b', s_upper):
                    found_terms.add(term)

    if text:
        _check_string(text)

    if summary:
        import json
        _check_string(json.dumps(summary))

    if df is not None and not df.empty:
        for col in df.columns:
            if df[col].dtype == 'object':
                for val in df[col].dropna():
                    _check_string(str(val))

    warnings = []
    if found_terms:
        warnings.append(f"FORBIDDEN TRADE TERMS FOUND: {list(found_terms)}")

    return {
        "valid": len(found_terms) == 0,
        "found_terms": list(found_terms),
        "warnings": warnings
    }

def build_portfolio_quality_report(summary: dict, returns_df: pd.DataFrame | None = None, corr_df: pd.DataFrame | None = None, baskets: list[VirtualBasketDefinition] | None = None, performance_df: pd.DataFrame | None = None) -> dict:
    warnings = []

    ret_q = check_returns_matrix_quality(returns_df, PortfolioResearchProfile(name="dummy", description="")) if returns_df is not None else {"valid": False}
    if not ret_q["valid"]: warnings.extend(ret_q.get("warnings", []))

    corr_q = check_correlation_matrix_quality(corr_df) if corr_df is not None else {"valid": False}
    if not corr_q["valid"]: warnings.extend(corr_q.get("warnings", []))

    bask_q = check_basket_definitions_quality(baskets, PortfolioResearchProfile(name="dummy", description="")) if baskets else {"valid": False}
    if not bask_q["valid"]: warnings.extend(bask_q.get("warnings", []))

    perf_q = check_basket_performance_quality(performance_df) if performance_df is not None else {"valid": False}
    if not perf_q["valid"]: warnings.extend(perf_q.get("warnings", []))

    term_q = check_for_forbidden_trade_terms_in_portfolio_research(summary=summary)
    if not term_q["valid"]: warnings.extend(term_q.get("warnings", []))

    passed = ret_q.get("valid", False) and term_q.get("valid", False)

    return {
        "returns_valid": ret_q.get("valid", False),
        "correlation_valid": corr_q.get("valid", False),
        "baskets_valid": bask_q.get("valid", False),
        "performance_valid": perf_q.get("valid", False),
        "disclaimer_required": True,
        "forbidden_trade_terms_found": not term_q.get("valid", True),
        "warning_count": len(warnings),
        "passed": passed,
        "warnings": warnings
    }
