import pytest
from pathlib import Path
from advanced_news_metadata.news_pipeline import NewsMetadataPipeline
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile

def test_news_pipeline():
    pipeline = NewsMetadataPipeline(None, None, Path("."))
    
    profiles, _ = pipeline.build_news_profiles_and_domains(save=False)
    assert not profiles["profiles"].empty
    assert not profiles["domains"].empty

    sources, _ = pipeline.build_news_sources_and_schemas(save=False)
    assert not sources["sources"].empty
    assert not sources["categories"].empty
    assert not sources["metadata_schema"].empty
    assert not sources["item_reference_schema"].empty

    tags, _ = pipeline.build_news_tags_and_linkages(save=False)
    assert not tags["asset_tags"].empty
    assert not tags["event_linkage"].empty

    reqs, _ = pipeline.build_news_requirements(save=False)
    assert not reqs["sentiment"].empty

    caps, _ = pipeline.build_news_provider_metadata_and_capabilities(save=False)
    assert not caps["capabilities"].empty

    contracts, _ = pipeline.build_news_contracts(save=False)
    assert not contracts["safety"].empty

    dry_df, _ = pipeline.build_news_dry_run_fixture(save=False)
    assert not dry_df.empty

    placeholders, _ = pipeline.build_news_placeholders(save=False)
    assert "manual" in placeholders

    health_df, _ = pipeline.build_news_health_check(save=False)
    assert not health_df.empty

    status_df, _ = pipeline.build_news_status(save=False)
    assert not status_df.empty
