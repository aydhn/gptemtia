with open("scripts/run_ml_training_batch.py", "r") as f:
    c = f.read()
c = c.replace("report = report_builder.build_ml_training_batch_report", "builder = report_builder.ReportBuilder(data_lake.paths)\n    report = builder.build_ml_training_batch_report")
with open("scripts/run_ml_training_batch.py", "w") as f:
    f.write(c)

with open("scripts/run_ml_training_preview.py", "r") as f:
    c = f.read()
c = c.replace("report = report_builder.build_ml_training_preview_report", "builder = report_builder.ReportBuilder(data_lake.paths)\n    report = builder.build_ml_training_preview_report")
with open("scripts/run_ml_training_preview.py", "w") as f:
    f.write(c)

with open("scripts/run_ml_model_evaluation_preview.py", "r") as f:
    c = f.read()
c = c.replace("report = report_builder.build_ml_model_evaluation_preview_report", "builder = report_builder.ReportBuilder(data_lake.paths)\n    report = builder.build_ml_model_evaluation_preview_report")
with open("scripts/run_ml_model_evaluation_preview.py", "w") as f:
    f.write(c)

with open("scripts/run_ml_model_registry_status.py", "r") as f:
    c = f.read()
c = c.replace("report = report_builder.build_ml_model_registry_status_report", "builder = report_builder.ReportBuilder(data_lake.paths)\n    report = builder.build_ml_model_registry_status_report")
with open("scripts/run_ml_model_registry_status.py", "w") as f:
    f.write(c)

with open("scripts/run_ml_model_artifact_status.py", "r") as f:
    c = f.read()
c = c.replace("report = report_builder.build_ml_model_artifact_status_report", "builder = report_builder.ReportBuilder(data_lake.paths)\n    report = builder.build_ml_model_artifact_status_report")
with open("scripts/run_ml_model_artifact_status.py", "w") as f:
    f.write(c)
