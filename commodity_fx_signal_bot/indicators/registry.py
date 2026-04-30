import logging
from typing import Callable, Optional

from indicators.indicator_config import list_indicator_specs

logger = logging.getLogger(__name__)


class IndicatorRegistry:
    def __init__(self):
        self._indicators = {}

    def register(
        self,
        name: str,
        func: Callable,
        category: str,
        default_params: Optional[dict] = None,
    ) -> None:
        if name in self._indicators:
            logger.warning(f"Indicator '{name}' is already registered. Overwriting.")
        self._indicators[name] = {
            "func": func,
            "category": category,
            "default_params": default_params or {},
        }

    def get(self, name: str) -> Callable:
        if name not in self._indicators:
            raise ValueError(f"Indicator '{name}' not found in registry.")
        return self._indicators[name]["func"]

    def list_names(self, category: Optional[str] = None) -> list[str]:
        if category:
            return [
                name
                for name, data in self._indicators.items()
                if data["category"] == category
            ]
        return list(self._indicators.keys())

    def exists(self, name: str) -> bool:
        return name in self._indicators

    def clear(self) -> None:
        self._indicators.clear()


GLOBAL_INDICATOR_REGISTRY = IndicatorRegistry()


def register_builtin_indicators():
    # To avoid circular imports, import modules dynamically when registering
    import indicators.mean_reversion as mean_reversion
    import indicators.momentum as momentum
    import indicators.price_action as price_action
    import indicators.transforms as transforms
    import indicators.trend as trend
    import indicators.trend_advanced as trend_advanced
    import indicators.trend_events as trend_events
    import indicators.trend_feature_set as trend_feature_set
    import indicators.volatility as volatility
    import indicators.volatility_advanced as volatility_advanced
    import indicators.volatility_events as volatility_events
    import indicators.volatility_feature_set as volatility_feature_set
    import indicators.volume_advanced as volume_advanced
    import indicators.volume_events as volume_events
    import indicators.volume_feature_set as volume_feature_set
    import indicators.volume as volume

    # We will register them based on specs
    specs = list_indicator_specs()

    # Map module names to module objects
    modules = {
        "momentum": [momentum],
        "trend": [trend, trend_advanced, trend_events, trend_feature_set],
        "volatility": [
            volatility,
            volatility_advanced,
            volatility_events,
            volatility_feature_set,
        ],
        "volume": [volume, volume_advanced, volume_events, volume_feature_set],
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
            )
        else:
            logger.warning(
                f"Function {spec.function_name} not found in module {spec.category} for indicator {spec.name}"
            )


def get_indicator(name: str) -> Callable:
    return GLOBAL_INDICATOR_REGISTRY.get(name)


def list_registered_indicators(category: Optional[str] = None) -> list[str]:
    return GLOBAL_INDICATOR_REGISTRY.list_names(category)
