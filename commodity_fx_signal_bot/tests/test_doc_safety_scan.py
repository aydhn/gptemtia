import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from documentation.doc_safety_scan import scan_doc_text_for_unsafe_language

def test_unsafe_language_caught():
    res = scan_doc_text_for_unsafe_language("Bu bot kesin al sinyali üretir.")
    assert res["is_safe"] is False
    assert len(res["findings"]) > 0

def test_false_positive_not_critical():
    res = scan_doc_text_for_unsafe_language("Bu proje yatırım tavsiyesi değildir.")
    assert isinstance(res["is_safe"], bool)

def test_safe_language():
    res = scan_doc_text_for_unsafe_language("Offline research platform.")
    assert res["is_safe"] is True
    assert len(res["findings"]) == 0
