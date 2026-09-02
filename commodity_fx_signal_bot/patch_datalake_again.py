import os

with open("data/storage/data_lake.py", "a", encoding="utf-8") as f:
    f.write('''

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

code = "\\n"
for m in methods:
    code += f"""
    def save_{m}(self, df: pd.DataFrame, summary: dict | None = None):
        dir_name = \\"{m.replace('_registry', '').replace('_lessons', '')}\\"
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / dir_name / \\"{m}.parquet\\"
        self._save_parquet(df, path)
        return path

    def load_{m}(self) -> pd.DataFrame:
        dir_name = \\"{m.replace('_registry', '').replace('_lessons', '')}\\"
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / dir_name / \\"{m}.parquet\\"
        return self._load_parquet(path)
"""

for m in pack_methods:
    code += f"""
    def save_{m}(self, text: str, summary: dict | None = None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / \\"packs\\" / \\"{m}.txt\\"
        self._save_text(text, path)
        return path

    def load_{m}(self) -> str:
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / \\"packs\\" / \\"{m}.txt\\"
        return self._load_text(path)
"""

code += """
    def save_training_quality(self, profile_name: str, quality: dict):
        path = self.paths.LAKE_LOCAL_TRAINING_QUALITY_DIR / f"{profile_name}_quality.json"
        self._save_json(quality, path)
        return path

    def load_training_quality(self, profile_name: str) -> dict:
        path = self.paths.LAKE_LOCAL_TRAINING_QUALITY_DIR / f"{profile_name}_quality.json"
        return self._load_json(path)

    def save_local_training_report(self, profile_name: str, report: dict, markdown: str | None = None):
        path = self.paths.LAKE_LOCAL_TRAINING_REPORTS_DIR / f"{profile_name}_report.json"
        self._save_json(report, path)
        return path

    def load_local_training_report(self, profile_name: str) -> dict:
        path = self.paths.LAKE_LOCAL_TRAINING_REPORTS_DIR / f"{profile_name}_report.json"
        return self._load_json(path)

    def list_local_training_reports(self) -> pd.DataFrame:
        if not self.paths.LAKE_LOCAL_TRAINING_REPORTS_DIR.exists():
            return pd.DataFrame()
        files = list(self.paths.LAKE_LOCAL_TRAINING_REPORTS_DIR.glob("*_report.json"))
        return pd.DataFrame([{"report_file": f.name} for f in files])
"""

import sys
sys.modules['__main__'].__dict__['code'] = code

with open("data/storage/data_lake.py", "r", encoding="utf-8") as file:
    content = file.read()
    
# We want to add these methods inside DataLake class. I'll just append them since the whole file is just that class mostly.
content += code

with open("data/storage/data_lake.py", "w", encoding="utf-8") as file:
    file.write(content)

'''
