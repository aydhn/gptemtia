import os

with open("local_training/training_report_builder.py", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("domain_df.to_markdown()", "domain_df.to_markdown() if 'tabulate' in __import__('sys').modules or __import__('importlib.util').util.find_spec('tabulate') else domain_df.to_string()")
content = content.replace("curriculum_df.to_markdown()", "curriculum_df.to_markdown() if 'tabulate' in __import__('sys').modules or __import__('importlib.util').util.find_spec('tabulate') else curriculum_df.to_string()")
content = content.replace("walkthrough_df.to_markdown()", "walkthrough_df.to_markdown() if 'tabulate' in __import__('sys').modules or __import__('importlib.util').util.find_spec('tabulate') else walkthrough_df.to_string()")
content = content.replace("status_df.to_markdown()", "status_df.to_markdown() if 'tabulate' in __import__('sys').modules or __import__('importlib.util').util.find_spec('tabulate') else status_df.to_string()")

with open("local_training/training_report_builder.py", "w", encoding="utf-8") as f:
    f.write(content)

