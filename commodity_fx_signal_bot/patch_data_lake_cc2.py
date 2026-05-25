import re

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

import_json = "import json\nimport uuid"
if "import json" not in content:
    content = content.replace("import uuid", import_json)

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
    f.write(content)
