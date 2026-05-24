import pandas as pd
from research_planning.planning_quality import build_planning_quality_report, FORBIDDEN_TRADE_TERMS

df = pd.DataFrame([{"text": "safe"}])
summary = {"key": "val"}

report = build_planning_quality_report(summary, None, df, None)
print(report)
print(FORBIDDEN_TRADE_TERMS)
