import re
from pathlib import Path
from typing import Tuple, Dict

try:
    import markdown
except ImportError:
    markdown = None

from report_exports.export_config import ReportExportProfile

def markdown_to_basic_html(markdown_text: str) -> str:
    if markdown:
        return markdown.markdown(markdown_text, extensions=['tables', 'fenced_code'])

    html = markdown_text
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'(?m)^### (.*?)$', r'<h3>\1</h3>', html)
    html = re.sub(r'(?m)^## (.*?)$', r'<h2>\1</h2>', html)
    html = re.sub(r'(?m)^# (.*?)$', r'<h1>\1</h1>', html)
    html = html.replace('\n', '<br>\n')
    return html

def build_research_css(theme: str = "clean_research") -> str:
    css = """
    body { font-family: sans-serif; }
    .disclaimer { border: 1px solid #ffeeba; background-color: #fff3cd; color: #856404; padding: 1rem; margin: 2rem 0; }
    """
    return css

def build_html_document(title: str, body_html: str, profile: ReportExportProfile) -> str:
    css = build_research_css(profile.html_theme)

    disclaimer_html = ""
    if profile.require_disclaimer:
        disclaimer_html = """
        <div class="disclaimer">
            <strong>UYARI:</strong> Bu çıktı offline araştırma raporu dışa aktarım/arşiv raporudur.
            Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="{profile.language}">
<head><meta charset="UTF-8"><title>{title}</title><style>{css}</style></head>
<body>{disclaimer_html}{body_html}{disclaimer_html}</body></html>"""
    return html

def render_markdown_report_to_html(markdown_text: str, title: str, profile: ReportExportProfile) -> Tuple[str, Dict]:
    body_html = markdown_to_basic_html(markdown_text)
    html_doc = build_html_document(title, body_html, profile)
    return html_doc, {"status": "success", "theme": profile.html_theme, "disclaimer_included": profile.require_disclaimer}

def save_html_report(html_text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_text)
    return output_path
