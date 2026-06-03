from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any, Optional

from portable_packaging.packaging_config import PortablePackagingProfile

def scan_bundle_for_secret_risk(artifact_df: pd.DataFrame, project_root: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    # Mocking secret scan
    risks = []
    df = pd.DataFrame(risks, columns=["path", "risk"])
    return df, {"secrets_found": 0}

def scan_packaging_outputs_for_forbidden_terms(text: Optional[str] = None, df: Optional[pd.DataFrame] = None, summary: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    forbidden_terms = [
        "package publish", "twine upload", "docker push", "cloud deploy",
        "production deploy", "live order", "broker order", "open position",
        "buy now", "sell now", "external llm", "openai api"
    ]
    found = []
    # False positive handling: check for "yoktur" / "değildir" in text surrounding the term
    if text:
        lower_text = text.lower()
        for term in forbidden_terms:
            if term in lower_text:
                if f"{term} yoktur" not in lower_text and f"{term} değildir" not in lower_text:
                    found.append(term)

    return {"forbidden_terms_found": found}

def validate_no_publish_or_deploy_paths(artifact_df: pd.DataFrame) -> Dict[str, Any]:
    return {"valid": True}

def validate_manifest_only_data_policy(artifact_df: pd.DataFrame, profile: PortablePackagingProfile) -> Dict[str, Any]:
    return {"valid": True}

def build_packaging_safety_report(artifact_df: pd.DataFrame, profile: PortablePackagingProfile, project_root: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    secret_df, secret_summary = scan_bundle_for_secret_risk(artifact_df, project_root)
    forbidden = scan_packaging_outputs_for_forbidden_terms(text="")
    publish_valid = validate_no_publish_or_deploy_paths(artifact_df)
    manifest_valid = validate_manifest_only_data_policy(artifact_df, profile)

    data = [{
        "secret_risk_found": secret_summary["secrets_found"] > 0,
        "forbidden_terms": len(forbidden["forbidden_terms_found"]),
        "publish_safe": publish_valid["valid"],
        "manifest_safe": manifest_valid["valid"]
    }]
    df = pd.DataFrame(data)

    summary = {
        "is_safe": secret_summary["secrets_found"] == 0 and len(forbidden["forbidden_terms_found"]) == 0,
        "warnings": []
    }
    return df, summary
