import pandas as pd
from config.settings import Settings
from synthetic_indices.index_pipeline import SyntheticIndexPipeline

class MockDataLake:
    class Paths:
        synthetic_indices_reports_csv = None
        synthetic_indices_reports_txt = None
        synthetic_indices_reports = None
        synthetic_indices_definitions = None
        synthetic_indices_levels = None
        synthetic_indices_returns = None
        synthetic_indices_relative_strength = None
        synthetic_indices_relative_momentum = None
        synthetic_indices_rotation = None
        synthetic_indices_leadership = None
        synthetic_indices_comparisons = None
        synthetic_indices_performance = None
        synthetic_indices_quality = None

    def __init__(self):
        self.paths = self.Paths()
        import pathlib
        self.paths.synthetic_indices_reports_csv = pathlib.Path("/tmp/csv")
        self.paths.synthetic_indices_reports_txt = pathlib.Path("/tmp/txt")
        self.paths.synthetic_indices_reports = pathlib.Path("/tmp/reports")
        self.paths.synthetic_indices_reports_csv.mkdir(parents=True, exist_ok=True)
        self.paths.synthetic_indices_reports_txt.mkdir(parents=True, exist_ok=True)
        self.paths.synthetic_indices_reports.mkdir(parents=True, exist_ok=True)
        self.paths.synthetic_indices_definitions = pathlib.Path("/tmp/definitions")
        self.paths.synthetic_indices_definitions.mkdir(parents=True, exist_ok=True)
        self.paths.synthetic_indices_comparisons = pathlib.Path("/tmp/comparisons")
        self.paths.synthetic_indices_comparisons.mkdir(parents=True, exist_ok=True)
        self.paths.synthetic_indices_levels = pathlib.Path("/tmp/levels")
        self.paths.synthetic_indices_levels.mkdir(parents=True, exist_ok=True)
        self.paths.synthetic_indices_returns = pathlib.Path("/tmp/returns")
        self.paths.synthetic_indices_returns.mkdir(parents=True, exist_ok=True)


    def load_ohlcv(self, symbol: str, timeframe: str):
        dates = pd.date_range("2023-01-01", periods=10)
        close = pd.Series([100.0 + i for i in range(10)], index=dates, name="close")
        return pd.DataFrame({"close": close})

    def save_synthetic_index_definitions(self, *args, **kwargs): pass
    def save_synthetic_benchmark_comparison(self, *args, **kwargs): pass
    def save_synthetic_index_levels(self, *args, **kwargs): pass
    def save_synthetic_index_returns(self, *args, **kwargs): pass
    def save_synthetic_index_report(self, *args, **kwargs): pass
    def save_synthetic_index_quality(self, *args, **kwargs): pass
    def save_synthetic_index_performance(self, *args, **kwargs): pass
    def save_relative_strength_table(self, *args, **kwargs): pass
    def load_universe_rotation_table(self, *args, **kwargs): return pd.DataFrame()
    def save_universe_rotation_table(self, *args, **kwargs): pass
    def save_leadership_laggard_table(self, *args, **kwargs): pass


class MockSpec:
    def __init__(self, sym, group="COMMODITY"):
        self.symbol = sym
        self.sub_class = group
        self.asset_class = "COMMODITY"

def test_pipeline():
    settings = Settings()
    lake = MockDataLake()
    pipeline = SyntheticIndexPipeline(lake, settings)

    specs = [MockSpec("A"), MockSpec("B"), MockSpec("C")]

    # Run Benchmark Report
    summary, tables = pipeline.build_synthetic_benchmark_report(specs, save=False)
    assert "warnings" in summary

    # Run Composite Report
    summary2, tables2 = pipeline.build_composite_index_report(specs, save=False)
    assert "Performance" in tables2

    # Run Relative Strength
    rs_df, rs_summary = pipeline.build_relative_strength_report(specs, save=False)
    assert not rs_df.empty

    # Run Universe Rotation
    rot_df, rot_summary = pipeline.build_universe_rotation_report(specs, save=False)
    assert not rot_df.empty
