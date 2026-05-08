with open("commodity_fx_signal_bot/scripts/run_ml_training_batch.py", "r") as f:
    content = f.read()

content = content.replace("report = report_builder.build_ml_training_batch_report(res, res.get(\"ranking_df\"))",
                          "report = report_builder.build_ml_training_batch_report(res, res.get(\"ranking_df\"))")

print("Let's look at the class vs function issue.")
