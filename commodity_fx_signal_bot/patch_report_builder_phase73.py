import os

with open("reports/report_builder.py", "r", encoding="utf-8") as f:
    content = f.read()

code = '''
def build_training_disclaimer() -> str:
    return "\\n\\n> UYARI: Bu çıktı offline/local knowledge-transfer ve onboarding education raporudur. Canlı trading eğitimi, yatırım danışmanlığı, production operator certification, canlı emir, broker talimatı, model deployment veya resmi eğitim sertifikası değildir.\\n"

def build_training_domain_registry_text_report(summary: dict, domain_df=None) -> str:
    r = "Training Domain Registry\\n"
    if domain_df is not None and not domain_df.empty: r += domain_df.to_string()
    r += build_training_disclaimer()
    return r

def build_onboarding_curriculum_text_report(summary: dict, curriculum_df=None) -> str:
    r = "Onboarding Curriculum\\n"
    if curriculum_df is not None and not curriculum_df.empty: r += curriculum_df.to_string()
    r += build_training_disclaimer()
    return r

def build_guided_walkthroughs_text_report(summary: dict, walkthrough_df=None) -> str:
    r = "Guided Walkthroughs\\n"
    if walkthrough_df is not None and not walkthrough_df.empty: r += walkthrough_df.to_string()
    r += build_training_disclaimer()
    return r

def build_training_packs_text_report(summary: dict, pack_text=None) -> str:
    r = "Training Packs\\n"
    if pack_text: r += pack_text
    r += build_training_disclaimer()
    return r

def build_handover_education_binder_text_report(summary: dict, binder_text=None) -> str:
    r = "Handover Binder\\n"
    if binder_text: r += binder_text
    r += build_training_disclaimer()
    return r

def build_training_quality_text_report(summary: dict, quality=None) -> str:
    r = "Training Quality\\n"
    if quality: r += str(quality)
    r += build_training_disclaimer()
    return r

def build_training_status_report(status_df, summary: dict) -> str:
    r = "Training Status\\n"
    if status_df is not None and not status_df.empty: r += status_df.to_string()
    r += build_training_disclaimer()
    return r
'''

content += "\n" + code

with open("reports/report_builder.py", "w", encoding="utf-8") as f:
    f.write(content)
