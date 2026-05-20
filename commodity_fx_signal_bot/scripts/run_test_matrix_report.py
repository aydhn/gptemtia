import argparse
from pathlib import Path
from devtools.test_matrix import build_test_matrix, export_test_matrix_markdown
from reports.report_builder import build_test_matrix_report

def main():
    parser = argparse.ArgumentParser(description="Run test matrix report")
    parser.parse_args()

    project_root = Path(__file__).parent.parent
    output_dir = project_root / "reports" / "output" / "dev_reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    df, summary = build_test_matrix(project_root)

    df.to_csv(output_dir / "test_matrix.csv", index=False)

    md_content = export_test_matrix_markdown(df)
    with open(output_dir / "test_matrix.md", "w", encoding="utf-8") as f:
        f.write(md_content)

    report = build_test_matrix_report(df, summary)
    with open(output_dir / "test_matrix_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("Test Matrix report generated.")

if __name__ == "__main__":
    main()
