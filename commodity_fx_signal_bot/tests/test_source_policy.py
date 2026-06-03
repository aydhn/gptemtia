from portable_packaging.source_policy import (
    build_source_inclusion_policy,
    build_source_exclusion_policy,
    validate_source_policy
)
from portable_packaging.packaging_config import get_default_portable_packaging_profile

def test_source_policy():
    profile = get_default_portable_packaging_profile()

    inc = build_source_inclusion_policy(profile)
    assert not inc.empty

    exc = build_source_exclusion_policy(profile)
    assert not exc.empty

    val = validate_source_policy(inc, exc)
    assert val["valid"]
