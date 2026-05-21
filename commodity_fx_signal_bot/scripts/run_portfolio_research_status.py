#!/usr/bin/env python3
import argparse
import sys
import logging
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data.storage.data_lake import DataLake

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    data_lake = DataLake()

    if hasattr(data_lake, 'list_portfolio_research_reports'):
        df = data_lake.list_portfolio_research_reports()
        if not df.empty:
            logger.info(f"Found {len(df)} portfolio research reports.")
            print(df.to_string())
        else:
            logger.info("No portfolio research reports found.")
    else:
        logger.warning("list_portfolio_research_reports not found in DataLake.")

if __name__ == "__main__":
    main()
