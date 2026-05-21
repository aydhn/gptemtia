from report_exports.pdf_renderer import detect_available_pdf_engines, render_html_to_pdf

def test_detect_available_pdf_engines():
    engines = detect_available_pdf_engines()
    assert "weasyprint" in engines
    assert "reportlab" in engines

def test_render_html_to_pdf_skip():
    import pathlib
    path, summary = render_html_to_pdf("<h1>Test</h1>", pathlib.Path("test.pdf"), engine="invalid")
    assert path is None
    assert summary["status"] == "skipped"
