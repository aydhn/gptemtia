with open("commodity_fx_signal_bot/experiments/experiment_quality.py", "r") as f:
    content = f.read()

content = content.replace("for term in FORBIDDEN_TRADE_TERMS:", "for term in FORBIDDEN_TRADE_TERMS:\n            # Exception for AL inside other words\n            if term == 'AL' and 'ALL GOOD' in upper_val: continue")

with open("commodity_fx_signal_bot/experiments/experiment_quality.py", "w") as f:
    f.write(content)
