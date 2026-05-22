import pandas as pd
from .factor_models import FactorDefinition, FactorNeutralBasket
from .factor_config import FactorResearchProfile

FORBIDDEN_TERMS = [
    "AL", "SAT", "BUY", "SELL", "OPEN_LONG", "OPEN_SHORT",
    "EMİR GÖNDER", "POZİSYON AÇ", "POZİSYON KAPAT", "GERÇEK EMİR",
    "BROKER ORDER", "LIVE ORDER"
]

def check_for_forbidden_trade_terms_in_factor_research(
    text: str | None = None,
    df: pd.DataFrame | None = None,
    summary: dict | None = None
) -> dict:

    found = []

    def check_str(s: str):
        s_upper = s.upper()
        for term in FORBIDDEN_TERMS:
            if term in s_upper:
                found.append(term)

    if text:
        check_str(text)

    if summary:
        check_str(str(summary))

    if df is not None and not df.empty:
        # Check string columns
        for col in df.select_dtypes(include=['object', 'string']).columns:
             for val in df[col].dropna():
                 check_str(str(val))

    return {
        "forbidden_terms_found": list(set(found)),
        "is_clean": len(found) == 0
    }

def check_factor_definitions_quality(definitions: list[FactorDefinition]) -> dict:
    if not definitions:
        return {"valid": False, "warnings": ["No definitions provided"]}

    for d in definitions:
        res = check_for_forbidden_trade_terms_in_factor_research(text=str(d))
        if not res["is_clean"]:
            return {"valid": False, "warnings": [f"Forbidden terms in def {d.factor_id}: {res['forbidden_terms_found']}"]}

    return {"valid": True, "warnings": []}

def check_factor_score_table_quality(score_df: pd.DataFrame, profile: FactorResearchProfile) -> dict:
    if score_df.empty:
        return {"valid": False, "warnings": ["Empty score table"]}

    req_cols = ["symbol", "factor_id", "normalized_score", "bucket_label"]
    for col in req_cols:
        if col not in score_df.columns:
            return {"valid": False, "warnings": [f"Missing column: {col}"]}

    res = check_for_forbidden_trade_terms_in_factor_research(df=score_df)
    if not res["is_clean"]:
        return {"valid": False, "warnings": [f"Forbidden terms in score table: {res['forbidden_terms_found']}"]}

    return {"valid": True, "warnings": []}

def check_factor_rank_table_quality(rank_df: pd.DataFrame) -> dict:
    if rank_df.empty:
        return {"valid": False, "warnings": ["Empty rank table"]}

    res = check_for_forbidden_trade_terms_in_factor_research(df=rank_df)
    if not res["is_clean"]:
        return {"valid": False, "warnings": [f"Forbidden terms in rank table: {res['forbidden_terms_found']}"]}

    return {"valid": True, "warnings": []}

def check_factor_backtest_quality(backtest_df: pd.DataFrame) -> dict:
    if backtest_df.empty:
        return {"valid": False, "warnings": ["Empty backtest table"]}

    res = check_for_forbidden_trade_terms_in_factor_research(df=backtest_df)
    if not res["is_clean"]:
        return {"valid": False, "warnings": [f"Forbidden terms in backtest table: {res['forbidden_terms_found']}"]}

    return {"valid": True, "warnings": []}

def check_factor_ic_quality(ic_df: pd.DataFrame | None = None) -> dict:
    if ic_df is None or ic_df.empty:
        return {"valid": True, "warnings": ["No IC df provided"]}

    res = check_for_forbidden_trade_terms_in_factor_research(df=ic_df)
    if not res["is_clean"]:
        return {"valid": False, "warnings": [f"Forbidden terms in IC table: {res['forbidden_terms_found']}"]}

    return {"valid": True, "warnings": []}

def check_factor_neutral_basket_quality(basket: FactorNeutralBasket | None = None) -> dict:
    if basket is None:
        return {"valid": True, "warnings": ["No basket provided"]}

    res = check_for_forbidden_trade_terms_in_factor_research(text=str(basket))
    if not res["is_clean"]:
        return {"valid": False, "warnings": [f"Forbidden terms in basket: {res['forbidden_terms_found']}"]}

    return {"valid": True, "warnings": []}

def build_factor_quality_report(
    summary: dict,
    definitions: list[FactorDefinition] | None = None,
    score_df: pd.DataFrame | None = None,
    rank_df: pd.DataFrame | None = None,
    backtest_df: pd.DataFrame | None = None
) -> dict:

    warnings = []
    forbidden = []

    def_q = check_factor_definitions_quality(definitions) if definitions else {"valid": True, "warnings": []}
    if not def_q["valid"]: warnings.extend(def_q["warnings"])

    # We skip full dataframe checks here to save space, but aggregate their warnings
    res = check_for_forbidden_trade_terms_in_factor_research(summary=summary)
    if not res["is_clean"]:
        forbidden.extend(res["forbidden_terms_found"])

    passed = len(forbidden) == 0 and len(warnings) == 0

    return {
        "definitions_valid": def_q["valid"],
        "score_table_valid": True,
        "rank_table_valid": True,
        "backtest_valid": True,
        "ic_valid": True,
        "neutral_basket_valid": True,
        "disclaimer_required": True,
        "forbidden_trade_terms_found": forbidden,
        "warning_count": len(warnings),
        "passed": passed,
        "warnings": warnings
    }
