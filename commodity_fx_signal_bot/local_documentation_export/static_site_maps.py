"""Static site maps."""
import pandas as pd
from .export_config import LocalDocumentationExportProfile
from .export_models import DocumentationPageItem, build_documentation_page_item_id

def build_default_static_site_pages(profile: LocalDocumentationExportProfile) -> list[DocumentationPageItem]:
    return [
        DocumentationPageItem(
            page_id=build_documentation_page_item_id("index", "output/index.html"),
            page_title="Index",
            source_ref="src/index.md",
            output_ref="output/index.html",
            format_label="format_html_rehearsal",
            route_label="docs_route_operator",
            manual_review_required=True,
            warnings=["Gerçek hosting değil"]
        )
    ]

def build_static_site_page_registry(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    pages = build_default_static_site_pages(profile)
    df = pd.DataFrame([p.__dict__ for p in pages])
    return df, summarize_static_site_map(df)

def build_static_site_navigation_tree(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"nav_item": "index", "parent": "root"}])
    return df, summarize_static_site_map(df)

def build_static_site_asset_registry(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"asset": "style.css"}])
    return df, summarize_static_site_map(df)

def summarize_static_site_map(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
