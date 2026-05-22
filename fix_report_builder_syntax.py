with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

content = content.replace('return "\n".join(lines)', 'return "\\n".join(lines)')
# Let's fix the multiline return
content = content.replace('return "\n', 'return "\\n')

with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
    f.write(content)
