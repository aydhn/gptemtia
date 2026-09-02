from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.simplification_validation import build_simplification_validation_report

def test_validation():
    p = get_default_local_simplification_profile()
    df, summary = build_simplification_validation_report({}, p)
    assert not df.empty
