import re

def patch_file():
    path = "commodity_fx_signal_bot/config/paths.py"
    with open(path, "r") as f:
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

    if "LAKE_PERFORMANCE_RUNTIME" not in content:
        # insert right before the list of dirs
        content = content.replace("    def get_all_directories(cls) -> list[Path]:", new_paths + "\n    @classmethod\n    def get_all_directories(cls) -> list[Path]:")

        # also add to the list
        all_dirs_list = """
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
        content = content.replace("            cls.LAKE_DIR,", "            cls.LAKE_DIR," + all_dirs_list)

    with open(path, "w") as f:
        f.write(content)

patch_file()
