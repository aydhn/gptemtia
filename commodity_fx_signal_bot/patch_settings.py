import os
import re
from pathlib import Path

def patch_settings():
    path = Path("config/settings.py")
    content = path.read_text()

    if "knowledge_base_enabled" in content:
        print("Settings already patched.")
        return

    addition = """

    # Phase 49: Knowledge Base & Analyst Workspace
    knowledge_base_enabled: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_ENABLED", "true")).lower() == "true")
    default_knowledge_base_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_KNOWLEDGE_BASE_PROFILE", "balanced_local_knowledge_base"))
    knowledge_base_default_timeframe: str = field(default_factory=lambda: os.getenv("KNOWLEDGE_BASE_DEFAULT_TIMEFRAME", "1d"))
    knowledge_base_scan_reports_output: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_REPORTS_OUTPUT", "true")).lower() == "true")
    knowledge_base_scan_docs: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_DOCS", "true")).lower() == "true")
    knowledge_base_scan_data_lake_reports: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_DATA_LAKE_REPORTS", "true")).lower() == "true")
    knowledge_base_scan_experiments: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_EXPERIMENTS", "true")).lower() == "true")
    knowledge_base_scan_governance: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_GOVERNANCE", "true")).lower() == "true")
    knowledge_base_scan_planning: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_PLANNING", "true")).lower() == "true")
    knowledge_base_scan_meta_research: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_META_RESEARCH", "true")).lower() == "true")
    knowledge_base_max_documents: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_MAX_DOCUMENTS", "5000")))
    knowledge_base_max_document_mb: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_MAX_DOCUMENT_MB", "10")))
    knowledge_base_chunk_size_chars: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_CHUNK_SIZE_CHARS", "1200")))
    knowledge_base_chunk_overlap_chars: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_CHUNK_OVERLAP_CHARS", "150")))
    knowledge_base_max_chunks: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_MAX_CHUNKS", "50000")))
    knowledge_base_retrieval_top_k: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_RETRIEVAL_TOP_K", "10")))
    knowledge_base_enable_tfidf: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_ENABLE_TFIDF", "true")).lower() == "true")
    knowledge_base_enable_fuzzy: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_ENABLE_FUZZY", "true")).lower() == "true")
    knowledge_base_enable_hybrid: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_ENABLE_HYBRID", "true")).lower() == "true")
    knowledge_base_save_index: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SAVE_INDEX", "true")).lower() == "true")
    knowledge_base_save_memory_cards: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SAVE_MEMORY_CARDS", "true")).lower() == "true")
    knowledge_base_save_reports: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SAVE_REPORTS", "true")).lower() == "true")
    knowledge_base_min_quality_score: float = field(default_factory=lambda: float(os.getenv("KNOWLEDGE_BASE_MIN_QUALITY_SCORE", "0.40")))
"""

    content = content.replace("self.live_trading_enabled = False", addition + "\n        self.live_trading_enabled = False")
    path.write_text(content)
    print("Settings patched successfully.")

def patch_env():
    path = Path(".env.example")
    content = path.read_text()

    if "KNOWLEDGE_BASE_ENABLED" in content:
        print("Env already patched.")
        return

    addition = """
# Phase 49: Knowledge Base & Analyst Workspace
KNOWLEDGE_BASE_ENABLED=true
DEFAULT_KNOWLEDGE_BASE_PROFILE=balanced_local_knowledge_base
KNOWLEDGE_BASE_DEFAULT_TIMEFRAME=1d
KNOWLEDGE_BASE_SCAN_REPORTS_OUTPUT=true
KNOWLEDGE_BASE_SCAN_DOCS=true
KNOWLEDGE_BASE_SCAN_DATA_LAKE_REPORTS=true
KNOWLEDGE_BASE_SCAN_EXPERIMENTS=true
KNOWLEDGE_BASE_SCAN_GOVERNANCE=true
KNOWLEDGE_BASE_SCAN_PLANNING=true
KNOWLEDGE_BASE_SCAN_META_RESEARCH=true
KNOWLEDGE_BASE_MAX_DOCUMENTS=5000
KNOWLEDGE_BASE_MAX_DOCUMENT_MB=10
KNOWLEDGE_BASE_CHUNK_SIZE_CHARS=1200
KNOWLEDGE_BASE_CHUNK_OVERLAP_CHARS=150
KNOWLEDGE_BASE_MAX_CHUNKS=50000
KNOWLEDGE_BASE_RETRIEVAL_TOP_K=10
KNOWLEDGE_BASE_ENABLE_TFIDF=true
KNOWLEDGE_BASE_ENABLE_FUZZY=true
KNOWLEDGE_BASE_ENABLE_HYBRID=true
KNOWLEDGE_BASE_SAVE_INDEX=true
KNOWLEDGE_BASE_SAVE_MEMORY_CARDS=true
KNOWLEDGE_BASE_SAVE_REPORTS=true
KNOWLEDGE_BASE_MIN_QUALITY_SCORE=0.40
"""

    path.write_text(content + "\n" + addition)
    print("Env patched successfully.")

if __name__ == "__main__":
    patch_settings()
    patch_env()
