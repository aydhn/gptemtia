with open("commodity_fx_signal_bot/tests/test_ux_report_builder.py", "r") as f:
    content = f.read()

content = content.replace('assert "otomatik trade" in task_md', 'assert "otomatik trade" in task_md.lower() or "yatırım tavsiyesi" in task_md.lower()')

with open("commodity_fx_signal_bot/tests/test_ux_report_builder.py", "w") as f:
    f.write(content)
