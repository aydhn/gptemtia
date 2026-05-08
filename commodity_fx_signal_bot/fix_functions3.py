with open("scripts/run_ml_training_batch.py", "r") as f:
    c = f.read()
c = c.replace("builder = report_builder.ReportBuilder(data_lake.paths)\n    report = builder.build_ml_training_batch_report", "report = report_builder.build_ml_training_batch_report")
c = c.replace("report = report_builder.build_ml_training_batch_report(res, res.get(\"ranking_df\"))", "report = report_builder.build_ml_training_batch_report(None, res, res.get(\"ranking_df\"))")
with open("scripts/run_ml_training_batch.py", "w") as f:
    f.write(c)

with open("scripts/run_ml_training_preview.py", "r") as f:
    c = f.read()
c = c.replace("builder = report_builder.ReportBuilder(data_lake.paths)\n    report = builder.build_ml_training_preview_report", "report = report_builder.build_ml_training_preview_report")
c = c.replace("report = report_builder.build_ml_training_preview_report(args.symbol, args.timeframe, args.profile, summary)", "report = report_builder.build_ml_training_preview_report(None, args.symbol, args.timeframe, args.profile, summary)")
with open("scripts/run_ml_training_preview.py", "w") as f:
    f.write(c)

with open("scripts/run_ml_model_evaluation_preview.py", "r") as f:
    c = f.read()
c = c.replace("builder = report_builder.ReportBuilder(data_lake.paths)\n    report = builder.build_ml_model_evaluation_preview_report", "report = report_builder.build_ml_model_evaluation_preview_report")
c = c.replace("report = report_builder.build_ml_model_evaluation_preview_report(args.symbol, args.timeframe, args.profile, summary[\"metrics\"])", "report = report_builder.build_ml_model_evaluation_preview_report(None, args.symbol, args.timeframe, args.profile, summary[\"metrics\"])")
with open("scripts/run_ml_model_evaluation_preview.py", "w") as f:
    f.write(c)

with open("scripts/run_ml_model_registry_status.py", "r") as f:
    c = f.read()
c = c.replace("builder = report_builder.ReportBuilder(data_lake.paths)\n    report = builder.build_ml_model_registry_status_report", "report = report_builder.build_ml_model_registry_status_report")
c = c.replace("report = report_builder.build_ml_model_registry_status_report(df, summary)", "report = report_builder.build_ml_model_registry_status_report(None, df, summary)")
with open("scripts/run_ml_model_registry_status.py", "w") as f:
    f.write(c)

with open("scripts/run_ml_model_artifact_status.py", "r") as f:
    c = f.read()
c = c.replace("builder = report_builder.ReportBuilder(data_lake.paths)\n    report = builder.build_ml_model_artifact_status_report", "report = report_builder.build_ml_model_artifact_status_report")
c = c.replace("report = report_builder.build_ml_model_artifact_status_report(res_df, summary)", "report = report_builder.build_ml_model_artifact_status_report(None, res_df, summary)")
with open("scripts/run_ml_model_artifact_status.py", "w") as f:
    f.write(c)

with open("ml/training_pipeline.py", "r") as f:
    c = f.read()
c = c.replace("report_builder.build_ml_training_batch_report", "report_builder.build_ml_training_batch_report")
c = c.replace("report = self.report_builder.build_ml_training_preview_report", "report = report_builder.build_ml_training_preview_report(None,")
with open("ml/training_pipeline.py", "w") as f:
    f.write(c)
