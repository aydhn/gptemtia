import os
import shutil

for file in ["fix_init.py", "fix_init2.py", "fix_missing_files.py", "fix_missing_files_2.py", "fix_missing_tests.py", "fix_report_builder.py", "fix_script_datalake.py", "fix_script_imports10.py", "fix_script_imports3.py", "fix_script_imports4.py", "fix_script_imports5.py", "fix_script_imports6.py", "fix_script_imports7.py", "fix_script_imports8.py", "fix_script_imports9.py", "fix_test_and_settings.py", "update_data_lake.py", "update_docs.py", "update_feature_store.py"]:
    if os.path.exists(file):
        os.remove(file)
