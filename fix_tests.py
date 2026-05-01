import re

files_to_fix = [
    "commodity_fx_signal_bot/tests/test_mtf_loader.py",
    "commodity_fx_signal_bot/tests/test_mtf_pipeline.py"
]

for file_path in files_to_fix:
    with open(file_path, "r") as f:
        content = f.read()

    content = content.replace("SymbolSpec(\"TEST\", \"crypto\")", "SymbolSpec(\"TEST\", \"crypto\", \"crypto\", \"crypto\", \"USD\")")

    with open(file_path, "w") as f:
        f.write(content)
