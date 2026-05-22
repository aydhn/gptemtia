import pandas as pd
import numpy as np

def calculate_symbol_factor_exposure(score_df: pd.DataFrame) -> pd.DataFrame:
    """
    Translates raw normalized scores (0-1) into standardized exposures (-1 to 1)
    where 0 is cross-sectional neutral.
    """
    if score_df.empty:
        return pd.DataFrame()

    exposures = []

    pivot_df = score_df.pivot(index="symbol", columns="factor_id", values="normalized_score")

    for factor_id in pivot_df.columns:
        scores = pivot_df[factor_id]
        mean_score = scores.mean()

        # Center around mean, bound between -1 and 1
        centered = scores - mean_score
        max_abs = centered.abs().max()
        if max_abs > 0:
            exp = centered / max_abs
        else:
            exp = centered

        for sym, val in exp.items():
            if not pd.isna(val):
                pct = scores.rank(pct=True).loc[sym]

                label = "neutral"
                if val > 0.5: label = "high_positive"
                elif val < -0.5: label = "high_negative"

                exposures.append({
                    "entity_id": sym,
                    "entity_type": "symbol",
                    "factor_id": factor_id,
                    "exposure_score": float(val),
                    "exposure_percentile": float(pct),
                    "exposure_label": label,
                    "warnings": []
                })

    return pd.DataFrame(exposures)

def calculate_basket_factor_exposure(weights: dict[str, float], score_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates weighted average exposure for a basket.
    """
    if not weights or score_df.empty:
        return pd.DataFrame()

    pivot_df = score_df.pivot(index="symbol", columns="factor_id", values="normalized_score")

    exposures = []
    for factor_id in pivot_df.columns:
        scores = pivot_df[factor_id]
        mean_score = scores.mean()
        centered = scores - mean_score
        max_abs = centered.abs().max()
        if max_abs > 0:
            exp = centered / max_abs
        else:
            exp = centered

        basket_exp = 0.0
        total_w = 0.0

        for sym, w in weights.items():
            if sym in exp.index and not pd.isna(exp.loc[sym]):
                basket_exp += exp.loc[sym] * w
                total_w += w

        if total_w > 0:
            final_exp = basket_exp / total_w

            label = "neutral"
            if final_exp > 0.5: label = "high_positive"
            elif final_exp < -0.5: label = "high_negative"

            exposures.append({
                "entity_id": "basket",
                "entity_type": "basket",
                "factor_id": factor_id,
                "exposure_score": float(final_exp),
                "exposure_percentile": None,
                "exposure_label": label,
                "warnings": []
            })

    return pd.DataFrame(exposures)

def build_factor_exposure_table(score_df: pd.DataFrame, baskets_df: pd.DataFrame | None = None) -> pd.DataFrame:
    if score_df.empty:
        return pd.DataFrame()

    sym_exp = calculate_symbol_factor_exposure(score_df)

    if baskets_df is not None and not baskets_df.empty:
        # Placeholder for basket logic if passed as df
        pass

    return sym_exp

def summarize_factor_exposure(exposure_df: pd.DataFrame) -> dict:
    if exposure_df.empty:
        return {"total_records": 0}

    high_pos = len(exposure_df[exposure_df['exposure_label'] == 'high_positive'])
    high_neg = len(exposure_df[exposure_df['exposure_label'] == 'high_negative'])

    return {
        "total_records": len(exposure_df),
        "high_positive_exposures": high_pos,
        "high_negative_exposures": high_neg
    }
