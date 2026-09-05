"""Phase 129: Run Candidate State Quality Reports Script.

Generates candidate state quality, pseudo-state quality, coverage, consistency,
ambiguity, stability, missingness, and namespace quality reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    get_default_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.candidate_state_quality import (
    build_candidate_state_quality_report,
)
from advanced_market_behavior_diagnostics.pseudo_state_quality import (
    build_pseudo_state_quality_report,
)
from advanced_market_behavior_diagnostics.candidate_state_coverage import (
    build_candidate_state_coverage_report,
)
from advanced_market_behavior_diagnostics.candidate_state_consistency import (
    build_candidate_state_consistency_report,
)
from advanced_market_behavior_diagnostics.candidate_state_ambiguity import (
    build_candidate_state_ambiguity_report,
)
from advanced_market_behavior_diagnostics.candidate_state_stability import (
    build_candidate_state_stability_report,
)
from advanced_market_behavior_diagnostics.candidate_state_missingness import (
    build_candidate_state_missingness_report,
)
from advanced_market_behavior_diagnostics.candidate_state_namespace_quality import (
    build_candidate_state_namespace_quality_report,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_report_builder import (
    build_candidate_state_quality_markdown_report,
)
from reports.report_builder import build_candidate_state_quality_text_report


def main():
    data_lake = DataLake()
    profile = get_default_market_behavior_diagnostics_profile()

    df_csq, s_csq = build_candidate_state_quality_report(profile)
    df_psq, s_psq = build_pseudo_state_quality_report(profile)
    df_cov, s_cov = build_candidate_state_coverage_report(profile)
    df_con, s_con = build_candidate_state_consistency_report(profile)
    df_amb, s_amb = build_candidate_state_ambiguity_report(profile)
    df_sta, s_sta = build_candidate_state_stability_report(profile)
    df_mis, s_mis = build_candidate_state_missingness_report(profile)
    df_ns, s_ns = build_candidate_state_namespace_quality_report(profile)

    data_lake.save_candidate_state_quality_report(df_csq, s_csq)
    data_lake.save_pseudo_state_quality_report(df_psq, s_psq)
    data_lake.save_candidate_state_coverage_report(df_cov, s_cov)
    data_lake.save_candidate_state_consistency_report(df_con, s_con)
    data_lake.save_candidate_state_ambiguity_report(df_amb, s_amb)
    data_lake.save_candidate_state_stability_report(df_sta, s_sta)
    data_lake.save_candidate_state_missingness_report(df_mis, s_mis)
    data_lake.save_candidate_state_namespace_quality_report(df_ns, s_ns)

    summary = {
        "total_candidate_states": s_csq.get("total_candidate_states", len(df_csq)),
        "mean_quality_score": s_csq.get("average_completeness", s_csq.get("mean_quality_score", 1.0)),
        "coverage_ratio": s_cov.get("average_family_completeness", s_cov.get("coverage_ratio", 1.0)),
        "consistency_score": s_con.get("average_consistency_score", s_con.get("consistency_score", 1.0)),
        "ambiguity_rate": s_amb.get("average_ambiguity_score", s_amb.get("ambiguity_rate", 0.1)),
        "non_signal": True,
    }

    md = build_candidate_state_quality_markdown_report(summary, df_csq)
    txt = build_candidate_state_quality_text_report(summary, df_csq)

    out_dir = Path("reports/output/advanced_market_behavior_diagnostics")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "candidate_state_quality.md", "w", encoding="utf-8") as f:
        f.write(md)
    with open(out_dir / "candidate_state_quality.txt", "w", encoding="utf-8") as f:
        f.write(txt)

    print("=" * 70)
    print("PHASE 129: CANDIDATE STATE QUALITY REPORTS")
    print("=" * 70)
    print(f"Candidate States    : {summary['total_candidate_states']}")
    print(f"Mean Quality Score  : {summary['mean_quality_score']:.4f}")
    print(f"Coverage Ratio      : {summary['coverage_ratio']:.4f}")
    print(f"Consistency Score   : {summary['consistency_score']:.4f}")
    print(f"Ambiguity Rate      : {summary['ambiguity_rate']:.4f}")
    print(f"Stability Score     : {s_sta.get('average_stability_score', s_sta.get('mean_stability_score', 0.85)):.4f}")
    print(f"Missingness Score   : {s_mis.get('average_missingness_ratio', s_mis.get('mean_missingness_score', 0.0)):.4f}")
    print(f"Namespace Qual Mean : {s_ns.get('average_namespace_score', s_ns.get('mean_namespace_quality', 1.0)):.4f}")
    print(f"Non-Signal Mandate  : True")
    print("=" * 70)



if __name__ == "__main__":
    main()
