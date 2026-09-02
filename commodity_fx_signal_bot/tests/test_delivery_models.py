from local_delivery.delivery_models import build_delivery_domain_id, build_delivery_item_id, build_delivery_trace_id, build_delivery_checklist_id, build_delivery_finding_id
from local_delivery.delivery_models import DeliveryDomain, delivery_domain_to_dict

def test_model_ids():
    assert build_delivery_domain_id("test") == build_delivery_domain_id("test")
    assert build_delivery_item_id("path", "lbl") == build_delivery_item_id("path", "lbl")
    assert build_delivery_trace_id("src", "tgt") == build_delivery_trace_id("src", "tgt")

def test_model_to_dict():
    d = DeliveryDomain("id", "lbl", "name", "desc", [], [])
    res = delivery_domain_to_dict(d)
    assert res["domain_id"] == "id"
