import pytest
import pandas as pd
from pathlib import Path
import tempfile
from research_reports.csv_exporter import (
    export_ranking_table,
    export_symbol_summary_table,
    export_section_table,
    build_csv_export_manifest
)
from research_reports.research_models import SymbolResearchSnapshot

def test_export_ranking_table():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "rank.csv"
        df = pd.DataFrame({"A": [1]})
        export_ranking_table(df, path)
        assert path.exists()

        path2 = Path(tmpdir) / "empty.csv"
        export_ranking_table(pd.DataFrame(), path2)
        assert path2.exists() # Should write empty file

def test_export_symbol_summary_table():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "sym.csv"
        snap = SymbolResearchSnapshot("AAPL", "1d", "stock", "2023", {}, {}, {}, {}, {}, {}, {}, {}, 0.5, "ready", [])
        export_symbol_summary_table([snap], path)
        assert path.exists()
        saved = pd.read_csv(path)
        assert "symbol" in saved.columns
        assert saved.iloc[0]["symbol"] == "AAPL"

def test_export_section_table():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "sec.csv"
        export_section_table(pd.DataFrame({"X": [1]}), path)
        assert path.exists()

def test_build_csv_export_manifest():
    manifest = build_csv_export_manifest([Path("a.csv"), Path("b.csv")])
    assert manifest["count"] == 2
    assert "a.csv" in manifest["exported_files"]
