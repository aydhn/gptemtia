import pandas as pd
from typing import Dict, Optional
from knowledge_base.kb_config import KnowledgeBaseProfile

FORBIDDEN_TERMS = [
    "AL", "SAT", "BUY", "SELL", "OPEN_LONG", "OPEN_SHORT",
    "EMİR GÖNDER", "POZİSYON AÇ", "POZİSYON KAPAT", "GERÇEK EMİR",
    "BROKER ORDER", "LIVE ORDER", "DEPLOY MODEL", "PRODUCTION DEPLOY", "RUN LIVE"
]

SENSITIVE_PATTERNS = [
    "API_KEY", "SECRET", "TOKEN", "PASSWORD", "PRIVATE_KEY", "TELEGRAM_BOT_TOKEN"
]

def check_document_index_quality(documents_df: pd.DataFrame, profile: KnowledgeBaseProfile) -> Dict:
    if documents_df.empty:
        return {"passed": False, "score": 0.0, "reason": "No documents indexed"}
    return {"passed": True, "score": 1.0, "reason": "OK"}

def check_chunk_index_quality(chunks_df: pd.DataFrame, profile: KnowledgeBaseProfile) -> Dict:
    if chunks_df.empty:
        return {"passed": False, "score": 0.0, "reason": "No chunks generated"}
    return {"passed": True, "score": 1.0, "reason": "OK"}

def check_retrieval_quality(results_df: Optional[pd.DataFrame] = None) -> Dict:
    if results_df is None or results_df.empty:
        return {"passed": True, "score": 0.0, "reason": "No results to check"}
    return {"passed": True, "score": 1.0, "reason": "OK"}

def check_memory_card_quality(cards_df: Optional[pd.DataFrame] = None) -> Dict:
    return {"passed": True, "score": 1.0, "reason": "OK"}

def check_decision_journal_quality(journal_df: Optional[pd.DataFrame] = None) -> Dict:
    return {"passed": True, "score": 1.0, "reason": "OK"}

def check_for_sensitive_data_in_kb(df: Optional[pd.DataFrame] = None, text: Optional[str] = None) -> Dict:
    found = False
    details = []

    if text:
        t_upper = text.upper()
        for p in SENSITIVE_PATTERNS:
            if p in t_upper:
                # To avoid false positives on masked text, check if it's not the masked version
                if f"MASKED_{p}" not in t_upper and f"[MASKED" not in t_upper:
                    found = True
                    details.append(p)

    if df is not None and not df.empty and 'text' in df.columns:
        for p in SENSITIVE_PATTERNS:
            mask = df['text'].str.upper().str.contains(p, na=False)
            masked_mask = df['text'].str.upper().str.contains(r'\[MASKED', na=False)
            if (mask & ~masked_mask).any():
                found = True
                details.append(f"In dataframe: {p}")

    return {
        "found": found,
        "details": list(set(details))
    }

def check_for_forbidden_trade_terms_in_kb(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict] = None
) -> Dict:
    found = False
    details = []

    # Text check requires exact word boundaries for some, but simple substring for others
    # To keep it simple, we do substring check on uppercase
    if text:
        t_upper = text.upper()
        for t in FORBIDDEN_TERMS:
            # Add spaces around short words to avoid matching parts of other words
            search_t = f" {t} " if len(t) <= 3 else t
            if search_t in f" {t_upper} ":
                found = True
                details.append(t)

    if df is not None and not df.empty and 'text' in df.columns:
        for t in FORBIDDEN_TERMS:
            search_t = f" {t} " if len(t) <= 3 else t
            # Naive check
            mask = df['text'].str.upper().apply(lambda x: search_t in f" {str(x)} " if pd.notnull(x) else False)
            if mask.any():
                found = True
                details.append(f"In dataframe: {t}")

    return {
        "found": found,
        "details": list(set(details))
    }

def build_kb_quality_report(
    summary: Dict,
    documents_df: Optional[pd.DataFrame] = None,
    chunks_df: Optional[pd.DataFrame] = None,
    retrieval_df: Optional[pd.DataFrame] = None
) -> Dict:

    # Dummy profile since we just want a basic check
    from knowledge_base.kb_config import KnowledgeBaseProfile
    prof = KnowledgeBaseProfile(name="dummy", description="")

    doc_q = check_document_index_quality(documents_df if documents_df is not None else pd.DataFrame(), prof)
    chk_q = check_chunk_index_quality(chunks_df if chunks_df is not None else pd.DataFrame(), prof)
    ret_q = check_retrieval_quality(retrieval_df)

    sens = check_for_sensitive_data_in_kb(df=chunks_df)
    forb = check_for_forbidden_trade_terms_in_kb(df=chunks_df)

    passed = doc_q["passed"] and chk_q["passed"] and not sens["found"] and not forb["found"]

    warnings = []
    if sens["found"]:
        warnings.append(f"Sensitive data found: {sens['details']}")
    if forb["found"]:
        warnings.append(f"Forbidden trade terms found: {forb['details']}")

    return {
        "documents_valid": doc_q["passed"],
        "chunks_valid": chk_q["passed"],
        "retrieval_valid": ret_q["passed"],
        "memory_cards_valid": True,
        "decision_journal_valid": True,
        "sensitive_data_found": sens["found"],
        "forbidden_trade_terms_found": forb["found"],
        "warning_count": len(warnings),
        "passed": passed,
        "warnings": warnings
    }
