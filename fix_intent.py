with open("commodity_fx_signal_bot/analyst_ux/intent_classifier.py", "r") as f:
    content = f.read()

# Fix order of matching in intent classifier, "regression" / "scenario" keywords should take precedence
new_classifier = """
    if any(k in q for k in ["regression", "snapshot", "golden output"]):
        intent_label = "scenario_regression_intent"
        confidence = 0.9
        matched.append("regression")
        related.append("scenario_regression")
    elif any(k in q for k in ["demo", "senaryo", "örnek akış"]):
        intent_label = "scenario_demo_intent"
        confidence = 0.8
        matched.append("demo")
        related.append("scenarios")
    elif any(k in q for k in ["durum", "status", "kontrol"]):
        intent_label = "status_check_intent"
        confidence = 0.9
        matched.append("status")
        related.append("status")
    elif any(k in q for k in ["rapor", "üret", "çalıştırılacak komut"]):
"""
content = content.replace("""    if any(k in q for k in ["durum", "status", "kontrol"]):
        intent_label = "status_check_intent"
        confidence = 0.9
        matched.append("status")
        related.append("status")
    elif any(k in q for k in ["rapor", "üret", "çalıştırılacak komut"]):""", new_classifier)

content = content.replace("""    elif any(k in q for k in ["demo", "senaryo", "örnek akış"]):
        intent_label = "scenario_demo_intent"
        confidence = 0.8
        matched.append("demo")
        related.append("scenarios")
    elif any(k in q for k in ["regression", "snapshot", "golden output"]):
        intent_label = "scenario_regression_intent"
        confidence = 0.9
        matched.append("regression")
        related.append("scenario_regression")
    elif any(k in q for k in ["final review", "audit", "acceptance"]):""", """    elif any(k in q for k in ["final review", "audit", "acceptance"]):""")

with open("commodity_fx_signal_bot/analyst_ux/intent_classifier.py", "w") as f:
    f.write(content)
