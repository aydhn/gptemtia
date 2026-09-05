import pandas as pd
from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile
from local_post_completion_preservation.preservation_models import KnowledgeCapsuleItem, build_knowledge_capsule_item_id

def build_default_knowledge_capsule_topics(profile: LocalPostCompletionPreservationProfile) -> list[KnowledgeCapsuleItem]:
    return [
        KnowledgeCapsuleItem(
            capsule_id=build_knowledge_capsule_item_id("topic1"),
            topic="topic1", summary="summary", source_refs=[], boundary_note="no live/broker/deploy/advice", warnings=[]
        )
    ]

def build_knowledge_capsule_topic_map(profile: LocalPostCompletionPreservationProfile) -> tuple[pd.DataFrame, dict]:
    topics = build_default_knowledge_capsule_topics(profile)
    df = pd.DataFrame([{"topic": t.topic} for t in topics])
    return df, summarize_knowledge_capsule_topic_map(df)

def summarize_knowledge_capsule_topic_map(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
