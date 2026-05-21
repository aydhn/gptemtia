import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.logger import get_logger
from config.paths import ensure_project_directories

logger = get_logger(__name__)

def main():
    logger.info("Running portfolio regime status check...")
    ensure_project_directories()
    logger.info("Status check completed.")

if __name__ == "__main__":
    main()
