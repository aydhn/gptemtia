from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.simplification_domain_registry import build_simplification_domain_registry

def test_build_simplification_domain_registry():
    p = get_default_local_simplification_profile()
    df, summary = build_simplification_domain_registry(p)
    assert not df.empty
    assert "required_reports" in df.columns
    assert "Bu registry official architecture simplification scope degildir." in summary["warnings"]
