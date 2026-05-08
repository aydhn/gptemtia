with open("reports/report_builder.py", "r") as f:
    content = f.read()

content = content.replace("return \"\n\".join(lines)", "return \"\\n\".join(lines)")

with open("reports/report_builder.py", "w") as f:
    f.write(content)
