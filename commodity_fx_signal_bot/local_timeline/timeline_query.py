"""
Timeline query logic.
"""

import pandas as pd
import hashlib

from local_timeline.timeline_config import LocalTimelineProfile
from local_timeline.timeline_models import TimelineQuery, TimelineQueryResult, build_timeline_query_id, build_timeline_query_result_id

def classify_timeline_query_intent(query_text: str) -> str:
    qt = query_text.lower()
    if "phase" in qt:
        return "find_events_by_phase"
    if "stale" in qt:
        return "find_stale_artifacts"
    if "gap" in qt:
        return "find_timeline_gaps"
    if "son" in qt or "recent" in qt or "yeni" in qt:
        return "find_recent_changes"
    if "modül" in qt or "module" in qt:
        return "find_events_by_module"
    return "unknown_timeline_query"

def parse_timeline_query(query_text: str, profile: LocalTimelineProfile) -> TimelineQuery:
    intent = classify_timeline_query_intent(query_text)
    qid = build_timeline_query_id(query_text)

    warnings = []
    # Hardcode catch for forbidden intents mapped from user inputs
    qt = query_text.lower()
    if any(x in qt for x in ["al", "sat", "trade", "buy", "sell"]):
        warnings.append("query_rejected_due_to_trading_intent")

    return TimelineQuery(
        query_id=qid,
        query_text=query_text,
        query_intent=intent,
        filters={},
        warnings=warnings
    )

def execute_timeline_query(query: TimelineQuery, event_df: pd.DataFrame, phase_df: pd.DataFrame | None = None, evolution_df: pd.DataFrame | None = None, profile: LocalTimelineProfile | None = None) -> tuple[pd.DataFrame, dict]:
    results = []

    if "query_rejected_due_to_trading_intent" in query.warnings:
        # return safe non-use policy rejection
        return pd.DataFrame(), {"status": "rejected"}

    # very naive matching for mockup
    if not event_df.empty:
        matched = event_df.head(5)
        rank = 1
        for _, row in matched.iterrows():
            results.append({
                "result_id": build_timeline_query_result_id(query.query_id, rank),
                "query_id": query.query_id,
                "event_id": row.get('event_id'),
                "artifact_id": None,
                "rank": rank,
                "score": 0.9,
                "explanation": f"Matched event {row.get('event_type')}",
                "warnings": []
            })
            rank += 1

    df = pd.DataFrame(results)
    if not df.empty:
        df = rank_timeline_query_results(df)

    summary = summarize_timeline_query_results(df)
    return df, summary

def rank_timeline_query_results(results_df: pd.DataFrame) -> pd.DataFrame:
    if results_df.empty:
        return results_df
    return results_df.sort_values(by="score", ascending=False)

def build_timeline_query_examples(profile: LocalTimelineProfile) -> pd.DataFrame:
    examples = [
        {"query": "Phase 60 sonrası hangi çıktılar oluştu?"},
        {"query": "Son değişen quality raporları neler?"},
        {"query": "Hangi artifactler stale görünüyor?"},
        {"query": "artifact_metadata modülü ne zaman güncellendi?"},
        {"query": "evidence governance ile ilgili son eventler neler?"},
        {"query": "scenario regression timeline gap var mı?"},
        {"query": "son 30 günde hangi generated docs değişti?"},
        {"query": "hangi fazlarda event eksik?"}
    ]
    return pd.DataFrame(examples)

def summarize_timeline_query_results(results_df: pd.DataFrame) -> dict:
    if results_df.empty:
        return {"total_results": 0}
    return {"total_results": len(results_df)}
