import re

with open("config/paths.py", "r") as f:
    content = f.read()

# Try to find the directories list and append new ones
import ast

def replace_list(content):
    if "LAKE_ML_QUALITY_DIR," in content and "LAKE_ML_MODEL_REGISTRY_DIR," not in content:
        return content.replace("LAKE_ML_QUALITY_DIR,",
        """LAKE_ML_QUALITY_DIR,
        LAKE_ML_MODELS_DIR,
        LAKE_ML_MODEL_ARTIFACTS_DIR,
        LAKE_ML_MODEL_REGISTRY_DIR,
        LAKE_ML_MODEL_EVALUATIONS_DIR,
        LAKE_ML_MODEL_CV_DIR,
        LAKE_ML_MODEL_QUALITY_DIR,
        REPORTS_ML_TRAINING_REPORTS_DIR,""")
    return content

new_content = replace_list(content)
if new_content != content:
    with open("config/paths.py", "w") as f:
        f.write(new_content)
    print("Fixed paths list")
else:
    print("No fix needed or couldn't find pattern")
