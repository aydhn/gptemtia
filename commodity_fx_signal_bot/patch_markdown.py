import os

with open("local_training/safe_usage_training.py", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace("rules_df.to_markdown()", "rules_df.to_string()")
with open("local_training/safe_usage_training.py", "w", encoding="utf-8") as f:
    f.write(content)

with open("local_training/non_use_policy_training.py", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace("df.to_markdown()", "df.to_string()")
with open("local_training/non_use_policy_training.py", "w", encoding="utf-8") as f:
    f.write(content)
