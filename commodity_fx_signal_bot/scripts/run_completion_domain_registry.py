import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_project_completion")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()
    print(f"Running completion domain registry with profile {args.profile}")
    
if __name__ == "__main__":
    main()
