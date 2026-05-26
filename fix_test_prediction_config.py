with open("commodity_fx_signal_bot/ml/prediction_config.py", "r") as f:
    content = f.read()

content = content.replace("from config.settings import settings", "from config.settings import get_settings\nsettings = get_settings()")

with open("commodity_fx_signal_bot/ml/prediction_config.py", "w") as f:
    f.write(content)
