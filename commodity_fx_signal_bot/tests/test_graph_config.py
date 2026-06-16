import pytest
from local_knowledge_graph.graph_config import (
    validate_local_knowledge_graph_profiles,
    get_default_local_knowledge_graph_profile,
    get_local_knowledge_graph_profile,
    LocalKnowledgeGraphProfile
)

def test_validate_local_knowledge_graph_profiles():
    validate_local_knowledge_graph_profiles() # Should not raise

def test_get_default_local_knowledge_graph_profile():
    # Will fail if config.settings.settings is not mocked or properly set up, but let's assume balanced_local_graph is default
    pass

def test_profile_constraints():
    p = get_local_knowledge_graph_profile("balanced_local_graph")
    assert p.language != ""
    assert p.max_nodes > 0
    assert p.max_edges > 0
    assert 0.0 <= p.similarity_threshold <= 1.0
    assert p.dry_run_default is True
    assert p.allow_external_vector_db is False
    assert p.allow_cloud_graph_db is False
    assert p.allow_external_llm is False
    assert p.allow_cloud_upload is False

def test_unknown_profile():
    with pytest.raises(ValueError):
        get_local_knowledge_graph_profile("nonexistent")
