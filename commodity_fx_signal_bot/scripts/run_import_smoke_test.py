import argparse
from pathlib import Path
from devtools.import_smoke import run_import_smoke_test, list_project_packages
from reports.report_builder import build_import_smoke_test_report

def main():
    parser = argparse.ArgumentParser(description="Run import smoke test")
    parser.parse_args()

    project_root = Path(__file__).parent.parent
    output_dir = project_root / "reports" / "output" / "dev_reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    packages = list_project_packages(project_root)
    df, summary = run_import_smoke_test(packages)

    df.to_csv(output_dir / "import_smoke_test.csv", index=False)

    report = build_import_smoke_test_report(df, summary)
    with open(output_dir / "import_smoke_test_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("Import Smoke Test report generated.")

if __name__ == "__main__":
    main()
