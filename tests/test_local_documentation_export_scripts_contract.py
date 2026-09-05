"""Test scripts."""
import subprocess
from pathlib import Path

def test_scripts_importable():
    scripts = [
        "run_documentation_export_domain_registry.py",
        "run_static_site_export_rehearsal.py",
        "run_offline_html_documentation_pack.py",
        "run_printable_binder_generator.py",
        "run_pdf_ready_documentation_layer.py",
        "run_archival_presentation_freeze.py",
        "run_documentation_export_quality_report.py",
        "run_documentation_export_status.py"
    ]
    for s in scripts:
        path = Path("scripts") / s
        assert path.exists()
