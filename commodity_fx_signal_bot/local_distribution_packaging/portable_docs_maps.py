import pandas as pd
from .packaging_config import LocalDistributionPackagingProfile
from .packaging_models import PortableDocsItem, build_portable_docs_item_id

def build_default_portable_docs_items(profile: LocalDistributionPackagingProfile) -> list[PortableDocsItem]:
    return [
        PortableDocsItem(
            portable_doc_id=build_portable_docs_item_id("README", "root"),
            doc_title="README",
            source_ref="root",
            route_label="package_route_operator",
            reading_priority=1,
            artifact_label="artifact_documentation_only",
            warnings=["Not real advice"]
        )
    ]

def build_portable_docs_reading_order(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_portable_docs_items(profile)
    df = pd.DataFrame([i.__dict__ for i in items])
    return df, summarize_portable_docs_map(df)

def build_portable_docs_role_map(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_portable_docs_items(profile)
    df = pd.DataFrame([i.__dict__ for i in items])
    return df, summarize_portable_docs_map(df)

def build_portable_docs_limitation_register(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"limitation": "No cloud sync"}])
    return df, summarize_portable_docs_map(df)

def summarize_portable_docs_map(df: pd.DataFrame) -> dict:
    return {"status": "generated", "rows": len(df)}
