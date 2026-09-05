from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.provider_name_normalization import (
    build_provider_name_normalization_registry,
    normalize_provider_name,
)


def test_provider_name_normalization():
    assert normalize_provider_name("FX Dry Run Fixture Provider") == "fx_dry_run_fixture_provider"
    assert normalize_provider_name("commodity dry run") == "commodity_dry_run_fixture_provider"
    assert normalize_provider_name("Macro Official Placeholder") == "macro_official_api_provider_placeholder"
    assert normalize_provider_name("News Public Dataset") == "news_public_dataset_provider_placeholder"

    prof = get_default_data_normalization_profile()
    df, summary = build_provider_name_normalization_registry(prof)
    assert not df.empty
    assert summary["total_mappings"] >= 5
