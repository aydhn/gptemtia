import os

with open("tests/test_training_pipeline.py", "r") as f:
    content = f.read()

content = content.replace("SymbolSpec(\"SYN_TEST\", \"synthetic\", \"synthetic\")", "SymbolSpec(\"SYN_TEST\", \"synthetic\", \"synthetic\", \"USD\", \"yahoo\")")
content = content.replace("SymbolSpec(\"GC=F\", \"metals\", \"yahoo\")", "SymbolSpec(\"GC=F\", \"metals\", \"gold\", \"USD\", \"yahoo\")")

with open("tests/test_training_pipeline.py", "w") as f:
    f.write(content)

with open("scripts/run_ml_training_preview.py", "r") as f:
    content = f.read()
content = content.replace("get_symbol_by_name", "get_symbol_spec")
content = content.replace("get_symbol_by_name(args.symbol)", "get_symbol_spec(args.symbol)")
with open("scripts/run_ml_training_preview.py", "w") as f:
    f.write(content)

with open("scripts/run_ml_model_evaluation_preview.py", "r") as f:
    content = f.read()
content = content.replace("get_symbol_by_name", "get_symbol_spec")
content = content.replace("get_symbol_by_name(args.symbol)", "get_symbol_spec(args.symbol)")
with open("scripts/run_ml_model_evaluation_preview.py", "w") as f:
    f.write(content)

with open("scripts/run_ml_training_batch.py", "r") as f:
    content = f.read()
content = content.replace("get_symbol_by_name", "get_symbol_spec")
content = content.replace("get_universe", "get_enabled_symbols")
with open("scripts/run_ml_training_batch.py", "w") as f:
    f.write(content)
