import re

def patch_file():
    path = "commodity_fx_signal_bot/data/storage/data_lake.py"
    with open(path, "r") as f:
        content = f.read()

    # ensure datetime is imported
    if "import datetime" not in content and "from datetime import datetime" not in content:
        content = "from datetime import datetime\n" + content

    # or just replace datetime.now() with pd.Timestamp.now() if datetime fails
    # Let's add a robust import block at the very top.
    imports = "import os\nfrom datetime import datetime\n"
    if "from datetime import datetime" not in content:
        content = imports + content

    with open(path, "w") as f:
        f.write(content)

patch_file()
