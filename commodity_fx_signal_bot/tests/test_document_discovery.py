import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from pathlib import Path
from knowledge_base.document_discovery import KnowledgeDocumentDiscovery
from knowledge_base.kb_config import get_default_knowledge_base_profile

def test_classify_document():
    disc = KnowledgeDocumentDiscovery(Path("."))
    assert disc.classify_document_type(Path("data/lake/experiments/foo.md")) == "experiment_document"

def test_infer_module():
    disc = KnowledgeDocumentDiscovery(Path("."))
    assert disc.infer_source_module(Path("data/lake/meta_research/bar.csv")) == "meta_research"
