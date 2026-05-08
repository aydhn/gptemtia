with open("commodity_fx_signal_bot/scripts/run_ml_training_preview.py", "r") as f:
    content = f.read()
content = content.replace("report_builder.build_ml_training_preview_report", "report_builder.ReportBuilder(data_lake.paths).build_ml_training_preview_report")
content = content.replace("pipeline.report_builder.", "report_builder.")
with open("commodity_fx_signal_bot/scripts/run_ml_training_preview.py", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/scripts/run_ml_model_evaluation_preview.py", "r") as f:
    content = f.read()
content = content.replace("report_builder.build_ml_model_evaluation_preview_report", "report_builder.ReportBuilder(data_lake.paths).build_ml_model_evaluation_preview_report")
with open("commodity_fx_signal_bot/scripts/run_ml_model_evaluation_preview.py", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/scripts/run_ml_training_batch.py", "r") as f:
    content = f.read()
content = content.replace("report_builder.build_ml_training_batch_report", "report_builder.ReportBuilder(data_lake.paths).build_ml_training_batch_report")
with open("commodity_fx_signal_bot/scripts/run_ml_training_batch.py", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/scripts/run_ml_model_registry_status.py", "r") as f:
    content = f.read()
content = content.replace("report_builder.build_ml_model_registry_status_report", "report_builder.ReportBuilder(data_lake.paths).build_ml_model_registry_status_report")
with open("commodity_fx_signal_bot/scripts/run_ml_model_registry_status.py", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/scripts/run_ml_model_artifact_status.py", "r") as f:
    content = f.read()
content = content.replace("report_builder.build_ml_model_artifact_status_report", "report_builder.ReportBuilder(data_lake.paths).build_ml_model_artifact_status_report")
with open("commodity_fx_signal_bot/scripts/run_ml_model_artifact_status.py", "w") as f:
    f.write(content)

# And report builder
with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

content = content.replace("    def build_ml_training_preview_report( symbol: str", "    def build_ml_training_preview_report(self, symbol: str")
content = content.replace("    def build_ml_model_evaluation_preview_report( symbol: str", "    def build_ml_model_evaluation_preview_report(self, symbol: str")
content = content.replace("    def build_ml_training_batch_report( summary: dict", "    def build_ml_training_batch_report(self, summary: dict")
content = content.replace("    def build_ml_model_registry_status_report( status_df: pd.DataFrame", "    def build_ml_model_registry_status_report(self, status_df: pd.DataFrame")
content = content.replace("    def build_ml_model_artifact_status_report( status_df: pd.DataFrame", "    def build_ml_model_artifact_status_report(self, status_df: pd.DataFrame")

with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
    f.write(content)
