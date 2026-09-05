import os
from pathlib import Path

ROOT_DIR = Path("C:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia")

docs_to_append = {
    "docs/OPERATOR_MANUAL.md": """
## Phase 105 & 106 Operations
- Phase 105 ile local bot altyapısı tamamlandı.
- Operator olarak Phase 106 veri soyutlama (Data Provider Abstraction) hazırlığı raporlarını `scripts.run_phase_106_data_foundation_handoff` ile kontrol edebilirsiniz.
- Scraping eylemi yasaktır. Harici veri kaynakları için local cache veya user-provided dosyalar kullanın.
""",
    "docs/ANALYST_HANDBOOK.md": """
## Phase 105 & 106 Analysis
- Phase 105 raporları, model analizlerinizde kullanılacak veri altyapısının Phase 106'da nasıl soyutlanacağını özetler.
- Phase 106 ile veri kaynağı bağımsız (provider-agnostic) çalışacaksınız.
- Hiçbir analiz kesin AL/SAT sinyali veya yatırım tavsiyesi olarak kullanılamaz.
""",
    "docs/CODEX_AGENT_GUIDE.md": """
## Phase 105 & 106 Agent Constraints
- Phase 105 raporlamalarında `scraping`, `deployment`, `broker` veya `live_trading` terimlerini pozitif yetenek olarak göstermeyin.
- Phase 106 için agent'a "data provider" görevleri verildiğinde, bunu *sadece* local stub veya resmi API adapter kullanarak çözün, scraping eylemine girişmeyin.
- Yatırım tavsiyesi veremeyeceğinizi daima disclaimer olarak koruyun.
"""
}

for rel_path, content in docs_to_append.items():
    filepath = ROOT_DIR / rel_path
    if filepath.exists():
        with open(filepath, "a", encoding="utf-8") as f:
            f.write("\n" + content + "\n")
    else:
        # Create it if it doesn't exist
        os.makedirs(filepath.parent, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content + "\n")

print("Appended remaining documentation files")
