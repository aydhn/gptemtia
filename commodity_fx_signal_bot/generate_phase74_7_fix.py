import os
from pathlib import Path

def write_file(path, content):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

write_file('generate_phase74_scripts.py', '''
import os
from pathlib import Path

def write_file(path, content):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\\n')

def make_script(name, method, kwargs=""):
    content = f"""
import argparse
from pathlib import Path
from data.storage.data_lake import DataLake
from config.settings import Settings
from local_briefing.briefing_config import get_local_briefing_profile
from local_briefing.briefing_pipeline import LocalBriefingPipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_briefing")
    parser.add_argument("--save", type=bool, default=True)
    args, _ = parser.parse_known_args()
    
    settings = Settings()
    data_lake = DataLake("data/lake")
    profile = get_local_briefing_profile(args.profile)
    
    pipeline = LocalBriefingPipeline(data_lake, settings, Path("."), profile)
    res, sum = pipeline.{method}(save=args.save{kwargs})
    print(f"{name} completed.")

if __name__ == "__main__":
    main()
"""
    write_file(f"scripts/{name}.py", content)

make_script("run_briefing_profile_registry", "build_briefing_profile_registry")
make_script("run_executive_summary_pack", "build_executive_summary_pack")
make_script("run_briefing_deck_source", "build_briefing_deck_source")
make_script("run_decision_context_binder", "build_decision_context_binder")
make_script("run_stakeholder_communication_kit", "build_stakeholder_communication_kit")
make_script("run_briefing_quality_report", "build_briefing_quality_report")
make_script("run_briefing_status", "build_briefing_status")
''')
