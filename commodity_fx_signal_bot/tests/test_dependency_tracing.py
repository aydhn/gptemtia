from governance.dependency_tracing import ArtifactDependencyTracer
from governance.governance_models import LineageEdge, LineageNode
from governance.lineage_graph import LineageGraph


def test_trace_upstream_downstream():
    n1 = LineageNode("n1", "a1", "raw", "r.csv", "raw/r", {}, [])
    n2 = LineageNode("n2", "a2", "proc", "p.csv", "proc/p", {}, [])
    e = LineageEdge("e1", "n1", "n2", "derived_from", 1.0, {}, [])

    g = LineageGraph([n1, n2], [e])
    tracer = ArtifactDependencyTracer(g)

    up, _ = tracer.trace_upstream("n2")
    assert not up.empty
    assert "n1" in up["node_id"].values

    down, _ = tracer.trace_downstream("n1")
    assert not down.empty
    assert "n2" in down["node_id"].values
