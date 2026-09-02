import os

def patch_file(path, search, replace):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if search in content:
        content = content.replace(search, replace)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

with open("config/paths.py", "r", encoding="utf-8") as f:
    if "local_briefing" not in f.read():
        patch_file("config/paths.py",
            "class ProjectPaths:",
            """class ProjectPaths:
    @property
    def local_briefing_dir(self): return self.data_lake_dir / "local_briefing"
    @property
    def local_briefing_reports_dir(self): return self.reports_dir / "output" / "local_briefing"
    @property
    def local_briefing_docs_dir(self): return self.docs_dir / "generated" / "local_briefing"
""")

with open(".env.example", "r", encoding="utf-8") as f:
    if "LOCAL_BRIEFING_ENABLED" not in f.read():
        with open(".env.example", "a", encoding="utf-8") as out:
            out.write("""
LOCAL_BRIEFING_ENABLED=true
DEFAULT_LOCAL_BRIEFING_PROFILE=balanced_local_briefing
LOCAL_BRIEFING_DEFAULT_LANGUAGE=tr
LOCAL_BRIEFING_DRY_RUN_DEFAULT=true
LOCAL_BRIEFING_ALLOW_INVESTMENT_ADVICE=false
LOCAL_BRIEFING_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_BRIEFING_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_BRIEFING_ALLOW_PRODUCTION_RELEASE_CLAIM=false
LOCAL_BRIEFING_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_BRIEFING_ALLOW_OFFICIAL_BOARD_DECISION_CLAIM=false
LOCAL_BRIEFING_ALLOW_CLOUD_UPLOAD=false
LOCAL_BRIEFING_ALLOW_EXTERNAL_SERVICE=false
LOCAL_BRIEFING_ALLOW_EXTERNAL_LLM=false
LOCAL_BRIEFING_ALLOW_FILE_MODIFICATION=false
LOCAL_BRIEFING_ALLOW_FILE_DELETION=false
LOCAL_BRIEFING_ALLOW_FILE_MOVE=false
LOCAL_BRIEFING_ALLOW_OVERWRITE=false
LOCAL_BRIEFING_SCAN_DOCS=true
LOCAL_BRIEFING_SCAN_REPORTS=true
LOCAL_BRIEFING_SCAN_DATA_LAKE=true
LOCAL_BRIEFING_SCAN_CROSS_LAYER_OUTPUTS=true
LOCAL_BRIEFING_SCAN_TRAINING_OUTPUTS=true
LOCAL_BRIEFING_MAX_SECTIONS=5000
LOCAL_BRIEFING_MAX_SLIDE_ITEMS=200
LOCAL_BRIEFING_MIN_QUALITY_SCORE=0.40
LOCAL_BRIEFING_SAVE_REPORTS=true
""")
