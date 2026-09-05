import pandas as pd
def build_continuity_knowledge_graph_rehearsal(profile) -> tuple[pd.DataFrame, dict]:
    df = build_default_knowledge_graph_edges(profile)
    return df, summarize_continuity_knowledge_graph(df)
def build_default_knowledge_graph_edges(profile) -> pd.DataFrame:
    return pd.DataFrame([{"source": "a", "target": "b", "relation": "c"}])
def summarize_continuity_knowledge_graph(df: pd.DataFrame) -> dict:
    return {"total": len(df)}