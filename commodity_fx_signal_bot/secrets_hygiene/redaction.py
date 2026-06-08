
from typing import Optional

def mask_secret_value(value: str, keep_start: int = 4, keep_end: int = 4) -> str:
    if not value: return ""
    value_len = len(value)
    if value_len <= keep_start + keep_end: return "*" * value_len
    start_str = value[:keep_start] if keep_start > 0 else ""
    end_str = value[-keep_end:] if keep_end > 0 else ""
    return f"{start_str}{'*' * (value_len - keep_start - keep_end)}{end_str}"

def mask_line_around_secret(line: str, start: int, end: int) -> str:
    if not line: return ""
    if start < 0 or end < 0 or start >= len(line) or end > len(line) or start >= end: return line
    return f"{line[:start]}{mask_secret_value(line[start:end])}{line[end:]}"

def safe_preview_line(line: str, max_len: int = 240) -> str:
    if not line: return ""
    if len(line) > max_len: return line[:max_len] + "..."
    return line

def redact_mapping_values(data: dict, sensitive_keys: Optional[list[str]] = None) -> dict:
    if not data: return {}
    s_keys = sensitive_keys or ["password", "secret", "token", "key", "credential", "auth", "access", "private", "api"]
    res = {}
    for k, v in data.items():
        if isinstance(v, dict): res[k] = redact_mapping_values(v, s_keys)
        elif isinstance(v, str) and any(sk.lower() in k.lower() for sk in s_keys): res[k] = mask_secret_value(v)
        else: res[k] = v
    return res

def assert_no_unmasked_secret(text: str, raw_value: str) -> bool:
    if not raw_value or not text: return True
    return raw_value not in text
