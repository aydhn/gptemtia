with open("commodity_fx_signal_bot/indicators/registry.py", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.strip() == "else:":
        # check previous line
        if new_lines and "GLOBAL_INDICATOR_REGISTRY.register(" in new_lines[-1] or "spec.name, func, spec.category, spec.default_params" in new_lines[-1] or "            )" in new_lines[-1]:
            pass
        else:
            new_lines.append(line)
    elif line.strip() == "logger.warning(":
        new_lines.append(line)
    elif line.strip() == "f\"Function {spec.function_name} not found in module {spec.category} for indicator {spec.name}\"":
        new_lines.append(line)
    elif line.strip() == ")":
        new_lines.append(line)
    else:
        new_lines.append(line)

fixed = """        if func:
            GLOBAL_INDICATOR_REGISTRY.register(
                spec.name, func, spec.category, spec.default_params
            )
        else:
            logger.warning(
                f"Function {spec.function_name} not found in module {spec.category} for indicator {spec.name}"
            )"""

with open("commodity_fx_signal_bot/indicators/registry.py", "r") as f:
    content = f.read()

content = content.replace("""        if func:
            GLOBAL_INDICATOR_REGISTRY.register(
                spec.name, func, spec.category, spec.default_params
            )
            else:
                logger.warning(
                    f"Function {spec.function_name} not found in module {spec.category} for indicator {spec.name}"
                )""", fixed)

with open("commodity_fx_signal_bot/indicators/registry.py", "w") as f:
    f.write(content)
