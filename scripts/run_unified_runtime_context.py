import sys
from advanced_runtime.runtime_pipeline import AdvancedRuntimePipeline
from advanced_runtime.runtime_report_builder import build_unified_runtime_context_markdown_report

def main():
    print("Running unified runtime context script...")
    p = AdvancedRuntimePipeline(None, None, None)
    txt, sum_d = p.build_unified_runtime_context(save=False)
    print(build_unified_runtime_context_markdown_report(sum_d, txt))
    print("Success")

if __name__ == "__main__":
    main()
