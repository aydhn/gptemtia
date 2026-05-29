with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

new_paths = """
        # Phase 58: Analyst UX
        self.analyst_ux_dir = LAKE_ANALYST_UX_DIR
        self.analyst_ux_profiles_dir = LAKE_ANALYST_UX_PROFILES_DIR
        self.analyst_ux_aliases_dir = LAKE_ANALYST_UX_ALIASES_DIR
        self.analyst_ux_intents_dir = LAKE_ANALYST_UX_INTENTS_DIR
        self.analyst_ux_suggestions_dir = LAKE_ANALYST_UX_SUGGESTIONS_DIR
        self.analyst_ux_prompt_packs_dir = LAKE_ANALYST_UX_PROMPT_PACKS_DIR
        self.analyst_ux_workflow_shortcuts_dir = LAKE_ANALYST_UX_WORKFLOW_SHORTCUTS_DIR
        self.analyst_ux_query_mappings_dir = LAKE_ANALYST_UX_QUERY_MAPPINGS_DIR
        self.analyst_ux_task_board_dir = LAKE_ANALYST_UX_TASK_BOARD_DIR
        self.analyst_ux_cheat_sheets_dir = LAKE_ANALYST_UX_CHEAT_SHEETS_DIR
        self.analyst_ux_checklists_dir = LAKE_ANALYST_UX_CHECKLISTS_DIR
        self.analyst_ux_validation_dir = LAKE_ANALYST_UX_VALIDATION_DIR
        self.analyst_ux_quality_dir = LAKE_ANALYST_UX_QUALITY_DIR

        self.reports_analyst_ux_dir = REPORTS_ANALYST_UX_DIR
        self.reports_analyst_ux_csv_dir = REPORTS_ANALYST_UX_CSV_DIR
        self.reports_analyst_ux_markdown_dir = REPORTS_ANALYST_UX_MARKDOWN_DIR
        self.reports_analyst_ux_txt_dir = REPORTS_ANALYST_UX_TXT_DIR
        self.reports_analyst_ux_json_dir = REPORTS_ANALYST_UX_JSON_DIR

        self.docs_analyst_ux_dir = DOCS_ANALYST_UX_DIR

"""

# Insert inside PathConfig.__init__ before "def ensure_project_directories"
content = content.replace("    def ensure_project_directories(", new_paths + "\n    def ensure_project_directories(")

# Append variables at the end
new_globals = """
# Phase 58: Analyst UX
LAKE_ANALYST_UX_DIR = LAKE_DIR / "analyst_ux"
LAKE_ANALYST_UX_PROFILES_DIR = LAKE_ANALYST_UX_DIR / "profiles"
LAKE_ANALYST_UX_ALIASES_DIR = LAKE_ANALYST_UX_DIR / "aliases"
LAKE_ANALYST_UX_INTENTS_DIR = LAKE_ANALYST_UX_DIR / "intents"
LAKE_ANALYST_UX_SUGGESTIONS_DIR = LAKE_ANALYST_UX_DIR / "suggestions"
LAKE_ANALYST_UX_PROMPT_PACKS_DIR = LAKE_ANALYST_UX_DIR / "prompt_packs"
LAKE_ANALYST_UX_WORKFLOW_SHORTCUTS_DIR = LAKE_ANALYST_UX_DIR / "workflow_shortcuts"
LAKE_ANALYST_UX_QUERY_MAPPINGS_DIR = LAKE_ANALYST_UX_DIR / "query_mappings"
LAKE_ANALYST_UX_TASK_BOARD_DIR = LAKE_ANALYST_UX_DIR / "task_board"
LAKE_ANALYST_UX_CHEAT_SHEETS_DIR = LAKE_ANALYST_UX_DIR / "cheat_sheets"
LAKE_ANALYST_UX_CHECKLISTS_DIR = LAKE_ANALYST_UX_DIR / "checklists"
LAKE_ANALYST_UX_VALIDATION_DIR = LAKE_ANALYST_UX_DIR / "validation"
LAKE_ANALYST_UX_QUALITY_DIR = LAKE_ANALYST_UX_DIR / "quality"

REPORTS_ANALYST_UX_DIR = REPORTS_DIR / "analyst_ux"
REPORTS_ANALYST_UX_CSV_DIR = REPORTS_ANALYST_UX_DIR / "csv"
REPORTS_ANALYST_UX_MARKDOWN_DIR = REPORTS_ANALYST_UX_DIR / "markdown"
REPORTS_ANALYST_UX_TXT_DIR = REPORTS_ANALYST_UX_DIR / "txt"
REPORTS_ANALYST_UX_JSON_DIR = REPORTS_ANALYST_UX_DIR / "json"

DOCS_ANALYST_UX_DIR = PROJECT_ROOT / "docs" / "generated" / "analyst_ux"
"""

content += new_globals

# Ensure ensure_project_directories creates these directories
dirs_to_add = """
            self.analyst_ux_dir, self.analyst_ux_profiles_dir, self.analyst_ux_aliases_dir, self.analyst_ux_intents_dir,
            self.analyst_ux_suggestions_dir, self.analyst_ux_prompt_packs_dir, self.analyst_ux_workflow_shortcuts_dir,
            self.analyst_ux_query_mappings_dir, self.analyst_ux_task_board_dir, self.analyst_ux_cheat_sheets_dir,
            self.analyst_ux_checklists_dir, self.analyst_ux_validation_dir, self.analyst_ux_quality_dir,
            self.reports_analyst_ux_dir, self.reports_analyst_ux_csv_dir, self.reports_analyst_ux_markdown_dir,
            self.reports_analyst_ux_txt_dir, self.reports_analyst_ux_json_dir, self.docs_analyst_ux_dir,
"""
content = content.replace("            self.scenario_regression_quality_dir,", "            self.scenario_regression_quality_dir," + dirs_to_add)

with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
    f.write(content)
