import sys
from advanced_runtime.runtime_pipeline import AdvancedRuntimePipeline
from advanced_runtime.runtime_report_builder import build_runtime_status_markdown_report

def main():
    print("Running runtime status script...")
    p = AdvancedRuntimePipeline(None, None, None)
    df, sum_d = p.build_runtime_status(save=False)
    print(build_runtime_status_markdown_report(sum_d, df))
    print("Success")

if __name__ == "__main__":
    main()
