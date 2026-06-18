from dataclasses import dataclass


@dataclass
class ConsistencyCheck:
    check_id: str
    check_type: str
    check_name: str
    source_layer: str
    target_layer: str
    description: str
    expected_artifacts: list[str]
    status: str
    warnings: list[str]

@dataclass
class ConsistencyFinding:
    finding_id: str
    check_id: str
    check_type: str
    status: str
    severity: str
    source_path: str | None
    target_path: str | None
    message: str
    recommendation: str
    warnings: list[str]

@dataclass
class ContradictionFinding:
    contradiction_id: str
    source_path: str | None
    target_path: str | None
    contradiction_type: str
    severity: str
    source_statement: str
    target_statement: str
    explanation: str
    warnings: list[str]

@dataclass
class ReferenceFinding:
    reference_id: str
    source_path: str
    referenced_path: str | None
    reference_text: str
    status: str
    recommendation: str
    warnings: list[str]

@dataclass
class ReconciliationRecommendation:
    recommendation_id: str
    finding_id: str | None
    title: str
    description: str
    safe_action: str
    destructive: bool
    requires_manual_review: bool
    warnings: list[str]

def build_consistency_check_id(check_type: str, source_layer: str, target_layer: str) -> str:
    return f"check_{check_type}_{source_layer}_{target_layer}".replace("/", "_").replace(".", "_")

def build_consistency_finding_id(check_id: str, source_path: str | None, target_path: str | None, message: str) -> str:
    import hashlib
    base = f"{check_id}_{source_path}_{target_path}_{message}"
    return f"finding_{hashlib.md5(base.encode('utf-8')).hexdigest()[:8]}"

def build_contradiction_id(source_path: str | None, target_path: str | None, contradiction_type: str) -> str:
    import hashlib
    base = f"{source_path}_{target_path}_{contradiction_type}"
    return f"contra_{hashlib.md5(base.encode('utf-8')).hexdigest()[:8]}"

def build_reference_id(source_path: str, reference_text: str) -> str:
    import hashlib
    base = f"{source_path}_{reference_text}"
    return f"ref_{hashlib.md5(base.encode('utf-8')).hexdigest()[:8]}"

def build_reconciliation_recommendation_id(title: str, finding_id: str | None = None) -> str:
    import hashlib
    base = f"{title}_{finding_id}"
    return f"rec_{hashlib.md5(base.encode('utf-8')).hexdigest()[:8]}"

def consistency_check_to_dict(item: ConsistencyCheck) -> dict:
    return {
        "check_id": item.check_id,
        "check_type": item.check_type,
        "check_name": item.check_name,
        "source_layer": item.source_layer,
        "target_layer": item.target_layer,
        "description": item.description,
        "expected_artifacts": item.expected_artifacts,
        "status": item.status,
        "warnings": item.warnings
    }

def consistency_finding_to_dict(item: ConsistencyFinding) -> dict:
    return {
        "finding_id": item.finding_id,
        "check_id": item.check_id,
        "check_type": item.check_type,
        "status": item.status,
        "severity": item.severity,
        "source_path": item.source_path,
        "target_path": item.target_path,
        "message": item.message,
        "recommendation": item.recommendation,
        "warnings": item.warnings
    }

def contradiction_finding_to_dict(item: ContradictionFinding) -> dict:
    return {
        "contradiction_id": item.contradiction_id,
        "source_path": item.source_path,
        "target_path": item.target_path,
        "contradiction_type": item.contradiction_type,
        "severity": item.severity,
        "source_statement": item.source_statement,
        "target_statement": item.target_statement,
        "explanation": item.explanation,
        "warnings": item.warnings
    }

def reference_finding_to_dict(item: ReferenceFinding) -> dict:
    return {
        "reference_id": item.reference_id,
        "source_path": item.source_path,
        "referenced_path": item.referenced_path,
        "reference_text": item.reference_text,
        "status": item.status,
        "recommendation": item.recommendation,
        "warnings": item.warnings
    }

def reconciliation_recommendation_to_dict(item: ReconciliationRecommendation) -> dict:
    return {
        "recommendation_id": item.recommendation_id,
        "finding_id": item.finding_id,
        "title": item.title,
        "description": item.description,
        "safe_action": item.safe_action,
        "destructive": item.destructive,
        "requires_manual_review": item.requires_manual_review,
        "warnings": item.warnings
    }
