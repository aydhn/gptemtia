with open("commodity_fx_signal_bot/ml/prediction_config.py", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.strip() == "from config.settings import get_settings":
        pass
    elif line.strip() == "settings = get_settings()":
        pass
    elif line.strip() == "return get_ml_prediction_profile(settings.default_ml_prediction_profile)":
        new_lines.append("    from config.settings import get_settings\n")
        new_lines.append("    settings = get_settings()\n")
        new_lines.append("    return get_ml_prediction_profile(getattr(settings, 'default_ml_prediction_profile', 'balanced_ml_prediction'))\n")
    else:
        new_lines.append(line)

with open("commodity_fx_signal_bot/ml/prediction_config.py", "w") as f:
    f.writelines(new_lines)
