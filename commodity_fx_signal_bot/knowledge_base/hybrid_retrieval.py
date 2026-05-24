import pandas as pd
from typing import Tuple, Dict, Optional
import numpy as np

from knowledge_base.kb_config import KnowledgeBaseProfile
from knowledge_base.tfidf_retrieval import run_tfidf_retrieval
from knowledge_base.fuzzy_retrieval import run_fuzzy_retrieval

def combine_retrieval_scores(
    tfidf_df: Optional[pd.DataFrame] = None,
    fuzzy_df: Optional[pd.DataFrame] = None,
    keyword_df: Optional[pd.DataFrame] = None
) -> pd.DataFrame:
    dfs = []
    if tfidf_df is not None and not tfidf_df.empty:
        dfs.append(tfidf_df[['chunk_id', 'tfidf_score']])
    if fuzzy_df is not None and not fuzzy_df.empty:
        dfs.append(fuzzy_df[['chunk_id', 'fuzzy_score']])

    if not dfs:
        return pd.DataFrame()

    # Merge on chunk_id
    combined = dfs[0]
    for df in dfs[1:]:
        combined = pd.merge(combined, df, on='chunk_id', how='outer')

    combined = combined.fillna(0.0)

    # Calculate hybrid score (simple average of non-zero components or weighted)
    # Give TF-IDF slightly higher weight if it exists
    tfidf_col = 'tfidf_score' if 'tfidf_score' in combined.columns else None
    fuzzy_col = 'fuzzy_score' if 'fuzzy_score' in combined.columns else None

    scores = []
    for _, row in combined.iterrows():
        t_score = row[tfidf_col] if tfidf_col else 0.0
        f_score = row[fuzzy_col] if fuzzy_col else 0.0

        # Weighted combination
        h_score = (t_score * 0.6) + (f_score * 0.4) if tfidf_col and fuzzy_col else max(t_score, f_score)
        scores.append(h_score)

    combined['hybrid_score'] = scores
    return combined

def run_hybrid_retrieval(query: str, documents_df: pd.DataFrame, chunks_df: pd.DataFrame, profile: KnowledgeBaseProfile) -> Tuple[pd.DataFrame, Dict]:
    if chunks_df.empty:
        return pd.DataFrame(), {"status": "skipped", "reason": "empty chunks"}

    tfidf_res = None
    if profile.enable_tfidf:
        tfidf_res, _ = run_tfidf_retrieval(query, chunks_df, top_k=profile.retrieval_top_k * 2)

    fuzzy_res = None
    if profile.enable_fuzzy:
        fuzzy_res, _ = run_fuzzy_retrieval(query, chunks_df, top_k=profile.retrieval_top_k * 2)

    combined_scores = combine_retrieval_scores(tfidf_res, fuzzy_res)

    if combined_scores.empty:
        return pd.DataFrame(), {"status": "success", "matches": 0}

    # Merge back chunk details
    results_df = pd.merge(combined_scores, chunks_df, on='chunk_id', how='inner')

    # Rerank with bonuses
    results_df = rerank_retrieval_results(results_df, query)

    # Filter by minimum quality score if applicable
    # This ensures we don't return garbage
    results_df = results_df[results_df['final_score'] >= profile.min_quality_score]

    results_df = results_df.sort_values('final_score', ascending=False).head(profile.retrieval_top_k)

    # Join document details (title, path)
    if not documents_df.empty:
        # Avoid dropping columns if names collide
        doc_details = documents_df[['document_id', 'title', 'path', 'relative_path', 'document_type']].copy()
        results_df = pd.merge(results_df, doc_details, on='document_id', how='left', suffixes=('', '_doc'))

    summary = summarize_retrieval_results(results_df)
    summary["query"] = query

    return results_df, summary

def rerank_retrieval_results(results_df: pd.DataFrame, query: str) -> pd.DataFrame:
    if results_df.empty:
        return results_df

    final_scores = []
    q_lower = query.lower()

    for _, row in results_df.iterrows():
        base_score = row.get('hybrid_score', 0.0)

        # Check for symbol match bonus
        symbols = row.get('symbols', [])
        symbol_bonus = 0.0
        if isinstance(symbols, list):
            for sym in symbols:
                if sym.lower() in q_lower:
                    symbol_bonus = 0.15
                    break

        # Check for module match bonus
        modules = row.get('modules', [])
        module_bonus = 0.0
        if isinstance(modules, list):
            for mod in modules:
                if mod.lower() in q_lower:
                    module_bonus = 0.10
                    break

        final_score = base_score + symbol_bonus + module_bonus
        final_scores.append(min(1.0, final_score))

    results_df['final_score'] = final_scores
    return results_df

def summarize_retrieval_results(results_df: pd.DataFrame) -> Dict:
    return {
        "status": "success",
        "matches": len(results_df),
        "max_score": float(results_df['final_score'].max()) if not results_df.empty else 0.0,
        "mean_score": float(results_df['final_score'].mean()) if not results_df.empty else 0.0
    }
