import os

path = "commodity_fx_signal_bot/data/storage/data_lake.py"
with open(path, "r") as f:
    content = f.read()

new_methods = """

    # Phase 47 Governance Methods
    def save_artifact_inventory(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.governance_dir / "inventory" / "artifact_inventory.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_artifact_inventory(self) -> pd.DataFrame:
        p = self.governance_dir / "inventory" / "artifact_inventory.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_artifact_fingerprints(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.governance_dir / "fingerprints" / "artifact_fingerprints.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_artifact_fingerprints(self) -> pd.DataFrame:
        p = self.governance_dir / "fingerprints" / "artifact_fingerprints.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_provenance_records(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.governance_dir / "provenance" / "provenance_records.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_provenance_records(self) -> pd.DataFrame:
        p = self.governance_dir / "provenance" / "provenance_records.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_lineage_nodes(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.governance_dir / "lineage" / "lineage_nodes.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_lineage_nodes(self) -> pd.DataFrame:
        p = self.governance_dir / "lineage" / "lineage_nodes.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_lineage_edges(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.governance_dir / "lineage" / "lineage_edges.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_lineage_edges(self) -> pd.DataFrame:
        p = self.governance_dir / "lineage" / "lineage_edges.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_dependency_trace(self, trace_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.governance_dir / "dependencies" / f"{trace_name}_trace.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_dependency_trace(self, trace_name: str) -> pd.DataFrame:
        p = self.governance_dir / "dependencies" / f"{trace_name}_trace.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_audit_trail(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.governance_dir / "audit" / "audit_trail.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_audit_trail(self) -> pd.DataFrame:
        p = self.governance_dir / "audit" / "audit_trail.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_source_attribution(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.governance_dir / "source_attribution" / "source_attribution.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_source_attribution(self) -> pd.DataFrame:
        p = self.governance_dir / "source_attribution" / "source_attribution.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_governance_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        p = self.governance_dir / "checklists" / "governance_checklist.parquet"
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(p, index=False)
        return p

    def load_governance_checklist(self) -> pd.DataFrame:
        p = self.governance_dir / "checklists" / "governance_checklist.parquet"
        if not p.exists(): return pd.DataFrame()
        return pd.read_parquet(p)

    def save_governance_quality(self, profile_name: str, quality: dict) -> Path:
        import json
        p = self.governance_dir / "quality" / f"{profile_name}_quality.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w") as f:
            json.dump(quality, f, indent=2)
        return p

    def load_governance_quality(self, profile_name: str) -> dict:
        import json
        p = self.governance_dir / "quality" / f"{profile_name}_quality.json"
        if not p.exists(): return {}
        with open(p, "r") as f:
            return json.load(f)

    def save_research_governance_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        import json
        p = self.governance_dir / f"{profile_name}_report.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w") as f:
            json.dump(report, f, indent=2)
        return p

    def load_research_governance_report(self, profile_name: str) -> dict:
        import json
        p = self.governance_dir / f"{profile_name}_report.json"
        if not p.exists(): return {}
        with open(p, "r") as f:
            return json.load(f)

    def list_governance_reports(self) -> pd.DataFrame:
        reports = []
        for p in self.governance_dir.glob("*_report.json"):
            reports.append({"report_name": p.stem, "path": str(p)})
        return pd.DataFrame(reports)

"""

if "save_artifact_inventory" not in content:
    content = content.replace("class DataLake:", "class DataLake:\n" + new_methods)
    with open(path, "w") as f:
        f.write(content)

    print("Added governance methods to DataLake")
else:
    print("Methods already exist in DataLake")
