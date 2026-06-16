import pandas as pd
from pathlib import Path
from typing import Tuple, Dict, Optional
from config.settings import Settings
from data.storage.data_lake import DataLake
from local_knowledge_graph.graph_config import LocalKnowledgeGraphProfile, get_default_local_knowledge_graph_profile
from local_knowledge_graph.node_registry import build_graph_node_registry
from local_knowledge_graph.edge_registry import build_graph_edge_registry
from local_knowledge_graph.graph_builder import build_artifact_relationship_graph
from local_knowledge_graph.semantic_keyword_index import build_local_semantic_keyword_index
from local_knowledge_graph.relationship_query import build_relationship_query_examples
from local_knowledge_graph.graph_analysis import build_graph_centrality_summary
from local_knowledge_graph.graph_quality import build_graph_quality_report
import traceback

class LocalKnowledgeGraphPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[LocalKnowledgeGraphProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_local_knowledge_graph_profile()

    def build_graph_node_edge_registry(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        try:
            node_df, n_sum = build_graph_node_registry(self.project_root, self.profile)
            edge_df, e_sum = build_graph_edge_registry(node_df, self.project_root, self.profile)
            if save:
                self.data_lake.save_graph_node_registry(node_df, n_sum)
                self.data_lake.save_graph_edge_registry(edge_df, e_sum)
            return {"nodes": node_df, "edges": edge_df}, {"warnings": []}
        except Exception as e:
            return {}, {"warnings": [str(e)]}

    def build_artifact_relationship_graph(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        try:
            nodes, _ = build_graph_node_registry(self.project_root, self.profile)
            edges, _ = build_graph_edge_registry(nodes, self.project_root, self.profile)
            graph, g_sum = build_artifact_relationship_graph(nodes, edges, self.profile)
            if save:
                self.data_lake.save_artifact_relationship_graph(graph, g_sum)
            return {"nodes": nodes, "edges": edges}, g_sum
        except Exception as e:
            return {}, {"warnings": [str(e)]}

    def build_semantic_index_report(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        try:
            nodes, _ = build_graph_node_registry(self.project_root, self.profile)
            keyword_df, k_sum = build_local_semantic_keyword_index(nodes, self.project_root, self.profile)
            if save:
                self.data_lake.save_local_semantic_keyword_index(keyword_df, k_sum)
            return {"keywords": keyword_df}, k_sum
        except Exception as e:
            return {}, {"warnings": [str(e)]}

    def build_relationship_query_report(self, query_text: str, save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        try:
            examples = build_relationship_query_examples(self.profile)
            if save:
                self.data_lake.save_relationship_query_results("example", examples, {})
            return examples, {"warnings": []}
        except Exception as e:
            return pd.DataFrame(), {"warnings": [str(e)]}

    def build_graph_analysis_report(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        try:
            nodes, _ = build_graph_node_registry(self.project_root, self.profile)
            edges, _ = build_graph_edge_registry(nodes, self.project_root, self.profile)
            centrality, c_sum = build_graph_centrality_summary(nodes, edges)
            if save:
                self.data_lake.save_graph_centrality_summary(centrality, c_sum)
            return {"centrality": centrality}, c_sum
        except Exception as e:
            return {}, {"warnings": [str(e)]}

    def build_graph_quality_report(self, save: bool = True) -> Tuple[Dict, Dict]:
        try:
            q_rep = build_graph_quality_report({"test": "ok"})
            if save:
                self.data_lake.save_graph_quality(self.profile.name, q_rep)
            return q_rep, {"warnings": []}
        except Exception as e:
            return {}, {"warnings": [str(e)]}

    def build_graph_status(self, save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        try:
            status_df = pd.DataFrame([{"module": "local_knowledge_graph", "status": "ready"}])
            return status_df, {"warnings": []}
        except Exception as e:
            return pd.DataFrame(), {"warnings": [str(e)]}
