import pandas as pd

from governance.governance_models import ProvenanceRecord
from governance.provenance_registry import (
    ProvenanceRegistry,
    build_provenance_records_from_inventory,
    infer_producer_module_from_path,
)


def test_add_load_record(tmp_path):
    reg_dir = tmp_path / "gov"
    reg = ProvenanceRegistry(reg_dir)

    rec = ProvenanceRecord(
        provenance_id="p1", artifact_id="a1", artifact_type="feat", source_system="sys",
        producer_module="mod", producer_script=None, run_id=None, experiment_id=None,
        timeframe=None, symbols=[], parameters_hash=None, input_artifact_ids=[],
        created_at_utc="now", warnings=[]
    )

    reg.add_record(rec)
    df = reg.load_records()
    assert not df.empty
    assert df.iloc[0]["provenance_id"] == "p1"

def test_infer_producer():
    assert infer_producer_module_from_path("data/lake/factor_research/f.csv") == "factor_research"

def test_build_records_from_inventory():
    inv_df = pd.DataFrame([{
        "artifact_id": "a1", "relative_path": "features/f.csv", "artifact_type": "feat"
    }])
    df, summary = build_provenance_records_from_inventory(inv_df)
    assert not df.empty
    assert "feature_pipeline" in df["producer_module"].values
