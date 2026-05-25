import re

def patch_file():
    path = "commodity_fx_signal_bot/data/storage/data_lake.py"
    with open(path, "r") as f:
        content = f.read()

    new_methods = """
    def save_runtime_profiles(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_RUNTIME.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_RUNTIME / f"runtime_profiles_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_runtime_profiles(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_RUNTIME.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_memory_profiles(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_MEMORY.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_MEMORY / f"memory_profiles_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_memory_profiles(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_MEMORY.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_cpu_gpu_awareness(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_CPU_GPU.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CPU_GPU / f"cpu_gpu_awareness_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_cpu_gpu_awareness(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_CPU_GPU.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_resource_budgets(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_BUDGET.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_BUDGET / f"resource_budgets_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_resource_budgets(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_BUDGET.glob("resource_budgets_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_resource_budget_violations(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_BUDGET.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_BUDGET / f"violations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_resource_budget_violations(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_BUDGET.glob("violations_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_cache_inventory(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_CACHE.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CACHE / f"inventory_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_cache_inventory(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_CACHE.glob("inventory_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_cache_strategy(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_CACHE.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CACHE / f"strategy_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_cache_strategy(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_CACHE.glob("strategy_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_cache_hit_miss_report(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_CACHE.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CACHE / f"hit_miss_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_cache_hit_miss_report(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_CACHE.glob("hit_miss_*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_batch_plans(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_BATCH_PLANS.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_BATCH_PLANS / f"batch_plans_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_batch_plans(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_BATCH_PLANS.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_checkpoint_manifest(self, manifest_name: str, manifest: dict) -> Path:
        self.paths.LAKE_PERFORMANCE_CHECKPOINTS.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_CHECKPOINTS / f"{manifest_name}.json"
        import json
        with open(path, "w") as f:
            json.dump(manifest, f)
        return path

    def load_checkpoint_manifest(self, manifest_name: str) -> dict:
        path = self.paths.LAKE_PERFORMANCE_CHECKPOINTS / f"{manifest_name}.json"
        if not path.exists(): return {}
        import json
        with open(path, "r") as f:
            return json.load(f)

    def save_large_run_stability_report(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_STABILITY.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_STABILITY / f"stability_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_large_run_stability_report(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_STABILITY.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_bottleneck_report(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_BOTTLENECKS.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_BOTTLENECKS / f"bottleneck_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_bottleneck_report(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_BOTTLENECKS.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_optimization_recommendations(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        self.paths.LAKE_PERFORMANCE_OPTIMIZATION.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_OPTIMIZATION / f"optimization_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(path, index=False)
        return path

    def load_optimization_recommendations(self) -> pd.DataFrame:
        files = list(self.paths.LAKE_PERFORMANCE_OPTIMIZATION.glob("*.csv"))
        if not files: return pd.DataFrame()
        latest = max(files, key=os.path.getctime)
        return pd.read_csv(latest)

    def save_performance_quality(self, profile_name: str, quality: dict) -> Path:
        self.paths.LAKE_PERFORMANCE_QUALITY.mkdir(parents=True, exist_ok=True)
        path = self.paths.LAKE_PERFORMANCE_QUALITY / f"{profile_name}_quality_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        import json
        with open(path, "w") as f:
            json.dump(quality, f)
        return path

    def load_performance_quality(self, profile_name: str) -> dict:
        files = list(self.paths.LAKE_PERFORMANCE_QUALITY.glob(f"{profile_name}_quality_*.json"))
        if not files: return {}
        latest = max(files, key=os.path.getctime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def save_performance_report(self, profile_name: str, report: dict, markdown: Optional[str] = None) -> Path:
        self.paths.REPORTS_PERFORMANCE_JSON.mkdir(parents=True, exist_ok=True)
        path = self.paths.REPORTS_PERFORMANCE_JSON / f"{profile_name}_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        import json
        with open(path, "w") as f:
            json.dump(report, f)

        if markdown:
            self.paths.REPORTS_PERFORMANCE_MARKDOWN.mkdir(parents=True, exist_ok=True)
            md_path = self.paths.REPORTS_PERFORMANCE_MARKDOWN / f"{profile_name}_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            with open(md_path, "w") as f:
                f.write(markdown)

        return path

    def load_performance_report(self, profile_name: str) -> dict:
        files = list(self.paths.REPORTS_PERFORMANCE_JSON.glob(f"{profile_name}_report_*.json"))
        if not files: return {}
        latest = max(files, key=os.path.getctime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def list_performance_reports(self) -> pd.DataFrame:
        files = list(self.paths.REPORTS_PERFORMANCE_JSON.glob("*.json"))
        if not files: return pd.DataFrame()
        records = []
        for f in files:
            records.append({
                "name": f.stem,
                "path": str(f),
                "created_at": datetime.fromtimestamp(os.path.getctime(f)).isoformat()
            })
        return pd.DataFrame(records)
"""

    if "def save_runtime_profiles" not in content:
        # Find the end of the class
        content += new_methods
        with open(path, "w") as f:
            f.write(content)

patch_file()
