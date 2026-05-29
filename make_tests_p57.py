import os

test_files = {
    "test_regression_config.py": """
import pytest
from scenario_regression.regression_config import (
    ScenarioRegressionProfile,
    get_scenario_regression_profile,
    list_scenario_regression_profiles,
    validate_scenario_regression_profiles,
    get_default_scenario_regression_profile,
    ConfigError
)

def test_validate_scenario_regression_profiles():
    validate_scenario_regression_profiles() # Should not raise

def test_get_default_scenario_regression_profile():
    p = get_default_scenario_regression_profile()
    assert isinstance(p, ScenarioRegressionProfile)
    assert p.use_synthetic_only is True
    assert p.allow_real_market_download is False

def test_invalid_profile():
    with pytest.raises(ConfigError):
        get_scenario_regression_profile("non_existent_profile")
""",
    "test_regression_labels.py": """
import pytest
from scenario_regression.regression_labels import (
    list_regression_type_labels, list_regression_status_labels,
    list_snapshot_diff_labels, list_replay_status_labels, list_acceptance_labels,
    validate_regression_type, validate_acceptance_label
)

def test_labels_not_empty():
    assert len(list_regression_type_labels()) > 0
    assert len(list_acceptance_labels()) > 0

def test_validate_labels():
    validate_regression_type("golden_output_regression")
    validate_acceptance_label("demo_accepted_offline")

    with pytest.raises(ValueError):
        validate_regression_type("invalid_label")
""",
    "test_regression_models.py": """
from scenario_regression.regression_models import (
    build_regression_id, build_golden_output_id, build_snapshot_id, build_replay_id,
    ScenarioRegressionDefinition, scenario_regression_definition_to_dict
)

def test_id_builders():
    assert len(build_regression_id("scen1", "type1")) > 0
    assert len(build_golden_output_id("scen1", "out1")) > 0
    assert len(build_snapshot_id("scen1", "snap1")) > 0
    assert len(build_replay_id("scen1", "2024")) > 0

def test_dataclass_to_dict():
    d = ScenarioRegressionDefinition("r1", "s1", "t1", "n1", "d1", ["out1"], ["g1"], ["snp1"], True, ["w1"])
    dic = scenario_regression_definition_to_dict(d)
    assert dic["regression_id"] == "r1"
    assert "out1" in dic["expected_outputs"]
""",
    "test_regression_registry.py": """
import pandas as pd
from scenario_regression.regression_registry import build_default_regression_definitions, regression_definitions_to_dataframe
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_build_default_regression_definitions():
    scen_df = pd.DataFrame([{"scenario_id": "scen1"}])
    prof = get_default_scenario_regression_profile()
    defs = build_default_regression_definitions(scen_df, prof)
    assert len(defs) > 0

    df = regression_definitions_to_dataframe(defs)
    assert "regression_id" in df.columns
""",
    "test_golden_outputs.py": """
import pandas as pd
from pathlib import Path
from scenario_regression.golden_outputs import build_golden_outputs_for_scenario

def test_golden_output_generation(tmp_path):
    f = tmp_path / "test.csv"
    f.write_text("a,b\\n1,2")

    expected_df = pd.DataFrame([{"scenario_id": "scen1", "output_name": "test", "output_path": str(f)}])

    # We pass the root as / so it uses absolute paths we passed
    df, summary = build_golden_outputs_for_scenario("scen1", expected_df, Path("/"))
    assert not df.empty
    assert "test" in df.iloc[0]["output_name"]
    assert df.iloc[0]["synthetic_only"] is True
""",
    "test_snapshot_capture.py": """
from scenario_regression.snapshot_capture import capture_snapshot_for_artifact
from scenario_regression.regression_config import get_default_scenario_regression_profile
from pathlib import Path

def test_snapshot_capture(tmp_path):
    f = tmp_path / "test.csv"
    f.write_text("a,b\\n1,2")
    prof = get_default_scenario_regression_profile()

    rec = capture_snapshot_for_artifact("scen1", "snap1", f, prof)
    assert rec.scenario_id == "scen1"
    assert rec.snapshot_name == "snap1"
    assert rec.row_count == 1
""",
    "test_snapshot_compare.py": """
import pandas as pd
from scenario_regression.snapshot_compare import compare_snapshot_tables
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_snapshot_compare():
    prof = get_default_scenario_regression_profile()
    b_df = pd.DataFrame([{"scenario_id": "s1", "snapshot_name": "n1", "snapshot_id": "b1", "schema_hash": "h1", "content_hash": "c1", "row_count": 1}])
    c_df = pd.DataFrame([{"scenario_id": "s1", "snapshot_name": "n1", "snapshot_id": "c1", "schema_hash": "h1", "content_hash": "c1", "row_count": 1}])

    diff_df, summary = compare_snapshot_tables(b_df, c_df, prof)
    assert not diff_df.empty
    assert diff_df.iloc[0]["diff_label"] == "snapshot_identical"
""",
    "test_deterministic_replay.py": """
import pandas as pd
from pathlib import Path
from scenario_regression.deterministic_replay import DeterministicReplayRunner
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_replay_runner():
    prof = get_default_scenario_regression_profile()
    runner = DeterministicReplayRunner(Path("/"), prof)
    res = runner.replay_scenario("scen1", pd.DataFrame(), pd.DataFrame())
    assert res.replay_status == "replay_skipped"
""",
    "test_fixture_reproducibility.py": """
import pandas as pd
from scenario_regression.fixture_reproducibility import compare_fixture_reproducibility, validate_fixture_seed_consistency
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_fixture_reproducibility():
    prof = get_default_scenario_regression_profile()
    f_df = pd.DataFrame([{"scenario_id": "s1", "synthetic": True, "random_seed": 42}])
    df, summ = compare_fixture_reproducibility(f_df, pd.DataFrame(), prof)
    assert not df.empty

    seed_res = validate_fixture_seed_consistency(f_df, 42)
    assert seed_res["consistent"] is True
""",
    "test_output_contract_validation.py": """
import pandas as pd
from pathlib import Path
from scenario_regression.output_contract_validation import validate_scenario_output_contracts
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_output_contract_validation(tmp_path):
    f = tmp_path / "test.csv"
    f.write_text("a,b\\n1,2")
    prof = get_default_scenario_regression_profile()

    e_df = pd.DataFrame([{"scenario_id": "s1", "output_name": "n1", "output_path": str(f)}])
    df, summ = validate_scenario_output_contracts(e_df, Path("/"), prof)
    assert not df.empty
""",
    "test_demo_workflow_regression.py": """
import pandas as pd
from scenario_regression.demo_workflow_regression import build_demo_workflow_regression_report
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_demo_workflow_regression():
    prof = get_default_scenario_regression_profile()
    df, summ = build_demo_workflow_regression_report(None, None, None, prof)
    assert summ["summary"]["workflow_valid"] is False
""",
    "test_end_to_end_acceptance.py": """
import pandas as pd
from scenario_regression.end_to_end_acceptance import build_end_to_end_demo_acceptance_report
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_end_to_end_acceptance():
    prof = get_default_scenario_regression_profile()
    df, summ = build_end_to_end_demo_acceptance_report(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert "score" in summ
""",
    "test_drift_detection.py": """
import pandas as pd
from scenario_regression.drift_detection import detect_golden_output_drift
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_drift_detection():
    prof = get_default_scenario_regression_profile()
    g_df = pd.DataFrame([{"scenario_id": "s1", "matched": True}])
    df = detect_golden_output_drift(g_df, prof)
    assert not df.empty
    assert df.iloc[0]["drift_label"] == "no_drift"
""",
    "test_failure_register.py": """
import pandas as pd
from scenario_regression.failure_register import build_failures_from_regression_results, classify_failure_severity

def test_failure_register():
    t_df = pd.DataFrame([{"scenario_id": "s1", "warnings": "live order found"}])
    fails = build_failures_from_regression_results({"tbl1": t_df})
    assert len(fails) > 0
    assert fails[0].severity == "critical_regression_failure"
""",
    "test_acceptance_checklist.py": """
from scenario_regression.acceptance_checklist import build_regression_acceptance_checklist
from scenario_regression.regression_config import get_default_scenario_regression_profile

def test_acceptance_checklist():
    prof = get_default_scenario_regression_profile()
    df = build_regression_acceptance_checklist(prof)
    assert not df.empty
""",
    "test_regression_quality.py": """
from scenario_regression.regression_quality import check_for_forbidden_terms_in_regression

def test_forbidden_terms():
    res = check_for_forbidden_terms_in_regression(text="Bu bir live order testidir")
    assert res["passed"] is False
    assert "live order" in res["forbidden_terms_found"]

    res2 = check_for_forbidden_terms_in_regression(text="Canlı emir yoktur.")
    assert res2["passed"] is True
""",
    "test_regression_report_builder.py": """
from scenario_regression.regression_report_builder import build_regression_disclaimer

def test_disclaimer():
    d = build_regression_disclaimer()
    assert "offline" in d
    assert "yatırım tavsiyesi değildir" in d
""",
    "test_regression_pipeline.py": """
import pytest
from pathlib import Path
from config.settings import settings
from scenario_regression.regression_config import get_default_scenario_regression_profile
from scenario_regression.regression_pipeline import ScenarioRegressionPipeline

class MockDataLake:
    def __getattr__(self, name):
        if name.startswith("save_"):
            return lambda *args, **kwargs: Path("/")
        if name.startswith("load_"):
            return lambda *args, **kwargs: None
        return super().__getattr__(name)

def test_regression_pipeline():
    prof = get_default_scenario_regression_profile()
    dl = MockDataLake()
    pipe = ScenarioRegressionPipeline(dl, settings, Path("/"), prof)

    df, summ = pipe.build_scenario_regression_status(save=False)
    assert not df.empty
""",
    "test_scenario_regression_scripts_contract.py": """
import pytest
import sys
from pathlib import Path

def test_scripts_importable():
    import scripts.run_scenario_regression_registry
    import scripts.run_golden_output_report
    import scripts.run_snapshot_comparison_report
    import scripts.run_deterministic_replay_report
    import scripts.run_demo_acceptance_report
    import scripts.run_scenario_regression_status
    assert True
"""
}

for filename, content in test_files.items():
    with open(os.path.join('commodity_fx_signal_bot/tests', filename), 'w') as f:
        f.write(content.strip() + "\n")
