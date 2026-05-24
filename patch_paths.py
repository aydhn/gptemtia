import re

with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

new_paths = """
# Phase 46: Experiment Tracking
LAKE_EXPERIMENTS_DIR = LAKE_DIR / "experiments"
LAKE_EXPERIMENTS_HYPOTHESES_DIR = LAKE_EXPERIMENTS_DIR / "hypotheses"
LAKE_EXPERIMENTS_DEFINITIONS_DIR = LAKE_EXPERIMENTS_DIR / "definitions"
LAKE_EXPERIMENTS_RUNS_DIR = LAKE_EXPERIMENTS_DIR / "runs"
LAKE_EXPERIMENTS_ARTIFACTS_DIR = LAKE_EXPERIMENTS_DIR / "artifacts"
LAKE_EXPERIMENTS_REPRODUCIBILITY_DIR = LAKE_EXPERIMENTS_DIR / "reproducibility"
LAKE_EXPERIMENTS_VERSIONS_DIR = LAKE_EXPERIMENTS_DIR / "versions"
LAKE_EXPERIMENTS_ABLATION_DIR = LAKE_EXPERIMENTS_DIR / "ablation"
LAKE_EXPERIMENTS_COMPARISONS_DIR = LAKE_EXPERIMENTS_DIR / "comparisons"
LAKE_EXPERIMENTS_LEADERBOARDS_DIR = LAKE_EXPERIMENTS_DIR / "leaderboards"
LAKE_EXPERIMENTS_QUALITY_DIR = LAKE_EXPERIMENTS_DIR / "quality"

REPORTS_EXPERIMENTS_DIR = REPORTS_DIR / "experiments"
REPORTS_EXPERIMENTS_CSV_DIR = REPORTS_EXPERIMENTS_DIR / "csv"
REPORTS_EXPERIMENTS_MARKDOWN_DIR = REPORTS_EXPERIMENTS_DIR / "markdown"
REPORTS_EXPERIMENTS_TXT_DIR = REPORTS_EXPERIMENTS_DIR / "txt"
REPORTS_EXPERIMENTS_JSON_DIR = REPORTS_EXPERIMENTS_DIR / "json"

"""

content = content.replace("class ProjectPaths:", new_paths + "class ProjectPaths:")

init_paths = """
        self.experiments_dir = LAKE_EXPERIMENTS_DIR
        self.experiments_hypotheses = LAKE_EXPERIMENTS_HYPOTHESES_DIR
        self.experiments_definitions = LAKE_EXPERIMENTS_DEFINITIONS_DIR
        self.experiments_runs = LAKE_EXPERIMENTS_RUNS_DIR
        self.experiments_artifacts = LAKE_EXPERIMENTS_ARTIFACTS_DIR
        self.experiments_reproducibility = LAKE_EXPERIMENTS_REPRODUCIBILITY_DIR
        self.experiments_versions = LAKE_EXPERIMENTS_VERSIONS_DIR
        self.experiments_ablation = LAKE_EXPERIMENTS_ABLATION_DIR
        self.experiments_comparisons = LAKE_EXPERIMENTS_COMPARISONS_DIR
        self.experiments_leaderboards = LAKE_EXPERIMENTS_LEADERBOARDS_DIR
        self.experiments_quality = LAKE_EXPERIMENTS_QUALITY_DIR

        self.experiments_reports = REPORTS_EXPERIMENTS_DIR
        self.experiments_reports_csv = REPORTS_EXPERIMENTS_CSV_DIR
        self.experiments_reports_markdown = REPORTS_EXPERIMENTS_MARKDOWN_DIR
        self.experiments_reports_txt = REPORTS_EXPERIMENTS_TXT_DIR
        self.experiments_reports_json = REPORTS_EXPERIMENTS_JSON_DIR

"""

content = content.replace("self.project_root = PROJECT_ROOT", init_paths + "        self.project_root = PROJECT_ROOT")


dirs_to_create = """
        LAKE_EXPERIMENTS_DIR,
        LAKE_EXPERIMENTS_HYPOTHESES_DIR,
        LAKE_EXPERIMENTS_DEFINITIONS_DIR,
        LAKE_EXPERIMENTS_RUNS_DIR,
        LAKE_EXPERIMENTS_ARTIFACTS_DIR,
        LAKE_EXPERIMENTS_REPRODUCIBILITY_DIR,
        LAKE_EXPERIMENTS_VERSIONS_DIR,
        LAKE_EXPERIMENTS_ABLATION_DIR,
        LAKE_EXPERIMENTS_COMPARISONS_DIR,
        LAKE_EXPERIMENTS_LEADERBOARDS_DIR,
        LAKE_EXPERIMENTS_QUALITY_DIR,
        REPORTS_EXPERIMENTS_DIR,
        REPORTS_EXPERIMENTS_CSV_DIR,
        REPORTS_EXPERIMENTS_MARKDOWN_DIR,
        REPORTS_EXPERIMENTS_TXT_DIR,
        REPORTS_EXPERIMENTS_JSON_DIR,
"""

content = content.replace("REPORTS_RESEARCH_REPORTS_TXT_DIR,", "REPORTS_RESEARCH_REPORTS_TXT_DIR," + dirs_to_create)

with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
    f.write(content)
