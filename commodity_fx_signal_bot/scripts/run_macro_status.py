import logging
from config.settings import settings
from ml.feature_store import FeatureStore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    fs = FeatureStore(settings)
    logger.info("Checking macro status...")

    try:
        macro_df = fs.load_macro_features()
        if not macro_df.empty:
            logger.info(
                f"Macro Features available: {len(macro_df)} rows. Latest: {macro_df.index.max()}"
            )
        else:
            logger.warning("Macro features not found or empty.")

        bench_df = fs.load_benchmark_features()
        if not bench_df.empty:
            logger.info(
                f"Benchmarks available: {len(bench_df)} rows. Latest: {bench_df.index.max()}"
            )
        else:
            logger.warning("Benchmarks not found or empty.")

    except Exception as e:
        logger.error(f"Error checking status: {e}")


if __name__ == "__main__":
    main()
