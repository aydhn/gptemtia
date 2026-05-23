import os
import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

meta_research_settings = """
    # Phase 45: Meta Research and Consensus Engine
    meta_research_enabled: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_ENABLED", "true")).lower() == "true")
    default_meta_research_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_META_RESEARCH_PROFILE", "balanced_meta_research"))
    meta_research_default_timeframe: str = field(default_factory=lambda: os.getenv("META_RESEARCH_DEFAULT_TIMEFRAME", "1d"))
    meta_research_min_sources: int = field(default_factory=lambda: int(os.getenv("META_RESEARCH_MIN_SOURCES", "3")))
    meta_research_min_evidence_quality: float = field(default_factory=lambda: float(os.getenv("META_RESEARCH_MIN_EVIDENCE_QUALITY", "0.40")))
    meta_research_conflict_threshold: float = field(default_factory=lambda: float(os.getenv("META_RESEARCH_CONFLICT_THRESHOLD", "0.35")))
    meta_research_high_agreement_threshold: float = field(default_factory=lambda: float(os.getenv("META_RESEARCH_HIGH_AGREEMENT_THRESHOLD", "0.70")))
    meta_research_uncertainty_penalty_enabled: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_UNCERTAINTY_PENALTY_ENABLED", "true")).lower() == "true")
    meta_research_quality_penalty_enabled: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_QUALITY_PENALTY_ENABLED", "true")).lower() == "true")
    meta_research_missing_source_penalty_enabled: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_MISSING_SOURCE_PENALTY_ENABLED", "true")).lower() == "true")
    meta_research_include_technical: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_TECHNICAL", "true")).lower() == "true")
    meta_research_include_strategy: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_STRATEGY", "true")).lower() == "true")
    meta_research_include_risk_level: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_RISK_LEVEL", "true")).lower() == "true")
    meta_research_include_backtest: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_BACKTEST", "true")).lower() == "true")
    meta_research_include_validation: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_VALIDATION", "true")).lower() == "true")
    meta_research_include_ml: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_ML", "true")).lower() == "true")
    meta_research_include_paper: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_PAPER", "true")).lower() == "true")
    meta_research_include_factor: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_FACTOR", "true")).lower() == "true")
    meta_research_include_synthetic_index: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_SYNTHETIC_INDEX", "true")).lower() == "true")
    meta_research_include_portfolio: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_PORTFOLIO", "true")).lower() == "true")
    meta_research_include_regime: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_REGIME", "true")).lower() == "true")
    meta_research_save_reports: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_SAVE_REPORTS", "true")).lower() == "true")
    meta_research_save_tables: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_SAVE_TABLES", "true")).lower() == "true")
    meta_research_min_quality_score: float = field(default_factory=lambda: float(os.getenv("META_RESEARCH_MIN_QUALITY_SCORE", "0.40")))

"""

if "META_RESEARCH_ENABLED" not in content:
    content = content.replace("    def __post_init__(self):", meta_research_settings + "\n    def __post_init__(self):")

    with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
        f.write(content)

with open("commodity_fx_signal_bot/.env.example", "r") as f:
    env_content = f.read()

if "META_RESEARCH_ENABLED" not in env_content:
    with open("commodity_fx_signal_bot/.env.example", "a") as f:
        f.write("""
# Phase 45: Meta Research and Consensus Engine
META_RESEARCH_ENABLED=true
DEFAULT_META_RESEARCH_PROFILE=balanced_meta_research
META_RESEARCH_DEFAULT_TIMEFRAME=1d
META_RESEARCH_MIN_SOURCES=3
META_RESEARCH_MIN_EVIDENCE_QUALITY=0.40
META_RESEARCH_CONFLICT_THRESHOLD=0.35
META_RESEARCH_HIGH_AGREEMENT_THRESHOLD=0.70
META_RESEARCH_UNCERTAINTY_PENALTY_ENABLED=true
META_RESEARCH_QUALITY_PENALTY_ENABLED=true
META_RESEARCH_MISSING_SOURCE_PENALTY_ENABLED=true
META_RESEARCH_INCLUDE_TECHNICAL=true
META_RESEARCH_INCLUDE_STRATEGY=true
META_RESEARCH_INCLUDE_RISK_LEVEL=true
META_RESEARCH_INCLUDE_BACKTEST=true
META_RESEARCH_INCLUDE_VALIDATION=true
META_RESEARCH_INCLUDE_ML=true
META_RESEARCH_INCLUDE_PAPER=true
META_RESEARCH_INCLUDE_FACTOR=true
META_RESEARCH_INCLUDE_SYNTHETIC_INDEX=true
META_RESEARCH_INCLUDE_PORTFOLIO=true
META_RESEARCH_INCLUDE_REGIME=true
META_RESEARCH_SAVE_REPORTS=true
META_RESEARCH_SAVE_TABLES=true
META_RESEARCH_MIN_QUALITY_SCORE=0.40
""")

with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

if "REPORTS_META_RESEARCH_DIR" not in content:
    report_paths = """
REPORTS_VALIDATION_DIR = REPORTS_DIR / "validation_reports"

# Meta Research paths
REPORTS_META_RESEARCH_DIR = REPORTS_DIR / "meta_research"
REPORTS_META_RESEARCH_CSV_DIR = REPORTS_META_RESEARCH_DIR / "csv"
REPORTS_META_RESEARCH_MD_DIR = REPORTS_META_RESEARCH_DIR / "markdown"
REPORTS_META_RESEARCH_TXT_DIR = REPORTS_META_RESEARCH_DIR / "txt"
"""
    content = content.replace('REPORTS_VALIDATION_DIR = REPORTS_DIR / "validation_reports"', report_paths)

if "LAKE_META_RESEARCH_DIR" not in content:
    content = re.sub(
        r'(LAKE_FACTOR_RESEARCH_REPORTS_DIR = LAKE_FACTOR_RESEARCH_DIR / "reports")',
        r'\1\n\n# Phase 45: Meta Research\nLAKE_META_RESEARCH_DIR = LAKE_DIR / "meta_research"\nLAKE_META_RESEARCH_EVIDENCE_DIR = LAKE_META_RESEARCH_DIR / "evidence"\nLAKE_META_RESEARCH_RELIABILITY_DIR = LAKE_META_RESEARCH_DIR / "reliability"\nLAKE_META_RESEARCH_CONSENSUS_DIR = LAKE_META_RESEARCH_DIR / "consensus"\nLAKE_META_RESEARCH_CONFLICTS_DIR = LAKE_META_RESEARCH_DIR / "conflicts"\nLAKE_META_RESEARCH_UNCERTAINTY_DIR = LAKE_META_RESEARCH_DIR / "uncertainty"\nLAKE_META_RESEARCH_ENSEMBLE_DIR = LAKE_META_RESEARCH_DIR / "ensemble"\nLAKE_META_RESEARCH_RANKINGS_DIR = LAKE_META_RESEARCH_DIR / "rankings"\nLAKE_META_RESEARCH_SNAPSHOTS_DIR = LAKE_META_RESEARCH_DIR / "snapshots"\nLAKE_META_RESEARCH_REPORTS_DIR = LAKE_META_RESEARCH_DIR / "reports"\nLAKE_META_RESEARCH_QUALITY_DIR = LAKE_META_RESEARCH_DIR / "quality"',
        content,
        count=1
    )

    content = re.sub(
        r'(REPORTS_FACTOR_RESEARCH_TXT_DIR,\s*)]',
        r'\1\n            # Phase 45: Meta Research\n            LAKE_META_RESEARCH_DIR,\n            LAKE_META_RESEARCH_EVIDENCE_DIR,\n            LAKE_META_RESEARCH_RELIABILITY_DIR,\n            LAKE_META_RESEARCH_CONSENSUS_DIR,\n            LAKE_META_RESEARCH_CONFLICTS_DIR,\n            LAKE_META_RESEARCH_UNCERTAINTY_DIR,\n            LAKE_META_RESEARCH_ENSEMBLE_DIR,\n            LAKE_META_RESEARCH_RANKINGS_DIR,\n            LAKE_META_RESEARCH_SNAPSHOTS_DIR,\n            LAKE_META_RESEARCH_REPORTS_DIR,\n            LAKE_META_RESEARCH_QUALITY_DIR,\n            REPORTS_META_RESEARCH_DIR,\n            REPORTS_META_RESEARCH_CSV_DIR,\n            REPORTS_META_RESEARCH_MD_DIR,\n            REPORTS_META_RESEARCH_TXT_DIR,\n        ]',
        content,
        count=1
    )

    with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
        f.write(content)
