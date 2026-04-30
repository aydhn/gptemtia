import os

for filename in ["commodity_fx_signal_bot/scripts/run_trend_batch_build.py", "commodity_fx_signal_bot/scripts/run_trend_status.py"]:
    with open(filename, "r") as f:
        content = f.read()

    content = content.replace("DEFAULT_SYMBOL_DEFAULT_SYMBOL_UNIVERSE", "DEFAULT_SYMBOL_UNIVERSE")

    with open(filename, "w") as f:
        f.write(content)
