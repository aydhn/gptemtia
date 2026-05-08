import pandas as pd
from dataclasses import dataclass
import dataclasses

@dataclass
class DatasetSplitManifest:
    symbol: str
    timeframe: str
    profile: str
    target_col: str
    train_start: str
    train_end: str
    validation_start: str | None
    validation_end: str | None
    test_start: str
    test_end: str
    embargo_bars: int
    purged: bool
    row_counts: dict
    warnings: list[str]

def chronological_train_test_split(dataset: pd.DataFrame, test_size_ratio: float = 0.20) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    n = len(dataset)
    if n == 0:
        return pd.DataFrame(), pd.DataFrame(), {"warnings": ["Empty dataset"]}

    test_size = int(n * test_size_ratio)
    train_size = n - test_size

    train_df = dataset.iloc[:train_size]
    test_df = dataset.iloc[train_size:]

    return train_df, test_df, {"train_size": len(train_df), "test_size": len(test_df)}

def chronological_train_validation_test_split(dataset: pd.DataFrame, validation_size_ratio: float = 0.20, test_size_ratio: float = 0.20) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict]:
    n = len(dataset)
    if n == 0:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), {"warnings": ["Empty dataset"]}

    test_size = int(n * test_size_ratio)
    val_size = int(n * validation_size_ratio)
    train_size = n - test_size - val_size

    train_df = dataset.iloc[:train_size]
    val_df = dataset.iloc[train_size : train_size+val_size]
    test_df = dataset.iloc[train_size+val_size:]

    return train_df, val_df, test_df, {"train_size": len(train_df), "val_size": len(val_df), "test_size": len(test_df)}

def apply_embargo(train_df: pd.DataFrame, test_df: pd.DataFrame, embargo_bars: int = 5) -> tuple[pd.DataFrame, dict]:
    if train_df.empty or embargo_bars <= 0:
        return train_df, {}

    # Drop the last 'embargo_bars' from train_df
    embargoed_train = train_df.iloc[:-embargo_bars]

    return embargoed_train, {"embargo_bars_removed": len(train_df) - len(embargoed_train)}

def apply_purging_for_target_horizon(train_df: pd.DataFrame, test_df: pd.DataFrame, max_horizon: int) -> tuple[pd.DataFrame, dict]:
    # Similar to embargo, but conceptualized specifically for overlap
    # In a simple chronological split, purging is just dropping the end of train
    # equivalent to max_horizon.
    return apply_embargo(train_df, test_df, max_horizon)

def build_split_manifest(
    symbol: str,
    timeframe: str,
    profile: str,
    target_col: str,
    train_df: pd.DataFrame,
    val_df: pd.DataFrame | None,
    test_df: pd.DataFrame,
    embargo_bars: int,
    purged: bool,
    warnings: list[str]
) -> DatasetSplitManifest:

    val_start = str(val_df.index[0]) if val_df is not None and not val_df.empty else None
    val_end = str(val_df.index[-1]) if val_df is not None and not val_df.empty else None

    return DatasetSplitManifest(
        symbol=symbol,
        timeframe=timeframe,
        profile=profile,
        target_col=target_col,
        train_start=str(train_df.index[0]) if not train_df.empty else "",
        train_end=str(train_df.index[-1]) if not train_df.empty else "",
        validation_start=val_start,
        validation_end=val_end,
        test_start=str(test_df.index[0]) if not test_df.empty else "",
        test_end=str(test_df.index[-1]) if not test_df.empty else "",
        embargo_bars=embargo_bars,
        purged=purged,
        row_counts={
             "train": len(train_df),
             "validation": len(val_df) if val_df is not None else 0,
             "test": len(test_df)
        },
        warnings=warnings
    )

def split_manifest_to_dict(manifest: DatasetSplitManifest) -> dict:
    return dataclasses.asdict(manifest)
