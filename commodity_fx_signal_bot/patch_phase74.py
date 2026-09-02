import os
import re

def patch_file(path, search, replace):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if search in content:
        content = content.replace(search, replace)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

# Patch settings.py
with open("config/settings.py", "r", encoding="utf-8") as f:
    if "local_briefing_enabled" not in f.read():
        patch_file("config/settings.py",
            "class Settings(BaseSettings):",
            """class Settings(BaseSettings):
    local_briefing_enabled: bool = True
    default_local_briefing_profile: str = "balanced_local_briefing"
    local_briefing_default_language: str = "tr"
    local_briefing_dry_run_default: bool = True
    local_briefing_allow_investment_advice: bool = False
    local_briefing_allow_live_trading_claim: bool = False
    local_briefing_allow_broker_readiness_claim: bool = False
    local_briefing_allow_production_release_claim: bool = False
    local_briefing_allow_model_deployment_claim: bool = False
    local_briefing_allow_official_board_decision_claim: bool = False
    local_briefing_allow_cloud_upload: bool = False
    local_briefing_allow_external_service: bool = False
    local_briefing_allow_external_llm: bool = False
    local_briefing_allow_file_modification: bool = False
    local_briefing_allow_file_deletion: bool = False
    local_briefing_allow_file_move: bool = False
    local_briefing_allow_overwrite: bool = False
    local_briefing_scan_docs: bool = True
    local_briefing_scan_reports: bool = True
    local_briefing_scan_data_lake: bool = True
    local_briefing_scan_cross_layer_outputs: bool = True
    local_briefing_scan_training_outputs: bool = True
    local_briefing_max_sections: int = 5000
    local_briefing_max_slide_items: int = 200
    local_briefing_min_quality_score: float = 0.40
    local_briefing_save_reports: bool = True
""")

# Patch data_lake.py
with open("data/storage/data_lake.py", "r", encoding="utf-8") as f:
    if "save_communication_profile_registry" not in f.read():
        patch_file("data/storage/data_lake.py",
            "class DataLake:",
            """class DataLake:
    def save_communication_profile_registry(self, df, summary=None): pass
    def load_communication_profile_registry(self): return pd.DataFrame()
    def save_stakeholder_audience_registry(self, df, summary=None): pass
    def load_stakeholder_audience_registry(self): return pd.DataFrame()
    def save_executive_summary_pack(self, text, summary=None): pass
    def load_executive_summary_pack(self): return ""
    def save_project_one_pager(self, text, summary=None): pass
    def load_project_one_pager(self): return ""
    def save_non_technical_briefing_deck_source(self, df, summary=None): pass
    def load_non_technical_briefing_deck_source(self): return pd.DataFrame()
    def save_project_narrative_report(self, text, summary=None): pass
    def load_project_narrative_report(self): return ""
    def save_decision_context_binder(self, text, summary=None): pass
    def load_decision_context_binder(self): return ""
    def save_capability_map_nontechnical(self, df, summary=None): pass
    def load_capability_map_nontechnical(self): return pd.DataFrame()
    def save_boundary_non_use_summary(self, text, summary=None): pass
    def load_boundary_non_use_summary(self): return ""
    def save_risk_limitation_narrative(self, text, summary=None): pass
    def load_risk_limitation_narrative(self): return ""
    def save_milestone_narrative(self, text, summary=None): pass
    def load_milestone_narrative(self): return ""
    def save_phase_evolution_narrative(self, text, summary=None): pass
    def load_phase_evolution_narrative(self): return ""
    def save_local_only_architecture_narrative(self, text, summary=None): pass
    def load_local_only_architecture_narrative(self): return ""
    def save_stakeholder_faq_registry(self, df, summary=None): pass
    def load_stakeholder_faq_registry(self): return pd.DataFrame()
    def save_executive_glossary_registry(self, df, summary=None): pass
    def load_executive_glossary_registry(self): return pd.DataFrame()
    def save_safe_communication_guide(self, text, summary=None): pass
    def load_safe_communication_guide(self): return ""
    def save_communication_do_dont_registry(self, df, summary=None): pass
    def load_communication_do_dont_registry(self): return pd.DataFrame()
    def save_decision_question_registry(self, df, summary=None): pass
    def load_decision_question_registry(self): return pd.DataFrame()
    def save_decision_context_matrix(self, df, summary=None): pass
    def load_decision_context_matrix(self): return pd.DataFrame()
    def save_stakeholder_update_templates(self, df, summary=None): pass
    def load_stakeholder_update_templates(self): return pd.DataFrame()
    def save_communication_gap_register(self, df, summary=None): pass
    def load_communication_gap_register(self): return pd.DataFrame()
    def save_communication_risk_summary(self, df, summary=None): pass
    def load_communication_risk_summary(self): return pd.DataFrame()
    def save_briefing_validation_report(self, df, summary=None): pass
    def load_briefing_validation_report(self): return pd.DataFrame()
    def save_briefing_quality(self, profile_name, quality): pass
    def load_briefing_quality(self, profile_name): return {}
    def save_local_briefing_report(self, profile_name, report, markdown=None): pass
    def load_local_briefing_report(self, profile_name): return {}
    def list_local_briefing_reports(self): return pd.DataFrame()
""")
