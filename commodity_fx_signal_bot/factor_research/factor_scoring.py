import pandas as pd
import numpy as np
from .factor_models import FactorScoreRecord, FactorDefinition
from .factor_config import FactorResearchProfile
from .factor_labels import FACTOR_BUCKETS

def minmax_normalize_series(series: pd.Series, higher_is_better: bool = True) -> pd.Series:
    s_min = series.min()
    s_max = series.max()
    if s_min == s_max:
        return pd.Series(0.5, index=series.index)

    norm = (series - s_min) / (s_max - s_min)
    if not higher_is_better:
        norm = 1.0 - norm
    return norm

def zscore_series(series: pd.Series) -> pd.Series:
    s_mean = series.mean()
    s_std = series.std()
    if s_std == 0 or pd.isna(s_std):
         return pd.Series(0.0, index=series.index)
    return (series - s_mean) / s_std

def percentile_rank_series(series: pd.Series, higher_is_better: bool = True) -> pd.Series:
    ranks = series.rank(pct=True, ascending=higher_is_better)
    return ranks

def assign_factor_buckets(score_series: pd.Series, top_quantile: float, bottom_quantile: float) -> pd.Series:
    ranks = score_series.rank(pct=True, ascending=True)

    def get_bucket(r):
        if pd.isna(r):
            return "insufficient_factor_data"
        if r >= (1.0 - top_quantile):
            return "top_factor_bucket"
        elif r <= bottom_quantile:
            return "bottom_factor_bucket"
        else:
            return "middle_factor_bucket"

    return ranks.apply(get_bucket)

def build_factor_score_records(
    score_df: pd.DataFrame,
    factor_id: str,
    timeframe: str,
    timestamp: str,
    direction: str,
    profile: FactorResearchProfile
) -> list[FactorScoreRecord]:

    records = []
    if factor_id not in score_df.columns:
        return records

    raw_series = score_df[factor_id]
    higher_is_better = (direction != "lower_is_better")

    norm_series = minmax_normalize_series(raw_series, higher_is_better=higher_is_better)
    pct_series = percentile_rank_series(raw_series, higher_is_better=higher_is_better)
    rank_series = raw_series.rank(ascending=not higher_is_better, method='min')
    bucket_series = assign_factor_buckets(pct_series, profile.rank_top_quantile, profile.rank_bottom_quantile)

    for symbol in score_df.index:
        raw_val = raw_series.loc[symbol]
        if pd.isna(raw_val):
            records.append(FactorScoreRecord(
                symbol=symbol,
                timeframe=timeframe,
                timestamp=timestamp,
                factor_id=factor_id,
                raw_score=None,
                normalized_score=None,
                rank=None,
                percentile=None,
                bucket_label="insufficient_factor_data",
                warnings=["Missing data"]
            ))
        else:
            records.append(FactorScoreRecord(
                symbol=symbol,
                timeframe=timeframe,
                timestamp=timestamp,
                factor_id=factor_id,
                raw_score=float(raw_val),
                normalized_score=float(norm_series.loc[symbol]),
                rank=int(rank_series.loc[symbol]),
                percentile=float(pct_series.loc[symbol]),
                bucket_label=str(bucket_series.loc[symbol]),
                warnings=[]
            ))

    return records

def build_factor_score_table(
    factor_scores: dict[str, pd.Series],
    timeframe: str,
    timestamp: str,
    definitions: list[FactorDefinition],
    profile: FactorResearchProfile
) -> pd.DataFrame:

    if not factor_scores:
        return pd.DataFrame()

    score_df = pd.DataFrame(factor_scores)
    all_records = []

    def_map = {d.factor_id: d for d in definitions}

    for factor_id in score_df.columns:
        direction = def_map[factor_id].direction if factor_id in def_map else "higher_is_better"
        records = build_factor_score_records(score_df, factor_id, timeframe, timestamp, direction, profile)
        all_records.extend(records)

    if not all_records:
         return pd.DataFrame()

    from .factor_models import factor_score_record_to_dict
    return pd.DataFrame([factor_score_record_to_dict(r) for r in all_records])
