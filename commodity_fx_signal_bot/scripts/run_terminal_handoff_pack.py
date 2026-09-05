import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_project_completion")
    args = parser.parse_args()
    print("Running terminal handoff pack")
    
if __name__ == "__main__":
    main()
