from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class LocalKnowledgeGraphProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_external_vector_db: bool = False
    allow_cloud_graph_db: bool = False
    allow_external_llm: bool = False
    allow_cloud_upload: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    scan_artifact_metadata: bool = True
    scan_evidence_governance: bool = True
    scan_report_summaries: bool = True
    scan_docs: bool = True
    scan_data_lake: bool = True
    scan_reports: bool = True
    max_nodes: int = 250000
    max_edges: int = 500000
    max_text_chars: int = 20000
    tfidf_max_features: int = 20000
    similarity_threshold: float = 0.20
    freshness_days_warning: int = 60
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = [
    LocalKnowledgeGraphProfile(
        name="balanced_local_graph",
        description="Balanced local graph configuration",
        language="tr",
        dry_run_default=True,
        allow_external_vector_db=False,
        allow_cloud_graph_db=False,
        allow_external_llm=False,
        allow_cloud_upload=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        scan_artifact_metadata=True,
        scan_evidence_governance=True,
        scan_report_summaries=True,
        scan_docs=True,
        scan_data_lake=True,
        scan_reports=True,
        max_nodes=250000,
        max_edges=500000,
        max_text_chars=20000,
        tfidf_max_features=20000,
        similarity_threshold=0.20,
        freshness_days_warning=60,
        min_quality_score=0.40,
        enabled=True,
        notes="Genel amaçlı local/offline artifact relationship graph ve semantic index profili."
    ),
    LocalKnowledgeGraphProfile(
        name="metadata_evidence_graph_focus",
        description="Metadata and evidence governance focus",
        language="tr",
        dry_run_default=True,
        allow_external_vector_db=False,
        allow_cloud_graph_db=False,
        allow_external_llm=False,
        allow_cloud_upload=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        scan_artifact_metadata=True,
        scan_evidence_governance=True,
        scan_report_summaries=True,
        scan_docs=True,
        scan_data_lake=True,
        scan_reports=True,
        max_nodes=250000,
        max_edges=500000,
        max_text_chars=20000,
        tfidf_max_features=20000,
        similarity_threshold=0.18,
        freshness_days_warning=60,
        min_quality_score=0.40,
        enabled=True,
        notes="Artifact metadata ve evidence governance ilişkilerini öne çıkaran profil."
    ),
    LocalKnowledgeGraphProfile(
        name="fast_local_graph",
        description="Fast local graph configuration",
        language="tr",
        dry_run_default=True,
        allow_external_vector_db=False,
        allow_cloud_graph_db=False,
        allow_external_llm=False,
        allow_cloud_upload=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        scan_artifact_metadata=True,
        scan_evidence_governance=True,
        scan_report_summaries=True,
        scan_docs=True,
        scan_data_lake=True,
        scan_reports=True,
        max_nodes=50000,
        max_edges=100000,
        max_text_chars=8000,
        tfidf_max_features=8000,
        similarity_threshold=0.25,
        freshness_days_warning=60,
        min_quality_score=0.40,
        enabled=True,
        notes="Hızlı local graph/index üretimi için profil."
    ),
    LocalKnowledgeGraphProfile(
        name="strict_graph_safety",
        description="Strict safety local graph configuration",
        language="tr",
        dry_run_default=True,
        allow_external_vector_db=False,
        allow_cloud_graph_db=False,
        allow_external_llm=False,
        allow_cloud_upload=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        scan_artifact_metadata=True,
        scan_evidence_governance=True,
        scan_report_summaries=True,
        scan_docs=True,
        scan_data_lake=True,
        scan_reports=True,
        max_nodes=250000,
        max_edges=500000,
        max_text_chars=10000,
        tfidf_max_features=20000,
        similarity_threshold=0.25,
        freshness_days_warning=60,
        min_quality_score=0.60,
        enabled=True,
        notes="External vector DB, cloud graph, live/broker/deploy ve raw secret risklerini sıkı denetleyen profil."
    )
]

def get_local_knowledge_graph_profile(name: str) -> LocalKnowledgeGraphProfile:
    for p in _PROFILES:
        if p.name == name:
            return p
    raise ValueError(f"Unknown local knowledge graph profile: {name}")

def list_local_knowledge_graph_profiles(enabled_only: bool = True) -> List[LocalKnowledgeGraphProfile]:
    if enabled_only:
        return [p for p in _PROFILES if p.enabled]
    return _PROFILES

def validate_local_knowledge_graph_profiles() -> None:
    for p in _PROFILES:
        if not p.language:
            raise ValueError(f"Profile {p.name} language is empty.")
        if p.max_nodes <= 0 or p.max_edges <= 0:
            raise ValueError(f"Profile {p.name} max_nodes/edges must be positive.")
        if p.max_text_chars <= 0:
            raise ValueError(f"Profile {p.name} max_text_chars must be positive.")
        if p.tfidf_max_features <= 0:
            raise ValueError(f"Profile {p.name} tfidf_max_features must be positive.")
        if not (0.0 <= p.similarity_threshold <= 1.0):
            raise ValueError(f"Profile {p.name} similarity_threshold must be between 0 and 1.")
        if p.freshness_days_warning <= 0:
            raise ValueError(f"Profile {p.name} freshness_days_warning must be positive.")
        if not p.dry_run_default:
            raise ValueError(f"Profile {p.name} dry_run_default must be True.")
        if p.allow_external_vector_db or p.allow_cloud_graph_db or p.allow_external_llm or p.allow_cloud_upload or p.allow_file_modification or p.allow_file_deletion:
            raise ValueError(f"Profile {p.name} safety flags must be False.")

def get_default_local_knowledge_graph_profile() -> LocalKnowledgeGraphProfile:
    from config.settings import settings
    return get_local_knowledge_graph_profile(settings.default_local_knowledge_graph_profile)
