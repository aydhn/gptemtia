import re

with open("commodity_fx_signal_bot/config/paths.py", "r") as f:
    content = f.read()

# Portfolio regime paths to add
portfolio_regime_lake_paths = """
# Phase 42: Portfolio Regime Research
LAKE_PORTFOLIO_REGIME_DIR = LAKE_DIR / "portfolio_regime"
LAKE_PORTFOLIO_REGIME_REGIMES_DIR = LAKE_PORTFOLIO_REGIME_DIR / "regimes"
LAKE_PORTFOLIO_REGIME_CONDITIONED_RETURNS_DIR = LAKE_PORTFOLIO_REGIME_DIR / "conditioned_returns"
LAKE_PORTFOLIO_REGIME_CORRELATION_DIR = LAKE_PORTFOLIO_REGIME_DIR / "correlation"
LAKE_PORTFOLIO_REGIME_SCENARIOS_DIR = LAKE_PORTFOLIO_REGIME_DIR / "scenarios"
LAKE_PORTFOLIO_REGIME_STRESS_TESTS_DIR = LAKE_PORTFOLIO_REGIME_DIR / "stress_tests"
LAKE_PORTFOLIO_REGIME_DRAWDOWNS_DIR = LAKE_PORTFOLIO_REGIME_DIR / "drawdowns"
LAKE_PORTFOLIO_REGIME_RECOVERY_DIR = LAKE_PORTFOLIO_REGIME_DIR / "recovery"
LAKE_PORTFOLIO_REGIME_TAIL_RISK_DIR = LAKE_PORTFOLIO_REGIME_DIR / "tail_risk"
LAKE_PORTFOLIO_REGIME_EXPOSURE_DIR = LAKE_PORTFOLIO_REGIME_DIR / "exposure"
LAKE_PORTFOLIO_REGIME_QUALITY_DIR = LAKE_PORTFOLIO_REGIME_DIR / "quality"

REPORTS_PORTFOLIO_REGIME_DIR = REPORTS_DIR / "portfolio_regime"
REPORTS_PORTFOLIO_REGIME_CSV_DIR = REPORTS_PORTFOLIO_REGIME_DIR / "csv"
REPORTS_PORTFOLIO_REGIME_MARKDOWN_DIR = REPORTS_PORTFOLIO_REGIME_DIR / "markdown"
REPORTS_PORTFOLIO_REGIME_TXT_DIR = REPORTS_PORTFOLIO_REGIME_DIR / "txt"

"""

portfolio_regime_dirs_to_ensure = """
        LAKE_PORTFOLIO_REGIME_DIR,
        LAKE_PORTFOLIO_REGIME_REGIMES_DIR,
        LAKE_PORTFOLIO_REGIME_CONDITIONED_RETURNS_DIR,
        LAKE_PORTFOLIO_REGIME_CORRELATION_DIR,
        LAKE_PORTFOLIO_REGIME_SCENARIOS_DIR,
        LAKE_PORTFOLIO_REGIME_STRESS_TESTS_DIR,
        LAKE_PORTFOLIO_REGIME_DRAWDOWNS_DIR,
        LAKE_PORTFOLIO_REGIME_RECOVERY_DIR,
        LAKE_PORTFOLIO_REGIME_TAIL_RISK_DIR,
        LAKE_PORTFOLIO_REGIME_EXPOSURE_DIR,
        LAKE_PORTFOLIO_REGIME_QUALITY_DIR,
        REPORTS_PORTFOLIO_REGIME_DIR,
        REPORTS_PORTFOLIO_REGIME_CSV_DIR,
        REPORTS_PORTFOLIO_REGIME_MARKDOWN_DIR,
        REPORTS_PORTFOLIO_REGIME_TXT_DIR,
"""

portfolio_regime_project_paths = """
        # Phase 42: Portfolio Regime Research
        self.portfolio_regime_dir = LAKE_PORTFOLIO_REGIME_DIR
        self.portfolio_regime_regimes = LAKE_PORTFOLIO_REGIME_REGIMES_DIR
        self.portfolio_regime_conditioned_returns = LAKE_PORTFOLIO_REGIME_CONDITIONED_RETURNS_DIR
        self.portfolio_regime_correlation = LAKE_PORTFOLIO_REGIME_CORRELATION_DIR
        self.portfolio_regime_scenarios = LAKE_PORTFOLIO_REGIME_SCENARIOS_DIR
        self.portfolio_regime_stress_tests = LAKE_PORTFOLIO_REGIME_STRESS_TESTS_DIR
        self.portfolio_regime_drawdowns = LAKE_PORTFOLIO_REGIME_DRAWDOWNS_DIR
        self.portfolio_regime_recovery = LAKE_PORTFOLIO_REGIME_RECOVERY_DIR
        self.portfolio_regime_tail_risk = LAKE_PORTFOLIO_REGIME_TAIL_RISK_DIR
        self.portfolio_regime_exposure = LAKE_PORTFOLIO_REGIME_EXPOSURE_DIR
        self.portfolio_regime_quality = LAKE_PORTFOLIO_REGIME_QUALITY_DIR
        self.portfolio_regime_reports = REPORTS_PORTFOLIO_REGIME_DIR
"""

content = content.replace("def ensure_project_directories() -> None:", portfolio_regime_lake_paths + "def ensure_project_directories() -> None:")

content = content.replace("        LAKE_REPORT_EXPORTS_QUALITY_DIR,", "        LAKE_REPORT_EXPORTS_QUALITY_DIR,\n" + portfolio_regime_dirs_to_ensure)

content = content.replace("        self.security_reports = REPORTS_SECURITY_REPORTS_DIR", "        self.security_reports = REPORTS_SECURITY_REPORTS_DIR\n\n" + portfolio_regime_project_paths)

with open("commodity_fx_signal_bot/config/paths.py", "w") as f:
    f.write(content)
