with open("commodity_fx_signal_bot/experiments/experiment_pipeline.py", "r") as f:
    content = f.read()

content = content.replace("        metrics = [\n            {\"run_id\": \"r1\", \"quality_adjusted_score\": 0.9, \"reproducibility_score\": 1.0, \"validation_score\": 0.8},\n            {\"run_id\": \"r2\", \"quality_adjusted_score\": 0.5, \"reproducibility_score\": 0.8, \"validation_score\": 0.5}\n        ]", "        metrics = [\n            {\"run_id\": \"r1\", \"metrics\": {\"quality_adjusted_score\": 0.9, \"reproducibility_score\": 1.0, \"validation_score\": 0.8}},\n            {\"run_id\": \"r2\", \"metrics\": {\"quality_adjusted_score\": 0.5, \"reproducibility_score\": 0.8, \"validation_score\": 0.5}}\n        ]")

with open("commodity_fx_signal_bot/experiments/experiment_pipeline.py", "w") as f:
    f.write(content)
