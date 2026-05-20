from dataclasses import dataclass, field

@dataclass
class CLICommandInfo:
    command_name: str
    module_path: str
    group: str
    description: str
    example: str
    supports_help: bool
    supports_dry_run: bool
    requires_symbol: bool
    requires_timeframe: bool
    output_report: str | None
    warnings: list[str]

@dataclass
class DXFinding:
    finding_id: str
    category: str
    status: str
    title: str
    description: str
    file_path: str | None = None
    recommended_action: str | None = None
    blocking: bool = False
    warnings: list[str] = field(default_factory=list)

@dataclass
class DXQualitySummary:
    summary_id: str
    created_at_utc: str
    total_findings: int
    failed_count: int
    warning_count: int
    passed_count: int
    dx_status: str
    warnings: list[str]

def build_dx_finding_id(category: str, title: str, file_path: str | None = None) -> str:
    base = f"{category}_{title}"
    if file_path:
        base += f"_{file_path}"
    return base.lower().replace(" ", "_").replace("/", "_").replace(".", "_")

def cli_command_info_to_dict(info: CLICommandInfo) -> dict:
    return {
        "command_name": info.command_name,
        "module_path": info.module_path,
        "group": info.group,
        "description": info.description,
        "example": info.example,
        "supports_help": info.supports_help,
        "supports_dry_run": info.supports_dry_run,
        "requires_symbol": info.requires_symbol,
        "requires_timeframe": info.requires_timeframe,
        "output_report": info.output_report,
        "warnings": info.warnings,
    }

def dx_finding_to_dict(finding: DXFinding) -> dict:
    return {
        "finding_id": finding.finding_id,
        "category": finding.category,
        "status": finding.status,
        "title": finding.title,
        "description": finding.description,
        "file_path": finding.file_path,
        "recommended_action": finding.recommended_action,
        "blocking": finding.blocking,
        "warnings": finding.warnings,
    }

def dx_quality_summary_to_dict(summary: DXQualitySummary) -> dict:
    return {
        "summary_id": summary.summary_id,
        "created_at_utc": summary.created_at_utc,
        "total_findings": summary.total_findings,
        "failed_count": summary.failed_count,
        "warning_count": summary.warning_count,
        "passed_count": summary.passed_count,
        "dx_status": summary.dx_status,
        "warnings": summary.warnings,
    }
