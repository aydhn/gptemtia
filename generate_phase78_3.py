import os
from pathlib import Path

BASE_DIR = Path("commodity_fx_signal_bot")

def write_file(path_str, content):
    p = BASE_DIR / path_str
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {p}")

write_file("local_delivery/delivery_docs_index.py", '''
import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_delivery_docs_index(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"doc_path": "README.md"}])
    return df, summarize_delivery_docs_index(df)

def summarize_delivery_docs_index(doc_df: pd.DataFrame) -> dict:
    return {"total_docs": len(doc_df)}
''')

write_file("local_delivery/delivery_reports_index.py", '''
import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_delivery_reports_index(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"report_path": "reports/dummy_report.csv"}])
    return df, summarize_delivery_reports_index(df)

def summarize_delivery_reports_index(report_df: pd.DataFrame) -> dict:
    return {"total_reports": len(report_df)}
''')

write_file("local_delivery/delivery_datalake_index.py", '''
import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_delivery_datalake_index(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"datalake_path": "data/lake/dummy.csv"}])
    return df, summarize_delivery_datalake_index(df)

def summarize_delivery_datalake_index(dl_df: pd.DataFrame) -> dict:
    return {"total_datalake_items": len(dl_df)}
''')

write_file("local_delivery/delivery_scripts_tests_index.py", '''
import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def classify_delivery_script_test_safety(path: Path, project_root: Path) -> dict:
    return {"is_safe": True, "notes": "Local script"}

def build_delivery_scripts_tests_index(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"script_path": "scripts/run_dummy.py"}])
    return df, summarize_delivery_scripts_tests_index(df)

def summarize_delivery_scripts_tests_index(st_df: pd.DataFrame) -> dict:
    return {"total_scripts_tests": len(st_df)}
''')

write_file("local_delivery/delivery_generated_docs_index.py", '''
import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_delivery_generated_docs_index(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"generated_doc_path": "docs/generated/dummy.md"}])
    return df, summarize_delivery_generated_docs_index(df)

def summarize_delivery_generated_docs_index(gdoc_df: pd.DataFrame) -> dict:
    return {"total_generated_docs": len(gdoc_df)}
''')

write_file("local_delivery/delivery_safety_boundary_index.py", '''
import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_delivery_safety_boundary_index(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"safety_doc_path": "SAFE_USAGE_GUIDE.md"}])
    return df, summarize_delivery_safety_boundary_index(df)

def summarize_delivery_safety_boundary_index(boundary_df: pd.DataFrame) -> dict:
    return {"total_safety_docs": len(boundary_df)}
''')

write_file("local_delivery/delivery_no_go_safe_go.py", '''
import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_delivery_no_go_conditions(profile: LocalDeliveryProfile) -> pd.DataFrame:
    conditions = [
        "raw secret included", ".env included", "live/broker/deploy claim",
        "investment advice wording", "official handoff claim", "compliance certification claim",
        "production handoff claim", "destructive command safe-listed", "package publish/cloud upload claim"
    ]
    return pd.DataFrame([{"condition": c, "type": "no-go"} for c in conditions])

def build_delivery_safe_go_conditions(profile: LocalDeliveryProfile) -> pd.DataFrame:
    conditions = [
        "local-only delivery documented", "no-use boundary documented",
        "final delivery manifest present", "handoff index present", "reviewer guide present",
        "transfer checklist present", "acceptance evidence available", "manual review register present"
    ]
    return pd.DataFrame([{"condition": c, "type": "safe-go"} for c in conditions])

def build_delivery_no_go_safe_go_summary(project_root: Path, profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    no_go = build_delivery_no_go_conditions(profile)
    safe_go = build_delivery_safe_go_conditions(profile)
    df = pd.concat([no_go, safe_go], ignore_index=True)
    return df, summarize_delivery_no_go_safe_go(df)

def summarize_delivery_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"total_conditions": len(summary_df)}
''')

write_file("local_delivery/delivery_faq.py", '''
import pandas as pd
from local_delivery.delivery_config import LocalDeliveryProfile

def build_default_delivery_faq(profile: LocalDeliveryProfile) -> pd.DataFrame:
    faqs = [
        {"q": "Bu gerçek teslim mi?", "a": "Hayır, bu bir provadır."},
        {"q": "Paket zip olarak üretildi mi?", "a": "Hayır, üretilmedi."},
        {"q": "Cloud'a yüklendi mi?", "a": "Hayır, yüklenmedi."},
        {"q": "Canlı trade yapılabilir mi?", "a": "Hayır, yapılamaz."},
        {"q": "Broker bağlantısı var mı?", "a": "Hayır, yoktur."},
        {"q": "Raporlar yatırım tavsiyesi mi?", "a": "Hayır, değildir."}
    ]
    return pd.DataFrame(faqs)

def build_delivery_recipient_faq(profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_delivery_faq(profile)
    return df, summarize_delivery_faq(df)

def summarize_delivery_faq(faq_df: pd.DataFrame) -> dict:
    return {"total_faqs": len(faq_df)}
''')

write_file("local_delivery/reading_order.py", '''
import pandas as pd
from local_delivery.delivery_config import LocalDeliveryProfile

def build_default_reading_order(profile: LocalDeliveryProfile) -> pd.DataFrame:
    order = [
        "README", "SAFE_USAGE_GUIDE", "PROJECT_COMPLETION_DOSSIER",
        "FINAL_SAFETY_BOUNDARY_BINDER", "INDEPENDENT_REVIEWER_PACK",
        "FINAL_VERIFICATION_EVIDENCE_BINDER", "RC_DRY_RUN_FREEZE_MANIFEST",
        "FINAL_OPERATOR_NAVIGATION_GUIDE", "reports/output status/quality reports",
        "DataLake indexes"
    ]
    return pd.DataFrame([{"step": i+1, "item": item} for i, item in enumerate(order)])

def build_delivery_package_reading_order(profile: LocalDeliveryProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_reading_order(profile)
    return df, summarize_delivery_reading_order(df)

def summarize_delivery_reading_order(order_df: pd.DataFrame) -> dict:
    return {"total_steps": len(order_df)}
''')
