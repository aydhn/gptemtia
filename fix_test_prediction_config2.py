with open("commodity_fx_signal_bot/ml/prediction_config.py", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.strip() == "return get_ml_prediction_profile(settings.default_ml_prediction_profile)":
        new_lines.append("    return get_ml_prediction_profile(settings.default_ml_prediction_profile)\n")
    else:
        new_lines.append(line)

with open("commodity_fx_signal_bot/ml/prediction_config.py", "w") as f:
    f.writelines(new_lines)
