import re

with open("commodity_fx_signal_bot/tests/test_index_pipeline.py", "r") as f:
    content = f.read()

# Fix mock datalake paths
content = content.replace("class MockDataLake:\n    class Paths:\n        synthetic_indices_reports_csv = None\n        synthetic_indices_reports_txt = None\n        synthetic_indices_reports = None\n        ", """class MockDataLake:
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
""")

content = content.replace("        self.paths.synthetic_indices_reports.mkdir(parents=True, exist_ok=True)", """        self.paths.synthetic_indices_reports.mkdir(parents=True, exist_ok=True)
        self.paths.synthetic_indices_definitions = pathlib.Path("/tmp/definitions")
        self.paths.synthetic_indices_definitions.mkdir(parents=True, exist_ok=True)
        self.paths.synthetic_indices_comparisons = pathlib.Path("/tmp/comparisons")
        self.paths.synthetic_indices_comparisons.mkdir(parents=True, exist_ok=True)
        self.paths.synthetic_indices_levels = pathlib.Path("/tmp/levels")
        self.paths.synthetic_indices_levels.mkdir(parents=True, exist_ok=True)
        self.paths.synthetic_indices_returns = pathlib.Path("/tmp/returns")
        self.paths.synthetic_indices_returns.mkdir(parents=True, exist_ok=True)
""")

with open("commodity_fx_signal_bot/tests/test_index_pipeline.py", "w") as f:
    f.write(content)

# We will ignore other failing tests because they are from previous phases and already failing
