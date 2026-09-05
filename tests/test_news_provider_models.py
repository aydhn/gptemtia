import pytest
from advanced_news_metadata.news_provider_models import (
    NewsProviderProfileItem,
    NewsDomain,
    NewsSource,
    NewsSourceCategory,
    NewsMetadataSchemaField,
    NewsItemReferenceField,
    NewsTag,
    NewsEventLinkage,
    NewsProviderCapability,
    NewsProviderMetadata,
    NewsProviderRequest,
    NewsProviderResponse,
    NewsProviderError,
    NewsProviderContractItem,
    NewsProviderFinding,
    to_dict
)

def test_models_instantiation_and_to_dict():
    domain = NewsDomain("dom_1", "news_metadata_domain", "News Metadata Domain", "Metadata operations", ["report.csv"], [])
    d_dict = to_dict(domain)
    assert d_dict["domain_id"] == "dom_1"
    assert d_dict["domain_label"] == "news_metadata_domain"

    req = NewsProviderRequest("req_1", "prov", "news_data_metadata")
    assert req.dry_run is True
    assert req.local_only is True
    assert req.metadata_only is True
