import sys
from advanced_runtime.runtime_pipeline import AdvancedRuntimePipeline
from advanced_runtime.runtime_report_builder import build_runtime_contracts_markdown_report

def main():
    print("Running runtime contracts script...")
    p = AdvancedRuntimePipeline(None, None, None)
    d, sum_d = p.build_runtime_contracts(save=False)
    print(build_runtime_contracts_markdown_report(sum_d, d.get("exec")))
    print("Success")

if __name__ == "__main__":
    main()
