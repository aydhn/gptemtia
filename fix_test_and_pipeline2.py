import os
import glob

def replace_in_file(filepath, old_str, new_str):
    with open(filepath, 'r') as f:
        content = f.read()

    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Fixed {filepath}")

replace_in_file("commodity_fx_signal_bot/ml/target_engineering.py",
                "trade = trade.iloc[0] # Take first trade on that bar",
                "trade = trade.iloc[0] if isinstance(trade, pd.DataFrame) else trade")
