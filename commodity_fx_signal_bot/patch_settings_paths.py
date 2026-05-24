import re
from pathlib import Path

# Update settings.py
settings_file = Path("config/settings.py")
content = settings_file.read_text()

if "research_planning_enabled" not in content:
    # Find the end of the Settings class attributes and inject
    match = re.search(r'(# Observability Quality Settings.*?observability_max_forbidden_terms_per_report:\s*int\s*=\s*\d+)', content, re.DOTALL)
    if match:
        insert_text = """

    # Research Planning Settings
    research_planning_enabled: bool = True
    default_research_planning_profile: str = "balanced_research_planning"
    research_planning_default_timeframe: str = "1d"
    research_planning_max_backlog_items: int = 500
    research_planning_max_next_best_experiments: int = 25
    research_planning_min_priority_score: float = 0.35
    research_planning_high_priority_threshold: float = 0.70
    research_planning_include_governance_signals: bool = True
    research_planning_include_experiment_signals: bool = True
    research_planning_include_meta_signals: bool = True
    research_planning_include_factor_signals: bool = True
    research_planning_include_portfolio_signals: bool = True
    research_planning_include_regime_signals: bool = True
    research_planning_include_validation_signals: bool = True
    research_planning_include_ml_signals: bool = True
    research_planning_include_paper_signals: bool = True
    research_planning_include_observability_signals: bool = True
    research_planning_save_backlog: bool = True
    research_planning_save_reports: bool = True
    research_planning_dry_run: bool = True
    research_planning_min_quality_score: float = 0.40"""

        content = content.replace(match.group(1), match.group(1) + insert_text)
        settings_file.write_text(content)
        print("Updated settings.py")
    else:
        # Fallback if pattern matching fails
        print("Could not find insertion point in settings.py")

# Update .env.example
env_file = Path(".env.example")
env_content = env_file.read_text()

if "RESEARCH_PLANNING_ENABLED" not in env_content:
    env_insert_text = """
# Research Planning
RESEARCH_PLANNING_ENABLED=true
DEFAULT_RESEARCH_PLANNING_PROFILE=balanced_research_planning
RESEARCH_PLANNING_DEFAULT_TIMEFRAME=1d
RESEARCH_PLANNING_MAX_BACKLOG_ITEMS=500
RESEARCH_PLANNING_MAX_NEXT_BEST_EXPERIMENTS=25
RESEARCH_PLANNING_MIN_PRIORITY_SCORE=0.35
RESEARCH_PLANNING_HIGH_PRIORITY_THRESHOLD=0.70
RESEARCH_PLANNING_INCLUDE_GOVERNANCE_SIGNALS=true
RESEARCH_PLANNING_INCLUDE_EXPERIMENT_SIGNALS=true
RESEARCH_PLANNING_INCLUDE_META_SIGNALS=true
RESEARCH_PLANNING_INCLUDE_FACTOR_SIGNALS=true
RESEARCH_PLANNING_INCLUDE_PORTFOLIO_SIGNALS=true
RESEARCH_PLANNING_INCLUDE_REGIME_SIGNALS=true
RESEARCH_PLANNING_INCLUDE_VALIDATION_SIGNALS=true
RESEARCH_PLANNING_INCLUDE_ML_SIGNALS=true
RESEARCH_PLANNING_INCLUDE_PAPER_SIGNALS=true
RESEARCH_PLANNING_INCLUDE_OBSERVABILITY_SIGNALS=true
RESEARCH_PLANNING_SAVE_BACKLOG=true
RESEARCH_PLANNING_SAVE_REPORTS=true
RESEARCH_PLANNING_DRY_RUN=true
RESEARCH_PLANNING_MIN_QUALITY_SCORE=0.40
"""
    env_content += env_insert_text
    env_file.write_text(env_content)
    print("Updated .env.example")

# Update paths.py
paths_file = Path("config/paths.py")
paths_content = paths_file.read_text()

if "RESEARCH_PLANNING_DIR" not in paths_content:
    # Insert path definitions
    path_insert = """
# Research Planning Paths
RESEARCH_PLANNING_DIR = DATA_LAKE_DIR / "research_planning"
RESEARCH_PLANNING_SIGNALS_DIR = RESEARCH_PLANNING_DIR / "signals"
RESEARCH_PLANNING_TASKS_DIR = RESEARCH_PLANNING_DIR / "tasks"
RESEARCH_PLANNING_BACKLOG_DIR = RESEARCH_PLANNING_DIR / "backlog"
RESEARCH_PLANNING_PRIORITIES_DIR = RESEARCH_PLANNING_DIR / "priorities"
RESEARCH_PLANNING_NEXT_BEST_DIR = RESEARCH_PLANNING_DIR / "next_best"
RESEARCH_PLANNING_DEBT_DIR = RESEARCH_PLANNING_DIR / "debt"
RESEARCH_PLANNING_OPPORTUNITIES_DIR = RESEARCH_PLANNING_DIR / "opportunities"
RESEARCH_PLANNING_ROADMAP_DIR = RESEARCH_PLANNING_DIR / "roadmap"
RESEARCH_PLANNING_DEPENDENCIES_DIR = RESEARCH_PLANNING_DIR / "dependencies"
RESEARCH_PLANNING_MILESTONES_DIR = RESEARCH_PLANNING_DIR / "milestones"
RESEARCH_PLANNING_ORCHESTRATION_DIR = RESEARCH_PLANNING_DIR / "orchestration"
RESEARCH_PLANNING_QUALITY_DIR = RESEARCH_PLANNING_DIR / "quality"

RESEARCH_PLANNING_REPORTS_DIR = REPORTS_OUTPUT_DIR / "research_planning"
RESEARCH_PLANNING_REPORTS_CSV_DIR = RESEARCH_PLANNING_REPORTS_DIR / "csv"
RESEARCH_PLANNING_REPORTS_MD_DIR = RESEARCH_PLANNING_REPORTS_DIR / "markdown"
RESEARCH_PLANNING_REPORTS_TXT_DIR = RESEARCH_PLANNING_REPORTS_DIR / "txt"
RESEARCH_PLANNING_REPORTS_JSON_DIR = RESEARCH_PLANNING_REPORTS_DIR / "json"
"""

    # Insert just before create_directories
    match1 = re.search(r'(# Helper Lists.*?DIRECTORIES_TO_CREATE = \[)', paths_content, re.DOTALL)
    if match1:
        paths_content = paths_content.replace("# Helper Lists", path_insert + "\n# Helper Lists")

        # Add to DIRECTORIES_TO_CREATE list
        match2 = re.search(r'(DIRECTORIES_TO_CREATE = \[[^\]]*)(])', paths_content, re.DOTALL)
        if match2:
            dirs_insert = """,
    RESEARCH_PLANNING_DIR,
    RESEARCH_PLANNING_SIGNALS_DIR,
    RESEARCH_PLANNING_TASKS_DIR,
    RESEARCH_PLANNING_BACKLOG_DIR,
    RESEARCH_PLANNING_PRIORITIES_DIR,
    RESEARCH_PLANNING_NEXT_BEST_DIR,
    RESEARCH_PLANNING_DEBT_DIR,
    RESEARCH_PLANNING_OPPORTUNITIES_DIR,
    RESEARCH_PLANNING_ROADMAP_DIR,
    RESEARCH_PLANNING_DEPENDENCIES_DIR,
    RESEARCH_PLANNING_MILESTONES_DIR,
    RESEARCH_PLANNING_ORCHESTRATION_DIR,
    RESEARCH_PLANNING_QUALITY_DIR,
    RESEARCH_PLANNING_REPORTS_DIR,
    RESEARCH_PLANNING_REPORTS_CSV_DIR,
    RESEARCH_PLANNING_REPORTS_MD_DIR,
    RESEARCH_PLANNING_REPORTS_TXT_DIR,
    RESEARCH_PLANNING_REPORTS_JSON_DIR"""

            paths_content = paths_content[:match2.end(1)] + dirs_insert + paths_content[match2.end(1):]
            paths_file.write_text(paths_content)
            print("Updated paths.py")
        else:
            print("Could not find DIRECTORIES_TO_CREATE list")
    else:
        print("Could not find insertion point in paths.py")
