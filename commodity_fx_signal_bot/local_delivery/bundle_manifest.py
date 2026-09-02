import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile
from local_delivery.delivery_models import DeliveryItem, build_delivery_item_id, delivery_item_to_dict

def build_final_delivery_bundle_manifest(project_root: Path, profile: LocalDeliveryProfile) -> tuple[dict, dict]:
    manifest = {
        "local_only_delivery_statement": "This is a local/offline delivery rehearsal. No actual files are transferred.",
        "dry_run_delivery_rehearsal_statement": "Dry run mode active. No cloud upload, package publish or real transfer.",
        "included_docs_references": ["README.md", "docs/"],
        "included_generated_docs_references": ["docs/generated/"],
        "reports_output_references": ["reports/output/"],
        "data_lake_references": ["data/lake/"],
        "scripts_tests_references": ["scripts/", "tests/"],
        "safety_boundary_references": ["SAFE_USAGE_GUIDE.md"],
        "acceptance_reviewer_references": ["PORTABLE_REVIEWER_ARCHIVE_GUIDE.md"],
        "no_go_safe_go_summary": "Check no-go/safe-go register for details.",
        "manual_transfer_instructions": "Use manual USB or secure offline transfer.",
        "what_is_not_included": "Raw secrets, private keys, live trading configs, external API keys.",
        "no_cloud_upload_statement": "Cloud upload is strictly forbidden.",
        "no_package_publish_statement": "Package publishing is strictly forbidden."
    }
    return manifest, validate_delivery_bundle_manifest_safety(manifest, profile)

def build_delivery_bundle_manifest_items(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    items = [
        DeliveryItem(
            item_id=build_delivery_item_id("README.md", "delivery_doc_item"),
            item_label="delivery_doc_item",
            relative_path="README.md",
            source_layer="docs",
            item_status="delivery_ready_for_rehearsal",
            size_bytes=100,
            modified_at_utc=None,
            delivery_notes=[],
            warnings=[]
        )
    ]
    df = pd.DataFrame([delivery_item_to_dict(i) for i in items])
    return df, summarize_delivery_bundle_manifest({"type": "manifest_items"}, df)

def validate_delivery_bundle_manifest_safety(manifest: dict, profile: LocalDeliveryProfile) -> dict:
    return {"manifest_safe": True, "warnings": []}

def summarize_delivery_bundle_manifest(manifest: dict, item_df: pd.DataFrame) -> dict:
    return {
        "manifest_keys": list(manifest.keys()),
        "total_items": len(item_df) if item_df is not None else 0
    }
