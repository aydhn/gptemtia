import pandas as pd
from typing import Tuple, Dict, Any

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def _build_generic_cadence_registry(category: str, items: list, cadence: str) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    data = [{"category": category, "item": item, "suggested_cadence": cadence} for item in items]
    df = pd.DataFrame(data)
    summary = {
        "category": category,
        "total_items": len(df),
        "cadence": cadence,
        "disclaimer": "This is a dry-run refresh plan, not an auto-run scheduler."
    }
    return df, summary

def build_report_refresh_cadence_registry(profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = ["System Status Report", "Quality Report", "Local Readiness Report"]
    return _build_generic_cadence_registry("reports", items, "refresh_weekly_manual" if profile.scan_reports else "refresh_not_applicable")

def build_datalake_refresh_cadence_registry(profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = ["Data Lake Verification", "Cache Integrity Check"]
    return _build_generic_cadence_registry("datalake", items, "refresh_monthly_manual" if profile.scan_data_lake else "refresh_not_applicable")

def build_documentation_refresh_cadence_registry(profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = ["ARCHITECTURE.md", "OPERATOR_MANUAL.md", "PHASE_LOG.md"]
    return _build_generic_cadence_registry("documentation", items, "refresh_monthly_manual" if profile.scan_docs else "refresh_not_applicable")

def build_test_refresh_cadence_registry(profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = ["Unit Tests", "Integration Tests", "Consistency Checks"]
    return _build_generic_cadence_registry("tests", items, "refresh_before_handoff_manual" if profile.scan_tests else "refresh_not_applicable")

def build_safety_security_refresh_cadence_registry(profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = ["Secrets Hygiene Scan", "Credential Boundary Check"]
    return _build_generic_cadence_registry("safety_security", items, "refresh_monthly_manual")

def build_backup_packaging_refresh_cadence_registry(profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = ["Portable Bundle Manifest", "Backup Dry Run"]
    return _build_generic_cadence_registry("backup_packaging", items, "refresh_monthly_manual")

def build_cross_layer_refresh_cadence_registry(profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = ["Cross Layer Consistency Matrix", "Contradiction Detection"]
    return _build_generic_cadence_registry("cross_layer", items, "refresh_monthly_manual" if profile.scan_cross_layer_outputs else "refresh_not_applicable")

def summarize_refresh_cadence(cadence_tables: Dict[str, pd.DataFrame]) -> Dict[str, Any]:
    total_items = sum(len(df) for df in cadence_tables.values() if df is not None)
    return {
        "total_cadence_items": total_items,
        "tables_included": list(cadence_tables.keys()),
        "disclaimer": "Refresh cadence defines manual intervals. Auto-run is strictly disabled."
    }
