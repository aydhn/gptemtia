import os

with open("reports/report_builder.py", "r") as f:
    content = f.read()

# Replace "def build_ml_" with "def build_ml_" outside of class if needed, or remove self from definitions
content = content.replace("def build_ml_training_preview_report(self,", "def build_ml_training_preview_report(")
content = content.replace("def build_ml_model_evaluation_preview_report(self,", "def build_ml_model_evaluation_preview_report(")
content = content.replace("def build_ml_training_batch_report(self,", "def build_ml_training_batch_report(")
content = content.replace("def build_ml_model_registry_status_report(self,", "def build_ml_model_registry_status_report(")
content = content.replace("def build_ml_model_artifact_status_report(self,", "def build_ml_model_artifact_status_report(")

with open("reports/report_builder.py", "w") as f:
    f.write(content)

with open("ml/training_pipeline.py", "r") as f:
    content = f.read()

content = content.replace("self.report_builder = ReportBuilder(data_lake.paths)", "")
content = content.replace("from reports.report_builder import ReportBuilder", "import reports.report_builder as report_builder")
content = content.replace("self.report_builder.", "report_builder.")
content = content.replace("pipeline.report_builder.", "report_builder.")

with open("ml/training_pipeline.py", "w") as f:
    f.write(content)

with open("scripts/run_ml_training_preview.py", "r") as f:
    content = f.read()
content = content.replace("pipeline.report_builder.", "report_builder.")
content = content.replace("from ml.training_pipeline import MLTrainingPipeline", "from ml.training_pipeline import MLTrainingPipeline\nimport reports.report_builder as report_builder")
with open("scripts/run_ml_training_preview.py", "w") as f:
    f.write(content)

with open("scripts/run_ml_model_evaluation_preview.py", "r") as f:
    content = f.read()
content = content.replace("pipeline.report_builder.", "report_builder.")
content = content.replace("from ml.training_pipeline import MLTrainingPipeline", "from ml.training_pipeline import MLTrainingPipeline\nimport reports.report_builder as report_builder")
with open("scripts/run_ml_model_evaluation_preview.py", "w") as f:
    f.write(content)

with open("scripts/run_ml_training_batch.py", "r") as f:
    content = f.read()
content = content.replace("pipeline.report_builder.", "report_builder.")
content = content.replace("from ml.training_pipeline import MLTrainingPipeline", "from ml.training_pipeline import MLTrainingPipeline\nimport reports.report_builder as report_builder")
with open("scripts/run_ml_training_batch.py", "w") as f:
    f.write(content)

with open("scripts/run_ml_model_registry_status.py", "r") as f:
    content = f.read()
content = content.replace("from reports.report_builder import ReportBuilder", "import reports.report_builder as report_builder")
content = content.replace("builder = ReportBuilder(data_lake.paths)", "")
content = content.replace("builder.", "report_builder.")
with open("scripts/run_ml_model_registry_status.py", "w") as f:
    f.write(content)

with open("scripts/run_ml_model_artifact_status.py", "r") as f:
    content = f.read()
content = content.replace("from reports.report_builder import ReportBuilder", "import reports.report_builder as report_builder")
content = content.replace("builder = ReportBuilder(data_lake.paths)", "")
content = content.replace("builder.", "report_builder.")
with open("scripts/run_ml_model_artifact_status.py", "w") as f:
    f.write(content)

print("Fixed report builder imports and usage")
