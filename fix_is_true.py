import re

file_path = 'commodity_fx_signal_bot/scripts/run_momentum_status.py'
with open(file_path, 'r') as f:
    content = f.read()

content = content.replace("df[\"Has Technical\"] is True", "df[\"Has Technical\"] == True")
content = content.replace("df[\"Has Momentum\"] is False", "df[\"Has Momentum\"] == False")
content = content.replace("df[\"Has Processed\"] is True", "df[\"Has Processed\"] == True")

# Since flake8 complains about == True for pandas dataframes (it thinks it's standard Python logic),
# we must use noqa or standard df column logic in pandas without the `== True`.

# Better yet, for pandas boolean masking:
# df[(df["Has Technical"]) & (~df["Has Momentum"])]

content = content.replace(
    'df[(df["Has Technical"] == True) & (df["Has Momentum"] == False)]',
    'df[(df["Has Technical"]) & (~df["Has Momentum"])]'
)
content = content.replace(
    'df[(df["Has Processed"] == True) & (df["Has Momentum"] == False)]',
    'df[(df["Has Processed"]) & (~df["Has Momentum"])]'
)

with open(file_path, 'w') as f:
    f.write(content)
