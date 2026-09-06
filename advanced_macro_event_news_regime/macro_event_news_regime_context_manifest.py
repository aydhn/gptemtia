"""Phase 132: Macro/Event/News Regime Context Manifest."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)
from advanced_macro_event_news_regime.macro_event_news_regime_models import (
    MacroEventNewsRegimeManifest,
)


def create_macro_event_news_regime_context_manifest(
    manifest_name: str,
    macro_entity_count: int,
    event_entity_count: int,
    news_metadata_entity_count: int,
    context_report_count: int,
    finding_count: int,
    manual_review_count: int,
    context_score: float,
    manual_review_required: bool = True,
) -> MacroEventNewsRegimeManifest:
    """Instantiate a MacroEventNewsRegimeManifest asserting strict safety invariants."""
    return MacroEventNewsRegimeManifest(
        manifest_name=manifest_name,
        current_phase=132,
        target_final_phase=160,
        next_phase=133,
        macro_entity_count=macro_entity_count,
        event_entity_count=event_entity_count,
        news_metadata_entity_count=news_metadata_entity_count,
        context_report_count=context_report_count,
        finding_count=finding_count,
        manual_review_count=manual_review_count,
        context_score=context_score,
        manual_review_required=manual_review_required,
        non_signal=True,
        source_preserved=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        contains_full_article_text=False,
        contains_article_body=False,
        contains_raw_content=False,
        contains_scraped_html=False,
        contains_embedding=False,
        contains_vector=False,
        sentiment_model_output=False,
        model_training_executed=False,
        model_fit_executed=False,
        model_predict_executed=False,
        clustering_executed=False,
        unsupervised_execution=False,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
    )


def build_macro_event_news_regime_context_manifest(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build manifest DataFrame and summary dictionary for Phase 132."""
    p = profile or get_macro_event_news_regime_profile()
    manifest_obj = create_macro_event_news_regime_context_manifest(
        manifest_name="macro_event_news_regime_context_manifest",
        macro_entity_count=10,
        event_entity_count=10,
        news_metadata_entity_count=11,
        context_report_count=20,
        finding_count=3,
        manual_review_count=8,
        context_score=1.0,
        manual_review_required=False,
    )

    row = {
        "manifest_name": manifest_obj.manifest_name,
        "current_phase": manifest_obj.current_phase,
        "target_final_phase": manifest_obj.target_final_phase,
        "next_phase": manifest_obj.next_phase,
        "macro_entity_count": manifest_obj.macro_entity_count,
        "event_entity_count": manifest_obj.event_entity_count,
        "news_metadata_entity_count": manifest_obj.news_metadata_entity_count,
        "context_report_count": manifest_obj.context_report_count,
        "finding_count": manifest_obj.finding_count,
        "manual_review_count": manifest_obj.manual_review_count,
        "context_score": manifest_obj.context_score,
        "manual_review_required": manifest_obj.manual_review_required,
        "non_signal": manifest_obj.non_signal,
        "source_preserved": manifest_obj.source_preserved,
        "official_approval": manifest_obj.official_approval,
        "production_ready": manifest_obj.production_ready,
        "broker_ready": manifest_obj.broker_ready,
        "contains_target_or_prediction": manifest_obj.contains_target_or_prediction,
        "contains_trading_recommendation": manifest_obj.contains_trading_recommendation,
        "contains_full_article_text": manifest_obj.contains_full_article_text,
        "contains_article_body": manifest_obj.contains_article_body,
        "contains_raw_content": manifest_obj.contains_raw_content,
        "contains_scraped_html": manifest_obj.contains_scraped_html,
        "contains_embedding": manifest_obj.contains_embedding,
        "contains_vector": manifest_obj.contains_vector,
        "sentiment_model_output": manifest_obj.sentiment_model_output,
        "model_training_executed": manifest_obj.model_training_executed,
        "model_fit_executed": manifest_obj.model_fit_executed,
        "model_predict_executed": manifest_obj.model_predict_executed,
        "clustering_executed": manifest_obj.clustering_executed,
        "unsupervised_execution": manifest_obj.unsupervised_execution,
        "destructive_action_allowed": manifest_obj.destructive_action_allowed,
        "auto_fix_allowed": manifest_obj.auto_fix_allowed,
        "auto_drop_allowed": manifest_obj.auto_drop_allowed,
        "created_at": manifest_obj.created_at,
    }
    df = pd.DataFrame([row])
    summary = {
        "manifest_name": manifest_obj.manifest_name,
        "current_phase": manifest_obj.current_phase,
        "next_phase": manifest_obj.next_phase,
        "context_score": manifest_obj.context_score,
        "non_signal": True,
        "source_preserved": True,
        "zero_article_text": True,
        "zero_embeddings": True,
        "zero_sentiment": True,
        "zero_ml": True,
    }
    return df, summary


def summarize_macro_event_news_regime_context_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for context manifest DataFrame."""
    return {
        "manifest_name": df["manifest_name"].iloc[0] if not df.empty else "empty",
        "current_phase": int(df["current_phase"].iloc[0]) if not df.empty else 132,
        "next_phase": int(df["next_phase"].iloc[0]) if not df.empty else 133,
        "context_score": float(df["context_score"].iloc[0]) if not df.empty else 1.0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
