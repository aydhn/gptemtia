import argparse
import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_governance_control")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()
    print("Running run_manual_approval_ledger...")

    # Create dummy outputs
    out_dir = ROOT / "reports" / "output" / "local_governance_control"
    (out_dir / "csv").mkdir(parents=True, exist_ok=True)
    (out_dir / "markdown").mkdir(parents=True, exist_ok=True)
    (out_dir / "txt").mkdir(parents=True, exist_ok=True)
    (out_dir / "json").mkdir(parents=True, exist_ok=True)

    pd.DataFrame([{'status': 'mock'}]).to_csv(out_dir / "csv" / "manual_approval_ledger.csv", index=False)
    pd.DataFrame([{'status': 'mock'}]).to_csv(out_dir / "csv" / "manual_approval_checklist_registry.csv", index=False)
    pd.DataFrame([{'status': 'mock'}]).to_csv(out_dir / "csv" / "manual_signoff_rehearsal_form_library.csv", index=False)
    pd.DataFrame([{'status': 'mock'}]).to_csv(out_dir / "csv" / "operator_supervision_checklist.csv", index=False)
    (out_dir / "markdown" / "manual_approval_ledger.md").write_text("# Mock manual_approval_ledger.md\nThis is a local offline rehearsal output.\n", encoding="utf-8")
    (out_dir / "txt" / "manual_approval_ledger.txt").write_text("Mock manual_approval_ledger.txt\nThis is a local offline rehearsal output.\n", encoding="utf-8")

if __name__ == "__main__":
    main()
