import re
from pathlib import Path

# Update settings.py
settings_file = Path("config/settings.py")
content = settings_file.read_text()

if "research_planning_enabled" not in content:
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
    research_planning_min_quality_score: float = 0.40

    def __post_init__(self):"""

    content = content.replace("    def __post_init__(self):", insert_text)
    settings_file.write_text(content)
    print("Updated settings.py")

# Update paths.py
paths_file = Path("config/paths.py")
paths_content = paths_file.read_text()

if "LAKE_RESEARCH_PLANNING_DIR" not in paths_content:
    # Append path definitions to the end
    path_insert = """

# Phase 48: Research Planning
LAKE_RESEARCH_PLANNING_DIR = LAKE_DIR / "research_planning"
LAKE_RESEARCH_PLANNING_SIGNALS_DIR = LAKE_RESEARCH_PLANNING_DIR / "signals"
LAKE_RESEARCH_PLANNING_TASKS_DIR = LAKE_RESEARCH_PLANNING_DIR / "tasks"
LAKE_RESEARCH_PLANNING_BACKLOG_DIR = LAKE_RESEARCH_PLANNING_DIR / "backlog"
LAKE_RESEARCH_PLANNING_PRIORITIES_DIR = LAKE_RESEARCH_PLANNING_DIR / "priorities"
LAKE_RESEARCH_PLANNING_NEXT_BEST_DIR = LAKE_RESEARCH_PLANNING_DIR / "next_best"
LAKE_RESEARCH_PLANNING_DEBT_DIR = LAKE_RESEARCH_PLANNING_DIR / "debt"
LAKE_RESEARCH_PLANNING_OPPORTUNITIES_DIR = LAKE_RESEARCH_PLANNING_DIR / "opportunities"
LAKE_RESEARCH_PLANNING_ROADMAP_DIR = LAKE_RESEARCH_PLANNING_DIR / "roadmap"
LAKE_RESEARCH_PLANNING_DEPENDENCIES_DIR = LAKE_RESEARCH_PLANNING_DIR / "dependencies"
LAKE_RESEARCH_PLANNING_MILESTONES_DIR = LAKE_RESEARCH_PLANNING_DIR / "milestones"
LAKE_RESEARCH_PLANNING_ORCHESTRATION_DIR = LAKE_RESEARCH_PLANNING_DIR / "orchestration"
LAKE_RESEARCH_PLANNING_QUALITY_DIR = LAKE_RESEARCH_PLANNING_DIR / "quality"

REPORTS_RESEARCH_PLANNING_DIR = REPORTS_DIR / "research_planning"
REPORTS_RESEARCH_PLANNING_CSV_DIR = REPORTS_RESEARCH_PLANNING_DIR / "csv"
REPORTS_RESEARCH_PLANNING_MARKDOWN_DIR = REPORTS_RESEARCH_PLANNING_DIR / "markdown"
REPORTS_RESEARCH_PLANNING_TXT_DIR = REPORTS_RESEARCH_PLANNING_DIR / "txt"
REPORTS_RESEARCH_PLANNING_JSON_DIR = REPORTS_RESEARCH_PLANNING_DIR / "json"

class PathsManager:
    # Added statically, the create function will be added dynamically by regex below
"""

    paths_content += path_insert

    # We also need to add these directories to ensure_directories
    # This might be tricky, let's search for the method and replace it
    # We don't have the full code of paths.py, let's just append to ensure_project_directories

    # Actually wait, there is a ensure_directories or similar in the project usually
    # Let's inspect the ensure_project_directories function
    print("Paths logic needs to check if we can just append to create directories list")
