from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.copyright_boundary_provenance import (
    build_copyright_boundary_provenance_registry,
    check_copyright_boundary_provenance,
    summarize_copyright_boundary_provenance,
)


def test_copyright_boundary():
    profile = get_default_data_lineage_profile()
    df, summary = build_copyright_boundary_provenance_registry(profile)
    assert len(df) >= 5
    assert summary["zero_full_text"] is True
    assert summary["all_passed"] is True

    chk = check_copyright_boundary_provenance(df)
    assert chk["passed"] is True
    assert len(chk["violations"]) == 0
