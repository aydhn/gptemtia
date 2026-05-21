import pandas as pd
from config.symbols import SymbolSpec
from portfolio_research.portfolio_config import PortfolioResearchProfile

def build_symbol_metadata_table(specs: list[SymbolSpec]) -> pd.DataFrame:
    rows = []
    for spec in specs:
        rows.append({
            "symbol": spec.symbol,
            "asset_class": spec.asset_class,
            "base_currency": spec.base_currency,
            "quote_currency": spec.quote_currency,
        })
    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows).set_index("symbol")

def calculate_asset_class_exposure(weights: dict[str, float], metadata_df: pd.DataFrame) -> pd.DataFrame:
    if metadata_df.empty or not weights:
        return pd.DataFrame()

    exposure = {}
    for sym, weight in weights.items():
        if sym in metadata_df.index:
            ac = metadata_df.loc[sym, "asset_class"]
            exposure[ac] = exposure.get(ac, 0.0) + weight

    if not exposure:
        return pd.DataFrame()

    df = pd.DataFrame(list(exposure.items()), columns=["asset_class", "exposure_weight"])
    return df.sort_values(by="exposure_weight", ascending=False).reset_index(drop=True)

def calculate_currency_exposure(weights: dict[str, float], metadata_df: pd.DataFrame) -> pd.DataFrame:
    if metadata_df.empty or not weights:
        return pd.DataFrame()

    exposure = {}
    for sym, weight in weights.items():
        if sym in metadata_df.index:
            bc = metadata_df.loc[sym, "base_currency"]
            qc = metadata_df.loc[sym, "quote_currency"]
            exposure[bc] = exposure.get(bc, 0.0) + (weight * 0.5)
            exposure[qc] = exposure.get(qc, 0.0) - (weight * 0.5)

    if not exposure:
        return pd.DataFrame()

    df = pd.DataFrame(list(exposure.items()), columns=["currency", "net_exposure"])
    df["abs_exposure"] = df["net_exposure"].abs()
    return df.sort_values(by="abs_exposure", ascending=False).reset_index(drop=True)

def calculate_symbol_exposure(weights: dict[str, float]) -> pd.DataFrame:
    if not weights:
        return pd.DataFrame()

    df = pd.DataFrame(list(weights.items()), columns=["symbol", "weight"])
    return df.sort_values(by="weight", ascending=False).reset_index(drop=True)

def infer_exposure_label(asset_class_exposure_df: pd.DataFrame, symbol_exposure_df: pd.DataFrame, profile: PortfolioResearchProfile) -> str:
    if symbol_exposure_df.empty:
        return "unknown_exposure"

    max_symbol_weight = symbol_exposure_df["weight"].max()
    if max_symbol_weight > profile.max_single_symbol_weight:
        return "symbol_concentrated"

    if not asset_class_exposure_df.empty:
        max_ac_weight = asset_class_exposure_df["exposure_weight"].max()
        if max_ac_weight > profile.max_asset_class_weight:
            return "asset_class_concentrated"

    return "balanced_exposure"

def build_cross_asset_exposure_report(weights: dict[str, float], specs: list[SymbolSpec], profile: PortfolioResearchProfile) -> tuple[dict[str, pd.DataFrame], dict]:
    metadata_df = build_symbol_metadata_table(specs)

    symbol_exp = calculate_symbol_exposure(weights)
    ac_exp = calculate_asset_class_exposure(weights, metadata_df)
    ccy_exp = calculate_currency_exposure(weights, metadata_df)

    label = infer_exposure_label(ac_exp, symbol_exp, profile)

    tables = {
        "symbol_exposure": symbol_exp,
        "asset_class_exposure": ac_exp,
        "currency_exposure": ccy_exp,
    }

    summary = {
        "exposure_label": label,
        "warnings": [],
        "note": "Exposure tablosu gercek portfoy beyani degildir. Agirliklar sanal arastirma agirligidir."
    }

    if label != "balanced_exposure":
        summary["warnings"].append(f"Concentration warning: {label} (This is not a trade instruction)")

    return tables, summary
