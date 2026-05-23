from typing import Optional

import pandas as pd

from meta_research.meta_config import MetaResearchProfile

FORBIDDEN_TERMS = [
    "AL ", " SAT ", "BUY", "SELL", "OPEN_LONG", "OPEN_SHORT",
    "EMİR GÖNDER", "POZİSYON AÇ", "POZİSYON KAPAT",
    "GERÇEK EMİR", "BROKER ORDER", "LIVE ORDER", "LIVE_ORDER"
]

def check_for_forbidden_trade_terms_in_meta_research(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[dict] = None
) -> dict:

    found_terms = set()

    def _check_string(s: str):
        if not isinstance(s, str):
            return
        s_upper = s.upper()
        for term in FORBIDDEN_TERMS:
            if term in s_upper:
                found_terms.add(term)

    if text:
        _check_string(text)

    if summary:
        _check_string(str(summary))

    if df is not None and not df.empty:
        for col in df.columns:
            _check_string(str(col))
        for col in df.select_dtypes(include=['object', 'string']).columns:
            for val in df[col].dropna():
                _check_string(str(val))

    return {
        "passed": len(found_terms) == 0,
        "found_terms": list(found_terms)
    }

def check_evidence_table_quality(evidence_df: pd.DataFrame, profile: MetaResearchProfile) -> dict:
    if evidence_df.empty:
        return {"passed": False, "warnings": ["Evidence table is empty"]}

    warnings = []
    if "evidence_direction" not in evidence_df.columns:
        warnings.append("Missing 'evidence_direction' column")

    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_consensus_table_quality(consensus_df: pd.DataFrame) -> dict:
    if consensus_df.empty:
        return {"passed": False, "warnings": ["Consensus table is empty"]}
    return {"passed": True, "warnings": []}

def check_ensemble_table_quality(ensemble_df: pd.DataFrame) -> dict:
    if ensemble_df.empty:
        return {"passed": False, "warnings": ["Ensemble table is empty"]}
    return {"passed": True, "warnings": []}

def check_conflict_report_quality(conflict_df: Optional[pd.DataFrame] = None) -> dict:
    if conflict_df is None or conflict_df.empty:
        return {"passed": False, "warnings": ["Conflict table is empty"]}
    return {"passed": True, "warnings": []}

def check_meta_ranking_quality(ranking_df: pd.DataFrame) -> dict:
    if ranking_df.empty:
        return {"passed": False, "warnings": ["Ranking table is empty"]}
    return {"passed": True, "warnings": []}

def build_meta_quality_report(
    summary: dict,
    evidence_df: Optional[pd.DataFrame] = None,
    consensus_df: Optional[pd.DataFrame] = None,
    ranking_df: Optional[pd.DataFrame] = None
) -> dict:

    term_check = check_for_forbidden_trade_terms_in_meta_research(
        text=str(summary), df=evidence_df
    )
    if consensus_df is not None:
        c_check = check_for_forbidden_trade_terms_in_meta_research(df=consensus_df)
        term_check["found_terms"].extend(c_check["found_terms"])

    if ranking_df is not None:
        r_check = check_for_forbidden_trade_terms_in_meta_research(df=ranking_df)
        term_check["found_terms"].extend(r_check["found_terms"])

    unique_terms = list(set(term_check["found_terms"]))

    return {
        "evidence_valid": evidence_df is not None and not evidence_df.empty,
        "consensus_valid": consensus_df is not None and not consensus_df.empty,
        "ranking_valid": ranking_df is not None and not ranking_df.empty,
        "disclaimer_required": True,
        "forbidden_trade_terms_found": len(unique_terms) > 0,
        "found_terms": unique_terms,
        "passed": len(unique_terms) == 0,
        "warnings": [f"Forbidden term found: {t}" for t in unique_terms]
    }
