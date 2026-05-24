path = "commodity_fx_signal_bot/scripts/run_research_governance_report.py"
with open(path, "r") as f:
    content = f.read()

if "import pandas as pd" not in content:
    content = content.replace("from pathlib import Path", "from pathlib import Path\nimport pandas as pd")
    with open(path, "w") as f:
        f.write(content)
