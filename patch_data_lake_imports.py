import re

def patch_file():
    path = "commodity_fx_signal_bot/data/storage/data_lake.py"
    with open(path, "r") as f:
        content = f.read()

    if "from typing import Optional" not in content and "from typing import " in content:
        content = content.replace("from typing import ", "from typing import Optional, ")
    elif "from typing import Optional" not in content:
        content = "from typing import Optional\n" + content

    with open(path, "w") as f:
        f.write(content)

patch_file()
