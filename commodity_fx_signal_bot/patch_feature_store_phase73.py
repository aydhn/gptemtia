import os

with open("ml/feature_store.py", "r", encoding="utf-8") as f:
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
    def load_{m}(self) -> pd.DataFrame:
        return self.data_lake.load_{m}()
'''

for m in pack_methods:
    code += f'''
    def load_{m}(self) -> str:
        return self.data_lake.load_{m}()
'''

code += '''
    def load_training_quality(self, profile_name: str | None = None) -> dict:
        if profile_name is None: profile_name = "balanced_local_training"
        return self.data_lake.load_training_quality(profile_name)

    def load_local_training_report(self, profile_name: str | None = None) -> dict:
        if profile_name is None: profile_name = "balanced_local_training"
        return self.data_lake.load_local_training_report(profile_name)

    def list_available_local_training_reports(self) -> dict:
        return {"reports": self.data_lake.list_local_training_reports().to_dict(orient="records")}
'''

content = content.replace("feature_store = FeatureStore(data_lake)", code + "\n\nfeature_store = FeatureStore(data_lake)")

with open("ml/feature_store.py", "w", encoding="utf-8") as f:
    f.write(content)
