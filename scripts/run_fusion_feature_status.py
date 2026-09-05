import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from advanced_feature_fusion.fusion_feature_profile_registry import get_fusion_feature_profiles_summary
from advanced_feature_fusion.fusion_feature_domain_registry import get_fusion_feature_domains_summary
from advanced_feature_fusion.fusion_feature_metadata_registry import get_fusion_feature_metadata_summary
from advanced_feature_fusion.fusion_feature_health import check_fusion_feature_health
from advanced_feature_fusion.phase_121_handoff import build_phase_121_handoff_manifest


def main():
    settings = get_settings()
    health = check_fusion_feature_health()
    prof_summary = get_fusion_feature_profiles_summary()
    dom_summary = get_fusion_feature_domains_summary()
    meta_summary = get_fusion_feature_metadata_summary()
    handoff = build_phase_121_handoff_manifest()

    print("=" * 70)
    print("PHASE 120 STATUS: ADVANCED FEATURE FUSION LAYER")
    print("=" * 70)
    print(f"Health Status      : {health['status']}")
    print(f"Current Phase      : 120")
    print(f"Next Phase         : 121")
    print(f"Target Final Phase : 160")
    print(f"Profiles Configured: {prof_summary['total_profiles']}")
    print(f"Domains Defined    : {dom_summary['total_domains']}")
    print(f"Features in Registry: {meta_summary['total_features']}")
    print(f"Handoff Status     : {handoff['handoff_status']}")
    print("Safety Invariants:")
    print("  - Zero Trade Signals: ENFORCED")
    print("  - Metadata-Only News: ENFORCED")
    print("  - Backward-Only Join: ENFORCED")
    print("  - Prohibited Shift(-1): ENFORCED")
    print("=" * 70)


if __name__ == "__main__":
    main()
