import re

with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

maintenance_methods = """
    # --- MAINTENANCE REPORTING ---
    def build_storage_inventory_text_report(self, summary: dict, inventory_df: pd.DataFrame | None = None) -> str:
        rep = "*** DISCLAIMER ***\\n"
        rep += "Bu çıktı offline data retention/storage lifecycle maintenance raporudur. "
        rep += "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        rep += "otomatik trade onayı veya yatırım tavsiyesi değildir. Varsayılan mod dry-run’dır; "
        rep += "dosyalar otomatik silinmez veya taşınmaz.\\n"
        rep += "******************\\n\\n"
        rep += "STORAGE INVENTORY REPORT\\n"
        rep += "========================\\n\\n"
        rep += f"Total Files: {summary.get('total_files', 0)}\\n"
        rep += f"Total Size (Bytes): {summary.get('total_size_bytes', 0)}\\n"
        rep += f"Protected Files: {summary.get('protected_files', 0)}\\n"
        return rep

    def build_retention_policy_text_report(self, summary: dict, policies_df: pd.DataFrame | None = None) -> str:
        rep = "*** DISCLAIMER ***\\n"
        rep += "Bu çıktı offline data retention/storage lifecycle maintenance raporudur. "
        rep += "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        rep += "otomatik trade onayı veya yatırım tavsiyesi değildir. Varsayılan mod dry-run’dır; "
        rep += "dosyalar otomatik silinmez veya taşınmaz.\\n"
        rep += "******************\\n\\n"
        rep += "RETENTION POLICIES REPORT\\n"
        rep += "=========================\\n\\n"
        rep += f"Total Policies: {summary.get('total_policies', 0)}\\n"
        return rep

    def build_cleanup_dry_run_text_report(self, summary: dict, cleanup_df: pd.DataFrame | None = None) -> str:
        rep = "*** DISCLAIMER ***\\n"
        rep += "Bu çıktı offline data retention/storage lifecycle maintenance raporudur. "
        rep += "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        rep += "otomatik trade onayı veya yatırım tavsiyesi değildir. Varsayılan mod dry-run’dır; "
        rep += "dosyalar otomatik silinmez veya taşınmaz.\\n"
        rep += "******************\\n\\n"
        rep += "CLEANUP DRY-RUN REPORT\\n"
        rep += "======================\\n\\n"
        rep += f"Cleanup Candidates: {summary.get('candidate_count', 0)}\\n"
        rep += f"Reclaimable Storage (Bytes): {summary.get('reclaimable_bytes', 0)}\\n"
        return rep

    def build_archive_dry_run_text_report(self, summary: dict, archive_df: pd.DataFrame | None = None) -> str:
        rep = "*** DISCLAIMER ***\\n"
        rep += "Bu çıktı offline data retention/storage lifecycle maintenance raporudur. "
        rep += "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        rep += "otomatik trade onayı veya yatırım tavsiyesi değildir. Varsayılan mod dry-run’dır; "
        rep += "dosyalar otomatik silinmez veya taşınmaz.\\n"
        rep += "******************\\n\\n"
        rep += "ARCHIVE DRY-RUN REPORT\\n"
        rep += "======================\\n\\n"
        rep += f"Archive Candidates: {summary.get('candidate_count', 0)}\\n"
        rep += f"Total Archive Size (Bytes): {summary.get('total_size_bytes', 0)}\\n"
        return rep

    def build_storage_lifecycle_text_report(self, summary: dict, health_df: pd.DataFrame | None = None) -> str:
        rep = "*** DISCLAIMER ***\\n"
        rep += "Bu çıktı offline data retention/storage lifecycle maintenance raporudur. "
        rep += "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        rep += "otomatik trade onayı veya yatırım tavsiyesi değildir. Varsayılan mod dry-run’dır; "
        rep += "dosyalar otomatik silinmez veya taşınmaz.\\n"
        rep += "******************\\n\\n"
        rep += "STORAGE LIFECYCLE REPORT\\n"
        rep += "========================\\n\\n"
        if "health" in summary:
            rep += f"Storage Pressure Score: {summary['health'].get('score', 0.0)}\\n"
            rep += f"Health Label: {summary['health'].get('label', 'unknown')}\\n"
        else:
            rep += f"Storage Pressure Score: {summary.get('score', 0.0)}\\n"
            rep += f"Health Label: {summary.get('label', 'unknown')}\\n"
        return rep

    def build_maintenance_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        rep = "*** DISCLAIMER ***\\n"
        rep += "Bu çıktı offline data retention/storage lifecycle maintenance raporudur. "
        rep += "Canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, "
        rep += "otomatik trade onayı veya yatırım tavsiyesi değildir. Varsayılan mod dry-run’dır; "
        rep += "dosyalar otomatik silinmez veya taşınmaz.\\n"
        rep += "******************\\n\\n"
        rep += "MAINTENANCE STATUS REPORT\\n"
        rep += "=========================\\n\\n"
        rep += f"Status: {summary.get('status', 'OK')}\\n"
        return rep
"""

if "def build_storage_inventory_text_report" not in content:
    # Just append to the class at the end
    content = re.sub(r'(\s*)$', r'\n\n' + maintenance_methods, content)
    with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
        f.write(content)
    print("report_builder.py patched")
else:
    print("report_builder.py already patched")
