import re

file_path = "commodity_fx_signal_bot/data/storage/data_lake.py"
with open(file_path, "r") as f:
    content = f.read()

imports_to_add = """from config.paths import (
    DATA_LAKE_ARTIFACT_METADATA_DIR,
    DATA_LAKE_ARTIFACT_METADATA_INVENTORY_DIR,
    DATA_LAKE_ARTIFACT_METADATA_REGISTRY_DIR,
    DATA_LAKE_ARTIFACT_METADATA_MODEL_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_DATASET_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_EXPERIMENT_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_REPRODUCIBILITY_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_BACKTEST_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_SCENARIO_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_REGRESSION_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_FEATURE_SET_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_SYNTHETIC_DATA_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_RESEARCH_REPORT_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_LINEAGE_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_LIMITATION_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_INTENDED_USE_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_NON_USE_POLICY_CARDS_DIR,
    DATA_LAKE_ARTIFACT_METADATA_SCORING_DIR,
    DATA_LAKE_ARTIFACT_METADATA_VALIDATION_DIR,
    DATA_LAKE_ARTIFACT_METADATA_QUALITY_DIR,
    DATA_LAKE_ARTIFACT_METADATA_EXPORTS_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_NODES_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_EDGES_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_GRAPHS_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_MODULE_GRAPHS_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_REPORT_GRAPHS_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_EVIDENCE_GRAPHS_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_CARD_GRAPHS_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_SCENARIO_REGRESSION_GRAPHS_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_COMMAND_REPORT_GRAPHS_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_SEMANTIC_INDEX_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_TFIDF_INDEX_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_QUERIES_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_NEIGHBORHOODS_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_ANALYSIS_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_GAPS_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_EXPORTS_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_VALIDATION_DIR,
    LAKE_LOCAL_KNOWLEDGE_GRAPH_QUALITY_DIR,
    REPORTS_LOCAL_KNOWLEDGE_GRAPH_JSON_DIR,
    REPORTS_LOCAL_KNOWLEDGE_GRAPH_CSV_DIR,
    REPORTS_LOCAL_KNOWLEDGE_GRAPH_TXT_DIR,
    REPORTS_LOCAL_KNOWLEDGE_GRAPH_MARKDOWN_DIR
)
"""

if "LAKE_LOCAL_KNOWLEDGE_GRAPH_NODES_DIR" not in content:
    content = re.sub(r'from config\.paths import \(.*?\n\)', imports_to_add, content, flags=re.DOTALL)

addition = """
    # Phase 66: Local Knowledge Graph
    def save_graph_node_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_NODES_DIR, "graph_node_registry")

    def load_graph_node_registry(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_NODES_DIR / "graph_node_registry.parquet")

    def save_graph_edge_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_EDGES_DIR, "graph_edge_registry")

    def load_graph_edge_registry(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_EDGES_DIR / "graph_edge_registry.parquet")

    def save_artifact_relationship_graph(self, graph: dict, summary: dict | None = None) -> Path:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_GRAPHS_DIR / "artifact_relationship_graph.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(graph, f, indent=4)
        return path

    def load_artifact_relationship_graph(self) -> dict:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_GRAPHS_DIR / "artifact_relationship_graph.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_module_relationship_graph(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_MODULE_GRAPHS_DIR, "module_relationship_graph")

    def load_module_relationship_graph(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_MODULE_GRAPHS_DIR / "module_relationship_graph.parquet")

    def save_report_relationship_graph(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_REPORT_GRAPHS_DIR, "report_relationship_graph")

    def load_report_relationship_graph(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_REPORT_GRAPHS_DIR / "report_relationship_graph.parquet")

    def save_evidence_relationship_graph(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_EVIDENCE_GRAPHS_DIR, "evidence_relationship_graph")

    def load_evidence_relationship_graph(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_EVIDENCE_GRAPHS_DIR / "evidence_relationship_graph.parquet")

    def save_card_relationship_graph(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_CARD_GRAPHS_DIR, "card_relationship_graph")

    def load_card_relationship_graph(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_CARD_GRAPHS_DIR / "card_relationship_graph.parquet")

    def save_scenario_regression_relationship_graph(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_SCENARIO_REGRESSION_GRAPHS_DIR, "scenario_regression_relationship_graph")

    def load_scenario_regression_relationship_graph(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_SCENARIO_REGRESSION_GRAPHS_DIR / "scenario_regression_relationship_graph.parquet")

    def save_command_report_relationship_graph(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_COMMAND_REPORT_GRAPHS_DIR, "command_report_relationship_graph")

    def load_command_report_relationship_graph(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_COMMAND_REPORT_GRAPHS_DIR / "command_report_relationship_graph.parquet")

    def save_local_semantic_keyword_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_SEMANTIC_INDEX_DIR, "local_semantic_keyword_index")

    def load_local_semantic_keyword_index(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_SEMANTIC_INDEX_DIR / "local_semantic_keyword_index.parquet")

    def save_local_tfidf_index_manifest(self, manifest: dict) -> Path:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_TFIDF_INDEX_DIR / "local_tfidf_index_manifest.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=4)
        return path

    def load_local_tfidf_index_manifest(self) -> dict:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_TFIDF_INDEX_DIR / "local_tfidf_index_manifest.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_relationship_query_results(self, query_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_QUERIES_DIR, f"relationship_query_results_{query_name}")

    def load_relationship_query_results(self, query_name: str) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_QUERIES_DIR / f"relationship_query_results_{query_name}.parquet")

    def save_graph_neighborhood_report(self, node_id: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_NEIGHBORHOODS_DIR, f"graph_neighborhood_report_{node_id}")

    def load_graph_neighborhood_report(self, node_id: str) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_NEIGHBORHOODS_DIR / f"graph_neighborhood_report_{node_id}.parquet")

    def save_graph_centrality_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_ANALYSIS_DIR, "graph_centrality_summary")

    def load_graph_centrality_summary(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_ANALYSIS_DIR / "graph_centrality_summary.parquet")

    def save_orphan_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_ANALYSIS_DIR, "orphan_artifact_report")

    def load_orphan_artifact_report(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_ANALYSIS_DIR / "orphan_artifact_report.parquet")

    def save_graph_gap_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_GAPS_DIR, "graph_gap_report")

    def load_graph_gap_report(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_GAPS_DIR / "graph_gap_report.parquet")

    def save_stale_relationship_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_GAPS_DIR, "stale_relationship_report")

    def load_stale_relationship_report(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_GAPS_DIR / "stale_relationship_report.parquet")

    def save_graph_export_manifest(self, manifest: dict) -> Path:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_EXPORTS_DIR / "graph_export_manifest.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=4)
        return path

    def load_graph_export_manifest(self) -> dict:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_EXPORTS_DIR / "graph_export_manifest.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_graph_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_parquet_and_csv(df, LAKE_LOCAL_KNOWLEDGE_GRAPH_VALIDATION_DIR, "graph_validation_report")

    def load_graph_validation_report(self) -> pd.DataFrame:
        return self._load_parquet(LAKE_LOCAL_KNOWLEDGE_GRAPH_VALIDATION_DIR / "graph_validation_report.parquet")

    def save_graph_quality(self, profile_name: str, quality: dict) -> Path:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_QUALITY_DIR / f"graph_quality_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=4)
        return path

    def load_graph_quality(self, profile_name: str) -> dict:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_QUALITY_DIR / f"graph_quality_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_local_knowledge_graph_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_EXPORTS_DIR / f"local_knowledge_graph_report_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        if markdown:
            md_path = REPORTS_LOCAL_KNOWLEDGE_GRAPH_MARKDOWN_DIR / f"local_knowledge_graph_report_{profile_name}.md"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown)
        return path

    def load_local_knowledge_graph_report(self, profile_name: str) -> dict:
        path = LAKE_LOCAL_KNOWLEDGE_GRAPH_EXPORTS_DIR / f"local_knowledge_graph_report_{profile_name}.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_local_knowledge_graph_reports(self) -> pd.DataFrame:
        return pd.DataFrame()
"""

if "save_graph_node_registry" not in content:
    content = content.replace("class DataLake:", "class DataLake:\n" + addition)

with open(file_path, "w") as f:
    f.write(content)
