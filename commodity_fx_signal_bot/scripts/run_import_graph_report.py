import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    logging.info("Running import graph report")
    print("Executed import graph report")
    return 0

if __name__ == "__main__":
    sys.exit(main())
