import sys
from advanced_runtime.runtime_pipeline import AdvancedRuntimePipeline
from advanced_runtime.runtime_report_builder import build_runtime_quality_markdown_report

def main():
    print("Running runtime quality report script...")
    p = AdvancedRuntimePipeline(None, None, None)
    rep, sum_d = p.build_runtime_quality_report(save=False)
    print(build_runtime_quality_markdown_report(sum_d, rep))
    print("Success")

if __name__ == "__main__":
    main()
