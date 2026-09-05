"""Export routes."""
import pandas as pd
from .export_config import LocalDocumentationExportProfile
from .export_models import DocumentationPageItem, build_documentation_page_item_id

def build_default_documentation_routes(profile: LocalDocumentationExportProfile) -> list[DocumentationPageItem]:
    return [
        DocumentationPageItem(
            page_id=build_documentation_page_item_id("RouteMap", "output/routes.md"),
            page_title="Route Map",
            source_ref="src/routes",
            output_ref="output/routes.md",
            format_label="format_markdown",
            route_label="docs_route_reviewer",
            manual_review_required=True,
            warnings=["Not an SOP"]
        )
    ]

def build_documentation_export_route_map(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    routes = build_default_documentation_routes(profile)
    df = pd.DataFrame([r.__dict__ for r in routes])
    return df, summarize_documentation_export_routes(df)

def build_documentation_export_role_map(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"role": "Analyst", "access": "read"}])
    return df, summarize_documentation_export_routes(df)

def summarize_documentation_export_routes(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
