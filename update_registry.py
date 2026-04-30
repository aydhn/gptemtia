with open("commodity_fx_signal_bot/indicators/registry.py", "r") as f:
    content = f.read()

if "import indicators.trend_advanced as trend_advanced" not in content:
    imports_to_add = """    import indicators.trend as trend
    import indicators.trend_advanced as trend_advanced
    import indicators.trend_events as trend_events
    import indicators.trend_feature_set as trend_feature_set"""

    content = content.replace("    import indicators.trend as trend", imports_to_add)

    module_maps_to_add = """        "trend": [trend, trend_advanced, trend_events, trend_feature_set],
        "volatility": [volatility],
        "volume": [volume],
        "mean_reversion": [mean_reversion],
        "price_action": [price_action],
        "transform": [transforms],
    }

    for spec in specs:
        mods = modules.get(spec.category)
        func = None
        if mods:
            for mod in mods:
                func = getattr(mod, spec.function_name, None)
                if func:
                    break

        if func:
            GLOBAL_INDICATOR_REGISTRY.register(
                spec.name, func, spec.category, spec.default_params
            )"""

    content = content.replace("""        "trend": trend,
        "volatility": volatility,
        "volume": volume,
        "mean_reversion": mean_reversion,
        "price_action": price_action,
        "transform": transforms,
    }

    for spec in specs:
        mod = modules.get(spec.category)
        if mod:
            func = getattr(mod, spec.function_name, None)
            if func:
                GLOBAL_INDICATOR_REGISTRY.register(
                    spec.name, func, spec.category, spec.default_params
                )""", module_maps_to_add)

    content = content.replace("""        "momentum": momentum,""", """        "momentum": [momentum],""")

    with open("commodity_fx_signal_bot/indicators/registry.py", "w") as f:
        f.write(content)
