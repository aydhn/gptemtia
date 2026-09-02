import re
import os

with open("data/storage/data_lake.py", "r", encoding="utf-8") as f:
    content = f.read()

methods = [
    "training_domain_registry",
    "role_based_onboarding_paths",
    "guided_walkthrough_registry",
    "local_walkthrough_lessons",
    "safe_command_lesson_registry",
    "report_reading_lesson_registry",
    "datalake_reading_lesson_registry",
    "cross_layer_lesson_registry",
    "troubleshooting_lesson_registry",
    "glossary_registry",
    "concept_map_registry",
    "faq_registry",
    "first_week_operator_curriculum",
    "knowledge_transfer_checklist",
    "training_gap_register",
    "training_risk_summary",
    "training_assessment_dry_run",
    "training_validation_report"
]

pack_methods = [
    "operator_training_pack",
    "analyst_training_pack",
    "developer_training_pack",
    "safe_usage_training_pack",
    "non_use_policy_training_pack",
    "handover_education_binder"
]

code = "\n"
for m in methods:
    code += f'''
    def save_{m}(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        dir_name = "{m.replace('_registry', '').replace('_lessons', '')}"
        path = LAKE_LOCAL_TRAINING_DIR / dir_name / "{m}.parquet"
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False)
        return path

    def load_{m}(self) -> pd.DataFrame:
        dir_name = "{m.replace('_registry', '').replace('_lessons', '')}"
        path = LAKE_LOCAL_TRAINING_DIR / dir_name / "{m}.parquet"
        if not path.exists():
            return pd.DataFrame()
        return pd.read_parquet(path)
'''

for m in pack_methods:
    code += f'''
    def save_{m}(self, text: str, summary: dict | None = None) -> Path:
        path = LAKE_LOCAL_TRAINING_DIR / "packs" / "{m}.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return path

    def load_{m}(self) -> str:
        path = LAKE_LOCAL_TRAINING_DIR / "packs" / "{m}.txt"
        if not path.exists():
            return ""
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
'''

code += '''
    def save_training_quality(self, profile_name: str, quality: dict) -> Path:
        path = LAKE_LOCAL_TRAINING_QUALITY_DIR / f"{profile_name}_quality.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=4)
        return path

    def load_training_quality(self, profile_name: str) -> dict:
        path = LAKE_LOCAL_TRAINING_QUALITY_DIR / f"{profile_name}_quality.json"
        if not path.exists():
            return {}
        import json
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_local_training_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        path = LAKE_LOCAL_TRAINING_REPORTS_DIR / f"{profile_name}_report.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        return path

    def load_local_training_report(self, profile_name: str) -> dict:
        path = LAKE_LOCAL_TRAINING_REPORTS_DIR / f"{profile_name}_report.json"
        if not path.exists():
            return {}
        import json
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_local_training_reports(self) -> pd.DataFrame:
        if not LAKE_LOCAL_TRAINING_REPORTS_DIR.exists():
            return pd.DataFrame()
        files = list(LAKE_LOCAL_TRAINING_REPORTS_DIR.glob("*_report.json"))
        return pd.DataFrame([{"report_file": f.name} for f in files])
'''

content = content.replace("data_lake = DataLake()", code + "\n\ndata_lake = DataLake()")

with open("data/storage/data_lake.py", "w", encoding="utf-8") as f:
    f.write(content)
