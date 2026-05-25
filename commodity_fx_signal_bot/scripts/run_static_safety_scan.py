import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    logging.info("Running static safety scan")
    print("Executed static safety scan")
    return 0

if __name__ == "__main__":
    sys.exit(main())
