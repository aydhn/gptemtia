import re

def patch_file():
    path = "commodity_fx_signal_bot/data/storage/data_lake.py"
    with open(path, "r") as f:
        content = f.read()

    if "from datetime import datetime" not in content:
        content = "from datetime import datetime\n" + content

    if "import os" not in content:
        content = "import os\n" + content

    with open(path, "w") as f:
        f.write(content)

patch_file()
