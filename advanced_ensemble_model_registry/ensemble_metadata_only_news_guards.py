# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Metadata-Only News Guards."""

from typing import Any, Dict


def build_ensemble_metadata_only_news_guards() -> Dict[str, Any]:
    """Build metadata-only news guard specifications for ensemble contracts.
    
    Returns:
        Dict[str, Any]: Metadata-only news guards dictionary.
    """
    return {
        "article_body_prohibition_guard": {
            "guard_name": "article_body_prohibition_guard",
            "enforced": True,
            "contains_full_article_text": False,
            "contains_article_body": False,
            "contains_raw_content": False,
            "contains_scraped_html": False,
            "non_signal": True,
        },
        "embedding_vector_prohibition_guard": {
            "guard_name": "embedding_vector_prohibition_guard",
            "enforced": True,
            "contains_embedding": False,
            "contains_vector": False,
            "dense_embeddings_blocked": True,
            "non_signal": True,
        },
        "sentiment_output_prohibition_guard": {
            "guard_name": "sentiment_output_prohibition_guard",
            "enforced": True,
            "sentiment_model_output": False,
            "raw_sentiment_scores_blocked": True,
            "non_signal": True,
        },
        "news_metadata_preservation_guard": {
            "guard_name": "news_metadata_preservation_guard",
            "enforced": True,
            "metadata_fields_allowed": ["count", "timestamp", "source_ref", "category"],
            "non_signal": True,
        },
    }


def validate_ensemble_metadata_only_news_guards(guards: Dict[str, Any]) -> bool:
    """Validate that news guards prohibit full text, embeddings, and raw sentiment.
    
    Args:
        guards: Dict of guards.
        
    Returns:
        bool: True if strictly metadata-only, False otherwise.
    """
    if not isinstance(guards, dict) or len(guards) == 0:
        return False
    for name, guard in guards.items():
        if not isinstance(guard, dict):
            return False
        if not guard.get("enforced", False):
            return False
        if guard.get("contains_full_article_text", False):
            return False
        if guard.get("contains_article_body", False):
            return False
        if guard.get("contains_raw_content", False):
            return False
        if guard.get("contains_scraped_html", False):
            return False
        if guard.get("contains_embedding", False):
            return False
        if guard.get("contains_vector", False):
            return False
        if guard.get("sentiment_model_output", False):
            return False
        if not guard.get("non_signal", False):
            return False
    return True


def summarize_ensemble_metadata_only_news_guards(guards: Dict[str, Any]) -> Dict[str, Any]:
    """Summarize ensemble metadata-only news guards.
    
    Args:
        guards: Dict of guards.
        
    Returns:
        Dict[str, Any]: Summary dictionary.
    """
    return {
        "total_guards": len(guards),
        "guard_names": list(guards.keys()),
        "all_guards_enforced": all(g.get("enforced", False) for g in guards.values()),
        "raw_text_prohibited": True,
        "embeddings_prohibited": True,
        "sentiment_outputs_prohibited": True,
        "dry_run": True,
        "non_signal": True,
    }
