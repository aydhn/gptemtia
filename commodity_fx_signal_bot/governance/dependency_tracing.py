import pandas as pd

from governance.lineage_graph import LineageGraph


class ArtifactDependencyTracer:
    def __init__(self, lineage_graph: LineageGraph):
        self.graph = lineage_graph
        self.nodes_df = lineage_graph.to_node_dataframe()

    def _build_trace_df(self, nodes: list[str], direction: str) -> tuple[pd.DataFrame, dict]:
        warnings = []
        if not nodes:
            warnings.append(f"No {direction} dependencies found.")
            return pd.DataFrame(), {"warnings": warnings}

        res = []
        # we don't track depth accurately in the simple list output of graph methods,
        # but we can return the nodes with their info.
        for n_id in nodes:
            if not self.nodes_df.empty and n_id in self.nodes_df["node_id"].values:
                row = self.nodes_df[self.nodes_df["node_id"] == n_id].iloc[0]
                res.append({
                    "depth": "unknown", # would need to track in graph traversal
                    "node_id": n_id,
                    "artifact_id": row.get("artifact_id"),
                    "artifact_type": row.get("artifact_type"),
                    "relation": direction,
                    "path": row.get("path"),
                    "confidence_score": 1.0,
                    "warnings": []
                })

        df = pd.DataFrame(res)
        return df, {"warnings": warnings}

    def trace_upstream(self, artifact_id_or_node_id: str, max_depth: int = 8) -> tuple[pd.DataFrame, dict]:
        node_id = artifact_id_or_node_id if artifact_id_or_node_id.startswith("n") else f"node_{artifact_id_or_node_id}"
        upstream_nodes = self.graph.get_upstream_nodes(node_id, max_depth)
        return self._build_trace_df(upstream_nodes, "upstream")

    def trace_downstream(self, artifact_id_or_node_id: str, max_depth: int = 8) -> tuple[pd.DataFrame, dict]:
        node_id = artifact_id_or_node_id if artifact_id_or_node_id.startswith("n") else f"node_{artifact_id_or_node_id}"
        downstream_nodes = self.graph.get_downstream_nodes(node_id, max_depth)
        return self._build_trace_df(downstream_nodes, "downstream")

    def trace_symbol_dependencies(self, symbol: str, inventory_df: pd.DataFrame, max_depth: int = 8) -> tuple[pd.DataFrame, dict]:
        warnings = ["Tracing symbol dependencies is an approximation. Live execution is NOT guaranteed."]

        if inventory_df.empty:
            return pd.DataFrame(), {"warnings": ["Inventory empty"]}

        # Find raw artifact for symbol
        mask = inventory_df["relative_path"].str.contains(symbol, case=False, na=False)
        symbol_nodes = inventory_df[mask]["artifact_id"].tolist()

        if not symbol_nodes:
            warnings.append(f"No artifacts found for symbol {symbol}")
            return pd.DataFrame(), {"warnings": warnings}

        all_downstream = set()
        for art_id in symbol_nodes:
            down_nodes = self.graph.get_downstream_nodes(f"node_{art_id}", max_depth)
            all_downstream.update(down_nodes)

        df, meta = self._build_trace_df(list(all_downstream), "downstream")
        meta["warnings"].extend(warnings)
        return df, meta

    def trace_module_dependencies(self, module_name: str, inventory_df: pd.DataFrame, max_depth: int = 8) -> tuple[pd.DataFrame, dict]:
        warnings = [f"Tracing module {module_name} dependencies is an approximation."]

        if inventory_df.empty:
            return pd.DataFrame(), {"warnings": ["Inventory empty"]}

        mask = inventory_df["relative_path"].str.contains(module_name, case=False, na=False)
        module_nodes = inventory_df[mask]["artifact_id"].tolist()

        if not module_nodes:
            warnings.append(f"No artifacts found for module {module_name}")
            return pd.DataFrame(), {"warnings": warnings}

        all_upstream = set()
        for art_id in module_nodes:
            up_nodes = self.graph.get_upstream_nodes(f"node_{art_id}", max_depth)
            all_upstream.update(up_nodes)

        df, meta = self._build_trace_df(list(all_upstream), "upstream")
        meta["warnings"].extend(warnings)
        return df, meta
