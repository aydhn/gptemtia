# Fix symbol spec tests
import glob

files_to_check = glob.glob("commodity_fx_signal_bot/tests/*.py")

for file in files_to_check:
    with open(file, 'r') as f:
        content = f.read()

    if "MockSpec(\"A\")" in content:
        content = content.replace("class MockSpec:\n    def __init__(self, sym):\n        self.symbol = sym", "class MockSpec:\n    def __init__(self, sym):\n        self.symbol = sym\n        self.group = 'COMMODITY'\n        self.asset_class = 'COMMODITY'")

        with open(file, 'w') as f:
            f.write(content)
