import pandas as pd
from .briefing_config import LocalBriefingProfile
from .briefing_models import StakeholderAudience, build_audience_id

def build_default_audiences(profile: LocalBriefingProfile) -> list[StakeholderAudience]:
    return [
        StakeholderAudience(
            audience_id=build_audience_id("executive_audience"),
            audience_label="executive_audience",
            audience_name="Executive",
            information_needs=["amac", "kapsam", "sinirliliklar", "karar baglami", "sonraki adimlar"],
            forbidden_framings=["yatirim komitesi onayina hazir", "canli trading onayli", "garanti getiri"],
            warnings=["Bu grup investment committee anlamina gelmez."]
        ),
        StakeholderAudience(
            audience_id=build_audience_id("business_stakeholder_audience"),
            audience_label="business_stakeholder_audience",
            audience_name="Business Stakeholder",
            information_needs=["platform ne yapar/ne yapmaz", "rapor turleri", "guvenlik sinirlari"],
            forbidden_framings=["production release onayli", "broker bagli"],
            warnings=[]
        ),
        StakeholderAudience(
            audience_id=build_audience_id("analyst_audience"),
            audience_label="analyst_audience",
            audience_name="Analyst",
            information_needs=["rapor okuma", "evidence", "metadata", "non-use policy"],
            forbidden_framings=["kesin AL/SAT sinyali", "yatirim tavsiyesi"],
            warnings=[]
        ),
        StakeholderAudience(
            audience_id=build_audience_id("operator_audience"),
            audience_label="operator_audience",
            audience_name="Operator",
            information_needs=["safe commands", "status outputs", "manual review"],
            forbidden_framings=["otomatik canli operasyon baslatilabilir"],
            warnings=[]
        ),
        StakeholderAudience(
            audience_id=build_audience_id("developer_audience"),
            audience_label="developer_audience",
            audience_name="Developer",
            information_needs=["mimari", "moduller", "test ve script contract"],
            forbidden_framings=["deployment onayi verildi"],
            warnings=[]
        ),
        StakeholderAudience(
            audience_id=build_audience_id("compliance_reviewer_audience"),
            audience_label="compliance_reviewer_audience",
            audience_name="Compliance Reviewer",
            information_needs=["non-use", "secret exclusion", "safety boundaries"],
            forbidden_framings=["resmi compliance raporudur"],
            warnings=[]
        ),
        StakeholderAudience(
            audience_id=build_audience_id("nontechnical_audience"),
            audience_label="nontechnical_audience",
            audience_name="Nontechnical",
            information_needs=["sade anlatim", "terim sozlugu", "risk/sinirlilik"],
            forbidden_framings=["kesin kazanc"],
            warnings=[]
        )
    ]

def build_stakeholder_audience_registry(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    audiences = build_default_audiences(profile)
    df = pd.DataFrame([vars(a) for a in audiences])
    summary = summarize_audiences(df)
    return df, summary

def summarize_audiences(audience_df: pd.DataFrame) -> dict:
    if audience_df is None or audience_df.empty:
        return {"total_audiences": 0}
    return {
        "total_audiences": len(audience_df),
        "audiences": audience_df["audience_name"].tolist()
    }
