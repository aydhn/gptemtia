import sys
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
    data_lake = DataLake(settings.paths if hasattr(settings, 'paths') else str(Path(__file__).resolve().parent.parent / 'data' / 'lake'))
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
