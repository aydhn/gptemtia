import pandas as pd

def build_common_issue_catalog() -> pd.DataFrame:
    data = [
        {"issue": "ModuleNotFoundError", "cause": "Missing package", "fix": "pip install"},
        {"issue": "Settings yüklenmiyor", "cause": "Invalid config", "fix": "Check config files"},
        {"issue": ".env okunmuyor", "cause": "Missing .env", "fix": "Create .env"},
        {"issue": "DataLake path eksik", "cause": "Missing dir", "fix": "Create dir"},
        {"issue": "yfinance/data provider veri vermiyor", "cause": "Network/API limits", "fix": "Retry/Check network"},
        {"issue": "feature dosyası yok", "cause": "Missing feature generation", "fix": "Run feature gen"},
        {"issue": "level candidate yok", "cause": "Missing candidate logic", "fix": "Run candidate logic"},
        {"issue": "backtest no trades", "cause": "No signals", "fix": "Check strategy"},
        {"issue": "ML dataset insufficient rows", "cause": "Not enough data", "fix": "Get more data"},
        {"issue": "model artifact missing", "cause": "Model not trained", "fix": "Train model"},
        {"issue": "Telegram not configured", "cause": "Missing token/chat_id", "fix": "Add to .env"},
        {"issue": "security audit secret warning", "cause": "Secret in code", "fix": "Remove secret"},
        {"issue": "orchestration dependency missing", "cause": "Missing script", "fix": "Create script"},
        {"issue": "pytest import error", "cause": "Missing package/PYTHONPATH", "fix": "Set PYTHONPATH"}
    ]
    return pd.DataFrame(data)

def find_troubleshooting_steps(issue_keyword: str) -> list[str]:
    df = build_common_issue_catalog()
    matches = df[df['issue'].str.contains(issue_keyword, case=False)]
    if matches.empty:
        return []
    return matches['fix'].tolist()

def build_troubleshooting_markdown() -> str:
    df = build_common_issue_catalog()
    return df.to_markdown(index=False)

def build_troubleshooting_report() -> tuple[pd.DataFrame, dict]:
    df = build_common_issue_catalog()
    return df, {"total_issues": len(df)}
