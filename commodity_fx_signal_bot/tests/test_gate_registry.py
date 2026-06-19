import pandas as pd
from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.gate_registry import build_default_readiness_gates, readiness_gates_to_dataframe, evaluate_readiness_gate_artifacts
from config.paths import PROJECT_ROOT

def test_default_readiness_gates():
    profile = get_default_local_readiness_profile()
    gates = build_default_readiness_gates(profile)
    assert len(gates) > 0

    df = readiness_gates_to_dataframe(gates)
    assert "gate_id" in df.columns

def test_evaluate_gates():
    profile = get_default_local_readiness_profile()
    gates = build_default_readiness_gates(profile)
    df = readiness_gates_to_dataframe(gates)
    eval_df, summ = evaluate_readiness_gate_artifacts(df, PROJECT_ROOT, profile)
    assert not eval_df.empty
