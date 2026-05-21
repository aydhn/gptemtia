from pathlib import Path
from report_exports.report_packager import ReportPackager

def test_build_package_dir(tmp_path):
    packager = ReportPackager(tmp_path)
    p = packager.build_package_dir("rpt_1", "symbol", "GC=F", "1d")
    assert p.exists()
    assert "GC_F" in p.name

def test_write_package_readme(tmp_path):
    packager = ReportPackager(tmp_path)
    p = packager.build_package_dir("rpt_1", "symbol", "GC=F", "1d")
    readme = packager.write_package_readme(p, {"report_id": "rpt_1", "report_type": "symbol", "timeframe": "1d"})

    assert readme.exists()
    content = readme.read_text(encoding="utf-8")
    assert "offline araştırma raporu" in content
    assert "Canlı emir" in content
