import re

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

maintenance_methods = """
    # --- MAINTENANCE SUPPORT ---
    def save_storage_inventory(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_INVENTORY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "inventory")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"storage_inventory_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_inventory(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_INVENTORY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "inventory")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_retention_policies(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_POLICIES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "policies")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"retention_policies_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_retention_policies(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_POLICIES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "policies")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cleanup_candidates(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cleanup_candidates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cleanup_candidates(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cleanup_candidates_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cleanup_dry_run_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cleanup_plan_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cleanup_dry_run_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_CLEANUP_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "cleanup")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cleanup_plan_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_archive_candidates(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"archive_candidates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_archive_candidates(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("archive_candidates_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_archive_manifest(self, archive_id: str, manifest: dict) -> Path:
        out_dir = getattr(self.paths, "ARCHIVES_MANIFESTS_DIR", self.paths.PROJECT_ROOT / "archives" / "manifests")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"{archive_id}.json"
        with open(path, "w") as f:
            json.dump(manifest, f, indent=2)
        return path

    def load_archive_manifest(self, archive_id: str) -> dict:
        import json
        out_dir = getattr(self.paths, "ARCHIVES_MANIFESTS_DIR", self.paths.PROJECT_ROOT / "archives" / "manifests")
        path = out_dir / f"{archive_id}.json"
        if not path.exists():
            return {}
        with open(path, "r") as f:
            return json.load(f)

    def save_archive_dry_run_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"archive_plan_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_archive_dry_run_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ARCHIVE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "archive")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("archive_plan_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_report_rotation_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"report_rotation_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_report_rotation_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("report_rotation_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_log_rotation_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"log_rotation_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_log_rotation_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("log_rotation_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_cache_pruning_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"cache_pruning_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_cache_pruning_plan(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_ROTATION_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "rotation")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("cache_pruning_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_duplicate_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_DUPLICATES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "duplicates")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"duplicates_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_duplicate_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_DUPLICATES_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "duplicates")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_stale_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_STALE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "stale")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"stale_artifacts_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_stale_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_STALE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "stale")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_large_artifact_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_LARGE_ARTIFACTS_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "large_artifacts")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"large_artifacts_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_large_artifact_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_LARGE_ARTIFACTS_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "large_artifacts")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_storage_growth_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"storage_growth_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_growth_report(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("storage_growth_*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_storage_growth_snapshot(self, snapshot: dict) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"snapshot_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(snapshot, f)
        return path

    def load_storage_growth_snapshots(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_GROWTH_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "growth")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("snapshot_*.json"))
        if not files:
            return pd.DataFrame()
        import json
        data = []
        for f in files:
            with open(f, "r") as fp:
                data.append(json.load(fp))
        return pd.DataFrame(data)

    def save_storage_lifecycle_health(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_LIFECYCLE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "lifecycle")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"lifecycle_health_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        df.to_parquet(path)
        return path

    def load_storage_lifecycle_health(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "MAINTENANCE_LIFECYCLE_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "lifecycle")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        latest = max(files, key=lambda f: f.stat().st_mtime)
        return pd.read_parquet(latest)

    def save_maintenance_quality(self, profile_name: str, quality: dict) -> Path:
        out_dir = getattr(self.paths, "MAINTENANCE_QUALITY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "quality")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"quality_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(quality, f, indent=2)
        return path

    def load_maintenance_quality(self, profile_name: str) -> dict:
        out_dir = getattr(self.paths, "MAINTENANCE_QUALITY_DIR", self.paths.DATA_LAKE_DIR / "maintenance" / "quality")
        if not out_dir.exists():
            return {}
        files = list(out_dir.glob(f"quality_{profile_name}_*.json"))
        if not files:
            return {}
        latest = max(files, key=lambda f: f.stat().st_mtime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def save_maintenance_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        out_dir.mkdir(parents=True, exist_ok=True)
        import json
        path = out_dir / f"maintenance_report_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(path, "w") as f:
            json.dump(report, f, indent=2)

        if markdown:
            md_dir = getattr(self.paths, "REPORTS_MAINTENANCE_MARKDOWN_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "markdown")
            md_dir.mkdir(parents=True, exist_ok=True)
            md_path = md_dir / f"maintenance_report_{profile_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.md"
            with open(md_path, "w") as f:
                f.write(markdown)

        return path

    def load_maintenance_report(self, profile_name: str) -> dict:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        if not out_dir.exists():
            return {}
        files = list(out_dir.glob(f"maintenance_report_{profile_name}_*.json"))
        if not files:
            return {}
        latest = max(files, key=lambda f: f.stat().st_mtime)
        import json
        with open(latest, "r") as f:
            return json.load(f)

    def list_maintenance_reports(self) -> pd.DataFrame:
        out_dir = getattr(self.paths, "REPORTS_MAINTENANCE_JSON_DIR", self.paths.REPORTS_OUTPUT_DIR / "maintenance" / "json")
        if not out_dir.exists():
            return pd.DataFrame()
        files = list(out_dir.glob("*.json"))
        records = []
        for f in files:
            records.append({
                "file_name": f.name,
                "modified_at": datetime.fromtimestamp(f.stat().st_mtime).isoformat()
            })
        return pd.DataFrame(records)
"""

if "def save_storage_inventory" not in content:
    # Just append to the class at the end
    content = re.sub(r'(\s*)$', r'\n\n' + maintenance_methods, content)
    with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
        f.write(content)
    print("data_lake.py patched")
else:
    print("data_lake.py already patched")
