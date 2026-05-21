from report_exports.export_pipeline import ReportExportPipeline
from report_exports.export_config import get_default_report_export_profile

class MockDataLake:
    def __init__(self):
        self.archive_records = []
        self.manifests = {}

    def load_research_report_markdown(self, report_id, report_type, symbol=None):
        return "# Mock Report\n\nThis is a mock offline araştırma raporu"

    def save_report_export_manifest(self, rid, m):
        self.manifests[rid] = m

    def save_report_archive_record(self, r):
        self.archive_records.append(r)

    def save_report_comparison(self, cid, c):
        pass

    def save_periodic_tracking_table(self, t, p, df):
        pass

    def save_report_export_quality(self, rid, q):
        pass

class MockSettings:
    default_report_export_profile = "balanced_report_export"

def test_export_pipeline_missing_report():
    lake = MockDataLake()
    lake.load_research_report_markdown = lambda *args: None
    pipeline = ReportExportPipeline(lake, MockSettings(), get_default_report_export_profile())

    _, summary = pipeline.export_symbol_report("GC=F", save=False)
    assert summary["status"] == "missing_report"

def test_export_pipeline_success():
    lake = MockDataLake()
    pipeline = ReportExportPipeline(lake, MockSettings(), get_default_report_export_profile())

    _, summary = pipeline.export_symbol_report("GC=F", save=False)
    assert summary["html_status"] == "success"
