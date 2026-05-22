import re

with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

new_paths = """
# Phase 43: Synthetic Indices
LAKE_SYNTHETIC_INDICES_DIR = LAKE_DIR / "synthetic_indices"
LAKE_SYNTHETIC_INDICES_DEFINITIONS_DIR = LAKE_SYNTHETIC_INDICES_DIR / "definitions"
LAKE_SYNTHETIC_INDICES_LEVELS_DIR = LAKE_SYNTHETIC_INDICES_DIR / "levels"
LAKE_SYNTHETIC_INDICES_RETURNS_DIR = LAKE_SYNTHETIC_INDICES_DIR / "returns"
LAKE_SYNTHETIC_INDICES_RELATIVE_STRENGTH_DIR = LAKE_SYNTHETIC_INDICES_DIR / "relative_strength"
LAKE_SYNTHETIC_INDICES_RELATIVE_MOMENTUM_DIR = LAKE_SYNTHETIC_INDICES_DIR / "relative_momentum"
LAKE_SYNTHETIC_INDICES_ROTATION_DIR = LAKE_SYNTHETIC_INDICES_DIR / "rotation"
LAKE_SYNTHETIC_INDICES_LEADERSHIP_DIR = LAKE_SYNTHETIC_INDICES_DIR / "leadership"
LAKE_SYNTHETIC_INDICES_COMPARISONS_DIR = LAKE_SYNTHETIC_INDICES_DIR / "comparisons"
LAKE_SYNTHETIC_INDICES_PERFORMANCE_DIR = LAKE_SYNTHETIC_INDICES_DIR / "performance"
LAKE_SYNTHETIC_INDICES_QUALITY_DIR = LAKE_SYNTHETIC_INDICES_DIR / "quality"

REPORTS_SYNTHETIC_INDICES_DIR = REPORTS_DIR / "synthetic_indices"
REPORTS_SYNTHETIC_INDICES_CSV_DIR = REPORTS_SYNTHETIC_INDICES_DIR / "csv"
REPORTS_SYNTHETIC_INDICES_MARKDOWN_DIR = REPORTS_SYNTHETIC_INDICES_DIR / "markdown"
REPORTS_SYNTHETIC_INDICES_TXT_DIR = REPORTS_SYNTHETIC_INDICES_DIR / "txt"


def ensure_project_directories():
"""

content = content.replace("def ensure_project_directories():", new_paths)


ensure_paths = """
        LAKE_SECURITY_READINESS_DIR,
        LAKE_SECURITY_QUALITY_DIR,
        REPORTS_SECURITY_REPORTS_DIR,
        LAKE_SYNTHETIC_INDICES_DIR,
        LAKE_SYNTHETIC_INDICES_DEFINITIONS_DIR,
        LAKE_SYNTHETIC_INDICES_LEVELS_DIR,
        LAKE_SYNTHETIC_INDICES_RETURNS_DIR,
        LAKE_SYNTHETIC_INDICES_RELATIVE_STRENGTH_DIR,
        LAKE_SYNTHETIC_INDICES_RELATIVE_MOMENTUM_DIR,
        LAKE_SYNTHETIC_INDICES_ROTATION_DIR,
        LAKE_SYNTHETIC_INDICES_LEADERSHIP_DIR,
        LAKE_SYNTHETIC_INDICES_COMPARISONS_DIR,
        LAKE_SYNTHETIC_INDICES_PERFORMANCE_DIR,
        LAKE_SYNTHETIC_INDICES_QUALITY_DIR,
        REPORTS_SYNTHETIC_INDICES_DIR,
        REPORTS_SYNTHETIC_INDICES_CSV_DIR,
        REPORTS_SYNTHETIC_INDICES_MARKDOWN_DIR,
        REPORTS_SYNTHETIC_INDICES_TXT_DIR,
    ]
"""

content = re.sub(r'        LAKE_SECURITY_READINESS_DIR,\n        LAKE_SECURITY_QUALITY_DIR,\n        REPORTS_SECURITY_REPORTS_DIR,\n    \]', ensure_paths, content)

project_paths = """
        self.portfolio_regime_reports = REPORTS_PORTFOLIO_REGIME_DIR

        # Phase 43: Synthetic Indices
        self.synthetic_indices_dir = LAKE_SYNTHETIC_INDICES_DIR
        self.synthetic_indices_definitions = LAKE_SYNTHETIC_INDICES_DEFINITIONS_DIR
        self.synthetic_indices_levels = LAKE_SYNTHETIC_INDICES_LEVELS_DIR
        self.synthetic_indices_returns = LAKE_SYNTHETIC_INDICES_RETURNS_DIR
        self.synthetic_indices_relative_strength = LAKE_SYNTHETIC_INDICES_RELATIVE_STRENGTH_DIR
        self.synthetic_indices_relative_momentum = LAKE_SYNTHETIC_INDICES_RELATIVE_MOMENTUM_DIR
        self.synthetic_indices_rotation = LAKE_SYNTHETIC_INDICES_ROTATION_DIR
        self.synthetic_indices_leadership = LAKE_SYNTHETIC_INDICES_LEADERSHIP_DIR
        self.synthetic_indices_comparisons = LAKE_SYNTHETIC_INDICES_COMPARISONS_DIR
        self.synthetic_indices_performance = LAKE_SYNTHETIC_INDICES_PERFORMANCE_DIR
        self.synthetic_indices_quality = LAKE_SYNTHETIC_INDICES_QUALITY_DIR
        self.synthetic_indices_reports = REPORTS_SYNTHETIC_INDICES_DIR
        self.synthetic_indices_reports_csv = REPORTS_SYNTHETIC_INDICES_CSV_DIR
        self.synthetic_indices_reports_markdown = REPORTS_SYNTHETIC_INDICES_MARKDOWN_DIR
        self.synthetic_indices_reports_txt = REPORTS_SYNTHETIC_INDICES_TXT_DIR
"""

content = content.replace("        self.portfolio_regime_reports = REPORTS_PORTFOLIO_REGIME_DIR", project_paths)

with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
    f.write(content)
