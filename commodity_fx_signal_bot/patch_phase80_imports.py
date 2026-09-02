import os
import glob

for py_file in glob.glob("scripts/*.py") + ["local_closure/closure_pipeline.py"]:
    with open(py_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace("from core.settings import Settings", "from config.settings import Settings")
    content = content.replace("from core.exceptions import ConfigError", "from config.settings import Settings\nclass ConfigError(Exception): pass")
    
    with open(py_file, "w", encoding="utf-8") as f:
        f.write(content)

for py_file in glob.glob("tests/*.py") + ["local_closure/closure_config.py"]:
    with open(py_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace("from core.exceptions import ConfigError", "class ConfigError(Exception): pass")
    
    with open(py_file, "w", encoding="utf-8") as f:
        f.write(content)

print("Imports patched.")
