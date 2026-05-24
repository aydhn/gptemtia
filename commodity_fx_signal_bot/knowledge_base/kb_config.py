from dataclasses import dataclass
from typing import List

class ConfigError(Exception):
    """Exception raised for configuration errors in Knowledge Base."""
    pass

@dataclass(frozen=True)
class KnowledgeBaseProfile:
    name: str
    description: str
    scan_reports_output: bool = True
    scan_docs: bool = True
    scan_data_lake_reports: bool = True
    scan_experiments: bool = True
    scan_governance: bool = True
    scan_planning: bool = True
    scan_meta_research: bool = True
    max_documents: int = 5000
    max_document_mb: int = 10
    chunk_size_chars: int = 1200
    chunk_overlap_chars: int = 150
    max_chunks: int = 50000
    retrieval_top_k: int = 10
    enable_tfidf: bool = True
    enable_fuzzy: bool = True
    enable_hybrid: bool = True
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

def _build_default_profiles() -> dict[str, KnowledgeBaseProfile]:
    return {
        "balanced_local_knowledge_base": KnowledgeBaseProfile(
            name="balanced_local_knowledge_base",
            description="Genel amaçlı local/offline research knowledge base profili.",
            scan_reports_output=True,
            scan_docs=True,
            scan_data_lake_reports=True,
            scan_experiments=True,
            scan_governance=True,
            scan_planning=True,
            scan_meta_research=True,
            max_documents=5000,
            max_document_mb=10,
            chunk_size_chars=1200,
            chunk_overlap_chars=150,
            max_chunks=50000,
            retrieval_top_k=10,
            enable_tfidf=True,
            enable_fuzzy=True,
            enable_hybrid=True,
            min_quality_score=0.40,
            notes="Genel amaçlı local/offline research knowledge base profili."
        ),
        "light_local_knowledge_base": KnowledgeBaseProfile(
            name="light_local_knowledge_base",
            description="Hızlı ve hafif local indexleme profili.",
            scan_reports_output=True,
            scan_docs=True,
            scan_data_lake_reports=False,
            scan_experiments=True,
            scan_governance=False,
            scan_planning=True,
            scan_meta_research=True,
            max_documents=1000,
            max_document_mb=5,
            chunk_size_chars=1000,
            chunk_overlap_chars=150,
            max_chunks=10000,
            retrieval_top_k=8,
            notes="Hızlı ve hafif local indexleme profili."
        ),
        "strict_research_memory": KnowledgeBaseProfile(
            name="strict_research_memory",
            description="Daha geniş rapor ve governance hafızası için sıkı profil.",
            scan_reports_output=True,
            scan_docs=True,
            scan_data_lake_reports=True,
            scan_experiments=True,
            scan_governance=True,
            scan_planning=True,
            scan_meta_research=True,
            max_documents=10000,
            max_document_mb=20,
            chunk_size_chars=1500,
            chunk_overlap_chars=200,
            max_chunks=50000,
            retrieval_top_k=15,
            min_quality_score=0.55,
            notes="Daha geniş rapor ve governance hafızası için sıkı profil."
        ),
        "analyst_workspace_focused": KnowledgeBaseProfile(
            name="analyst_workspace_focused",
            description="Analist çalışma alanı, memory card ve decision journal odaklı profil.",
            scan_reports_output=True,
            scan_docs=True,
            scan_data_lake_reports=True,
            scan_experiments=True,
            scan_governance=True,
            scan_planning=True,
            scan_meta_research=True,
            max_documents=5000,
            max_document_mb=10,
            chunk_size_chars=1200,
            chunk_overlap_chars=150,
            max_chunks=50000,
            retrieval_top_k=20,
            min_quality_score=0.40,
            notes="Analist çalışma alanı, memory card ve decision journal odaklı profil."
        ),
    }

DEFAULT_PROFILES = _build_default_profiles()

def get_knowledge_base_profile(name: str) -> KnowledgeBaseProfile:
    if name not in DEFAULT_PROFILES:
        raise ConfigError(f"Unknown knowledge base profile: {name}")
    return DEFAULT_PROFILES[name]

def list_knowledge_base_profiles(enabled_only: bool = True) -> List[KnowledgeBaseProfile]:
    profiles = list(DEFAULT_PROFILES.values())
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles

def validate_knowledge_base_profiles() -> None:
    for name, profile in DEFAULT_PROFILES.items():
        if profile.max_documents <= 0:
            raise ConfigError(f"Profile {name} must have max_documents > 0")
        if profile.max_document_mb <= 0:
            raise ConfigError(f"Profile {name} must have max_document_mb > 0")
        if profile.chunk_size_chars <= 0:
            raise ConfigError(f"Profile {name} must have chunk_size_chars > 0")
        if profile.chunk_overlap_chars < 0:
            raise ConfigError(f"Profile {name} must have chunk_overlap_chars >= 0")
        if profile.chunk_overlap_chars >= profile.chunk_size_chars:
            raise ConfigError(f"Profile {name} must have chunk_overlap_chars < chunk_size_chars")
        if profile.max_chunks <= 0:
            raise ConfigError(f"Profile {name} must have max_chunks > 0")
        if profile.retrieval_top_k <= 0:
            raise ConfigError(f"Profile {name} must have retrieval_top_k > 0")
        if not (0 <= profile.min_quality_score <= 1):
            raise ConfigError(f"Profile {name} must have min_quality_score between 0 and 1")

        flags = [
            profile.scan_reports_output, profile.scan_docs, profile.scan_data_lake_reports,
            profile.scan_experiments, profile.scan_governance, profile.scan_planning,
            profile.scan_meta_research
        ]
        if not any(flags):
            raise ConfigError(f"Profile {name} must have at least one scan flag enabled")

def get_default_knowledge_base_profile() -> KnowledgeBaseProfile:
    from config.settings import settings
    return get_knowledge_base_profile(settings.default_knowledge_base_profile)
