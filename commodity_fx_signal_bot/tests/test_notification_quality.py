import pytest
from notifications.notification_quality import (
    check_message_not_empty,
    check_message_length,
    check_for_sensitive_tokens,
    check_for_forbidden_trade_instruction_terms
)
from notifications.notification_models import NotificationMessage

def test_check_message_not_empty():
    msg = NotificationMessage("1", "test", "info", "", "", "now")
    res = check_message_not_empty(msg)
    assert not res["passed"]

def test_check_message_length():
    res = check_message_length("A" * 100, 50)
    assert not res["passed"]

def test_check_for_sensitive_tokens():
    res = check_for_sensitive_tokens("Token 123456789:ABCdefGHIjklMNOpqrsTUVwxyz123456789")
    assert not res["passed"]

def test_check_for_forbidden_terms():
    res = check_for_forbidden_trade_instruction_terms("Lütfen bu emri SAT olarak gönder.")
    assert not res["passed"]
    assert r"\bSAT\b" in res["found_terms"]
