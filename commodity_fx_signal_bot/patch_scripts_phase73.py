import os
import glob

for file in glob.glob("scripts/run_training*.py") + glob.glob("scripts/run_onboarding_curriculum.py") + glob.glob("scripts/run_guided_walkthroughs.py") + glob.glob("scripts/run_handover_education_binder.py"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace("from data.storage.data_lake import data_lake", "from data.storage.data_lake import DataLake")
    content = content.replace("pipeline = LocalTrainingPipeline(data_lake, settings, PROJECT_ROOT, profile)", "pipeline = LocalTrainingPipeline(DataLake(), settings, PROJECT_ROOT, profile)")

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

