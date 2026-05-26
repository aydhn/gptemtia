import json
from pathlib import Path
import pandas as pd
from datetime import datetime, timezone

from documentation.documentation_models import (
    DocumentationPackManifest,
    build_documentation_manifest_id,
    documentation_pack_manifest_to_dict
)
from documentation.documentation_config import DocumentationProfile

def build_documentation_pack_manifest(
    profile: DocumentationProfile,
    docs_df: pd.DataFrame,
    coverage_df: pd.DataFrame,
    safety_df: pd.DataFrame
) -> DocumentationPackManifest:

    created_at = datetime.now(timezone.utc).isoformat()
    manifest_id = build_documentation_manifest_id(profile.name, created_at)

    gen_docs = []
    if profile.generate_user_guide: gen_docs.append("USER_GUIDE.md")
    if profile.generate_operator_manual: gen_docs.append("OPERATOR_MANUAL.md")
    if profile.generate_analyst_handbook: gen_docs.append("ANALYST_HANDBOOK.md")
    if profile.generate_developer_guide: gen_docs.append("DEVELOPER_GUIDE.md")
    if profile.generate_codex_agent_guide: gen_docs.append("CODEX_AGENT_GUIDE.md")
    if profile.generate_safe_usage_guide: gen_docs.append("SAFE_USAGE_GUIDE.md")
    if profile.generate_troubleshooting: gen_docs.append("TROUBLESHOOTING_COOKBOOK.md")
    if profile.generate_references:
         gen_docs.extend(["FAQ.md", "GLOSSARY.md", "MODULE_MAP.md", "SCRIPT_REFERENCE.md", "OUTPUT_REFERENCE.md", "DOCUMENTATION_INDEX.md"])

    actual_docs = []
    if docs_df is not None and not docs_df.empty:
         actual_docs = docs_df["relative_path"].tolist()

    missing_docs = [doc for doc in gen_docs if not any(doc in p for p in actual_docs)]

    quality_score = 1.0
    if safety_df is not None and not safety_df.empty:
         unsafe = len(safety_df[safety_df["is_safe"] == False])
         if unsafe > 0:
              quality_score -= 0.5

    if missing_docs:
         quality_score -= (len(missing_docs) * 0.05)

    quality_score = max(0.0, quality_score)

    warnings = []
    if quality_score < profile.min_quality_score:
         warnings.append(f"Quality score {quality_score:.2f} is below minimum {profile.min_quality_score:.2f}")

    return DocumentationPackManifest(
        manifest_id=manifest_id,
        profile_name=profile.name,
        created_at_utc=created_at,
        document_count=len(actual_docs),
        required_document_count=len(gen_docs),
        generated_documents=gen_docs,
        missing_documents=missing_docs,
        quality_score=quality_score,
        warnings=warnings
    )

def build_documentation_pack_manifest_json(manifest: DocumentationPackManifest, docs_df: pd.DataFrame) -> dict:
    d = documentation_pack_manifest_to_dict(manifest)
    d["disclaimer"] = "This is a documentation pack manifest for an offline research platform. It is not a production release manifest."
    return d

def save_documentation_pack_manifest(manifest_json: dict, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(manifest_json, f, indent=2, ensure_ascii=False)
    return output_path

def summarize_documentation_pack_manifest(manifest_json: dict) -> dict:
    return {
        "manifest_id": manifest_json.get("manifest_id"),
        "profile": manifest_json.get("profile_name"),
        "quality_score": manifest_json.get("quality_score"),
        "warnings": manifest_json.get("warnings", [])
    }
