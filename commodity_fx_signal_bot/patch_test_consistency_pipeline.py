import re

with open("tests/test_consistency_pipeline.py", "r") as f:
    content = f.read()

content = content.replace("data_lake = DataLake()", "data_lake = DataLake(paths.lake_dir)")
with open("tests/test_consistency_pipeline.py", "w") as f:
    f.write(content)

with open("scripts/run_consistency_check_registry.py", "r") as f:
    content = f.read()
content = content.replace("data_lake = DataLake()", "data_lake = DataLake(paths.lake_dir)")
with open("scripts/run_consistency_check_registry.py", "w") as f:
    f.write(content)

with open("scripts/run_cross_layer_consistency_matrix.py", "r") as f:
    content = f.read()
content = content.replace("data_lake = DataLake()", "data_lake = DataLake(paths.lake_dir)")
with open("scripts/run_cross_layer_consistency_matrix.py", "w") as f:
    f.write(content)

with open("scripts/run_contradiction_detection_report.py", "r") as f:
    content = f.read()
content = content.replace("data_lake = DataLake()", "data_lake = DataLake(paths.lake_dir)")
with open("scripts/run_contradiction_detection_report.py", "w") as f:
    f.write(content)

with open("scripts/run_stale_reconciliation_plan.py", "r") as f:
    content = f.read()
content = content.replace("data_lake = DataLake()", "data_lake = DataLake(paths.lake_dir)")
with open("scripts/run_stale_reconciliation_plan.py", "w") as f:
    f.write(content)

with open("scripts/run_system_coherence_report.py", "r") as f:
    content = f.read()
content = content.replace("data_lake = DataLake()", "data_lake = DataLake(paths.lake_dir)")
with open("scripts/run_system_coherence_report.py", "w") as f:
    f.write(content)

with open("scripts/run_consistency_quality_report.py", "r") as f:
    content = f.read()
content = content.replace("data_lake = DataLake()", "data_lake = DataLake(paths.lake_dir)")
with open("scripts/run_consistency_quality_report.py", "w") as f:
    f.write(content)

with open("scripts/run_consistency_status.py", "r") as f:
    content = f.read()
content = content.replace("data_lake = DataLake()", "data_lake = DataLake(paths.lake_dir)")
with open("scripts/run_consistency_status.py", "w") as f:
    f.write(content)
