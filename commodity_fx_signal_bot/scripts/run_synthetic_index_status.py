import logging
import pandas as pd
from config.settings import settings
from data.storage.data_lake import DataLake
from reports.report_builder import build_synthetic_index_status_report

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("run_synthetic_index_status")

def main():
    logger.info("Checking synthetic index status...")
    data_lake = DataLake(settings)

    reports_df = data_lake.list_synthetic_index_reports()

    summary = {
        "reports_found": len(reports_df) if not reports_df.empty else 0
    }

    logger.info(f"Found {summary['reports_found']} synthetic index reports.")

    if settings.synthetic_indices_enabled:
         txt_path = data_lake.paths.synthetic_indices_reports / "synthetic_index_status_report.txt"
         txt_content = build_synthetic_index_status_report(reports_df, summary)
         with open(txt_path, "w") as f:
             f.write(txt_content)

         if not reports_df.empty:
              csv_path = data_lake.paths.synthetic_indices_reports / "synthetic_index_status.csv"
              reports_df.to_csv(csv_path, index=False)

         logger.info("Status report saved.")

if __name__ == "__main__":
    main()
