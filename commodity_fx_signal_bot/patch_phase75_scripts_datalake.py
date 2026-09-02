import os
from pathlib import Path

base_dir = Path("c:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia/commodity_fx_signal_bot")
scripts_dir = base_dir / "scripts"

for file in scripts_dir.glob("run_synthesis_*.py"):
    text = file.read_text(encoding="utf-8")
    text = text.replace("data_lake = DataLake(paths, settings)", "data_lake = DataLake(str(Path(__file__).parent.parent))")
    file.write_text(text, encoding="utf-8")

for file in scripts_dir.glob("run_master_index*.py"):
    text = file.read_text(encoding="utf-8")
    text = text.replace("data_lake = DataLake(paths, settings)", "data_lake = DataLake(str(Path(__file__).parent.parent))")
    file.write_text(text, encoding="utf-8")

for file in scripts_dir.glob("run_cross_phase*.py"):
    text = file.read_text(encoding="utf-8")
    text = text.replace("data_lake = DataLake(paths, settings)", "data_lake = DataLake(str(Path(__file__).parent.parent))")
    file.write_text(text, encoding="utf-8")

for file in scripts_dir.glob("run_project_completion*.py"):
    text = file.read_text(encoding="utf-8")
    text = text.replace("data_lake = DataLake(paths, settings)", "data_lake = DataLake(str(Path(__file__).parent.parent))")
    file.write_text(text, encoding="utf-8")

for file in scripts_dir.glob("run_end_state*.py"):
    text = file.read_text(encoding="utf-8")
    text = text.replace("data_lake = DataLake(paths, settings)", "data_lake = DataLake(str(Path(__file__).parent.parent))")
    file.write_text(text, encoding="utf-8")

