import argparse
from pathlib import Path
from devtools.dx_pipeline import DeveloperExperiencePipeline
from reports.report_builder import build_dx_quality_report

def main():
    parser = argparse.ArgumentParser(description="Run DX quality report")
    parser.parse_args()

    project_root = Path(__file__).parent.parent
    output_dir = project_root / "reports" / "output" / "dev_reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    pipeline = DeveloperExperiencePipeline(project_root)
    df, summary = pipeline.run_full_dx_check(save=False)

    df.to_csv(output_dir / "dx_quality.csv", index=False)

    report = build_dx_quality_report(df, summary)
    with open(output_dir / "dx_quality_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("DX Quality report generated.")

if __name__ == "__main__":
    main()
