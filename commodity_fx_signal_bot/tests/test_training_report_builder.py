import pandas as pd
from local_training.training_report_builder import build_training_domain_registry_markdown_report, build_training_disclaimer

def test_report_builder():
    r = build_training_domain_registry_markdown_report({}, pd.DataFrame([{"1": 2}]))
    assert "UYARI" in r
    assert "UYARI" in build_training_disclaimer()
