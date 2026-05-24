
import pandas as pd

from governance.governance_models import (
    LineageEdge,
    LineageNode,
    build_lineage_edge_id,
    build_lineage_node_id,
)


class LineageGraph:
    def __init__(self, nodes: list[LineageNode], edges: list[LineageEdge]):
        self.nodes = nodes
        self.edges = edges

    def to_node_dataframe(self) -> pd.DataFrame:
        if not self.nodes:
            return pd.DataFrame()
        return pd.DataFrame([n.__dict__ for n in self.nodes])

    def to_edge_dataframe(self) -> pd.DataFrame:
        if not self.edges:
            return pd.DataFrame()
        return pd.DataFrame([e.__dict__ for e in self.edges])

    def build_adjacency(self) -> dict[str, list[str]]:
        adj = {n.node_id: [] for n in self.nodes}
        for e in self.edges:
            if e.source_node_id in adj:
                adj[e.source_node_id].append(e.target_node_id)
        return adj

    def get_upstream_nodes(self, node_id: str, max_depth: int = 8) -> list[str]:
        # Upstream means nodes that THIS node depends on (target -> source, or source produces target)
        # Actually standard definition: upstream = source of data. So if edge is (source -> target),
        # upstream of target is source. We need reverse adjacency.
        rev_adj = {n.node_id: [] for n in self.nodes}
        for e in self.edges:
            if e.target_node_id in rev_adj:
                rev_adj[e.target_node_id].append(e.source_node_id)

        visited = set()
        queue = [(node_id, 0)]
        upstream = []

        while queue:
            curr, depth = queue.pop(0)
            if depth >= max_depth:
                continue
            for nxt in rev_adj.get(curr, []):
                if nxt not in visited:
                    visited.add(nxt)
                    upstream.append(nxt)
                    queue.append((nxt, depth + 1))
        return upstream

    def get_downstream_nodes(self, node_id: str, max_depth: int = 8) -> list[str]:
        adj = self.build_adjacency()
        visited = set()
        queue = [(node_id, 0)]
        downstream = []

        while queue:
            curr, depth = queue.pop(0)
            if depth >= max_depth:
                continue
            for nxt in adj.get(curr, []):
                if nxt not in visited:
                    visited.add(nxt)
                    downstream.append(nxt)
                    queue.append((nxt, depth + 1))
        return downstream

    def detect_cycles(self) -> dict:
        adj = self.build_adjacency()
        visited = set()
        rec_stack = set()
        cycles = []

        def dfs(node):
            visited.add(node)
            rec_stack.add(node)
            for neighbor in adj.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    cycles.append((node, neighbor))
                    return True
            rec_stack.remove(node)
            return False

        for n in adj:
            if n not in visited:
                dfs(n)

        return {
            "has_cycles": len(cycles) > 0,
            "cycle_edges": cycles
        }

    def summarize(self) -> dict:
        return {
            "node_count": len(self.nodes),
            "edge_count": len(self.edges),
            "cycles": self.detect_cycles()
        }

def build_lineage_nodes_from_inventory(inventory_df: pd.DataFrame) -> list[LineageNode]:
    nodes = []
    if inventory_df.empty:
        return nodes

    for _, row in inventory_df.iterrows():
        n = LineageNode(
            node_id=build_lineage_node_id(row["artifact_id"]),
            artifact_id=row["artifact_id"],
            artifact_type=row["artifact_type"],
            label=row["file_name"],
            path=row["relative_path"],
            metadata={"size_bytes": row.get("size_bytes")},
            warnings=[]
        )
        nodes.append(n)
    return nodes

def build_lineage_edges_from_provenance(provenance_df: pd.DataFrame, inventory_df: pd.DataFrame) -> list[LineageEdge]:
    edges = []
    if provenance_df is None or provenance_df.empty or inventory_df.empty:
        return edges

    # Example logic: if provenance specifies input_artifact_ids
    for _, prov in provenance_df.iterrows():
        target_art = prov["artifact_id"]
        target_node = build_lineage_node_id(target_art)

        inputs = prov.get("input_artifact_ids", [])
        if isinstance(inputs, list):
            for inp_art in inputs:
                source_node = build_lineage_node_id(inp_art)
                edge_id = build_lineage_edge_id(source_node, target_node, "derived_from")
                edges.append(LineageEdge(
                    edge_id=edge_id,
                    source_node_id=source_node,
                    target_node_id=target_node,
                    relation="derived_from",
                    confidence_score=1.0,
                    metadata={"provenance_id": prov.get("provenance_id")},
                    warnings=[]
                ))
    return edges

def infer_lineage_edges_by_path_patterns(inventory_df: pd.DataFrame) -> tuple[list[LineageEdge], dict]:
    # Approximations based on paths (e.g. raw -> processed -> features)
    edges = []
    warnings = []

    if inventory_df.empty:
        return edges, {"warnings": warnings}

    raw_nodes = inventory_df[inventory_df["artifact_type"] == "raw_data_artifact"]
    proc_nodes = inventory_df[inventory_df["artifact_type"] == "processed_data_artifact"]
    feat_nodes = inventory_df[inventory_df["artifact_type"] == "feature_artifact"]

    # Just an example heuristic: all processed depend on all raw
    # This is a very rough approximation, typically we'd match symbols or timeframes
    # For now, we just add warnings that it's inferred

    for _, p_row in proc_nodes.iterrows():
        p_node = build_lineage_node_id(p_row["artifact_id"])
        for _, r_row in raw_nodes.iterrows():
            r_node = build_lineage_node_id(r_row["artifact_id"])
            edge_id = build_lineage_edge_id(r_node, p_node, "derived_from")
            edges.append(LineageEdge(
                edge_id=edge_id,
                source_node_id=r_node,
                target_node_id=p_node,
                relation="derived_from",
                confidence_score=0.3,
                metadata={"inference": "path_pattern_raw_to_processed"},
                warnings=["Inferred edge based on path pattern approximation"]
            ))

    warnings.append("Path pattern edge inference used, high chance of approximation.")

    return edges, {"warnings": warnings}

def build_artifact_lineage_graph(inventory_df: pd.DataFrame, provenance_df: pd.DataFrame | None = None) -> tuple[LineageGraph, dict]:
    nodes = build_lineage_nodes_from_inventory(inventory_df)
    edges = []
    meta = {"warnings": []}

    if provenance_df is not None and not provenance_df.empty:
        prov_edges = build_lineage_edges_from_provenance(provenance_df, inventory_df)
        edges.extend(prov_edges)

    inferred_edges, inf_meta = infer_lineage_edges_by_path_patterns(inventory_df)
    edges.extend(inferred_edges)
    meta["warnings"].extend(inf_meta.get("warnings", []))

    graph = LineageGraph(nodes, edges)
    meta.update(graph.summarize())

    return graph, meta
