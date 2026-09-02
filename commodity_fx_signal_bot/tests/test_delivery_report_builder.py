from local_delivery.delivery_report_builder import build_delivery_domain_registry_markdown_report
import pandas as pd

def test_build_domain_registry_report():
    txt = build_delivery_domain_registry_markdown_report({"total": 0})
    assert isinstance(txt, str)
