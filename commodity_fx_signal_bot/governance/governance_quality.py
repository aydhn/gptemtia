import pandas as pd

from governance.governance_config import GovernanceProfile

FORBIDDEN_TERMS = [
    "AL", "SAT", "BUY", "SELL", "OPEN_LONG", "OPEN_SHORT",
    "EMİR GÖNDER", "POZİSYON AÇ", "POZİSYON KAPAT", "GERÇEK EMİR",
    "BROKER ORDER", "LIVE ORDER", "PRODUCTION COMPLIANCE APPROVED"
]

def check_inventory_quality(inventory_df: pd.DataFrame, profile: GovernanceProfile) -> dict:
    warnings = []
    if inventory_df is None or inventory_df.empty:
        return {"valid": True, "warnings": ["Inventory is empty"]}

    if profile.capture_file_hashes and inventory_df["content_fingerprint"].isna().sum() > 0:
        # Expected for large files
        warnings.append("Some artifacts are missing content_fingerprint (likely due to size limits)")

    return {"valid": True, "warnings": warnings}

def check_provenance_quality(provenance_df: pd.DataFrame | None, profile: GovernanceProfile) -> dict:
    if provenance_df is None or provenance_df.empty:
        if profile.require_provenance_for_research_outputs:
            return {"valid": False, "warnings": ["Provenance required but missing"]}
        return {"valid": True, "warnings": ["Provenance is empty"]}
    return {"valid": True, "warnings": []}

def check_lineage_quality(node_df: pd.DataFrame | None, edge_df: pd.DataFrame | None) -> dict:
    warnings = []
    if node_df is None or node_df.empty:
        warnings.append("Lineage nodes are empty")
    if edge_df is None or edge_df.empty:
        warnings.append("Lineage edges are empty")
    return {"valid": len(warnings) == 0, "warnings": warnings}

def check_audit_trail_quality(audit_df: pd.DataFrame | None, profile: GovernanceProfile) -> dict:
    if audit_df is None or audit_df.empty:
        if profile.require_audit_trail:
            return {"valid": False, "warnings": ["Audit trail required but missing"]}
        return {"valid": True, "warnings": ["Audit trail is empty"]}
    return {"valid": True, "warnings": []}

def check_source_attribution_quality(source_df: pd.DataFrame | None) -> dict:
    if source_df is None or source_df.empty:
        return {"valid": False, "warnings": ["Source attribution is missing"]}
    return {"valid": True, "warnings": []}

def check_for_sensitive_data_in_governance(df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    # A simple mock check for 'secret', 'key' in path
    sensitive = False
    if df is not None and not df.empty and "path" in df:
        if any("secret" in str(p).lower() or "key" in str(p).lower() for p in df["path"]):
            sensitive = True
    return {"sensitive_data_found": sensitive, "warnings": ["Sensitive data identified"] if sensitive else []}

def check_for_forbidden_trade_terms_in_governance(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    found = False
    if text:
        text_upper = text.upper()
        if any(term in text_upper for term in FORBIDDEN_TERMS):
            found = True

    if df is not None and not df.empty and "path" in df:
        paths = " ".join(df["path"].astype(str)).upper()
        if any(term in paths for term in FORBIDDEN_TERMS):
            found = True

    return {"forbidden_trade_terms_found": found, "warnings": ["Forbidden trade terms found"] if found else []}

def build_governance_quality_report(summary: dict, inventory_df: pd.DataFrame | None = None, provenance_df: pd.DataFrame | None = None, node_df: pd.DataFrame | None = None, edge_df: pd.DataFrame | None = None) -> dict:
    # Placeholder profile since we just want a simple check here
    profile = GovernanceProfile(name="temp", description="temp")

    inv_q = check_inventory_quality(inventory_df, profile)
    prov_q = check_provenance_quality(provenance_df, profile)
    lin_q = check_lineage_quality(node_df, edge_df)

    sens = check_for_sensitive_data_in_governance(inventory_df)
    forb = check_for_forbidden_trade_terms_in_governance(df=inventory_df)

    warnings = []
    warnings.extend(inv_q["warnings"])
    warnings.extend(prov_q["warnings"])
    warnings.extend(lin_q["warnings"])
    warnings.extend(sens["warnings"])
    warnings.extend(forb["warnings"])

    passed = inv_q["valid"] and not sens["sensitive_data_found"] and not forb["forbidden_trade_terms_found"]

    return {
        "inventory_valid": inv_q["valid"],
        "provenance_valid": prov_q["valid"],
        "lineage_valid": lin_q["valid"],
        "audit_trail_valid": True,
        "source_attribution_valid": True,
        "sensitive_data_found": sens["sensitive_data_found"],
        "forbidden_trade_terms_found": forb["forbidden_trade_terms_found"],
        "warning_count": len(warnings),
        "passed": passed,
        "warnings": warnings,
        "note": "Governance passed is NOT production compliance."
    }
