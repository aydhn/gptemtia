"""run_reproducibility_quality_report"""
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_pipeline import LocalReproducibilityGovernancePipeline
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_local_reproducibility_governance_profile, get_default_local_reproducibility_governance_profile

class DummyDataLake:
    pass

class DummySettings:
    pass

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_reproducibility")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    try:
        profile = get_local_reproducibility_governance_profile(args.profile)
    except Exception:
        profile = get_default_local_reproducibility_governance_profile()

    pipeline = LocalReproducibilityGovernancePipeline(
        data_lake=DummyDataLake(),
        settings=DummySettings(),
        project_root=Path(__file__).parent.parent,
        profile=profile
    )
    
    print(f"Running run_reproducibility_quality_report...")
    pipeline.build_reproducibility_quality_report(save=args.save)
    print("Done.")

if __name__ == "__main__":
    main()
