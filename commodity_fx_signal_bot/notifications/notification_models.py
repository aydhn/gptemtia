from dataclasses import dataclass, field
import hashlib
import re

@dataclass
class NotificationMessage:
    message_id: str
    notification_type: str
    severity: str
    title: str
    body: str
    created_at_utc: str
    symbol: str | None = None
    timeframe: str | None = None
    profile_name: str | None = None
    metadata: dict = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)

@dataclass
class DeliveryResult:
    message_id: str
    delivery_status: str
    dry_run: bool
    destination: str | None
    sent_at_utc: str | None
    error_message: str | None
    response_metadata: dict = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)

def build_notification_message_id(notification_type: str, title: str, created_at_utc: str) -> str:
    raw = f"{notification_type}_{title}_{created_at_utc}"
    return f"msg_{hashlib.md5(raw.encode('utf-8')).hexdigest()[:12]}"

def notification_message_to_dict(message: NotificationMessage) -> dict:
    return {
        "message_id": message.message_id,
        "notification_type": message.notification_type,
        "severity": message.severity,
        "title": message.title,
        "body": message.body,
        "created_at_utc": message.created_at_utc,
        "symbol": message.symbol,
        "timeframe": message.timeframe,
        "profile_name": message.profile_name,
        "metadata": sanitize_metadata(message.metadata),
        "warnings": message.warnings
    }

def delivery_result_to_dict(result: DeliveryResult) -> dict:
    return {
        "message_id": result.message_id,
        "delivery_status": result.delivery_status,
        "dry_run": result.dry_run,
        "destination": result.destination,
        "sent_at_utc": result.sent_at_utc,
        "error_message": result.error_message,
        "response_metadata": sanitize_metadata(result.response_metadata),
        "warnings": result.warnings
    }

def sanitize_sensitive_text(text: str) -> str:
    # Basic sanitization of tokens (e.g. format like 123456789:ABCdefGHIjklMNOpqrsTUVwxyz)
    sanitized = re.sub(r'\b\d{8,10}:[a-zA-Z0-9_-]{35}\b', '***TOKEN***', text)
    return sanitized

def sanitize_metadata(metadata: dict) -> dict:
    sanitized = {}
    for k, v in metadata.items():
        if "token" in k.lower() or "secret" in k.lower() or k.lower() == "key" or "api_key" in k.lower() or "secret_key" in k.lower():
            sanitized[k] = "***MASKED***"
        elif isinstance(v, str):
            sanitized[k] = sanitize_sensitive_text(v)
        else:
            sanitized[k] = v
    return sanitized
