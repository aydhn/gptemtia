with open("commodity_fx_signal_bot/scripts/run_ml_training_batch.py", "r") as f:
    c = f.read()
c = c.replace("report_builder.ReportBuilder", "report_builder.build_ml_training_batch_report")
c = c.replace("report_builder.build_ml_training_batch_report(data_lake.paths).build_ml_training_batch_report", "report_builder.build_ml_training_batch_report")
with open("commodity_fx_signal_bot/scripts/run_ml_training_batch.py", "w") as f:
    f.write(c)

with open("commodity_fx_signal_bot/scripts/run_ml_training_preview.py", "r") as f:
    c = f.read()
c = c.replace("report_builder.ReportBuilder", "report_builder.build_ml_training_preview_report")
c = c.replace("report_builder.build_ml_training_preview_report(data_lake.paths).build_ml_training_preview_report", "report_builder.build_ml_training_preview_report")
with open("commodity_fx_signal_bot/scripts/run_ml_training_preview.py", "w") as f:
    f.write(c)

with open("commodity_fx_signal_bot/scripts/run_ml_model_evaluation_preview.py", "r") as f:
    c = f.read()
c = c.replace("report_builder.ReportBuilder", "report_builder.build_ml_model_evaluation_preview_report")
c = c.replace("report_builder.build_ml_model_evaluation_preview_report(data_lake.paths).build_ml_model_evaluation_preview_report", "report_builder.build_ml_model_evaluation_preview_report")
with open("commodity_fx_signal_bot/scripts/run_ml_model_evaluation_preview.py", "w") as f:
    f.write(c)

with open("commodity_fx_signal_bot/scripts/run_ml_model_registry_status.py", "r") as f:
    c = f.read()
c = c.replace("report_builder.ReportBuilder", "report_builder.build_ml_model_registry_status_report")
c = c.replace("report_builder.build_ml_model_registry_status_report(data_lake.paths).build_ml_model_registry_status_report", "report_builder.build_ml_model_registry_status_report")
with open("commodity_fx_signal_bot/scripts/run_ml_model_registry_status.py", "w") as f:
    f.write(c)

with open("commodity_fx_signal_bot/scripts/run_ml_model_artifact_status.py", "r") as f:
    c = f.read()
c = c.replace("report_builder.ReportBuilder", "report_builder.build_ml_model_artifact_status_report")
c = c.replace("report_builder.build_ml_model_artifact_status_report(data_lake.paths).build_ml_model_artifact_status_report", "report_builder.build_ml_model_artifact_status_report")
with open("commodity_fx_signal_bot/scripts/run_ml_model_artifact_status.py", "w") as f:
    f.write(c)


with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    c = f.read()
c = c.replace("    def build_ml_training_preview_report(self,", "def build_ml_training_preview_report(")
c = c.replace("    def build_ml_model_evaluation_preview_report(self,", "def build_ml_model_evaluation_preview_report(")
c = c.replace("    def build_ml_training_batch_report(self,", "def build_ml_training_batch_report(")
c = c.replace("    def build_ml_model_registry_status_report(self,", "def build_ml_model_registry_status_report(")
c = c.replace("    def build_ml_model_artifact_status_report(self,", "def build_ml_model_artifact_status_report(")
with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
    f.write(c)
