import os
import re

def update_settings():
    settings_path = "commodity_fx_signal_bot/config/settings.py"
    with open(settings_path, "r") as f:
        content = f.read()

    new_settings = """
    # Performance Profiling and Stability Settings
    performance_monitoring_enabled: bool = True
    default_performance_profile: str = "balanced_local_performance"
    performance_default_timeframe: str = "1d"
    performance_profile_scripts: bool = True
    performance_profile_memory: bool = True
    performance_profile_cpu: bool = True
    performance_detect_gpu: bool = True
    performance_allow_gpu_optional: bool = True
    performance_max_runtime_seconds_per_script: int = 300
    performance_max_memory_mb_per_script: int = 2048
    performance_max_batch_symbols: int = 50
    performance_max_parallel_workers: int = 1
    performance_enable_cache: bool = True
    performance_cache_format: str = "parquet_or_csv"
    performance_cache_ttl_hours: int = 24
    performance_cache_max_size_mb: int = 2048
    performance_enable_checkpointing: bool = True
    performance_checkpoint_every_items: int = 25
    performance_save_reports: bool = True
    performance_min_quality_score: float = 0.40
"""
    if "performance_monitoring_enabled" not in content:
        content = content.replace("class Settings(BaseSettings):", "class Settings(BaseSettings):\n" + new_settings)

    with open(settings_path, "w") as f:
        f.write(content)

def update_env_example():
    env_path = "commodity_fx_signal_bot/.env.example"
    with open(env_path, "r") as f:
        content = f.read()

    new_env = """
# Performance Profiling
PERFORMANCE_MONITORING_ENABLED=true
DEFAULT_PERFORMANCE_PROFILE=balanced_local_performance
PERFORMANCE_DEFAULT_TIMEFRAME=1d
PERFORMANCE_PROFILE_SCRIPTS=true
PERFORMANCE_PROFILE_MEMORY=true
PERFORMANCE_PROFILE_CPU=true
PERFORMANCE_DETECT_GPU=true
PERFORMANCE_ALLOW_GPU_OPTIONAL=true
PERFORMANCE_MAX_RUNTIME_SECONDS_PER_SCRIPT=300
PERFORMANCE_MAX_MEMORY_MB_PER_SCRIPT=2048
PERFORMANCE_MAX_BATCH_SYMBOLS=50
PERFORMANCE_MAX_PARALLEL_WORKERS=1
PERFORMANCE_ENABLE_CACHE=true
PERFORMANCE_CACHE_FORMAT=parquet_or_csv
PERFORMANCE_CACHE_TTL_HOURS=24
PERFORMANCE_CACHE_MAX_SIZE_MB=2048
PERFORMANCE_ENABLE_CHECKPOINTING=true
PERFORMANCE_CHECKPOINT_EVERY_ITEMS=25
PERFORMANCE_SAVE_REPORTS=true
PERFORMANCE_MIN_QUALITY_SCORE=0.40
"""
    if "PERFORMANCE_MONITORING_ENABLED" not in content:
        content += new_env

    with open(env_path, "w") as f:
        f.write(content)

def update_paths():
    paths_path = "commodity_fx_signal_bot/config/paths.py"
    with open(paths_path, "r") as f:
        content = f.read()

    new_paths = """
    LAKE_PERFORMANCE = LAKE_DIR / "performance"
    LAKE_PERFORMANCE_PROFILES = LAKE_PERFORMANCE / "profiles"
    LAKE_PERFORMANCE_RUNTIME = LAKE_PERFORMANCE / "runtime"
    LAKE_PERFORMANCE_MEMORY = LAKE_PERFORMANCE / "memory"
    LAKE_PERFORMANCE_BUDGET = LAKE_PERFORMANCE / "resource_budget"
    LAKE_PERFORMANCE_CPU_GPU = LAKE_PERFORMANCE / "cpu_gpu"
    LAKE_PERFORMANCE_CACHE = LAKE_PERFORMANCE / "cache"
    LAKE_PERFORMANCE_BATCH_PLANS = LAKE_PERFORMANCE / "batch_plans"
    LAKE_PERFORMANCE_CHECKPOINTS = LAKE_PERFORMANCE / "checkpoints"
    LAKE_PERFORMANCE_STABILITY = LAKE_PERFORMANCE / "stability"
    LAKE_PERFORMANCE_BOTTLENECKS = LAKE_PERFORMANCE / "bottlenecks"
    LAKE_PERFORMANCE_OPTIMIZATION = LAKE_PERFORMANCE / "optimization"
    LAKE_PERFORMANCE_QUALITY = LAKE_PERFORMANCE / "quality"

    REPORTS_PERFORMANCE = REPORTS_OUTPUT_DIR / "performance"
    REPORTS_PERFORMANCE_CSV = REPORTS_PERFORMANCE / "csv"
    REPORTS_PERFORMANCE_MARKDOWN = REPORTS_PERFORMANCE / "markdown"
    REPORTS_PERFORMANCE_TXT = REPORTS_PERFORMANCE / "txt"
    REPORTS_PERFORMANCE_JSON = REPORTS_PERFORMANCE / "json"
"""
    new_dirs = """
        cls.LAKE_PERFORMANCE,
        cls.LAKE_PERFORMANCE_PROFILES,
        cls.LAKE_PERFORMANCE_RUNTIME,
        cls.LAKE_PERFORMANCE_MEMORY,
        cls.LAKE_PERFORMANCE_BUDGET,
        cls.LAKE_PERFORMANCE_CPU_GPU,
        cls.LAKE_PERFORMANCE_CACHE,
        cls.LAKE_PERFORMANCE_BATCH_PLANS,
        cls.LAKE_PERFORMANCE_CHECKPOINTS,
        cls.LAKE_PERFORMANCE_STABILITY,
        cls.LAKE_PERFORMANCE_BOTTLENECKS,
        cls.LAKE_PERFORMANCE_OPTIMIZATION,
        cls.LAKE_PERFORMANCE_QUALITY,
        cls.REPORTS_PERFORMANCE,
        cls.REPORTS_PERFORMANCE_CSV,
        cls.REPORTS_PERFORMANCE_MARKDOWN,
        cls.REPORTS_PERFORMANCE_TXT,
        cls.REPORTS_PERFORMANCE_JSON,
"""

    if "LAKE_PERFORMANCE" not in content:
        content = re.sub(r'(LAKE_REPORTS_.*?\n)', r'\1' + new_paths, content, count=1)
        content = re.sub(r'(cls\.LAKE_REPORTS_.*?,)', r'\1' + new_dirs, content, count=1)

    with open(paths_path, "w") as f:
        f.write(content)

if __name__ == "__main__":
    update_settings()
    update_env_example()
    update_paths()
