from typing import Optional, List, Tuple, Dict
import pandas as pd

def build_symbol_tracking_table(archive_df: pd.DataFrame, symbol: str, timeframe: Optional[str] = None) -> pd.DataFrame:
    if archive_df.empty:
        return pd.DataFrame()
    mask = archive_df["symbol"] == symbol
    if timeframe:
        mask = mask & (archive_df["timeframe"] == timeframe)
    symbol_df = archive_df[mask].copy()
    if symbol_df.empty:
        return symbol_df
    symbol_df = symbol_df.sort_values("created_at_utc").reset_index(drop=True)
    return calculate_tracking_deltas(symbol_df)

def build_universe_tracking_table(archive_df: pd.DataFrame, timeframe: Optional[str] = None) -> pd.DataFrame:
    if archive_df.empty:
        return pd.DataFrame()
    mask = archive_df["report_type"] == "symbol"
    if timeframe:
        mask = mask & (archive_df["timeframe"] == timeframe)
    universe_df = archive_df[mask].copy()
    if universe_df.empty:
        return universe_df
    universe_df = universe_df.sort_values(["symbol", "created_at_utc"]).reset_index(drop=True)
    results = []
    for sym, group in universe_df.groupby("symbol"):
        group_with_deltas = calculate_tracking_deltas(group)
        latest = group_with_deltas.iloc[-1:]
        results.append(latest)
    if results:
        return pd.concat(results, ignore_index=True)
    return pd.DataFrame()

def calculate_tracking_deltas(tracking_df: pd.DataFrame) -> pd.DataFrame:
    df = tracking_df.copy()
    if len(df) > 1:
        df["research_score_delta"] = df["research_score"].diff()
        df["warning_delta"] = df["warning_count"].diff()
        df["missing_sources_delta"] = df["missing_sources_count"].diff()
    else:
        df["research_score_delta"] = None
        df["warning_delta"] = None
        df["missing_sources_delta"] = None
    def _assign_label(delta):
        if pd.isna(delta):
            return "insufficient_history"
        if delta > 0.05:
            return "improved"
        elif delta < -0.05:
            return "deteriorated"
        return "unchanged"
    df["comparison_label"] = df["research_score_delta"].apply(_assign_label)
    columns_to_keep = [
        "created_at_utc", "report_id", "symbol", "timeframe",
        "research_score", "research_score_delta",
        "warning_count", "warning_delta",
        "missing_sources_count", "missing_sources_delta",
        "quality_passed", "comparison_label"
    ]
    columns = [c for c in columns_to_keep if c in df.columns]
    return df[columns]

def summarize_tracking_table(tracking_df: pd.DataFrame) -> Dict:
    if tracking_df.empty:
        return {"symbols_tracked": 0}
    return {
        "symbols_tracked": int(tracking_df["symbol"].nunique()) if "symbol" in tracking_df.columns else 0,
        "improved_count": int((tracking_df["comparison_label"] == "improved").sum()) if "comparison_label" in tracking_df.columns else 0,
        "deteriorated_count": int((tracking_df["comparison_label"] == "deteriorated").sum()) if "comparison_label" in tracking_df.columns else 0
    }

def build_periodic_tracking_report(archive_df: pd.DataFrame, symbols: Optional[List[str]] = None, timeframe: str = "1d") -> Tuple[pd.DataFrame, Dict]:
    if symbols:
        results = []
        for sym in symbols:
            df = build_symbol_tracking_table(archive_df, sym, timeframe)
            if not df.empty:
                results.append(df.iloc[-1:])
        if results:
            final_df = pd.concat(results, ignore_index=True)
        else:
            final_df = pd.DataFrame()
    else:
        final_df = build_universe_tracking_table(archive_df, timeframe)
    summary = summarize_tracking_table(final_df)
    summary["disclaimer"] = "Periodic tracking score/warning/missing source deltas are for research monitoring only and do not constitute trade signals."
    return final_df, summary
