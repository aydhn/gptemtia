import numpy as np
import pandas as pd


def classify_inflation_regime(macro_df: pd.DataFrame) -> pd.DataFrame:
    """Classify inflation regimes."""
    df = pd.DataFrame(index=macro_df.index)

    if "TR_CPI_yoy_rising" in macro_df.columns:
        df["macro_tr_inflation_rising"] = (macro_df["TR_CPI_yoy_rising"] == 1.0).astype(
            int
        )
        df["macro_tr_inflation_falling"] = (
            macro_df["TR_CPI_yoy_falling"] == 1.0
        ).astype(int)

    if "US_CPI_yoy_rising" in macro_df.columns:
        df["macro_us_inflation_rising"] = (macro_df["US_CPI_yoy_rising"] == 1.0).astype(
            int
        )
        df["macro_us_inflation_falling"] = (
            macro_df["US_CPI_yoy_falling"] == 1.0
        ).astype(int)

    return df


def classify_fx_pressure_regime(macro_df: pd.DataFrame) -> pd.DataFrame:
    """Classify FX pressure regimes."""
    df = pd.DataFrame(index=macro_df.index)

    if "usdtry_depreciation_pressure" in macro_df.columns:
        df["macro_try_depreciation_pressure"] = (
            macro_df["usdtry_depreciation_pressure"] == 1.0
        ).astype(int)
        df["macro_try_stabilizing"] = (
            macro_df["usdtry_depreciation_pressure"] == 0.0
        ).astype(int)

    return df


def classify_real_return_regime(macro_df: pd.DataFrame) -> pd.DataFrame:
    """Classify regimes based on real returns."""
    df = pd.DataFrame(index=macro_df.index)

    if "real_gold_try_vs_tr_cpi" in macro_df.columns:
        # Check if real index is growing over a 6-month period
        idx_series = macro_df["real_gold_try_vs_tr_cpi"]
        df["macro_real_gold_positive"] = (idx_series > idx_series.shift(126)).astype(
            int
        )  # ~6 months
        df.loc[
            idx_series.isna() | idx_series.shift(126).isna(), "macro_real_gold_positive"
        ] = np.nan

    if "real_usdtry_vs_tr_cpi" in macro_df.columns:
        idx_series = macro_df["real_usdtry_vs_tr_cpi"]
        df["macro_real_usdtry_positive"] = (idx_series > idx_series.shift(126)).astype(
            int
        )
        df.loc[
            idx_series.isna() | idx_series.shift(126).isna(),
            "macro_real_usdtry_positive",
        ] = np.nan

    return df


def classify_macro_regime(macro_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Combine partial classifications into a master regime."""
    if macro_df.empty:
        return pd.DataFrame(), {"error": "Empty macro dataframe"}

    result = pd.DataFrame(index=macro_df.index)

    # Run sub-classifications
    inf_df = classify_inflation_regime(macro_df)
    fx_df = classify_fx_pressure_regime(macro_df)
    rr_df = classify_real_return_regime(macro_df)

    # Combine
    result = pd.concat([result, inf_df, fx_df, rr_df], axis=1)

    # Composite regimes
    result["macro_high_local_inflation_regime"] = 0
    if (
        "macro_tr_inflation_rising" in result.columns
        and "TR_CPI_yoy" in macro_df.columns
    ):
        # High inflation regime: rising inflation or simply YoY > 20%
        high_inf_mask = (result["macro_tr_inflation_rising"] == 1) | (
            macro_df["TR_CPI_yoy"] > 0.20
        )
        result.loc[high_inf_mask, "macro_high_local_inflation_regime"] = 1

    result["macro_disinflation_regime"] = 0
    if "macro_tr_inflation_falling" in result.columns:
        result.loc[
            result["macro_tr_inflation_falling"] == 1, "macro_disinflation_regime"
        ] = 1

    result["macro_fx_pressure_regime"] = 0
    if "macro_try_depreciation_pressure" in result.columns:
        result.loc[
            result["macro_try_depreciation_pressure"] == 1, "macro_fx_pressure_regime"
        ] = 1

    # Primary label heuristic
    def determine_label(row):
        score = 0
        if row.get("macro_high_local_inflation_regime", 0) == 1:
            score += 1
        if row.get("macro_fx_pressure_regime", 0) == 1:
            score += 1

        if score == 2:
            return "high_local_inflation_fx_pressure", 0.9
        elif score == 1:
            if row.get("macro_high_local_inflation_regime", 0) == 1:
                return "high_local_inflation", 0.7
            else:
                return "fx_pressure", 0.7
        elif row.get("macro_disinflation_regime", 0) == 1:
            return "disinflation", 0.8
        elif row.get("macro_real_gold_positive", 0) == 1:
            return "real_asset_supportive", 0.6
        else:
            # Check if all inputs are nan
            if pd.isna(row.get("macro_high_local_inflation_regime")):
                return "unknown", 0.0
            return "macro_stable", 0.5

    labels_scores = result.apply(determine_label, axis=1)
    result["macro_primary_label"] = [ls[0] for ls in labels_scores]
    result["macro_confidence"] = [ls[1] for ls in labels_scores]

    summary = {
        "rows": len(result),
        "columns": list(result.columns),
        "labels": (
            result["macro_primary_label"].value_counts().to_dict()
            if not result.empty
            else {}
        ),
    }

    return result, summary
