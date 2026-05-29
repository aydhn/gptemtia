with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'r') as f:
    lines = f.readlines()

import ast
while True:
    try:
        ast.parse(''.join(lines))
        break
    except IndentationError as e:
        print(f"Fixing indentation at line {e.lineno}")
        line = lines[e.lineno - 1]
        lines[e.lineno - 1] = "    " + line.lstrip()

with open('commodity_fx_signal_bot/data/storage/data_lake.py', 'w') as f:
    f.writelines(lines)
