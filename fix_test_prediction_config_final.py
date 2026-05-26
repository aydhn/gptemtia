with open("commodity_fx_signal_bot/ml/prediction_config.py", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "from config.settings import get_settings" in line:
        pass # Drop it
    elif "settings = get_settings()" in line:
        pass # Drop it
    elif "return get_ml_prediction_profile(settings.default_ml_prediction_profile)" in line:
        # Instead of importing settings which causes circular dependency in some paths,
        # just read it when needed
        new_lines.append("    from config.settings import get_settings\n")
        new_lines.append("    settings = get_settings()\n")
        new_lines.append("    return get_ml_prediction_profile(settings.default_ml_prediction_profile)\n")
    else:
        new_lines.append(line)

with open("commodity_fx_signal_bot/ml/prediction_config.py", "w") as f:
    f.writelines(new_lines)
