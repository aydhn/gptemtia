import re

file_path = "commodity_fx_signal_bot/ml/feature_store.py"
with open(file_path, "r") as f:
    content = f.read()

addition = """
    # Phase 66: Local Knowledge Graph
    def load_graph_node_registry(self) -> pd.DataFrame:
        return self.data_lake.load_graph_node_registry()

    def load_graph_edge_registry(self) -> pd.DataFrame:
        return self.data_lake.load_graph_edge_registry()

    def load_artifact_relationship_graph(self) -> dict:
        return self.data_lake.load_artifact_relationship_graph()

    def load_module_relationship_graph(self) -> pd.DataFrame:
        return self.data_lake.load_module_relationship_graph()

    def load_report_relationship_graph(self) -> pd.DataFrame:
        return self.data_lake.load_report_relationship_graph()

    def load_evidence_relationship_graph(self) -> pd.DataFrame:
        return self.data_lake.load_evidence_relationship_graph()

    def load_card_relationship_graph(self) -> pd.DataFrame:
        return self.data_lake.load_card_relationship_graph()

    def load_scenario_regression_relationship_graph(self) -> pd.DataFrame:
        return self.data_lake.load_scenario_regression_relationship_graph()

    def load_command_report_relationship_graph(self) -> pd.DataFrame:
        return self.data_lake.load_command_report_relationship_graph()

    def load_local_semantic_keyword_index(self) -> pd.DataFrame:
        return self.data_lake.load_local_semantic_keyword_index()

    def load_local_tfidf_index_manifest(self) -> dict:
        return self.data_lake.load_local_tfidf_index_manifest()

    def load_relationship_query_results(self, query_name: str) -> pd.DataFrame:
        return self.data_lake.load_relationship_query_results(query_name)

    def load_graph_neighborhood_report(self, node_id: str) -> pd.DataFrame:
        return self.data_lake.load_graph_neighborhood_report(node_id)

    def load_graph_centrality_summary(self) -> pd.DataFrame:
        return self.data_lake.load_graph_centrality_summary()

    def load_orphan_artifact_report(self) -> pd.DataFrame:
        return self.data_lake.load_orphan_artifact_report()

    def load_graph_gap_report(self) -> pd.DataFrame:
        return self.data_lake.load_graph_gap_report()

    def load_stale_relationship_report(self) -> pd.DataFrame:
        return self.data_lake.load_stale_relationship_report()

    def load_graph_export_manifest(self) -> dict:
        return self.data_lake.load_graph_export_manifest()

    def load_graph_validation_report(self) -> pd.DataFrame:
        return self.data_lake.load_graph_validation_report()

    def load_graph_quality(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_graph_quality(profile_name or "balanced_local_graph")

    def load_local_knowledge_graph_report(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_local_knowledge_graph_report(profile_name or "balanced_local_graph")

    def list_available_local_knowledge_graph_reports(self) -> dict:
        return {"reports": []}
"""

if "load_graph_node_registry" not in content:
    content = content.replace("class FeatureStore:", "class FeatureStore:\n" + addition)

with open(file_path, "w") as f:
    f.write(content)
