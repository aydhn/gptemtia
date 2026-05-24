import re
from pathlib import Path

# Update paths.py ensure_project_directories
paths_file = Path("config/paths.py")
paths_content = paths_file.read_text()

# We know the path constants are already appended at the end
# Now we need to add them to the directories list inside ensure_project_directories
insert_dirs = """
        LAKE_RESEARCH_PLANNING_DIR,
        LAKE_RESEARCH_PLANNING_SIGNALS_DIR,
        LAKE_RESEARCH_PLANNING_TASKS_DIR,
        LAKE_RESEARCH_PLANNING_BACKLOG_DIR,
        LAKE_RESEARCH_PLANNING_PRIORITIES_DIR,
        LAKE_RESEARCH_PLANNING_NEXT_BEST_DIR,
        LAKE_RESEARCH_PLANNING_DEBT_DIR,
        LAKE_RESEARCH_PLANNING_OPPORTUNITIES_DIR,
        LAKE_RESEARCH_PLANNING_ROADMAP_DIR,
        LAKE_RESEARCH_PLANNING_DEPENDENCIES_DIR,
        LAKE_RESEARCH_PLANNING_MILESTONES_DIR,
        LAKE_RESEARCH_PLANNING_ORCHESTRATION_DIR,
        LAKE_RESEARCH_PLANNING_QUALITY_DIR,
        REPORTS_RESEARCH_PLANNING_DIR,
        REPORTS_RESEARCH_PLANNING_CSV_DIR,
        REPORTS_RESEARCH_PLANNING_MARKDOWN_DIR,
        REPORTS_RESEARCH_PLANNING_TXT_DIR,
        REPORTS_RESEARCH_PLANNING_JSON_DIR,
"""

# Find the start of the list
if "LAKE_RESEARCH_PLANNING_DIR" not in paths_content[paths_content.find("directories = ["):]:
    paths_content = paths_content.replace(
        "directories = [",
        "directories = [" + insert_dirs
    )
    paths_file.write_text(paths_content)
    print("Updated paths.py ensure_project_directories")
