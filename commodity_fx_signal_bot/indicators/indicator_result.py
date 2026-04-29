from dataclasses import asdict, dataclass

import pandas as pd


@dataclass
class IndicatorResult:
    name: str
    columns: list[str]
    dataframe: pd.DataFrame
    params: dict
    category: str
    warmup_period: int
    nan_ratio: float
    success: bool
    error: str = ""
    notes: str = ""


def indicator_result_to_dict(result: IndicatorResult) -> dict:
    d = asdict(result)
    # Don't serialize the dataframe in the dictionary
    d.pop("dataframe", None)
    return d
