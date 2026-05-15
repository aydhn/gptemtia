import pytest
import pandas as pd
from notifications.delivery_log import DeliveryLog, build_delivery_audit
from notifications.notification_models import DeliveryResult

def test_delivery_log():
    log = DeliveryLog()
    res = DeliveryResult("1", "delivery_sent", False, "dest", "now", None)
    log.add_delivery_results([res])

    df = log.to_dataframe()
    assert not df.empty
    assert len(df) == 1

    summary = log.summarize()
    assert summary["sent_count"] == 1

    audit = build_delivery_audit(df)
    assert audit["total_messages"] == 1
