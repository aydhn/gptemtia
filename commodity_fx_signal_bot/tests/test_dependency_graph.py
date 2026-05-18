import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from orchestration.dependency_graph import DependencyGraph
from orchestration.orchestration_models import PipelineJob

def test_dependency_graph_basics():
    job1 = PipelineJob("job1", "name1", "type", "desc", None, None, [], [], [], [])
    job2 = PipelineJob("job2", "name2", "type", "desc", None, None, [], [], ["job1"], [])

    graph = DependencyGraph([job1, job2])

    assert "job1" in graph.adjacency
    assert "job2" in graph.adjacency["job1"]

    order, cycle_info = graph.topological_sort()
    assert not cycle_info["has_cycles"]
    assert order == ["job1", "job2"]

    downstream = graph.get_downstream_jobs("job1")
    assert "job2" in downstream

    df = graph.to_dataframe()
    assert not df.empty
    assert "job_id" in df.columns

def test_dependency_graph_cycles():
    job1 = PipelineJob("job1", "name1", "type", "desc", None, None, [], [], ["job2"], [])
    job2 = PipelineJob("job2", "name2", "type", "desc", None, None, [], [], ["job1"], [])

    graph = DependencyGraph([job1, job2])
    cycle_info = graph.detect_cycles()
    assert cycle_info["has_cycles"]
