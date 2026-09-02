import sys
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
    data_lake = DataLake(settings.paths if hasattr(settings, 'paths') else str(Path(__file__).resolve().parent.parent / 'data' / 'lake'))
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
