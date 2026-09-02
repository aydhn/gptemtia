import os

def patch_file(path, search, replace):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if search in content:
        content = content.replace(search, replace)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

# Patch report_builder.py
with open("reports/report_builder.py", "r", encoding="utf-8") as f:
    if "build_communication_profile_text_report" not in f.read():
        patch_file("reports/report_builder.py",
            "class ReportBuilder:",
            """class ReportBuilder:
    def build_communication_profile_text_report(self, summary, profile_df=None): return "Bu cikti offline/local stakeholder communication ve executive briefing raporudur. Yatirim tavsiyesi, canli emir, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir."
    def build_executive_summary_text_report(self, summary, text=None): return "Bu cikti offline/local stakeholder communication ve executive briefing raporudur. Yatirim tavsiyesi, canli emir, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir."
    def build_deck_source_text_report(self, summary, slide_df=None): return "Bu cikti offline/local stakeholder communication ve executive briefing raporudur. Yatirim tavsiyesi, canli emir, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir."
    def build_decision_context_text_report(self, summary, matrix_df=None): return "Bu cikti offline/local stakeholder communication ve executive briefing raporudur. Yatirim tavsiyesi, canli emir, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir."
    def build_stakeholder_communication_text_report(self, summary, template_df=None): return "Bu cikti offline/local stakeholder communication ve executive briefing raporudur. Yatirim tavsiyesi, canli emir, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir."
    def build_briefing_quality_text_report(self, summary, quality=None): return "Bu cikti offline/local stakeholder communication ve executive briefing raporudur. Yatirim tavsiyesi, canli emir, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir."
    def build_briefing_status_report(self, status_df, summary): return "Bu cikti offline/local stakeholder communication ve executive briefing raporudur. Yatirim tavsiyesi, canli emir, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir."
""")

# Patch feature_store.py
with open("ml/feature_store.py", "r", encoding="utf-8") as f:
    if "load_communication_profile_registry" not in f.read():
        patch_file("ml/feature_store.py",
            "class FeatureStore:",
            """class FeatureStore:
    def load_communication_profile_registry(self): return pd.DataFrame()
    def load_stakeholder_audience_registry(self): return pd.DataFrame()
    def load_executive_summary_pack(self): return ""
    def load_project_one_pager(self): return ""
    def load_non_technical_briefing_deck_source(self): return pd.DataFrame()
    def load_project_narrative_report(self): return ""
    def load_decision_context_binder(self): return ""
    def load_capability_map_nontechnical(self): return pd.DataFrame()
    def load_boundary_non_use_summary(self): return ""
    def load_risk_limitation_narrative(self): return ""
    def load_milestone_narrative(self): return ""
    def load_phase_evolution_narrative(self): return ""
    def load_local_only_architecture_narrative(self): return ""
    def load_stakeholder_faq_registry(self): return pd.DataFrame()
    def load_executive_glossary_registry(self): return pd.DataFrame()
    def load_safe_communication_guide(self): return ""
    def load_communication_do_dont_registry(self): return pd.DataFrame()
    def load_decision_question_registry(self): return pd.DataFrame()
    def load_decision_context_matrix(self): return pd.DataFrame()
    def load_stakeholder_update_templates(self): return pd.DataFrame()
    def load_communication_gap_register(self): return pd.DataFrame()
    def load_communication_risk_summary(self): return pd.DataFrame()
    def load_briefing_validation_report(self): return pd.DataFrame()
    def load_briefing_quality(self, profile_name=None): return {}
    def load_local_briefing_report(self, profile_name=None): return {}
    def list_available_local_briefing_reports(self): return {}
""")
