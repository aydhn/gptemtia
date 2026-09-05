import tempfile
from pathlib import Path
import pandas as pd
from advanced_data_normalization.normalized_output_writer import (
    write_normalized_view_copy,
    write_normalization_report_json,
    build_normalized_output_manifest,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_write_normalized_view_copy_non_destructive():
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir) / "output.csv"
        df1 = pd.DataFrame([{"a": 1}])
        df2 = pd.DataFrame([{"a": 2}])

        # Write first copy
        p1 = write_normalized_view_copy(df1, tmp_path, allow_overwrite=False)
        assert p1 == tmp_path
        assert tmp_path.exists()

        # Write second copy with allow_overwrite=False: must not overwrite, but create v1
        p2 = write_normalized_view_copy(df2, tmp_path, allow_overwrite=False)
        assert p2 != tmp_path
        assert p2.exists()
        assert tmp_path.exists()


def test_build_normalized_output_manifest():
    prof = get_default_data_normalization_profile()
    df, summary = build_normalized_output_manifest(prof)
    assert not df.empty
    assert summary["source_preserved_all"] is True
    assert summary["destructive_action_allowed_zero"] is True
