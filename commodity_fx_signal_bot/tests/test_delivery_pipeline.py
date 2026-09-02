from local_delivery.delivery_pipeline import LocalDeliveryPipeline
from pathlib import Path

class MockDataLake:
    pass

def test_pipeline_init():
    pipe = LocalDeliveryPipeline(MockDataLake(), None, Path("."))
    assert pipe.project_root == Path(".")
