import logging
from config.settings import settings
from data.storage.data_lake import DataLake
from macro.macro_pipeline import MacroPipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    lake = DataLake(settings)
    pipeline = MacroPipeline(data_lake=lake, settings=settings)

    logger.info("Building benchmarks...")
    df, summary = pipeline.build_benchmarks(save=False)

    if not df.empty:
        print("\n--- BENCHMARKS (Last 10) ---")
        print(df.tail(10).to_string())
    else:
        logger.warning("No benchmarks returned.")


if __name__ == "__main__":
    main()
