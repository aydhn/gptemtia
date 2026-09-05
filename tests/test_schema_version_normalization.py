from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.schema_version_normalization import (
    build_schema_version_normalization_registry,
    normalize_schema_version,
)


def test_schema_version_normalization():
    assert normalize_schema_version("fx_quote", "1") == "v1.0"
    assert normalize_schema_version("fx_quote", "v2.1") == "v2.1"
    assert normalize_schema_version("fx_quote", None) == "unknown_version_manual_review"

    prof = get_default_data_normalization_profile()
    df, summary = build_schema_version_normalization_registry(prof)
    assert not df.empty
