import pandas as pd
import numpy as np


def calculate_drawdown_series(equity_curve: pd.DataFrame) -> pd.DataFrame:
    if equity_curve.empty or "equity" not in equity_curve.columns:
        return pd.DataFrame()

    df = pd.DataFrame(index=equity_curve.index)
    df["equity"] = equity_curve["equity"]
    df["rolling_peak"] = df["equity"].cummax()
    df["drawdown"] = df["equity"] - df["rolling_peak"]

    rolling_peak_safe = df["rolling_peak"].replace(0, np.nan)
    df["drawdown_pct"] = df["drawdown"] / rolling_peak_safe
    df["drawdown_pct"] = df["drawdown_pct"].fillna(0)

    df["is_underwater"] = df["drawdown"] < 0
    return df


def calculate_max_drawdown(equity_curve: pd.DataFrame) -> dict:
    if equity_curve.empty:
        return {"max_drawdown": 0.0, "max_drawdown_pct": 0.0}

    dd_series = calculate_drawdown_series(equity_curve)
    if dd_series.empty:
        return {"max_drawdown": 0.0, "max_drawdown_pct": 0.0}

    return {
        "max_drawdown": float(abs(dd_series["drawdown"].min())),
        "max_drawdown_pct": float(abs(dd_series["drawdown_pct"].min())),
    }


def calculate_drawdown_durations(drawdown_df: pd.DataFrame) -> pd.DataFrame:
    if drawdown_df.empty or "is_underwater" not in drawdown_df.columns:
        return pd.DataFrame()

    is_under = drawdown_df["is_underwater"].astype(int)
    diff = is_under.diff().fillna(is_under.iloc[0])

    starts = drawdown_df.index[diff == 1].tolist()
    ends = drawdown_df.index[diff == -1].tolist()

    if len(starts) > len(ends):
        ends.append(drawdown_df.index[-1])

    durations = []
    for start, end in zip(starts, ends):
        period = drawdown_df.loc[start:end]
        max_dd = period["drawdown_pct"].min()
        max_dd_amount = period["drawdown"].min()
        valley_date = period["drawdown_pct"].idxmin()

        duration_bars = len(period)

        if end != drawdown_df.index[-1] or diff.iloc[-1] == -1:
            recovery_bars = len(period.loc[valley_date:end]) - 1
        else:
            recovery_bars = np.nan

        durations.append(
            {
                "drawdown_start": start,
                "drawdown_end": end,
                "valley_date": valley_date,
                "max_drawdown": abs(max_dd_amount),
                "max_drawdown_pct": abs(max_dd),
                "duration_bars": duration_bars,
                "recovery_bars": recovery_bars,
                "is_recovered": pd.notna(recovery_bars),
            }
        )

    return pd.DataFrame(durations)


def calculate_top_drawdowns(drawdown_df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    durations_df = calculate_drawdown_durations(drawdown_df)
    if durations_df.empty:
        return pd.DataFrame()

    return (
        durations_df.sort_values(by="max_drawdown_pct", ascending=False)
        .head(top_n)
        .reset_index(drop=True)
    )


def calculate_underwater_periods(drawdown_df: pd.DataFrame) -> pd.DataFrame:
    durations_df = calculate_drawdown_durations(drawdown_df)
    if durations_df.empty:
        return pd.DataFrame()
    return durations_df[~durations_df["is_recovered"]].reset_index(drop=True)


def build_drawdown_analysis(equity_curve: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    if equity_curve.empty:
        return pd.DataFrame(), {}

    dd_series = calculate_drawdown_series(equity_curve)
    max_dd = calculate_max_drawdown(equity_curve)
    top_dds = calculate_top_drawdowns(dd_series)

    summary = {
        "max_drawdown": max_dd["max_drawdown"],
        "max_drawdown_pct": max_dd["max_drawdown_pct"],
    }

    if not top_dds.empty:
        summary["longest_drawdown_bars"] = int(top_dds["duration_bars"].max())
        recovered_dds = top_dds[top_dds["is_recovered"]]
        summary["avg_recovery_bars"] = (
            float(recovered_dds["recovery_bars"].mean())
            if not recovered_dds.empty
            else None
        )

        current_dd = dd_series["is_underwater"].iloc[-1]
        summary["currently_underwater"] = bool(current_dd)
        if current_dd:
            summary["current_drawdown_pct"] = float(
                abs(dd_series["drawdown_pct"].iloc[-1])
            )
        else:
            summary["current_drawdown_pct"] = 0.0

    else:
        summary["longest_drawdown_bars"] = 0
        summary["avg_recovery_bars"] = 0
        summary["currently_underwater"] = False
        summary["current_drawdown_pct"] = 0.0

    return dd_series, summary
