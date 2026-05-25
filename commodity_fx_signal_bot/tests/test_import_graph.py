import pandas as pd
from pathlib import Path
from quality_gates.import_graph import (
    parse_python_imports,
    build_import_graph,
    detect_circular_imports,
    validate_module_importability,
    summarize_import_graph
)

def test_parse_python_imports():
    res = parse_python_imports(Path("."))
    assert isinstance(res, dict)

def test_build_import_graph():
    nodes, edges, summary = build_import_graph(Path("."))
    assert isinstance(nodes, pd.DataFrame)
    assert isinstance(edges, pd.DataFrame)
    assert isinstance(summary, dict)

def test_detect_circular_imports():
    df = pd.DataFrame()
    circular, summary = detect_circular_imports(df)
    assert isinstance(circular, pd.DataFrame)
    assert isinstance(summary, dict)

def test_validate_module_importability():
    df, summary = validate_module_importability(Path("."))
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)

def test_summarize_import_graph():
    nodes = pd.DataFrame()
    edges = pd.DataFrame()
    summary = summarize_import_graph(nodes, edges)
    assert isinstance(summary, dict)
