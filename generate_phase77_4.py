import os
from pathlib import Path

BASE_DIR = Path("commodity_fx_signal_bot")
SCRIPTS_DIR = BASE_DIR / "scripts"
os.makedirs(SCRIPTS_DIR, exist_ok=True)

# scripts/run_acceptance_domain_registry.py
with open(SCRIPTS_DIR / "run_acceptance_domain_registry.py", "w", encoding="utf-8") as f:
    f.write('''import argparse
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_acceptance.acceptance_pipeline import LocalAcceptancePipeline
from local_acceptance.acceptance_config import get_local_acceptance_profile
from local_acceptance.acceptance_report_builder import build_acceptance_domain_registry_markdown_report
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_acceptance")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    settings = Settings()
    data_lake = DataLake(settings)
    report_builder = ReportBuilder(settings, data_lake)
    profile = get_local_acceptance_profile(args.profile)

    pipeline = LocalAcceptancePipeline(data_lake, settings, project_root, profile)
    dfs, summary = pipeline.build_acceptance_domain_registry(save=args.save)
    
    if args.save:
        md = build_acceptance_domain_registry_markdown_report(summary["domain"], dfs["domain"])
        txt = report_builder.build_acceptance_domain_registry_text_report(summary["domain"], dfs["domain"])
        
        md_path = settings.paths["output_local_acceptance_markdown"] / "acceptance_domain_registry_report.md"
        txt_path = settings.paths["output_local_acceptance_txt"] / "acceptance_domain_registry_report.txt"
        
        md_path.parent.mkdir(parents=True, exist_ok=True)
        txt_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(md_path, "w", encoding="utf-8") as f: f.write(md)
        with open(txt_path, "w", encoding="utf-8") as f: f.write(txt)
        
        csv_dir = settings.paths["output_local_acceptance_csv"]
        csv_dir.mkdir(parents=True, exist_ok=True)
        dfs["domain"].to_csv(csv_dir / "acceptance_domain_registry.csv", index=False)
        dfs["criteria"].to_csv(csv_dir / "acceptance_criteria_registry.csv", index=False)
        dfs["no_go"].to_csv(csv_dir / "acceptance_no_go_register.csv", index=False)
        dfs["safe_go"].to_csv(csv_dir / "acceptance_safe_go_register.csv", index=False)
        
        print("Acceptance domain registry saved.")

if __name__ == "__main__":
    main()
''')

# scripts/run_final_acceptance_simulation.py
with open(SCRIPTS_DIR / "run_final_acceptance_simulation.py", "w", encoding="utf-8") as f:
    f.write('''import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_acceptance.acceptance_pipeline import LocalAcceptancePipeline
from local_acceptance.acceptance_report_builder import build_final_acceptance_simulation_markdown_report
from reports.report_builder import ReportBuilder

def main():
    project_root = Path(__file__).resolve().parent.parent
    settings = Settings()
    data_lake = DataLake(settings)
    report_builder = ReportBuilder(settings, data_lake)
    pipeline = LocalAcceptancePipeline(data_lake, settings, project_root)

    dfs, summary = pipeline.build_final_acceptance_simulation(save=True)
    
    md = build_final_acceptance_simulation_markdown_report(summary["checklist"], dfs["checklist"])
    txt = report_builder.build_final_acceptance_simulation_text_report(summary["checklist"], dfs["checklist"])
    
    md_path = settings.paths["output_local_acceptance_markdown"] / "final_acceptance_simulation_report.md"
    txt_path = settings.paths["output_local_acceptance_txt"] / "final_acceptance_simulation_report.txt"
    
    md_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(md_path, "w", encoding="utf-8") as f: f.write(md)
    with open(txt_path, "w", encoding="utf-8") as f: f.write(txt)
    
    csv_dir = settings.paths["output_local_acceptance_csv"]
    csv_dir.mkdir(parents=True, exist_ok=True)
    dfs["checklist"].to_csv(csv_dir / "final_acceptance_simulation_checklist.csv", index=False)
    dfs["exceptions"].to_csv(csv_dir / "acceptance_exception_register.csv", index=False)
    dfs["score"].to_csv(csv_dir / "acceptance_readiness_score_report.csv", index=False)
    
    print("Final acceptance simulation saved.")

if __name__ == "__main__":
    main()
''')

# scripts/run_independent_reviewer_pack.py
with open(SCRIPTS_DIR / "run_independent_reviewer_pack.py", "w", encoding="utf-8") as f:
    f.write('''import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_acceptance.acceptance_pipeline import LocalAcceptancePipeline
from local_acceptance.acceptance_config import get_local_acceptance_profile
from local_acceptance.acceptance_report_builder import build_independent_reviewer_pack_markdown_report
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="independent_reviewer_focus")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    settings = Settings()
    data_lake = DataLake(settings)
    report_builder = ReportBuilder(settings, data_lake)
    profile = get_local_acceptance_profile(args.profile)
    pipeline = LocalAcceptancePipeline(data_lake, settings, project_root, profile)

    text, summary = pipeline.build_independent_reviewer_pack(save=True)
    
    md = build_independent_reviewer_pack_markdown_report(summary, text)
    txt = report_builder.build_independent_reviewer_pack_text_report(summary, text)
    
    md_path = settings.paths["output_local_acceptance_markdown"] / "independent_reviewer_pack.md"
    txt_path = settings.paths["output_local_acceptance_txt"] / "independent_reviewer_pack.txt"
    
    md_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(md_path, "w", encoding="utf-8") as f: f.write(md)
    with open(txt_path, "w", encoding="utf-8") as f: f.write(txt)
    
    docs_dir = settings.paths["docs_generated_local_acceptance"]
    docs_dir.mkdir(parents=True, exist_ok=True)
    with open(docs_dir / "INDEPENDENT_REVIEWER_PACK.md", "w", encoding="utf-8") as f: f.write(md)
    
    print("Independent reviewer pack saved.")

if __name__ == "__main__":
    main()
''')

# scripts/run_acceptance_evidence_trail.py
with open(SCRIPTS_DIR / "run_acceptance_evidence_trail.py", "w", encoding="utf-8") as f:
    f.write('''import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_acceptance.acceptance_pipeline import LocalAcceptancePipeline
from local_acceptance.acceptance_config import get_local_acceptance_profile
from local_acceptance.acceptance_report_builder import build_acceptance_evidence_trail_markdown_report
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="evidence_trail_focus")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    settings = Settings()
    data_lake = DataLake(settings)
    report_builder = ReportBuilder(settings, data_lake)
    profile = get_local_acceptance_profile(args.profile)
    pipeline = LocalAcceptancePipeline(data_lake, settings, project_root, profile)

    dfs, summary = pipeline.build_acceptance_evidence_trail(save=True)
    
    md = build_acceptance_evidence_trail_markdown_report(summary["evidence"], dfs["evidence"])
    txt = report_builder.build_acceptance_evidence_trail_text_report(summary["evidence"], dfs["evidence"])
    
    md_path = settings.paths["output_local_acceptance_markdown"] / "acceptance_evidence_trail_report.md"
    txt_path = settings.paths["output_local_acceptance_txt"] / "acceptance_evidence_trail_report.txt"
    
    md_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(md_path, "w", encoding="utf-8") as f: f.write(md)
    with open(txt_path, "w", encoding="utf-8") as f: f.write(txt)
    
    csv_dir = settings.paths["output_local_acceptance_csv"]
    csv_dir.mkdir(parents=True, exist_ok=True)
    dfs["evidence"].to_csv(csv_dir / "audit_style_local_evidence_trail.csv", index=False)
    dfs["output_trace"].to_csv(csv_dir / "evidence_output_trace_matrix.csv", index=False)
    dfs["test_trace"].to_csv(csv_dir / "evidence_test_trace_matrix.csv", index=False)
    dfs["doc_trace"].to_csv(csv_dir / "evidence_doc_trace_matrix.csv", index=False)
    dfs["safety_trace"].to_csv(csv_dir / "evidence_safety_boundary_trace_matrix.csv", index=False)
    
    print("Acceptance evidence trail saved.")

if __name__ == "__main__":
    main()
''')

# scripts/run_signoff_rehearsal.py
with open(SCRIPTS_DIR / "run_signoff_rehearsal.py", "w", encoding="utf-8") as f:
    f.write('''import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_acceptance.acceptance_pipeline import LocalAcceptancePipeline
from local_acceptance.acceptance_report_builder import build_signoff_rehearsal_markdown_report
from reports.report_builder import ReportBuilder

def main():
    project_root = Path(__file__).resolve().parent.parent
    settings = Settings()
    data_lake = DataLake(settings)
    report_builder = ReportBuilder(settings, data_lake)
    pipeline = LocalAcceptancePipeline(data_lake, settings, project_root)

    text, summary = pipeline.build_signoff_rehearsal(save=True)
    
    md = build_signoff_rehearsal_markdown_report(summary, text)
    txt = report_builder.build_signoff_rehearsal_text_report(summary, text)
    
    md_path = settings.paths["output_local_acceptance_markdown"] / "signoff_rehearsal_report.md"
    txt_path = settings.paths["output_local_acceptance_txt"] / "signoff_rehearsal_report.txt"
    
    md_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(md_path, "w", encoding="utf-8") as f: f.write(md)
    with open(txt_path, "w", encoding="utf-8") as f: f.write(txt)
    
    print("Sign-off rehearsal saved.")

if __name__ == "__main__":
    main()
''')

# scripts/run_acceptance_quality_report.py
with open(SCRIPTS_DIR / "run_acceptance_quality_report.py", "w", encoding="utf-8") as f:
    f.write('''import argparse
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_acceptance.acceptance_pipeline import LocalAcceptancePipeline
from local_acceptance.acceptance_config import get_local_acceptance_profile
from local_acceptance.acceptance_report_builder import build_acceptance_quality_markdown_report
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="strict_acceptance_safety")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    settings = Settings()
    data_lake = DataLake(settings)
    report_builder = ReportBuilder(settings, data_lake)
    profile = get_local_acceptance_profile(args.profile)
    pipeline = LocalAcceptancePipeline(data_lake, settings, project_root, profile)

    q, s = pipeline.build_acceptance_quality_report(save=True)
    
    md = build_acceptance_quality_markdown_report(s, q)
    txt = report_builder.build_acceptance_quality_text_report(s, q)
    
    md_path = settings.paths["output_local_acceptance_markdown"] / "acceptance_quality_report.md"
    txt_path = settings.paths["output_local_acceptance_txt"] / "acceptance_quality_report.txt"
    json_path = settings.paths["output_local_acceptance_json"] / "acceptance_quality_report.json"
    
    md_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(md_path, "w", encoding="utf-8") as f: f.write(md)
    with open(txt_path, "w", encoding="utf-8") as f: f.write(txt)
    with open(json_path, "w", encoding="utf-8") as f: json.dump(q, f, indent=2)
    
    print("Acceptance quality report saved.")

if __name__ == "__main__":
    main()
''')

# scripts/run_acceptance_status.py
with open(SCRIPTS_DIR / "run_acceptance_status.py", "w", encoding="utf-8") as f:
    f.write('''import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from local_acceptance.acceptance_pipeline import LocalAcceptancePipeline
from local_acceptance.acceptance_report_builder import build_acceptance_status_markdown_report
from reports.report_builder import ReportBuilder

def main():
    project_root = Path(__file__).resolve().parent.parent
    settings = Settings()
    data_lake = DataLake(settings)
    report_builder = ReportBuilder(settings, data_lake)
    pipeline = LocalAcceptancePipeline(data_lake, settings, project_root)

    df, s = pipeline.build_acceptance_status(save=True)
    
    md = build_acceptance_status_markdown_report(s, df)
    txt = report_builder.build_acceptance_status_report(df, s)
    
    md_path = settings.paths["output_local_acceptance_markdown"] / "acceptance_status_report.md"
    txt_path = settings.paths["output_local_acceptance_txt"] / "acceptance_status_report.txt"
    
    md_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(md_path, "w", encoding="utf-8") as f: f.write(md)
    with open(txt_path, "w", encoding="utf-8") as f: f.write(txt)
    
    csv_dir = settings.paths["output_local_acceptance_csv"]
    csv_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_dir / "acceptance_status.csv", index=False)
    
    print("Acceptance status saved.")

if __name__ == "__main__":
    main()
''')
