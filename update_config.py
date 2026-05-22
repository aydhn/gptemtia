import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

new_settings = """
    # Phase 43: Synthetic Benchmark Baskets & Composite Indices
    synthetic_indices_enabled: bool = field(default_factory=lambda: str(os.getenv("SYNTHETIC_INDICES_ENABLED", "true")).lower() == "true")
    default_synthetic_index_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_SYNTHETIC_INDEX_PROFILE", "balanced_synthetic_index_research"))
    synthetic_index_default_timeframe: str = field(default_factory=lambda: os.getenv("SYNTHETIC_INDEX_DEFAULT_TIMEFRAME", "1d"))
    synthetic_index_base_value: float = field(default_factory=lambda: float(os.getenv("SYNTHETIC_INDEX_BASE_VALUE", "100.0")))
    synthetic_index_return_method: str = field(default_factory=lambda: os.getenv("SYNTHETIC_INDEX_RETURN_METHOD", "log"))
    synthetic_index_rebalance_method: str = field(default_factory=lambda: os.getenv("SYNTHETIC_INDEX_REBALANCE_METHOD", "static"))
    synthetic_index_rebalance_frequency: str = field(default_factory=lambda: os.getenv("SYNTHETIC_INDEX_REBALANCE_FREQUENCY", "monthly"))
    synthetic_index_min_symbols: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_MIN_SYMBOLS", "3")))
    synthetic_index_min_observations: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_MIN_OBSERVATIONS", "120")))
    synthetic_index_max_symbols_per_index: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_MAX_SYMBOLS_PER_INDEX", "20")))
    synthetic_index_max_single_weight: float = field(default_factory=lambda: float(os.getenv("SYNTHETIC_INDEX_MAX_SINGLE_WEIGHT", "0.35")))
    synthetic_index_relative_strength_windows: tuple[int, ...] = field(default_factory=lambda: tuple(map(int, os.getenv("SYNTHETIC_INDEX_RELATIVE_STRENGTH_WINDOWS", "20,60,120").split(","))))
    synthetic_index_rotation_lookback: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_ROTATION_LOOKBACK", "60")))
    synthetic_index_rotation_top_n: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_ROTATION_TOP_N", "5")))
    synthetic_index_rotation_bottom_n: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_ROTATION_BOTTOM_N", "5")))
    synthetic_index_save_definitions: bool = field(default_factory=lambda: str(os.getenv("SYNTHETIC_INDEX_SAVE_DEFINITIONS", "true")).lower() == "true")
    synthetic_index_save_levels: bool = field(default_factory=lambda: str(os.getenv("SYNTHETIC_INDEX_SAVE_LEVELS", "true")).lower() == "true")
    synthetic_index_save_reports: bool = field(default_factory=lambda: str(os.getenv("SYNTHETIC_INDEX_SAVE_REPORTS", "true")).lower() == "true")
    synthetic_index_min_quality_score: float = field(default_factory=lambda: float(os.getenv("SYNTHETIC_INDEX_MIN_QUALITY_SCORE", "0.40")))

    def __post_init__(self):
"""

content = content.replace("    def __post_init__(self):", new_settings)

with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
    f.write(content)
