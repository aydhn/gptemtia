import re
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class ReportExportArtifact:
    artifact_id: str
    report_id: str
    export_type: str
    status: str
    path: Optional[str]
    created_at_utc: str
    file_size_bytes: Optional[int]
    warnings: list[str]

@dataclass
class ReportArchiveRecord:
    archive_id: str
    report_id: str
    report_type: str
    symbol: Optional[str]
    timeframe: str
    profile_name: str
    created_at_utc: str
    research_score: Optional[float]
    warning_count: int
    missing_sources_count: int
    markdown_path: Optional[str]
    html_path: Optional[str]
    pdf_path: Optional[str]
    csv_paths: list[str]
    quality_passed: bool
    metadata: dict

@dataclass
class ReportComparisonResult:
    comparison_id: str
    current_report_id: str
    previous_report_id: Optional[str]
    symbol: Optional[str]
    timeframe: str
    comparison_label: str
    score_delta: Optional[float]
    warning_delta: Optional[int]
    missing_sources_delta: Optional[int]
    changed_sections: list[str]
    summary: dict
    warnings: list[str]

def build_export_artifact_id(report_id: str, export_type: str) -> str:
    return f"art_{report_id}_{export_type}"

def build_archive_id(report_id: str, created_at_utc: str) -> str:
    clean_date = created_at_utc.replace(":", "").replace("-", "").replace(" ", "_").replace("T", "_").replace("Z", "")
    return f"arc_{report_id}_{clean_date}"

def build_comparison_id(current_report_id: str, previous_report_id: Optional[str]) -> str:
    prev = previous_report_id if previous_report_id else "none"
    return f"comp_{current_report_id}_{prev}"

def report_export_artifact_to_dict(artifact: ReportExportArtifact) -> dict:
    return asdict(artifact)

def report_archive_record_to_dict(record: ReportArchiveRecord) -> dict:
    return asdict(record)

def report_comparison_result_to_dict(result: ReportComparisonResult) -> dict:
    return asdict(result)

def sanitize_export_filename(value: str) -> str:
    if not value:
        return "unknown"
    value = str(value)
    sanitized = re.sub(r'[^a-zA-Z0-9_-]', '_', value)
    return sanitized.strip('_')
