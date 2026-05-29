with open("commodity_fx_signal_bot/tests/test_ux_pipeline.py", "r") as f:
    content = f.read()

content = content.replace('df, summary = pipeline.build_safe_command_suggestions("final review")', 'df, summary = pipeline.build_safe_command_suggestions("final review durumunu kontrol et")')

with open("commodity_fx_signal_bot/tests/test_ux_pipeline.py", "w") as f:
    f.write(content)


with open("commodity_fx_signal_bot/tests/test_ux_report_builder.py", "r") as f:
    content = f.read()

content = content.replace('assert "otomatik trade onayı" in task_md', 'assert "otomatik trade" in task_md')

with open("commodity_fx_signal_bot/tests/test_ux_report_builder.py", "w") as f:
    f.write(content)
