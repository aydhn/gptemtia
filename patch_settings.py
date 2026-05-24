import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

new_settings = """
    # Phase 46: Experiment Tracking and Research Versioning
    experiment_tracking_enabled: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_TRACKING_ENABLED", "true")).lower() == "true")
    default_experiment_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_EXPERIMENT_PROFILE", "balanced_experiment_tracking"))
    experiment_default_timeframe: str = field(default_factory=lambda: os.getenv("EXPERIMENT_DEFAULT_TIMEFRAME", "1d"))
    experiment_save_run_manifest: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_SAVE_RUN_MANIFEST", "true")).lower() == "true")
    experiment_save_artifact_manifest: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_SAVE_ARTIFACT_MANIFEST", "true")).lower() == "true")
    experiment_save_reproducibility_manifest: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_SAVE_REPRODUCIBILITY_MANIFEST", "true")).lower() == "true")
    experiment_save_quality_report: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_SAVE_QUALITY_REPORT", "true")).lower() == "true")
    experiment_max_runs_in_leaderboard: int = field(default_factory=lambda: int(os.getenv("EXPERIMENT_MAX_RUNS_IN_LEADERBOARD", "500")))
    experiment_min_quality_score: float = field(default_factory=lambda: float(os.getenv("EXPERIMENT_MIN_QUALITY_SCORE", "0.40")))
    experiment_default_baseline_name: str = field(default_factory=lambda: os.getenv("EXPERIMENT_DEFAULT_BASELINE_NAME", "baseline_research_run"))
    experiment_enable_ablation_studies: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_ENABLE_ABLATION_STUDIES", "true")).lower() == "true")
    experiment_enable_comparison: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_ENABLE_COMPARISON", "true")).lower() == "true")
    experiment_enable_leaderboard: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_ENABLE_LEADERBOARD", "true")).lower() == "true")
    experiment_require_hypothesis: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_REQUIRE_HYPOTHESIS", "false")).lower() == "true")
    experiment_require_reproducibility_manifest: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_REQUIRE_REPRODUCIBILITY_MANIFEST", "true")).lower() == "true")
    experiment_capture_environment: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_CAPTURE_ENVIRONMENT", "true")).lower() == "true")
    experiment_capture_config_snapshot: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_CAPTURE_CONFIG_SNAPSHOT", "true")).lower() == "true")
    experiment_capture_artifact_snapshot: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_CAPTURE_ARTIFACT_SNAPSHOT", "true")).lower() == "true")
    experiment_allow_rerun_candidates: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_ALLOW_RERUN_CANDIDATES", "true")).lower() == "true")
    experiment_tracking_dry_run: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_TRACKING_DRY_RUN", "true")).lower() == "true")

"""

content = content.replace("    def __post_init__(self):", new_settings + "    def __post_init__(self):")

with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
    f.write(content)
