import pandas as pd
from typing import Tuple, Dict, List
import re

from knowledge_base.kb_models import RetrievalResult, build_retrieval_result_id, sanitize_query_text

def calculate_simple_fuzzy_score(query: str, text: str) -> float:
    if not query or not text:
        return 0.0

    sanitized_query = sanitize_query_text(query).lower()
    text_lower = text.lower()

    query_tokens = set(sanitized_query.split())
    if not query_tokens:
        return 0.0

    text_tokens = set(re.findall(r'\b\w+\b', text_lower))

    # Calculate simple Jaccard-like overlap
    intersection = query_tokens.intersection(text_tokens)

    # Give weight to exact full phrase match
    phrase_bonus = 0.5 if sanitized_query in text_lower else 0.0

    # Base score on percentage of query tokens found
    token_score = len(intersection) / len(query_tokens)

    final_score = (token_score * 0.5) + phrase_bonus
    return min(1.0, final_score)

def run_fuzzy_retrieval(query: str, chunks_df: pd.DataFrame, top_k: int = 10) -> Tuple[pd.DataFrame, Dict]:
    if chunks_df.empty or 'text' not in chunks_df.columns:
        return pd.DataFrame(), {"status": "skipped", "reason": "empty dataframe"}

    scores = chunks_df['text'].apply(lambda x: calculate_simple_fuzzy_score(query, str(x)))

    valid_mask = scores > 0
    if not valid_mask.any():
        return pd.DataFrame(), {"status": "success", "matches": 0}

    results_df = chunks_df[valid_mask].copy()
    results_df['fuzzy_score'] = scores[valid_mask]

    results_df = results_df.sort_values('fuzzy_score', ascending=False).head(top_k)

    return results_df, {"status": "success", "matches": len(results_df)}

def build_fuzzy_retrieval_results(query: str, scored_df: pd.DataFrame, top_k: int = 10) -> List[RetrievalResult]:
    results = []

    if scored_df.empty or 'fuzzy_score' not in scored_df.columns:
        return results

    sorted_df = scored_df.sort_values('fuzzy_score', ascending=False).head(top_k)

    for _, row in sorted_df.iterrows():
        doc_id = row.get('document_id', 'unknown')
        chunk_id = row.get('chunk_id')
        score = row.get('fuzzy_score', 0.0)

        text = row.get('text', '')
        snippet = text[:200] + "..." if len(text) > 200 else text

        result_id = build_retrieval_result_id(query, doc_id, chunk_id, "fuzzy_retrieval")

        res = RetrievalResult(
            result_id=result_id,
            query=query,
            document_id=doc_id,
            chunk_id=chunk_id,
            method="fuzzy_retrieval",
            score=float(score),
            title=f"Chunk {chunk_id} from {doc_id}",
            path="unknown",
            snippet=snippet,
            metadata={"source_module": row.get('modules', [])},
            warnings=[]
        )
        results.append(res)

    return results
