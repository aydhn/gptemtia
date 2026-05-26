import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from documentation.doc_templates import (
    build_standard_disclaimer,
    build_safe_usage_guide_template,
    build_user_guide_template,
    build_troubleshooting_template,
    build_glossary_template
)

def test_standard_disclaimer_not_empty():
    assert len(build_standard_disclaimer()) > 0

def test_safe_usage_template_contains_disclaimer():
    template = build_safe_usage_guide_template()
    assert "offline/local araştırma platformu" in template

def test_user_guide_template_contains_safety_boundaries():
    template = build_user_guide_template()
    assert "Güvenlik Sınırları" in template

def test_troubleshooting_template_does_not_suggest_live_broker():
    template = build_troubleshooting_template()
    assert "canlı" not in template or "canlı trade araçları yüklemeyin" in template

def test_glossary_template_generates():
    template = build_glossary_template()
    assert "Sözlük (Glossary)" in template
