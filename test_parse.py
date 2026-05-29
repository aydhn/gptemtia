import ast
try:
    with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'r') as f:
        ast.parse(f.read())
    print("Parsed OK")
except IndentationError as e:
    print(f"Indentation error line {e.lineno}")
