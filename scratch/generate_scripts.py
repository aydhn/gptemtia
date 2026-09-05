import os
from pathlib import Path

SCRIPTS_DIR = Path("C:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia/scripts")

def w(name, content):
    with open(SCRIPTS_DIR / name, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

w("run_functional_gap_closure_profile_registry.py", """
import sys
def main():
    print("Running functional gap closure profile registry...")
if __name__ == "__main__":
    main()
""")

w("run_advanced_readiness_reconciliation.py", """
import sys
def main():
    print("Running advanced readiness reconciliation...")
if __name__ == "__main__":
    main()
""")

w("run_mvp_to_v2_closure_matrix.py", """
import sys
def main():
    print("Running MVP to v2 closure matrix...")
if __name__ == "__main__":
    main()
""")

w("run_phase_101_104_foundation_audit.py", """
import sys
def main():
    print("Running phase 101-104 foundation audit...")
if __name__ == "__main__":
    main()
""")

w("run_phase_106_data_foundation_handoff.py", """
import sys
def main():
    print("Running phase 106 data foundation handoff...")
if __name__ == "__main__":
    main()
""")

w("run_functional_gap_quality_report.py", """
import sys
def main():
    print("Running functional gap quality report...")
if __name__ == "__main__":
    main()
""")

w("run_functional_gap_status.py", """
import sys
def main():
    print("Running functional gap status...")
if __name__ == "__main__":
    main()
""")

print("Generated scripts")
