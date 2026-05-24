import pandas as pd
from typing import Tuple, Dict, List
import numpy as np

from knowledge_base.kb_models import RetrievalResult, build_retrieval_result_id, sanitize_query_text
from core.logger import get_logger

logger = get_logger(__name__)

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

def build_tfidf_matrix(chunks_df: pd.DataFrame) -> Tuple[object, object, Dict]:
    if not SKLEARN_AVAILABLE:
        logger.warning("scikit-learn is not available. TF-IDF retrieval will be disabled.")
        return None, None, {"status": "disabled", "reason": "scikit-learn missing"}

    if chunks_df.empty or 'text' not in chunks_df.columns:
        return None, None, {"status": "skipped", "reason": "empty dataframe or missing 'text' column"}

    vectorizer = TfidfVectorizer(stop_words='english', min_df=2, max_features=10000)
    try:
        tfidf_matrix = vectorizer.fit_transform(chunks_df['text'].fillna(''))
        return vectorizer, tfidf_matrix, {"status": "success", "vocab_size": len(vectorizer.vocabulary_)}
    except Exception as e:
        logger.error(f"Failed to build TF-IDF matrix: {e}")
        return None, None, {"status": "failed", "error": str(e)}

def score_tfidf_results(query: str, chunks_df: pd.DataFrame) -> pd.Series:
    if not SKLEARN_AVAILABLE or chunks_df.empty:
        return pd.Series(0.0, index=chunks_df.index)

    vectorizer, tfidf_matrix, _ = build_tfidf_matrix(chunks_df)
    if vectorizer is None or tfidf_matrix is None:
        return pd.Series(0.0, index=chunks_df.index)

    sanitized_query = sanitize_query_text(query)
    if not sanitized_query:
        return pd.Series(0.0, index=chunks_df.index)

    try:
        query_vec = vectorizer.transform([sanitized_query])
        scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
        return pd.Series(scores, index=chunks_df.index)
    except Exception as e:
        logger.error(f"Error scoring TF-IDF: {e}")
        return pd.Series(0.0, index=chunks_df.index)

def run_tfidf_retrieval(query: str, chunks_df: pd.DataFrame, top_k: int = 10) -> Tuple[pd.DataFrame, Dict]:
    if not SKLEARN_AVAILABLE:
        return pd.DataFrame(), {"status": "disabled", "reason": "scikit-learn missing"}

    scores = score_tfidf_results(query, chunks_df)

    # Filter for non-zero scores
    valid_mask = scores > 0
    if not valid_mask.any():
        return pd.DataFrame(), {"status": "success", "matches": 0}

    results_df = chunks_df[valid_mask].copy()
    results_df['tfidf_score'] = scores[valid_mask]

    # Sort and take top k
    results_df = results_df.sort_values('tfidf_score', ascending=False).head(top_k)

    return results_df, {"status": "success", "matches": len(results_df)}

def build_tfidf_retrieval_results(query: str, scored_df: pd.DataFrame, top_k: int = 10) -> List[RetrievalResult]:
    results: List[RetrievalResult] = []

    if scored_df.empty or 'tfidf_score' not in scored_df.columns:
        return results

    sorted_df = scored_df.sort_values('tfidf_score', ascending=False).head(top_k)

    for _, row in sorted_df.iterrows():
        doc_id = row.get('document_id', 'unknown')
        chunk_id = row.get('chunk_id')
        score = row.get('tfidf_score', 0.0)

        # Determine snippet
        text = row.get('text', '')
        snippet = text[:200] + "..." if len(text) > 200 else text

        result_id = build_retrieval_result_id(query, doc_id, chunk_id, "tfidf_retrieval")

        res = RetrievalResult(
            result_id=result_id,
            query=query,
            document_id=doc_id,
            chunk_id=chunk_id,
            method="tfidf_retrieval",
            score=float(score),
            title=f"Chunk {chunk_id} from {doc_id}", # We might need document details joined here in a real scenario
            path="unknown", # Typically joined from documents_df
            snippet=snippet,
            metadata={"source_module": row.get('modules', [])},
            warnings=[]
        )
        results.append(res)

    return results
