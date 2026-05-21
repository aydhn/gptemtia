from pathlib import Path
from typing import Dict, Optional, List
import pandas as pd
from report_exports.export_models import ReportExportArtifact, ReportArchiveRecord, ReportComparisonResult

FORBIDDEN_TRADE_TERMS = [
    " AL ", " SAT ", " BUY ", " SELL ",
    "OPEN_LONG", "OPEN_SHORT",
    "EMİR GÖNDER", "POZİSYON AÇ", "POZİSYON KAPAT",
    "GERÇEK EMİR", "BROKER ORDER", "LIVE ORDER"
]

def check_html_export_quality(html_text: Optional[str]) -> Dict:
    if not html_text:
        return {"passed": False, "warnings": ["Missing HTML content."]}
    warnings = []
    if "<script" in html_text.lower():
        warnings.append("HTML contains script tags (not allowed).")
    if "offline araştırma raporu" not in html_text.lower():
        warnings.append("Disclaimer is missing from HTML.")
    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_pdf_export_quality(pdf_path: Optional[Path]) -> Dict:
    if not pdf_path or not pdf_path.exists():
        return {"passed": True, "warnings": ["PDF is missing (skipped)."]}
    if pdf_path.stat().st_size == 0:
        return {"passed": False, "warnings": ["PDF file is empty."]}
    return {"passed": True, "warnings": []}

def check_manifest_quality(manifest: Dict) -> Dict:
    from report_exports.report_manifest import validate_report_export_manifest
    result = validate_report_export_manifest(manifest)
    return {"passed": result["valid"], "warnings": result["errors"]}

def check_archive_record_quality(record: ReportArchiveRecord | dict) -> Dict:
    warnings = []
    if isinstance(record, dict):
        if not record.get("report_id"):
            warnings.append("Archive record missing report_id.")
    else:
        if not record.report_id:
            warnings.append("Archive record missing report_id.")
    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_comparison_quality(comparison: ReportComparisonResult | dict) -> Dict:
    warnings = []
    if isinstance(comparison, dict):
        if not comparison.get("comparison_id"):
            warnings.append("Comparison missing comparison_id.")
    else:
        if not comparison.comparison_id:
            warnings.append("Comparison missing comparison_id.")
    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_for_forbidden_trade_terms_in_exports(text: Optional[str] = None, df: Optional[pd.DataFrame] = None, summary: Optional[Dict] = None) -> Dict:
    found_terms = []
    def _check_text(s: str):
        if not s:
            return
        s_upper = s.upper()
        for term in FORBIDDEN_TRADE_TERMS:
            if term.strip() in ["AL", "SAT", "BUY", "SELL"]:
                if term in s_upper:
                    found_terms.append(term.strip())
            else:
                if term in s_upper:
                    found_terms.append(term)
    if text:
        _check_text(text)
    if df is not None and not df.empty:
        for col in df.select_dtypes(include=['object']):
            for val in df[col].head(10).dropna():
                _check_text(str(val))
    if summary:
        _check_text(str(summary))
    found_terms = list(set(found_terms))
    return {
        "passed": len(found_terms) == 0,
        "warnings": [f"Forbidden trade terms found: {found_terms}"] if found_terms else [],
        "forbidden_terms": found_terms
    }

def build_report_export_quality_report(
    artifacts: List[ReportExportArtifact],
    manifest: Optional[Dict] = None,
    archive_record: Optional[ReportArchiveRecord | dict] = None,
    comparison: Optional[ReportComparisonResult | dict] = None,
) -> Dict:
    warnings = []
    html_passed = False
    pdf_status = "skipped"
    for art in artifacts:
        if art.export_type == "html_export":
            html_passed = art.status == "success"
        elif art.export_type == "pdf_export":
            pdf_status = art.status
    manifest_qual = check_manifest_quality(manifest) if manifest else {"passed": False, "warnings": ["No manifest."]}
    archive_qual = check_archive_record_quality(archive_record) if archive_record else {"passed": False, "warnings": ["No archive record."]}
    if not manifest_qual["passed"]:
        warnings.extend(manifest_qual["warnings"])
    if not archive_qual["passed"]:
        warnings.extend(archive_qual["warnings"])
    forbidden_qual = check_for_forbidden_trade_terms_in_exports(summary=manifest)
    if not forbidden_qual["passed"]:
        warnings.extend(forbidden_qual["warnings"])
    disclaimer_present = manifest.get("disclaimer_present", False) if manifest else False
    if not disclaimer_present:
        warnings.append("Disclaimer is missing from the export manifest.")
    passed = html_passed and manifest_qual["passed"] and disclaimer_present and forbidden_qual["passed"]
    return {
        "html_available": html_passed,
        "pdf_available_or_skipped": pdf_status in ["success", "skipped"],
        "manifest_valid": manifest_qual["passed"],
        "archive_record_valid": archive_qual["passed"],
        "disclaimer_present": disclaimer_present,
        "forbidden_trade_terms_found": not forbidden_qual["passed"],
        "artifact_count": len(artifacts),
        "warning_count": len(warnings),
        "passed": passed,
        "warnings": list(set(warnings))
    }
