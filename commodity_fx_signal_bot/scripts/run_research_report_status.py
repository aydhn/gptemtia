import sys
import logging
import pandas as pd
from data.storage.data_lake import DataLake
from config.paths import REPORTS_RESEARCH_REPORTS_CSV_DIR, REPORTS_RESEARCH_REPORTS_TXT_DIR
from reports.report_builder import build_research_report_status_report

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Checking research report status...")

    data_lake = DataLake()

    status_df = data_lake.list_research_reports()

    text_report = build_research_report_status_report(status_df, {})

    csv_path = REPORTS_RESEARCH_REPORTS_CSV_DIR / "research_report_status.csv"
    txt_path = REPORTS_RESEARCH_REPORTS_TXT_DIR / "research_report_status_report.txt"

    if not status_df.empty:
        status_df.to_csv(csv_path, index=False)
    else:
        pd.DataFrame(columns=["status", "message"]).to_csv(csv_path, index=False)

    txt_path.write_text(text_report, encoding='utf-8')

    logger.info(f"Research report status saved to {txt_path}")
    logger.info("NOTE: Bu çıktı offline araştırma/simülasyon raporudur. Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.")
    sys.exit(0)

if __name__ == "__main__":
    main()
