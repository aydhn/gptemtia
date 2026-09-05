import sys
from advanced_runtime.runtime_pipeline import AdvancedRuntimePipeline
from advanced_runtime.runtime_report_builder import build_runtime_profile_registry_markdown_report

def main():
    print("Running advanced runtime profile registry script...")
    p = AdvancedRuntimePipeline(None, None, None)
    df, sum_d = p.build_runtime_profile_registry(save=False)
    p.build_runtime_capabilities(save=False)
    print(build_runtime_profile_registry_markdown_report(sum_d, df))
    print("Success")

if __name__ == "__main__":
    main()
