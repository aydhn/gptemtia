import pandas as pd
from typing import Dict, Optional
import datetime

def build_workspace_summary(
    documents_df: pd.DataFrame,
    chunks_df: pd.DataFrame,
    memory_cards_df: Optional[pd.DataFrame] = None
) -> Dict:

    doc_count = len(documents_df) if not documents_df.empty else 0
    chunk_count = len(chunks_df) if not chunks_df.empty else 0
    card_count = len(memory_cards_df) if memory_cards_df is not None and not memory_cards_df.empty else 0

    warning_count = 0
    if not chunks_df.empty and 'text' in chunks_df.columns:
        warning_count = chunks_df['text'].str.lower().str.contains("warning").sum()

    return {
        "document_count": int(doc_count),
        "chunk_count": int(chunk_count),
        "memory_card_count": int(card_count),
        "warning_count": int(warning_count),
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }

def build_module_coverage_summary(documents_df: pd.DataFrame) -> pd.DataFrame:
    if documents_df.empty or 'source_module' not in documents_df.columns:
        return pd.DataFrame(columns=['source_module', 'document_count'])

    cov = documents_df['source_module'].value_counts().reset_index()
    cov.columns = ['source_module', 'document_count']
    return cov

def build_symbol_coverage_summary(chunks_df: pd.DataFrame) -> pd.DataFrame:
    if chunks_df.empty or 'symbols' not in chunks_df.columns:
        return pd.DataFrame(columns=['symbol', 'chunk_count'])

    exploded = chunks_df.explode('symbols')
    if exploded.empty or 'symbols' not in exploded.columns:
        return pd.DataFrame(columns=['symbol', 'chunk_count'])

    cov = exploded['symbols'].value_counts().reset_index()
    cov.columns = ['symbol', 'chunk_count']
    return cov

def build_workspace_status_table(documents_df: pd.DataFrame, chunks_df: pd.DataFrame) -> pd.DataFrame:
    summary = build_workspace_summary(documents_df, chunks_df)

    data = [
        {"metric": "Total Documents", "value": summary["document_count"]},
        {"metric": "Total Chunks", "value": summary["chunk_count"]},
        {"metric": "Memory Cards", "value": summary["memory_card_count"]},
        {"metric": "Warnings Detected", "value": summary["warning_count"]}
    ]
    return pd.DataFrame(data)

def summarize_workspace_health(summary: Dict) -> Dict:
    doc_c = summary.get("document_count", 0)
    score = min(1.0, doc_c / 100.0) if doc_c > 0 else 0.0

    return {
        "status": "Healthy" if score > 0.5 else "Needs More Research",
        "health_score": score,
        "note": "Workspace health represents offline research capacity, not production readiness."
    }
