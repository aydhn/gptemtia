import logging
from config.settings import settings
from data.storage.data_lake import DataLake
from macro.macro_pipeline import MacroPipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    lake = DataLake(settings)
    pipeline = MacroPipeline(data_lake=lake, settings=settings)

    logger.info("Starting macro batch build...")
    pipeline.update_macro_data(save=True)
    pipeline.build_macro_features(save=True)
    pipeline.build_benchmarks(save=True)
    logger.info("Batch build completed successfully.")


if __name__ == "__main__":
    main()
