import re


def fix_batch():
    with open("scripts/run_decision_batch_build.py", "r") as f:
        content = f.read()
    content = content.replace(
        "from config.symbols import get_symbol_spec, get_all_symbols",
        "from config.symbols import get_symbol_spec, get_enabled_symbols",
    )
    content = content.replace("get_all_symbols()", "get_enabled_symbols()")
    with open("scripts/run_decision_batch_build.py", "w") as f:
        f.write(content)


def fix_pool():
    with open("scripts/run_decision_pool_preview.py", "r") as f:
        content = f.read()
    content = content.replace(
        "from config.symbols import get_all_symbols",
        "from config.symbols import get_enabled_symbols",
    )
    content = content.replace("get_all_symbols()", "get_enabled_symbols()")
    with open("scripts/run_decision_pool_preview.py", "w") as f:
        f.write(content)


def fix_status():
    with open("scripts/run_decision_status.py", "r") as f:
        content = f.read()
    content = content.replace(
        "from config.symbols import get_all_symbols",
        "from config.symbols import get_enabled_symbols",
    )
    content = content.replace("get_all_symbols()", "get_enabled_symbols()")
    with open("scripts/run_decision_status.py", "w") as f:
        f.write(content)


def fix_test():
    with open("tests/test_decision_pipeline.py", "r") as f:
        content = f.read()
    content = content.replace(
        'spec = get_symbol_spec("DXY")', 'spec = get_symbol_spec("DX-Y.NYB")'
    )
    with open("tests/test_decision_pipeline.py", "w") as f:
        f.write(content)


fix_batch()
fix_pool()
fix_status()
fix_test()
