import logging
from pathlib import Path
from typing import Tuple, Dict, Optional

from report_exports.export_config import ReportExportProfile
from report_exports.html_renderer import render_markdown_report_to_html

logger = logging.getLogger(__name__)

def detect_available_pdf_engines() -> Dict[str, bool]:
    engines = {"weasyprint": False, "reportlab": False}
    try:
        import weasyprint
        engines["weasyprint"] = True
    except ImportError:
        pass
    try:
        import reportlab
        engines["reportlab"] = True
    except ImportError:
        pass
    return engines

def render_html_to_pdf(html_text: str, output_path: Path, engine: str = "auto") -> Tuple[Optional[Path], Dict]:
    engines = detect_available_pdf_engines()
    summary = {"status": "failed", "engine_used": None, "error": None}

    target_engine = None
    if engine == "auto":
        if engines["weasyprint"]:
            target_engine = "weasyprint"
        elif engines["reportlab"]:
            target_engine = "reportlab"
    elif engine in engines and engines[engine]:
        target_engine = engine

    if not target_engine:
        summary["status"] = "skipped"
        summary["error"] = "export_dependency_missing"
        return None, summary

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        if target_engine == "weasyprint":
            from weasyprint import HTML
            HTML(string=html_text).write_pdf(output_path)
        elif target_engine == "reportlab":
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import letter
            import re
            text = re.sub('<[^<]+>', '', html_text)
            c = canvas.Canvas(str(output_path), pagesize=letter)
            width, height = letter
            y = height - 40
            for line in text.split('\n'):
                if y < 40:
                    c.showPage()
                    y = height - 40
                c.drawString(40, y, line[:100])
                y -= 15
            c.save()
        summary["status"] = "success"
        summary["engine_used"] = target_engine
        return output_path, summary
    except Exception as e:
        summary["error"] = str(e)
        return None, summary

def render_markdown_to_pdf(markdown_text: str, output_path: Path, profile: ReportExportProfile) -> Tuple[Optional[Path], Dict]:
    if not profile.include_pdf:
        return None, {"status": "skipped", "reason": "pdf disabled in profile"}
    html_text, _ = render_markdown_report_to_html(markdown_text, "Report Export", profile)
    return render_html_to_pdf(html_text, output_path, engine=profile.pdf_engine)

def build_pdf_export_summary(path: Optional[Path], engine_summary: Dict) -> Dict:
    return {
        "pdf_path": str(path) if path else None,
        "pdf_status": engine_summary.get("status", "unknown"),
        "pdf_engine": engine_summary.get("engine_used"),
        "pdf_error": engine_summary.get("error")
    }
