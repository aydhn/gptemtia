from pathlib import Path
from devtools.cli_catalog import (
    discover_script_modules, infer_command_group, build_command_example,
    build_cli_command_catalog, export_cli_catalog_markdown
)

def test_infer_command_group():
    assert infer_command_group("scripts.run_data_pipeline") == "data"
    assert infer_command_group("scripts.run_signal_generator") == "candidates"

def test_build_command_example():
    assert build_command_example("scripts.test", "data") == "python -m scripts.test"

def test_build_cli_command_catalog(tmp_path):
    df, summary = build_cli_command_catalog(tmp_path)
    assert "total_commands" in summary
    assert isinstance(export_cli_catalog_markdown(df), str)
