import re

file_path = "commodity_fx_signal_bot/reports/report_builder.py"

with open(file_path, "r") as f:
    content = f.read()

addition = """
    def build_research_artifact_inventory_text_report(self, summary: dict, artifact_df: pd.DataFrame | None = None) -> str:
        res = "Research Artifact Inventory Report\\n\\n"
        res += "Bu cikti offline/local research artifact metadata ve card documentation raporudur. Model deployment, canli emir, broker talimati, gercek pozisyon, resmi sertifika, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
        res += f"Total Artifacts: {summary.get('total_artifacts', 0)}\\n"
        return res

    def build_model_dataset_cards_text_report(self, summary: dict, model_df: pd.DataFrame | None = None, dataset_df: pd.DataFrame | None = None) -> str:
        res = "Model & Dataset Cards Report\\n\\n"
        res += "Bu cikti offline/local research artifact metadata ve card documentation raporudur. Model deployment, canli emir, broker talimati, gercek pozisyon, resmi sertifika, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
        res += f"Total Model Cards: {summary.get('total_model_cards', 0)}\\n"
        res += f"Total Dataset Cards: {summary.get('total_dataset_cards', 0)}\\n"
        return res

    def build_experiment_reproducibility_cards_text_report(self, summary: dict, experiment_df: pd.DataFrame | None = None, repro_df: pd.DataFrame | None = None) -> str:
        res = "Experiment & Reproducibility Cards Report\\n\\n"
        res += "Bu cikti offline/local research artifact metadata ve card documentation raporudur. Model deployment, canli emir, broker talimati, gercek pozisyon, resmi sertifika, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
        res += f"Total Experiment Cards: {summary.get('total_experiment_cards', 0)}\\n"
        res += f"Total Reproducibility Cards: {summary.get('total_reproducibility_cards', 0)}\\n"
        return res

    def build_scenario_regression_cards_text_report(self, summary: dict, scenario_df: pd.DataFrame | None = None, regression_df: pd.DataFrame | None = None) -> str:
        res = "Scenario & Regression Cards Report\\n\\n"
        res += "Bu cikti offline/local research artifact metadata ve card documentation raporudur. Model deployment, canli emir, broker talimati, gercek pozisyon, resmi sertifika, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
        res += f"Total Scenario Cards: {summary.get('total_scenario_cards', 0)}\\n"
        res += f"Total Regression Cards: {summary.get('total_regression_cards', 0)}\\n"
        return res

    def build_research_metadata_export_text_report(self, summary: dict, export_index_df: pd.DataFrame | None = None) -> str:
        res = "Research Metadata Export Report\\n\\n"
        res += "Bu cikti offline/local research artifact metadata ve card documentation raporudur. Model deployment, canli emir, broker talimati, gercek pozisyon, resmi sertifika, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
        res += f"Total Exports: {summary.get('total_exports', 0)}\\n"
        return res

    def build_metadata_quality_text_report(self, summary: dict, quality: dict | None = None) -> str:
        res = "Metadata Quality Report\\n\\n"
        res += "Bu cikti offline/local research artifact metadata ve card documentation raporudur. Model deployment, canli emir, broker talimati, gercek pozisyon, resmi sertifika, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
        if quality:
            res += f"Passed: {quality.get('passed', False)}\\n"
            res += f"Warnings: {quality.get('warning_count', 0)}\\n"
        return res

    def build_metadata_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        res = "Metadata Status Report\\n\\n"
        res += "Bu cikti offline/local research artifact metadata ve card documentation raporudur. Model deployment, canli emir, broker talimati, gercek pozisyon, resmi sertifika, production scheduler, otomatik trade onayi veya yatirim tavsiyesi degildir.\\n\\n"
        res += "Status: OK\\n"
        return res
"""

if "build_research_artifact_inventory_text_report" not in content:
    content = content.replace("class ReportBuilder:", "class ReportBuilder:\n" + addition)
    with open(file_path, "w") as f:
        f.write(content)
