import pandas as pd
from typing import Tuple, Dict, List
from advanced_news_metadata.news_provider_config import NewsProviderProfile
from advanced_news_metadata.news_provider_models import NewsProviderContractItem, build_news_provider_contract_id

def build_default_news_adapter_contract_items(profile: NewsProviderProfile) -> List[NewsProviderContractItem]:
    forbidden_base = [
        "no scraping", "no news page scraping", "no browser automation",
        "no hidden API reverse engineering", "no paywall bypass", "no credential output",
        "no full article download", "no copyrighted article copy", "no broker/live/order",
        "no investment advice", "no news directional claim", "no sentiment-as-signal",
        "no external LLM", "no vector DB", "no embedding API", "no deployment",
        "no destructive file action"
    ]
    
    contract_areas = [
        ("News metadata contract", "Valid metadata fields complying with news_metadata_schema.", "Structured metadata DataFrame or response."),
        ("News source registry contract", "Canonical source identifiers and category metadata.", "Registered sources without credential requirements."),
        ("News item reference contract", "Canonical pointers and content hash placeholders.", "Reference records without raw article text."),
        ("News tag mapping contract", "Asset, macro, commodity, and FX tag labels.", "Standardized canonical taxonomy tags."),
        ("News event linkage contract", "News topics and calendar release linkages.", "Bi-directional event association references."),
        ("News request validation contract", "Valid NewsProviderRequest instance with metadata_only=True.", "Validated request or descriptive validation error."),
        ("News fetch response contract", "Executed request parameters in dry-run or local mode.", "Conforming NewsProviderResponse instance."),
        ("News error handling contract", "Failure or constraint violation.", "Standardized NewsProviderError without crashing."),
        ("News manual file contract", "Offline user-supplied metadata files.", "Parsed metadata records without file alteration."),
        ("News local cache contract", "Local lake cached news metadata.", "Read-only access to cached files."),
        ("News official API placeholder contract", "Public agency announcement requests.", "Offline placeholder response without network call."),
        ("News licensed placeholder contract", "Institutional feed requests.", "Offline placeholder with licensing warning."),
        ("News public dataset placeholder contract", "Public benchmark dataset requests.", "Offline placeholder with usage terms review note."),
        ("News dry-run fixture contract", "Synthetic request testing.", "Valid synthetic metadata response."),
        ("News sentiment placeholder requirement contract", "Topic categorization for downstream phases.", "Categorical sentiment placeholder without NLP signals."),
        ("News impact placeholder requirement contract", "Qualitative impact tags.", "Impact placeholder without price directional forecasts."),
        ("News freshness requirement contract", "Publication timestamps and staleness thresholds.", "Standardized UTC timestamp evaluation."),
        ("News deduplication requirement contract", "Duplicate key and similarity thresholds.", "Deduplication metadata attributes for Phase 112."),
        ("News output validation contract", "Generated news metadata outputs.", "Compliance with Phase 112-115 quality standards."),
        ("News copyright boundary contract", "External news reference requests.", "Strict enforcement of zero raw article copying."),
        ("News safety contract", "All operations within news provider layer.", "Absolute adherence to non-production safety invariants.")
    ]

    items = []
    for area, inp, outp in contract_areas:
        items.append(NewsProviderContractItem(
            contract_id=build_news_provider_contract_id(area),
            contract_area=area,
            input_expectation=inp,
            output_expectation=outp,
            forbidden_behavior=forbidden_base,
            manual_review_required=True
        ))
    return items

def build_news_adapter_contract(profile: NewsProviderProfile) -> Tuple[pd.DataFrame, Dict]:
    items = build_default_news_adapter_contract_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    summary = summarize_news_adapter_contract(df)
    return df, summary

def summarize_news_adapter_contract(df: pd.DataFrame) -> Dict:
    return {
        "total_contracts": len(df),
        "contract_areas": df["contract_area"].tolist() if not df.empty else []
    }
