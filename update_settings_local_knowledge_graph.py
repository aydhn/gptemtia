import re

file_path = "commodity_fx_signal_bot/config/settings.py"
with open(file_path, "r") as f:
    content = f.read()

dataclass_additions = """
    # Phase 66: Local Knowledge Graph
    local_knowledge_graph_enabled: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ENABLED", "true")).lower() == "true")
    default_local_knowledge_graph_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_LOCAL_KNOWLEDGE_GRAPH_PROFILE", "balanced_local_graph"))
    local_knowledge_graph_default_language: str = field(default_factory=lambda: os.getenv("LOCAL_KNOWLEDGE_GRAPH_DEFAULT_LANGUAGE", "tr"))
    local_knowledge_graph_dry_run_default: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_DRY_RUN_DEFAULT", "true")).lower() == "true")
    local_knowledge_graph_allow_external_vector_db: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_EXTERNAL_VECTOR_DB", "false")).lower() == "true")
    local_knowledge_graph_allow_cloud_graph_db: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_CLOUD_GRAPH_DB", "false")).lower() == "true")
    local_knowledge_graph_allow_external_llm: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_EXTERNAL_LLM", "false")).lower() == "true")
    local_knowledge_graph_allow_cloud_upload: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_CLOUD_UPLOAD", "false")).lower() == "true")
    local_knowledge_graph_allow_file_modification: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_FILE_MODIFICATION", "false")).lower() == "true")
    local_knowledge_graph_allow_file_deletion: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_FILE_DELETION", "false")).lower() == "true")
    local_knowledge_graph_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    local_knowledge_graph_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    local_knowledge_graph_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    local_knowledge_graph_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    local_knowledge_graph_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    local_knowledge_graph_scan_artifact_metadata: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SCAN_ARTIFACT_METADATA", "true")).lower() == "true")
    local_knowledge_graph_scan_evidence_governance: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SCAN_EVIDENCE_GOVERNANCE", "true")).lower() == "true")
    local_knowledge_graph_scan_report_summaries: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SCAN_REPORT_SUMMARIES", "true")).lower() == "true")
    local_knowledge_graph_scan_docs: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SCAN_DOCS", "true")).lower() == "true")
    local_knowledge_graph_scan_data_lake: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SCAN_DATA_LAKE", "true")).lower() == "true")
    local_knowledge_graph_scan_reports: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SCAN_REPORTS", "true")).lower() == "true")
    local_knowledge_graph_max_nodes: int = field(default_factory=lambda: int(os.getenv("LOCAL_KNOWLEDGE_GRAPH_MAX_NODES", "250000")))
    local_knowledge_graph_max_edges: int = field(default_factory=lambda: int(os.getenv("LOCAL_KNOWLEDGE_GRAPH_MAX_EDGES", "500000")))
    local_knowledge_graph_max_text_chars: int = field(default_factory=lambda: int(os.getenv("LOCAL_KNOWLEDGE_GRAPH_MAX_TEXT_CHARS", "20000")))
    local_knowledge_graph_tfidf_max_features: int = field(default_factory=lambda: int(os.getenv("LOCAL_KNOWLEDGE_GRAPH_TFIDF_MAX_FEATURES", "20000")))
    local_knowledge_graph_similarity_threshold: float = field(default_factory=lambda: float(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SIMILARITY_THRESHOLD", "0.20")))
    local_knowledge_graph_freshness_days_warning: int = field(default_factory=lambda: int(os.getenv("LOCAL_KNOWLEDGE_GRAPH_FRESHNESS_DAYS_WARNING", "60")))
    local_knowledge_graph_save_reports: bool = field(default_factory=lambda: str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SAVE_REPORTS", "true")).lower() == "true")
    local_knowledge_graph_min_quality_score: float = field(default_factory=lambda: float(os.getenv("LOCAL_KNOWLEDGE_GRAPH_MIN_QUALITY_SCORE", "0.40")))

    def __post_init__(self):
"""

post_init_additions = """
        # Local Knowledge Graph
        self.local_knowledge_graph_enabled = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ENABLED", str(self.local_knowledge_graph_enabled))).lower() == "true"
        self.default_local_knowledge_graph_profile = str(os.getenv("DEFAULT_LOCAL_KNOWLEDGE_GRAPH_PROFILE", self.default_local_knowledge_graph_profile))
        self.local_knowledge_graph_default_language = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_DEFAULT_LANGUAGE", self.local_knowledge_graph_default_language))
        self.local_knowledge_graph_dry_run_default = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_DRY_RUN_DEFAULT", str(self.local_knowledge_graph_dry_run_default))).lower() == "true"
        self.local_knowledge_graph_allow_external_vector_db = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_EXTERNAL_VECTOR_DB", str(self.local_knowledge_graph_allow_external_vector_db))).lower() == "true"
        self.local_knowledge_graph_allow_cloud_graph_db = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_CLOUD_GRAPH_DB", str(self.local_knowledge_graph_allow_cloud_graph_db))).lower() == "true"
        self.local_knowledge_graph_allow_external_llm = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_EXTERNAL_LLM", str(self.local_knowledge_graph_allow_external_llm))).lower() == "true"
        self.local_knowledge_graph_allow_cloud_upload = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_CLOUD_UPLOAD", str(self.local_knowledge_graph_allow_cloud_upload))).lower() == "true"
        self.local_knowledge_graph_allow_file_modification = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_FILE_MODIFICATION", str(self.local_knowledge_graph_allow_file_modification))).lower() == "true"
        self.local_knowledge_graph_allow_file_deletion = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_FILE_DELETION", str(self.local_knowledge_graph_allow_file_deletion))).lower() == "true"
        self.local_knowledge_graph_allow_live_commands = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_LIVE_COMMANDS", str(self.local_knowledge_graph_allow_live_commands))).lower() == "true"
        self.local_knowledge_graph_allow_broker_commands = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_BROKER_COMMANDS", str(self.local_knowledge_graph_allow_broker_commands))).lower() == "true"
        self.local_knowledge_graph_allow_deploy_commands = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_DEPLOY_COMMANDS", str(self.local_knowledge_graph_allow_deploy_commands))).lower() == "true"
        self.local_knowledge_graph_allow_background_daemons = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_BACKGROUND_DAEMONS", str(self.local_knowledge_graph_allow_background_daemons))).lower() == "true"
        self.local_knowledge_graph_allow_real_market_download = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_ALLOW_REAL_MARKET_DOWNLOAD", str(self.local_knowledge_graph_allow_real_market_download))).lower() == "true"
        self.local_knowledge_graph_scan_artifact_metadata = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SCAN_ARTIFACT_METADATA", str(self.local_knowledge_graph_scan_artifact_metadata))).lower() == "true"
        self.local_knowledge_graph_scan_evidence_governance = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SCAN_EVIDENCE_GOVERNANCE", str(self.local_knowledge_graph_scan_evidence_governance))).lower() == "true"
        self.local_knowledge_graph_scan_report_summaries = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SCAN_REPORT_SUMMARIES", str(self.local_knowledge_graph_scan_report_summaries))).lower() == "true"
        self.local_knowledge_graph_scan_docs = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SCAN_DOCS", str(self.local_knowledge_graph_scan_docs))).lower() == "true"
        self.local_knowledge_graph_scan_data_lake = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SCAN_DATA_LAKE", str(self.local_knowledge_graph_scan_data_lake))).lower() == "true"
        self.local_knowledge_graph_scan_reports = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SCAN_REPORTS", str(self.local_knowledge_graph_scan_reports))).lower() == "true"

        try:
            self.local_knowledge_graph_max_nodes = int(os.getenv("LOCAL_KNOWLEDGE_GRAPH_MAX_NODES", str(self.local_knowledge_graph_max_nodes)))
        except ValueError:
            pass

        try:
            self.local_knowledge_graph_max_edges = int(os.getenv("LOCAL_KNOWLEDGE_GRAPH_MAX_EDGES", str(self.local_knowledge_graph_max_edges)))
        except ValueError:
            pass

        try:
            self.local_knowledge_graph_max_text_chars = int(os.getenv("LOCAL_KNOWLEDGE_GRAPH_MAX_TEXT_CHARS", str(self.local_knowledge_graph_max_text_chars)))
        except ValueError:
            pass

        try:
            self.local_knowledge_graph_tfidf_max_features = int(os.getenv("LOCAL_KNOWLEDGE_GRAPH_TFIDF_MAX_FEATURES", str(self.local_knowledge_graph_tfidf_max_features)))
        except ValueError:
            pass

        try:
            self.local_knowledge_graph_similarity_threshold = float(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SIMILARITY_THRESHOLD", str(self.local_knowledge_graph_similarity_threshold)))
        except ValueError:
            pass

        try:
            self.local_knowledge_graph_freshness_days_warning = int(os.getenv("LOCAL_KNOWLEDGE_GRAPH_FRESHNESS_DAYS_WARNING", str(self.local_knowledge_graph_freshness_days_warning)))
        except ValueError:
            pass

        self.local_knowledge_graph_save_reports = str(os.getenv("LOCAL_KNOWLEDGE_GRAPH_SAVE_REPORTS", str(self.local_knowledge_graph_save_reports))).lower() == "true"

        try:
            self.local_knowledge_graph_min_quality_score = float(os.getenv("LOCAL_KNOWLEDGE_GRAPH_MIN_QUALITY_SCORE", str(self.local_knowledge_graph_min_quality_score)))
        except ValueError:
            pass

        self.live_trading_enabled = False
"""

if "local_knowledge_graph_enabled" not in content:
    content = re.sub(r'    def __post_init__\(self\):', dataclass_additions, content)
    content = re.sub(r'        self\.live_trading_enabled = False', post_init_additions, content)
    with open(file_path, "w") as f:
        f.write(content)

with open("commodity_fx_signal_bot/.env.example", "a") as f:
    f.write("""
# Local Knowledge Graph
LOCAL_KNOWLEDGE_GRAPH_ENABLED=true
DEFAULT_LOCAL_KNOWLEDGE_GRAPH_PROFILE=balanced_local_graph
LOCAL_KNOWLEDGE_GRAPH_DEFAULT_LANGUAGE=tr
LOCAL_KNOWLEDGE_GRAPH_DRY_RUN_DEFAULT=true
LOCAL_KNOWLEDGE_GRAPH_ALLOW_EXTERNAL_VECTOR_DB=false
LOCAL_KNOWLEDGE_GRAPH_ALLOW_CLOUD_GRAPH_DB=false
LOCAL_KNOWLEDGE_GRAPH_ALLOW_EXTERNAL_LLM=false
LOCAL_KNOWLEDGE_GRAPH_ALLOW_CLOUD_UPLOAD=false
LOCAL_KNOWLEDGE_GRAPH_ALLOW_FILE_MODIFICATION=false
LOCAL_KNOWLEDGE_GRAPH_ALLOW_FILE_DELETION=false
LOCAL_KNOWLEDGE_GRAPH_ALLOW_LIVE_COMMANDS=false
LOCAL_KNOWLEDGE_GRAPH_ALLOW_BROKER_COMMANDS=false
LOCAL_KNOWLEDGE_GRAPH_ALLOW_DEPLOY_COMMANDS=false
LOCAL_KNOWLEDGE_GRAPH_ALLOW_BACKGROUND_DAEMONS=false
LOCAL_KNOWLEDGE_GRAPH_ALLOW_REAL_MARKET_DOWNLOAD=false
LOCAL_KNOWLEDGE_GRAPH_SCAN_ARTIFACT_METADATA=true
LOCAL_KNOWLEDGE_GRAPH_SCAN_EVIDENCE_GOVERNANCE=true
LOCAL_KNOWLEDGE_GRAPH_SCAN_REPORT_SUMMARIES=true
LOCAL_KNOWLEDGE_GRAPH_SCAN_DOCS=true
LOCAL_KNOWLEDGE_GRAPH_SCAN_DATA_LAKE=true
LOCAL_KNOWLEDGE_GRAPH_SCAN_REPORTS=true
LOCAL_KNOWLEDGE_GRAPH_MAX_NODES=250000
LOCAL_KNOWLEDGE_GRAPH_MAX_EDGES=500000
LOCAL_KNOWLEDGE_GRAPH_MAX_TEXT_CHARS=20000
LOCAL_KNOWLEDGE_GRAPH_TFIDF_MAX_FEATURES=20000
LOCAL_KNOWLEDGE_GRAPH_SIMILARITY_THRESHOLD=0.20
LOCAL_KNOWLEDGE_GRAPH_FRESHNESS_DAYS_WARNING=60
LOCAL_KNOWLEDGE_GRAPH_SAVE_REPORTS=true
LOCAL_KNOWLEDGE_GRAPH_MIN_QUALITY_SCORE=0.40
""")
