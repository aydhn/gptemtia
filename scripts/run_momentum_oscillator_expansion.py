import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.momentum_indicators import build_momentum_indicator_expansion_registry
from advanced_technical_indicators.oscillator_indicators import build_oscillator_indicator_registry


def main():
    profile = get_default_technical_indicator_profile()
    mom_df, mom_sum = build_momentum_indicator_expansion_registry(profile)
    osc_df, osc_sum = build_oscillator_indicator_registry(profile)

    print("=" * 70)
    print("PHASE 117: MOMENTUM & OSCILLATOR INDICATORS EXPANSION")
    print("=" * 70)
    print(f"Momentum Indicators : {len(mom_df)}")
    print(f"Oscillator Inds     : {len(osc_df)}")
    print(f"Non-Signal Policy   : {mom_sum['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
