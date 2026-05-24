from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from knowledge_base.kb_pipeline import KnowledgeBasePipeline
from knowledge_base.kb_config import get_default_knowledge_base_profile

def test_pipeline_init():
    settings = Settings()
    lake = DataLake(Path("."))
    prof = get_default_knowledge_base_profile()
    pl = KnowledgeBasePipeline(lake, settings, Path("."), prof)
    assert pl.profile.name == "balanced_local_knowledge_base"
