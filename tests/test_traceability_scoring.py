from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.traceability_scoring import (
    build_dataset_traceability_score_report,
    build_provider_traceability_score_report,
    calculate_dataset_traceability_score,
    calculate_provider_traceability_score,
    summarize_traceability_scores,
)


def test_traceability_scoring():
    profile = get_default_data_lineage_profile()
    ds_df, ds_sum = build_dataset_traceability_score_report(profile)
    assert len(ds_df) >= 8
    assert 0.0 <= ds_sum["mean_traceability_score"] <= 1.0

    prov_df, prov_sum = build_provider_traceability_score_report(profile)
    assert len(prov_df) >= 8
    assert 0.0 <= prov_sum["mean_traceability_score"] <= 1.0

    sc_ds = calculate_dataset_traceability_score(ds_df, "fx_quote_contract_dataset", profile)
    assert 0.0 <= sc_ds <= 1.0

    sc_prov = calculate_provider_traceability_score(prov_df, "advanced_fx_providers_engine", profile)
    assert 0.0 <= sc_prov <= 1.0
