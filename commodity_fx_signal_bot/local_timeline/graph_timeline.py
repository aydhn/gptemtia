"""
Graph evolution timeline module.
"""

from pathlib import Path
import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def classify_graph_event(path: Path, project_root: Path) -> str:
    rel = path.relative_to(project_root).as_posix()
    if "node" in rel:
        return "node_update"
    if "edge" in rel:
        return "edge_update"
    return "graph_structure_update"

def link_graph_events_to_nodes_edges(project_root: Path, graph_df: pd.DataFrame) -> pd.DataFrame:
    if graph_df.empty:
        return pd.DataFrame()
    mapped = graph_df.copy()
    mapped['linked_element'] = "inferred_element"
    return mapped

def build_knowledge_graph_evolution_timeline(project_root: Path, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "extracted in pipeline"}

def summarize_graph_timeline(graph_df: pd.DataFrame) -> dict:
    if graph_df.empty:
        return {"total_graph_events": 0}
    return {
        "total_graph_events": len(graph_df),
        "unique_graph_files": graph_df['relative_path'].nunique() if 'relative_path' in graph_df else 0
    }
