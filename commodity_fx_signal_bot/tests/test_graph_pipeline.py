import pytest
from pathlib import Path
from unittest.mock import Mock, patch
from local_knowledge_graph.graph_pipeline import LocalKnowledgeGraphPipeline
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_graph_pipeline_methods():
    mock_dl = Mock()
    mock_settings = Mock()
    profile = get_local_knowledge_graph_profile("balanced_local_graph")

    pipeline = LocalKnowledgeGraphPipeline(mock_dl, mock_settings, Path("."), profile)

    res, sum_ = pipeline.build_graph_node_edge_registry(save=False)
    assert res is not None

    res2, sum2 = pipeline.build_artifact_relationship_graph(save=False)
    assert res2 is not None

    res3, sum3 = pipeline.build_semantic_index_report(save=False)
    assert res3 is not None

    res4, sum4 = pipeline.build_relationship_query_report("query", save=False)
    assert res4 is not None

    res5, sum5 = pipeline.build_graph_analysis_report(save=False)
    assert res5 is not None

    res6, sum6 = pipeline.build_graph_quality_report(save=False)
    assert res6 is not None

    res7, sum7 = pipeline.build_graph_status(save=False)
    assert res7 is not None
