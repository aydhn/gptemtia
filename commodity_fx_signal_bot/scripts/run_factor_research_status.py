import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.paths import DATA_DIR
from data.storage.data_lake import DataLake

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Checking Factor Research Status...")
    dl = DataLake()

    try:
         df = dl.list_factor_research_reports()
         if df.empty:
              logger.info("No factor research reports found.")
         else:
              logger.info(f"Found {len(df)} reports.")
              logger.info(f"\n{df.head()}")
    except Exception as e:
         logger.error(f"Error checking status: {e}")

if __name__ == "__main__":
    main()
