"""
Dependency graph for pipeline jobs.
"""

from typing import List, Dict, Tuple
import pandas as pd
from orchestration.orchestration_models import PipelineJob

class DependencyGraph:
    def __init__(self, jobs: List[PipelineJob]):
        self.jobs = {job.job_id: job for job in jobs if job.enabled}
        self.adjacency = self.build_adjacency()

    def build_adjacency(self) -> Dict[str, List[str]]:
        adjacency: Dict[str, List[str]] = {job_id: [] for job_id in self.jobs}
        for job_id, job in self.jobs.items():
            # Add required dependencies (must be in the graph)
            for dep_id in job.dependencies:
                if dep_id in self.jobs:
                    adjacency[dep_id].append(job_id)
            # Add optional dependencies (only if they are enabled and in graph)
            for dep_id in job.optional_dependencies:
                 if dep_id in self.jobs:
                    adjacency[dep_id].append(job_id)
        return adjacency

    def detect_cycles(self) -> dict:
        visited = set()
        rec_stack = set()
        cycles = []

        def dfs(node, path):
            visited.add(node)
            rec_stack.add(node)
            path.append(node)

            for neighbor in self.adjacency.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, path)
                elif neighbor in rec_stack:
                    cycle_start_index = path.index(neighbor)
                    cycles.append(path[cycle_start_index:] + [neighbor])

            rec_stack.remove(node)
            path.pop()

        for node in self.jobs:
            if node not in visited:
                dfs(node, [])

        return {
            "has_cycles": len(cycles) > 0,
            "cycles": cycles
        }

    def topological_sort(self) -> Tuple[List[str], dict]:
        cycle_info = self.detect_cycles()
        if cycle_info["has_cycles"]:
            return [], cycle_info

        visited = set()
        stack = []

        def dfs(node):
            visited.add(node)
            for neighbor in self.adjacency.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(node)

        for node in self.jobs:
            if node not in visited:
                dfs(node)

        return stack[::-1], cycle_info

    def get_upstream_jobs(self, job_id: str) -> List[str]:
        if job_id not in self.jobs:
            return []

        upstream = []
        # Build reverse adjacency
        rev_adj = {node: [] for node in self.jobs}
        for u, neighbors in self.adjacency.items():
            for v in neighbors:
                rev_adj[v].append(u)

        visited = set()
        def dfs(node):
            for neighbor in rev_adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    upstream.append(neighbor)
                    dfs(neighbor)

        dfs(job_id)
        return list(set(upstream))

    def get_downstream_jobs(self, job_id: str) -> List[str]:
        if job_id not in self.jobs:
            return []

        downstream = []
        visited = set()

        def dfs(node):
            for neighbor in self.adjacency.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    downstream.append(neighbor)
                    dfs(neighbor)

        dfs(job_id)
        return list(set(downstream))

    def to_dataframe(self) -> pd.DataFrame:
        data = []
        for job_id, job in self.jobs.items():
            data.append({
                "job_id": job_id,
                "job_name": job.job_name,
                "job_type": job.job_type,
                "dependencies_count": len(job.dependencies),
                "downstream_count": len(self.get_downstream_jobs(job_id))
            })
        if not data:
             return pd.DataFrame(columns=["job_id", "job_name", "job_type", "dependencies_count", "downstream_count"])
        return pd.DataFrame(data)

    def summarize(self) -> dict:
        cycle_info = self.detect_cycles()
        return {
            "job_count": len(self.jobs),
            "edge_count": sum(len(neighbors) for neighbors in self.adjacency.values()),
            "has_cycles": cycle_info["has_cycles"],
            "cycle_count": len(cycle_info["cycles"])
        }
