import pandas as pd
from .factor_models import FactorDefinition
from .factor_config import FactorResearchProfile

def build_trend_factor_definitions(profile: FactorResearchProfile) -> list[FactorDefinition]:
    defs = []
    for w in profile.trend_windows:
        defs.append(FactorDefinition(
            factor_id=f"trend_{w}",
            factor_name=f"Price Trend {w}",
            factor_type="trend_factor",
            description=f"{w}-period return based price trend.",
            direction="higher_is_better",
            required_inputs=["close"],
            lookback_windows=[w],
            methodology="Simple return over window.",
            warnings=["Trend score canlı sinyal değildir."]
        ))
    return defs

def build_momentum_factor_definitions(profile: FactorResearchProfile) -> list[FactorDefinition]:
    defs = []
    for w in profile.momentum_windows:
        defs.append(FactorDefinition(
            factor_id=f"momentum_{w}",
            factor_name=f"Return Momentum {w}",
            factor_type="momentum_factor",
            description=f"{w}-period return momentum.",
            direction="higher_is_better",
            required_inputs=["returns"],
            lookback_windows=[w],
            methodology="Cumulative return over window.",
            warnings=["Momentum rank işlem talimatı değildir."]
        ))
    return defs

def build_volatility_factor_definitions(profile: FactorResearchProfile) -> list[FactorDefinition]:
    defs = []
    for w in profile.volatility_windows:
        defs.append(FactorDefinition(
            factor_id=f"inverse_volatility_{w}",
            factor_name=f"Inverse Volatility {w}",
            factor_type="volatility_factor",
            description=f"Inverse of {w}-period realized volatility.",
            direction="lower_is_better",
            required_inputs=["returns"],
            lookback_windows=[w],
            methodology="1 / (std(returns) * sqrt(252)).",
            warnings=["Volatility factor risk proxy'sidir, gerçek risk modeli değildir."]
        ))
    return defs

def build_carry_proxy_factor_definitions(profile: FactorResearchProfile) -> list[FactorDefinition]:
    return [
        FactorDefinition(
            factor_id="carry_proxy_fx_try",
            factor_name="FX TRY Carry Proxy",
            factor_type="carry_proxy_factor",
            description="Proxy carry for FX using TRY rate spread.",
            direction="higher_is_better",
            required_inputs=["metadata"],
            lookback_windows=[],
            methodology="Placeholder proxy approach based on simple assumptions.",
            warnings=["Carry proxy gerçek carry değildir.", "Canlı işlem sinyali değildir."]
        ),
        FactorDefinition(
            factor_id="carry_proxy_commodity_term_structure_placeholder",
            factor_name="Commodity Carry Placeholder",
            factor_type="carry_proxy_factor",
            description="Placeholder for commodity term structure.",
            direction="higher_is_better",
            required_inputs=["metadata"],
            lookback_windows=[],
            methodology="Placeholder proxy approach.",
            warnings=["Carry proxy gerçek carry değildir.", "Commodity term structure yoksa açık placeholder warning üret."]
        )
    ]

def build_value_proxy_factor_definitions(profile: FactorResearchProfile) -> list[FactorDefinition]:
    return [
        FactorDefinition(
            factor_id="value_proxy_distance_from_long_ma",
            factor_name="Distance from Long MA",
            factor_type="value_proxy_factor",
            description="Distance from 252-period moving average.",
            direction="lower_is_better",
            required_inputs=["close"],
            lookback_windows=[252],
            methodology="(Close - MA) / MA.",
            warnings=["Value proxy gerçek fundamental ucuzluk/pahalılık değildir."]
        ),
        FactorDefinition(
            factor_id="value_proxy_zscore_from_rolling_mean",
            factor_name="Z-Score from Rolling Mean",
            factor_type="value_proxy_factor",
            description="Z-score distance from 252-period mean.",
            direction="lower_is_better",
            required_inputs=["close"],
            lookback_windows=[252],
            methodology="(Close - Mean) / Std.",
            warnings=["Value proxy gerçek fundamental ucuzluk/pahalılık değildir.", "Z-score low/high yorumları işlem tavsiyesi değildir."]
        )
    ]

def build_macro_sensitivity_factor_definitions(profile: FactorResearchProfile) -> list[FactorDefinition]:
    return [
        FactorDefinition(
            factor_id="usdtry_sensitivity_proxy",
            factor_name="USDTRY Sensitivity",
            factor_type="usdtry_sensitivity_factor",
            description="Beta to USDTRY returns.",
            direction="neutral_direction",
            required_inputs=["returns"],
            lookback_windows=[60],
            methodology="Rolling 60-period beta.",
            warnings=["Beta proxy gerçek risk modeli değildir.", "Sensitivity yüksekliği işlem çağrısı değildir."]
        ),
        FactorDefinition(
            factor_id="gold_relative_strength_factor",
            factor_name="Gold Relative Strength",
            factor_type="gold_relative_factor",
            description="Relative return compared to Gold.",
            direction="higher_is_better",
            required_inputs=["returns"],
            lookback_windows=[60],
            methodology="Symbol return - Gold return.",
            warnings=["Sensitivity yüksekliği işlem çağrısı değildir."]
        ),
        FactorDefinition(
            factor_id="oil_relative_strength_factor",
            factor_name="Oil Relative Strength",
            factor_type="oil_relative_factor",
            description="Relative return compared to Oil.",
            direction="higher_is_better",
            required_inputs=["returns"],
            lookback_windows=[60],
            methodology="Symbol return - Oil return.",
            warnings=["Sensitivity yüksekliği işlem çağrısı değildir."]
        ),
        FactorDefinition(
            factor_id="inflation_sensitivity_proxy",
            factor_name="Inflation Sensitivity Proxy",
            factor_type="inflation_sensitivity_factor",
            description="Sensitivity to inflation proxy.",
            direction="higher_is_better",
            required_inputs=["returns"],
            lookback_windows=[60],
            methodology="Rolling 60-period beta to proxy.",
            warnings=["Inflation sensitivity proxy tahmin değildir."]
        )
    ]

def build_default_factor_definitions(profile: FactorResearchProfile) -> list[FactorDefinition]:
    defs = []
    defs.extend(build_trend_factor_definitions(profile))
    defs.extend(build_momentum_factor_definitions(profile))
    defs.extend(build_volatility_factor_definitions(profile))
    defs.extend(build_carry_proxy_factor_definitions(profile))
    defs.extend(build_value_proxy_factor_definitions(profile))
    defs.extend(build_macro_sensitivity_factor_definitions(profile))

    defs.append(FactorDefinition(
        factor_id="composite_factor_score",
        factor_name="Composite Factor Score",
        factor_type="composite_factor",
        description="Equal weighted composite of selected factors.",
        direction="higher_is_better",
        required_inputs=["factor_scores"],
        lookback_windows=[],
        methodology="Mean of normalized scores.",
        warnings=["Composite rank canlı sinyal değildir.", "En yüksek composite score al anlamına gelmez."]
    ))

    defs.append(FactorDefinition(
        factor_id="defensive_low_drawdown_factor",
        factor_name="Defensive Low Drawdown",
        factor_type="defensive_factor",
        description="Inverse of maximum drawdown.",
        direction="lower_is_better",
        required_inputs=["returns"],
        lookback_windows=[252],
        methodology="1 / Abs(Max Drawdown).",
        warnings=["Düşük drawdown gelecek performansı garantilemez."]
    ))

    return defs

def factor_definitions_to_dataframe(definitions: list[FactorDefinition]) -> pd.DataFrame:
    records = []
    for d in definitions:
        records.append({
            "factor_id": d.factor_id,
            "factor_name": d.factor_name,
            "factor_type": d.factor_type,
            "description": d.description,
            "direction": d.direction,
            "required_inputs": ",".join(d.required_inputs),
            "lookback_windows": ",".join(map(str, d.lookback_windows)),
            "methodology": d.methodology,
            "warnings": " | ".join(d.warnings)
        })
    return pd.DataFrame(records)
