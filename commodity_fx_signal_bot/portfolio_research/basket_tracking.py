import pandas as pd

def build_basket_tracking_table(performance_df: pd.DataFrame, previous_tracking_df: pd.DataFrame | None = None) -> pd.DataFrame:
    if performance_df.empty:
        return pd.DataFrame()

    df = performance_df.copy()

    if previous_tracking_df is not None and not previous_tracking_df.empty:
        if 'basket_id' in previous_tracking_df.columns:
            prev_indexed = previous_tracking_df.set_index('basket_id')
        else:
            prev_indexed = previous_tracking_df

        curr_indexed = df.set_index('basket_id') if 'basket_id' in df.columns else df

        common_ids = curr_indexed.index.intersection(prev_indexed.index)

        curr_indexed['total_return_delta'] = 0.0
        curr_indexed['max_drawdown_delta'] = 0.0
        curr_indexed['volatility_delta'] = 0.0
        curr_indexed['diversification_delta'] = 0.0
        curr_indexed['tracking_label'] = "new"

        for bid in common_ids:
            try:
                curr_indexed.loc[bid, 'total_return_delta'] = curr_indexed.loc[bid, 'total_return_pct'] - prev_indexed.loc[bid, 'total_return_pct']
                curr_indexed.loc[bid, 'max_drawdown_delta'] = curr_indexed.loc[bid, 'max_drawdown_pct'] - prev_indexed.loc[bid, 'max_drawdown_pct']
                curr_indexed.loc[bid, 'volatility_delta'] = curr_indexed.loc[bid, 'annualized_volatility_pct'] - prev_indexed.loc[bid, 'annualized_volatility_pct']
                curr_indexed.loc[bid, 'diversification_delta'] = curr_indexed.loc[bid, 'diversification_score'] - prev_indexed.loc[bid, 'diversification_score']

                if curr_indexed.loc[bid, 'total_return_delta'] > 0 and curr_indexed.loc[bid, 'max_drawdown_delta'] > 0:
                    curr_indexed.loc[bid, 'tracking_label'] = "improved"
                elif curr_indexed.loc[bid, 'total_return_delta'] < 0 and curr_indexed.loc[bid, 'max_drawdown_delta'] < 0:
                    curr_indexed.loc[bid, 'tracking_label'] = "degraded"
                else:
                    curr_indexed.loc[bid, 'tracking_label'] = "mixed"
            except Exception:
                pass

        return curr_indexed.reset_index()
    else:
        df['total_return_delta'] = 0.0
        df['max_drawdown_delta'] = 0.0
        df['volatility_delta'] = 0.0
        df['diversification_delta'] = 0.0
        df['tracking_label'] = "baseline"
        return df

def calculate_basket_performance_deltas(current_df: pd.DataFrame, previous_df: pd.DataFrame | None) -> pd.DataFrame:
    return build_basket_tracking_table(current_df, previous_df)

def summarize_basket_tracking(tracking_df: pd.DataFrame) -> dict:
    if tracking_df.empty:
        return {"tracked_baskets": 0, "improved": 0, "degraded": 0}

    counts = tracking_df['tracking_label'].value_counts().to_dict()

    return {
        "tracked_baskets": len(tracking_df),
        "improved": counts.get("improved", 0),
        "degraded": counts.get("degraded", 0),
        "mixed": counts.get("mixed", 0),
        "baseline": counts.get("baseline", 0),
        "new": counts.get("new", 0),
        "note": "Tracking degisimi trade sinyali degildir. Improved basket gercek portfoy onerisi degildir."
    }

def build_basket_tracking_report(performance_df: pd.DataFrame, previous_tracking_df: pd.DataFrame | None = None) -> tuple[pd.DataFrame, dict]:
    tracking_df = build_basket_tracking_table(performance_df, previous_tracking_df)
    summary = summarize_basket_tracking(tracking_df)

    return tracking_df, summary
