from maintenance.maintenance_report_builder import build_maintenance_disclaimer, build_storage_inventory_markdown_report

def test_maintenance_report_builder():
    disc = build_maintenance_disclaimer()
    assert "gerçek emir" in disc
    assert "yatırım tavsiyesi değildir" in disc

    md = build_storage_inventory_markdown_report({"total_files": 10})
    assert "**Total Files:** 10" in md
    assert "DISCLAIMER" in md
