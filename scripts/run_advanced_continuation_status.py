#!/usr/bin/env python3
import sys
import logging
from pathlib import Path

# Add commodity_fx_signal_bot to path so it uses the real packages
sys.path.insert(0, str(Path(__file__).parent.parent / "commodity_fx_signal_bot"))

from config.settings import default_advanced_continuation_profile
from config.paths import LAKE_DIR
from advanced_continuation.continuation_config import get_advanced_continuation_profile
from advanced_continuation.continuation_pipeline import AdvancedContinuationPipeline
from data.storage.data_lake import DataLake

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    profile = get_advanced_continuation_profile(default_advanced_continuation_profile)
    data_lake = DataLake(LAKE_DIR)
    project_root = Path(__file__).parent.parent
    pipeline = AdvancedContinuationPipeline(data_lake, project_root=project_root, profile=profile)

    logger.info("Running run_advanced_continuation_status.py...")
    pipeline.build_advanced_continuation_status()
    logger.info("Done.")

if __name__ == "__main__":
    main()
