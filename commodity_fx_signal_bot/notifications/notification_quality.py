import re
from notifications.notification_models import NotificationMessage, DeliveryResult
from notifications.notification_config import NotificationProfile

def check_message_not_empty(message: NotificationMessage) -> dict:
    is_empty = not message.title.strip() and not message.body.strip()
    return {
        "passed": not is_empty,
        "warning": "Message is empty" if is_empty else None
    }

def check_message_length(message_text: str, max_chars: int) -> dict:
    length = len(message_text)
    is_too_long = length > max_chars
    return {
        "passed": not is_too_long,
        "length": length,
        "warning": f"Message exceeds maximum character limit ({length} > {max_chars})" if is_too_long else None
    }

def check_for_sensitive_tokens(text: str, metadata: dict | None = None) -> dict:
    warnings = []
    # Basic token regex check
    if re.search(r'\b\d{8,10}:[a-zA-Z0-9_-]{35}\b', text):
        warnings.append("Sensitive token format found in message text")

    if metadata:
        metadata_str = str(metadata)
        if re.search(r'\b\d{8,10}:[a-zA-Z0-9_-]{35}\b', metadata_str):
            warnings.append("Sensitive token format found in metadata")

    return {
        "passed": len(warnings) == 0,
        "warnings": warnings
    }

def check_for_forbidden_trade_instruction_terms(text: str) -> dict:
    # We want to avoid using terms that make it look like a live instruction
    forbidden_terms = [
        r"\bAL\b", r"\bSAT\b", r"\bBUY\b", r"\bSELL\b",
        r"\bOPEN_LONG\b", r"\bOPEN_SHORT\b", r"\bEMİR GÖNDER\b",
        r"\bPOZİSYON AÇ\b", r"\bPOZİSYON KAPAT\b", r"\bGERÇEK EMİR\b",
        r"\bBROKER ORDER\b", r"\bLIVE ORDER\b"
    ]

    found_terms = []
    text_upper = text.upper()
    for term in forbidden_terms:
        if re.search(term, text_upper):
            found_terms.append(term)

    return {
        "passed": len(found_terms) == 0,
        "found_terms": found_terms,
        "warning": f"Found forbidden trade instruction terms: {', '.join(found_terms)}" if found_terms else None
    }

def check_delivery_results(results: list[DeliveryResult]) -> dict:
    failed = [r for r in results if r.delivery_status == "delivery_failed"]
    rate_limited = [r for r in results if r.delivery_status == "delivery_rate_limited"]

    warnings = []
    if failed:
        warnings.append(f"{len(failed)} parts failed delivery")
    if rate_limited:
        warnings.append(f"{len(rate_limited)} parts were rate limited")

    return {
        "passed": len(failed) == 0,
        "warnings": warnings,
        "failed_count": len(failed),
        "rate_limited_count": len(rate_limited)
    }

def build_notification_quality_report(
    message: NotificationMessage,
    formatted_text: str,
    delivery_results: list[DeliveryResult],
    profile: NotificationProfile
) -> dict:

    empty_check = check_message_not_empty(message)
    length_check = check_message_length(formatted_text, profile.message_max_chars)
    sensitive_check = check_for_sensitive_tokens(formatted_text, message.metadata)
    instruction_check = check_for_forbidden_trade_instruction_terms(formatted_text)
    delivery_check = check_delivery_results(delivery_results)

    all_warnings = []
    for check in [empty_check, length_check, instruction_check]:
        if not check["passed"] and check.get("warning"):
            all_warnings.append(check["warning"])

    all_warnings.extend(sensitive_check.get("warnings", []))
    all_warnings.extend(delivery_check.get("warnings", []))

    passed = empty_check["passed"] and sensitive_check["passed"] and instruction_check["passed"]

    return {
        "message_id": message.message_id,
        "notification_type": message.notification_type,
        "profile_name": profile.name,
        "passed": passed,
        "warnings": all_warnings,
        "details": {
            "message_not_empty": empty_check["passed"],
            "length_ok": length_check["passed"],
            "sensitive_token_found": not sensitive_check["passed"],
            "forbidden_instruction_terms_found": not instruction_check["passed"],
            "delivery_status_summary": {
                "failed": delivery_check["failed_count"],
                "rate_limited": delivery_check["rate_limited_count"]
            }
        }
    }
