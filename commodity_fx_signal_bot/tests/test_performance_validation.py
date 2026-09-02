from local_performance.performance_validation import validate_performance_domains
from local_performance.performance_config import get_default_local_performance_profile
import pandas as pd

def test_performance_validation():
    p = get_default_local_performance_profile()
    v = validate_performance_domains(pd.DataFrame(), p)
    assert v["valid"]
