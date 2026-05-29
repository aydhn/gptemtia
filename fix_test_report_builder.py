with open("commodity_fx_signal_bot/tests/test_ux_report_builder.py", "r") as f:
    content = f.read()

content = content.replace('assert "offline analyst UX" in alias_md', 'assert "offline analyst UX/productivity" in alias_md')

with open("commodity_fx_signal_bot/tests/test_ux_report_builder.py", "w") as f:
    f.write(content)
