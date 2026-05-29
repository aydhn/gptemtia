import re

def update_datalake():
    with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'r') as f:
        content = f.read()

    if "save_scenario_regression_registry" in content:
        print("Already updated datalake")
        return

    insert_idx = content.find("def save_scenario_registry(")

    new_dl = """
    def save_scenario_regression_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_REGISTRY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_REGISTRY_DIR / "regression_registry.csv"
        LAKE_SCENARIO_REGRESSION_REGISTRY_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_scenario_regression_registry(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_REGISTRY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_REGISTRY_DIR / "regression_registry.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_golden_outputs(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR / "golden_outputs.csv"
        LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_golden_outputs(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR / "golden_outputs.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_golden_output_manifest(self, manifest: dict) -> Path:
        import json
        from config.paths import LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR / "golden_output_manifest.json"
        LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        if manifest:
            with open(file_path, 'w') as f:
                json.dump(manifest, f, indent=2)
        return file_path

    def load_golden_output_manifest(self) -> dict:
        import json
        from config.paths import LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR / "golden_output_manifest.json"
        if file_path.exists():
            with open(file_path, 'r') as f:
                return json.load(f)
        return {}

    def save_snapshot_manifest(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR / "snapshot_manifest.csv"
        LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_snapshot_manifest(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR / "snapshot_manifest.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_snapshot_diff_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR / "snapshot_diff_report.csv"
        LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_snapshot_diff_report(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR / "snapshot_diff_report.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_deterministic_replay_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_REPLAY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_REPLAY_DIR / "deterministic_replay_report.csv"
        LAKE_SCENARIO_REGRESSION_REPLAY_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_deterministic_replay_report(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_REPLAY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_REPLAY_DIR / "deterministic_replay_report.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_fixture_reproducibility_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR / "fixture_reproducibility_report.csv"
        LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_fixture_reproducibility_report(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR / "fixture_reproducibility_report.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_scenario_output_contract_validation(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR / "scenario_output_contract_validation.csv"
        LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_scenario_output_contract_validation(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR / "scenario_output_contract_validation.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_demo_workflow_regression_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR / "demo_workflow_regression_report.csv"
        LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_demo_workflow_regression_report(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR / "demo_workflow_regression_report.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_end_to_end_demo_acceptance(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR
        file_path = LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR / "end_to_end_demo_acceptance.csv"
        LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_end_to_end_demo_acceptance(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR
        file_path = LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR / "end_to_end_demo_acceptance.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_scenario_drift_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_DRIFT_DIR
        file_path = LAKE_SCENARIO_REGRESSION_DRIFT_DIR / "scenario_drift_report.csv"
        LAKE_SCENARIO_REGRESSION_DRIFT_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_scenario_drift_report(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_DRIFT_DIR
        file_path = LAKE_SCENARIO_REGRESSION_DRIFT_DIR / "scenario_drift_report.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_regression_failure_register(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_FAILURES_DIR
        file_path = LAKE_SCENARIO_REGRESSION_FAILURES_DIR / "regression_failure_register.csv"
        LAKE_SCENARIO_REGRESSION_FAILURES_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_regression_failure_register(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_FAILURES_DIR
        file_path = LAKE_SCENARIO_REGRESSION_FAILURES_DIR / "regression_failure_register.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_regression_acceptance_checklist(self, df: pd.DataFrame, summary: dict = None) -> Path:
        from config.paths import LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR / "regression_acceptance_checklist.csv"
        LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR.mkdir(parents=True, exist_ok=True)
        if df is not None and not df.empty:
            df.to_csv(file_path, index=False)
        return file_path

    def load_regression_acceptance_checklist(self) -> pd.DataFrame:
        from config.paths import LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR
        file_path = LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR / "regression_acceptance_checklist.csv"
        if file_path.exists():
            return pd.read_csv(file_path)
        return pd.DataFrame()

    def save_scenario_regression_quality(self, profile_name: str, quality: dict) -> Path:
        import json
        from config.paths import LAKE_SCENARIO_REGRESSION_QUALITY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_QUALITY_DIR / f"quality_{profile_name}.json"
        LAKE_SCENARIO_REGRESSION_QUALITY_DIR.mkdir(parents=True, exist_ok=True)
        if quality:
            with open(file_path, 'w') as f:
                json.dump(quality, f, indent=2)
        return file_path

    def load_scenario_regression_quality(self, profile_name: str) -> dict:
        import json
        from config.paths import LAKE_SCENARIO_REGRESSION_QUALITY_DIR
        file_path = LAKE_SCENARIO_REGRESSION_QUALITY_DIR / f"quality_{profile_name}.json"
        if file_path.exists():
            with open(file_path, 'r') as f:
                return json.load(f)
        return {}

    def save_scenario_regression_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        import json
        from config.paths import REPORTS_SCENARIO_REGRESSION_JSON_DIR, REPORTS_SCENARIO_REGRESSION_MARKDOWN_DIR

        REPORTS_SCENARIO_REGRESSION_JSON_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_SCENARIO_REGRESSION_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)

        json_path = REPORTS_SCENARIO_REGRESSION_JSON_DIR / f"report_{profile_name}.json"
        with open(json_path, 'w') as f:
            json.dump(report, f, indent=2)

        if markdown:
            md_path = REPORTS_SCENARIO_REGRESSION_MARKDOWN_DIR / f"{profile_name}.md"
            with open(md_path, 'w') as f:
                f.write(markdown)

        return json_path

    def load_scenario_regression_report(self, profile_name: str) -> dict:
        import json
        from config.paths import REPORTS_SCENARIO_REGRESSION_JSON_DIR
        file_path = REPORTS_SCENARIO_REGRESSION_JSON_DIR / f"report_{profile_name}.json"
        if file_path.exists():
            with open(file_path, 'r') as f:
                return json.load(f)
        return {}

    def list_scenario_regression_reports(self) -> pd.DataFrame:
        from config.paths import REPORTS_SCENARIO_REGRESSION_JSON_DIR
        if not REPORTS_SCENARIO_REGRESSION_JSON_DIR.exists():
            return pd.DataFrame()

        reports = []
        for file in REPORTS_SCENARIO_REGRESSION_JSON_DIR.glob("*.json"):
            reports.append({
                "profile_name": file.stem.replace("report_", ""),
                "path": str(file)
            })
        return pd.DataFrame(reports)

"""
    content = content[:insert_idx] + new_dl + content[insert_idx:]
    with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'w') as f:
        f.write(content)

def update_featurestore():
    with open('commodity_fx_signal_bot/ml/feature_store.py', 'r') as f:
        content = f.read()

    if "load_scenario_regression_registry" in content:
        print("Already updated featurestore")
        return

    insert_idx = content.find("def load_scenario_registry(")

    new_fs = """
    def load_scenario_regression_registry(self) -> pd.DataFrame:
        return self.data_lake.load_scenario_regression_registry()

    def load_golden_outputs(self) -> pd.DataFrame:
        return self.data_lake.load_golden_outputs()

    def load_golden_output_manifest(self) -> dict:
        return self.data_lake.load_golden_output_manifest()

    def load_snapshot_manifest(self) -> pd.DataFrame:
        return self.data_lake.load_snapshot_manifest()

    def load_snapshot_diff_report(self) -> pd.DataFrame:
        return self.data_lake.load_snapshot_diff_report()

    def load_deterministic_replay_report(self) -> pd.DataFrame:
        return self.data_lake.load_deterministic_replay_report()

    def load_fixture_reproducibility_report(self) -> pd.DataFrame:
        return self.data_lake.load_fixture_reproducibility_report()

    def load_scenario_output_contract_validation(self) -> pd.DataFrame:
        return self.data_lake.load_scenario_output_contract_validation()

    def load_demo_workflow_regression_report(self) -> pd.DataFrame:
        return self.data_lake.load_demo_workflow_regression_report()

    def load_end_to_end_demo_acceptance(self) -> pd.DataFrame:
        return self.data_lake.load_end_to_end_demo_acceptance()

    def load_scenario_drift_report(self) -> pd.DataFrame:
        return self.data_lake.load_scenario_drift_report()

    def load_regression_failure_register(self) -> pd.DataFrame:
        return self.data_lake.load_regression_failure_register()

    def load_regression_acceptance_checklist(self) -> pd.DataFrame:
        return self.data_lake.load_regression_acceptance_checklist()

    def load_scenario_regression_quality(self, profile_name: str | None = None) -> dict:
        if profile_name is None:
            from config.settings import settings
            profile_name = settings.default_scenario_regression_profile
        return self.data_lake.load_scenario_regression_quality(profile_name)

    def load_scenario_regression_report(self, profile_name: str | None = None) -> dict:
        if profile_name is None:
            from config.settings import settings
            profile_name = settings.default_scenario_regression_profile
        return self.data_lake.load_scenario_regression_report(profile_name)

    def list_available_scenario_regression_reports(self) -> dict:
        df = self.data_lake.list_scenario_regression_reports()
        if df.empty:
            return {"reports": []}
        return {"reports": df.to_dict(orient="records")}

"""
    content = content[:insert_idx] + new_fs + content[insert_idx:]
    with open('commodity_fx_signal_bot/ml/feature_store.py', 'w') as f:
        f.write(content)

def update_reportbuilder():
    with open('commodity_fx_signal_bot/reports/report_builder.py', 'r') as f:
        content = f.read()

    if "build_scenario_regression_registry_text_report" in content:
        print("Already updated reportbuilder")
        return

    insert_idx = content.find("def build_universe_report(")

    new_rb = """
def _get_regression_disclaimer_rb() -> str:
    return (
        "*** WARNING / UYARI ***\\n"
        "Bu çıktı offline scenario regression/deterministic replay raporudur. "
        "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        "otomatik trade onayı veya yatırım tavsiyesi değildir.\\n"
        "***\\n\\n"
    )

def build_scenario_regression_registry_text_report(summary: dict, regression_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Scenario Regression Registry Report\\n\\n"
    txt += f"Total definitions: {summary.get('total_definitions', 0)}\\n\\n"
    if regression_df is not None and not regression_df.empty:
        txt += regression_df.head(10).to_string() + "\\n"
    return txt

def build_golden_output_text_report(summary: dict, golden_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Golden Output Report\\n\\n"
    txt += f"Total golden outputs: {summary.get('total_golden_outputs', 0)}\\n\\n"
    if golden_df is not None and not golden_df.empty:
        txt += golden_df.head(10).to_string() + "\\n"
    return txt

def build_snapshot_comparison_text_report(summary: dict, diff_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Snapshot Comparison Report\\n\\n"
    txt += f"Total diffs: {summary.get('total_diffs', 0)}\\n\\n"
    if diff_df is not None and not diff_df.empty:
        txt += diff_df.head(10).to_string() + "\\n"
    return txt

def build_deterministic_replay_text_report(summary: dict, replay_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Deterministic Replay Report\\n\\n"
    txt += f"Total replays: {summary.get('total_replays', 0)}\\n\\n"
    if replay_df is not None and not replay_df.empty:
        txt += replay_df.head(10).to_string() + "\\n"
    return txt

def build_demo_acceptance_text_report(summary: dict, acceptance_df: pd.DataFrame | None = None) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Demo Acceptance Report\\n\\n"
    txt += f"Score: {summary.get('score', 0)}\\n"
    txt += f"Label: {summary.get('label', 'unknown')}\\n\\n"
    if acceptance_df is not None and not acceptance_df.empty:
        txt += acceptance_df.to_string() + "\\n"
    return txt

def build_scenario_regression_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    txt = _get_regression_disclaimer_rb()
    txt += "Scenario Regression Status\\n\\n"
    if status_df is not None and not status_df.empty:
        txt += status_df.to_string() + "\\n"
    return txt

"""
    content = content[:insert_idx] + new_rb + content[insert_idx:]
    with open('commodity_fx_signal_bot/reports/report_builder.py', 'w') as f:
        f.write(content)

update_datalake()
update_featurestore()
update_reportbuilder()
