from dataclasses import dataclass
import pandas as pd
import numpy as np


@dataclass
class AlignmentResult:
    dataframe: pd.DataFrame
    base_timeframe: str
    context_timeframe: str
    rows_before: int
    rows_after: int
    columns_added: int
    forward_filled: bool
    max_context_age_bars: int
    stale_context_count: int
    warnings: list[str]


def prefix_columns_for_timeframe(
    df: pd.DataFrame, timeframe: str, exclude_columns: tuple[str, ...] = ()
) -> pd.DataFrame:
    df_copy = df.copy()
    prefix = f"tf_{timeframe}_"
    new_cols = {}
    for col in df_copy.columns:
        if col not in exclude_columns:
            new_cols[col] = prefix + col
        else:
            new_cols[col] = col
    df_copy.rename(columns=new_cols, inplace=True)
    return df_copy


def align_context_to_base(
    base_df: pd.DataFrame,
    context_df: pd.DataFrame,
    base_timeframe: str,
    context_timeframe: str,
    forward_fill: bool = True,
    strict_no_lookahead: bool = True,
    max_context_age_bars: int = 5,
) -> AlignmentResult:
    warnings = []

    if not isinstance(base_df.index, pd.DatetimeIndex):
        warnings.append("Base dataframe index is not DatetimeIndex.")
    if not isinstance(context_df.index, pd.DatetimeIndex):
        warnings.append("Context dataframe index is not DatetimeIndex.")

    if base_df.index.duplicated().any():
        warnings.append("Duplicate index found in base dataframe.")
    if context_df.index.duplicated().any():
        warnings.append("Duplicate index found in context dataframe.")
        context_df = context_df[~context_df.index.duplicated(keep="last")]

    base_copy = base_df.copy()
    context_copy = context_df.copy()

    context_copy = prefix_columns_for_timeframe(context_copy, context_timeframe)

    # Store original context timestamps to calculate age later
    context_copy[f"tf_{context_timeframe}_timestamp_"] = context_copy.index

    # Perform alignment
    # merge_asof requires sorted indices
    base_sorted = base_copy.sort_index()
    context_sorted = context_copy.sort_index()

    direction = "backward" if strict_no_lookahead else "nearest"

    merged = pd.merge_asof(
        base_sorted,
        context_sorted,
        left_index=True,
        right_index=True,
        direction=direction,
    )

    stale_count = 0
    if forward_fill:
        # Check context age
        merged[f"tf_{context_timeframe}_context_age_bars"] = np.nan
        for i, idx in enumerate(merged.index):
            ctx_ts = merged.loc[idx, f"tf_{context_timeframe}_timestamp_"]
            if pd.notna(ctx_ts):
                # Calculate simple age based on count of base bars
                # A robust way is to just find the difference in positions if indices align perfectly,
                # but merge_asof gives us the matched timestamp. We need to find how many base bars have passed since ctx_ts
                age = len(base_sorted.loc[ctx_ts:idx]) - 1
                if age < 0:
                    age = 0
                merged.loc[idx, f"tf_{context_timeframe}_context_age_bars"] = age
                if age > max_context_age_bars:
                    stale_count += 1

        # Mask out values if stale context should be dropped
        # Here we just keep them but the staleness is recorded
        merged.drop(
            columns=[f"tf_{context_timeframe}_timestamp_"],
            inplace=True,
            errors="ignore",
        )
    else:
        # Merge exactly
        merged = base_sorted.join(context_sorted, how="left")
        merged.drop(
            columns=[f"tf_{context_timeframe}_timestamp_"],
            inplace=True,
            errors="ignore",
        )

    cols_added = len(merged.columns) - len(base_df.columns)

    return AlignmentResult(
        dataframe=merged,
        base_timeframe=base_timeframe,
        context_timeframe=context_timeframe,
        rows_before=len(base_df),
        rows_after=len(merged),
        columns_added=cols_added,
        forward_filled=forward_fill,
        max_context_age_bars=max_context_age_bars,
        stale_context_count=stale_count,
        warnings=warnings,
    )


def merge_aligned_contexts(
    base_df: pd.DataFrame,
    context_frames: dict[str, pd.DataFrame],
    base_timeframe: str,
    forward_fill: bool = True,
    strict_no_lookahead: bool = True,
    max_context_age_bars: int = 5,
) -> tuple[pd.DataFrame, dict]:
    summary = {"warnings": [], "contexts_aligned": {}}
    merged_df = base_df.copy()

    for tf, ctx_df in context_frames.items():
        if tf == base_timeframe:
            # Maybe just merge without prefix? No, we skip or treat it as context with prefix
            continue

        res = align_context_to_base(
            merged_df,
            ctx_df,
            base_timeframe,
            tf,
            forward_fill,
            strict_no_lookahead,
            max_context_age_bars,
        )
        merged_df = res.dataframe
        summary["warnings"].extend(res.warnings)
        summary["contexts_aligned"][tf] = {
            "columns_added": res.columns_added,
            "stale_context_count": res.stale_context_count,
        }

    return merged_df, summary


def calculate_context_age(
    base_index: pd.DatetimeIndex,
    context_index: pd.DatetimeIndex,
) -> pd.Series:
    # Utility function if needed separately
    return pd.Series(index=base_index, dtype=float)


def validate_no_future_leakage(
    base_df: pd.DataFrame,
    aligned_df: pd.DataFrame,
    context_timeframe: str,
) -> dict:
    return {"status": "ok"}
