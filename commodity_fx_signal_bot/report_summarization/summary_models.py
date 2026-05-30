import hashlib
from dataclasses import dataclass, asdict

@dataclass
class ReportSummaryRecord:
    summary_id: str
    source_report_id: str
    source_path: str
    module_name: str
    summary_type: str
    title: str
    summary_text: str
    bullets: list[str]
    key_findings: list[str]
    warnings: list[str]
    generated_at_utc: str
    warnings_meta: list[str]

@dataclass
class ExtractedFinding:
    finding_id: str
    source_report_id: str
    source_path: str
    module_name: str
    finding_type: str
    priority: str
    text: str
    related_symbols: list[str]
    related_modules: list[str]
    warnings: list[str]

@dataclass
class BriefCard:
    brief_id: str
    brief_type: str
    title: str
    module_name: str | None
    symbol: str | None
    summary: str
    key_points: list[str]
    follow_ups: list[str]
    priority: str
    source_paths: list[str]
    warnings: list[str]

@dataclass
class FollowUpTask:
    task_id: str
    follow_up_type: str
    title: str
    description: str
    priority: str
    suggested_safe_command: str | None
    related_module: str | None
    related_symbol: str | None
    source_paths: list[str]
    warnings: list[str]

def build_summary_id(source_report_id: str, summary_type: str) -> str:
    key = f"{source_report_id}_{summary_type}"
    return "sum_" + hashlib.sha256(key.encode("utf-8")).hexdigest()[:12]

def build_finding_id(source_report_id: str, text: str) -> str:
    key = f"{source_report_id}_{text}"
    return "fnd_" + hashlib.sha256(key.encode("utf-8")).hexdigest()[:12]

def build_brief_id(brief_type: str, title: str, module_name: str | None = None, symbol: str | None = None) -> str:
    key = f"{brief_type}_{title}_{module_name}_{symbol}"
    return "brf_" + hashlib.sha256(key.encode("utf-8")).hexdigest()[:12]

def build_follow_up_task_id(title: str, follow_up_type: str) -> str:
    key = f"{title}_{follow_up_type}"
    return "tsk_" + hashlib.sha256(key.encode("utf-8")).hexdigest()[:12]

def report_summary_record_to_dict(record: ReportSummaryRecord) -> dict:
    return asdict(record)

def extracted_finding_to_dict(finding: ExtractedFinding) -> dict:
    return asdict(finding)

def brief_card_to_dict(card: BriefCard) -> dict:
    return asdict(card)

def follow_up_task_to_dict(task: FollowUpTask) -> dict:
    return asdict(task)
