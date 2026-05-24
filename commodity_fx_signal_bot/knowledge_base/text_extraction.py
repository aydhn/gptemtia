from pathlib import Path
from typing import Tuple, Dict
import pandas as pd
import json
import yaml
import re

def mask_sensitive_text(text: str) -> str:
    if not text:
        return text

    # Simple regex replacements to mask typical secrets
    patterns = [
        (r'(api_key\s*[:=]\s*)["\']?[a-zA-Z0-9_\-]+["\']?', r'\1[MASKED_API_KEY]'),
        (r'(secret\s*[:=]\s*)["\']?[a-zA-Z0-9_\-]+["\']?', r'\1[MASKED_SECRET]'),
        (r'(token\s*[:=]\s*)["\']?[a-zA-Z0-9_\-]+["\']?', r'\1[MASKED_TOKEN]'),
        (r'(password\s*[:=]\s*)["\']?[a-zA-Z0-9_\-]+["\']?', r'\1[MASKED_PASSWORD]'),
        (r'(private_key\s*[:=]\s*)["\']?[a-zA-Z0-9_\-]+["\']?', r'\1[MASKED_PRIVATE_KEY]'),
        (r'(telegram_bot_token\s*[:=]\s*)["\']?[a-zA-Z0-9_\-]+["\']?', r'\1[MASKED_BOT_TOKEN]'),
    ]

    masked = text
    for pattern, repl in patterns:
        masked = re.sub(pattern, repl, masked, flags=re.IGNORECASE)

    return masked

def estimate_token_count(text: str) -> int:
    if not text:
        return 0
    # Simple rough estimate: words + punctuation
    return len(re.findall(r'\w+|[^\w\s]', text))

def extract_text_from_markdown(path: Path) -> Tuple[str, Dict]:
    text = path.read_text(encoding='utf-8', errors='replace')
    masked = mask_sensitive_text(text)
    return masked, {"extracted_length": len(masked)}

def extract_text_from_txt(path: Path) -> Tuple[str, Dict]:
    text = path.read_text(encoding='utf-8', errors='replace')
    masked = mask_sensitive_text(text)
    return masked, {"extracted_length": len(masked)}

def extract_text_from_csv(path: Path, max_rows: int = 200) -> Tuple[str, Dict]:
    try:
        df = pd.read_csv(path)
        metadata = {
            "total_rows": len(df),
            "columns": list(df.columns)
        }

        truncated = False
        if len(df) > max_rows:
            df = df.head(max_rows)
            truncated = True

        text = df.to_csv(index=False)
        masked = mask_sensitive_text(text)

        if truncated:
            masked += f"\n\n[TRUNCATED: Showing first {max_rows} rows out of {metadata['total_rows']}]"

        return masked, metadata
    except Exception as e:
        return "", {"error": str(e)}

def extract_text_from_json(path: Path, max_chars: int = 100000) -> Tuple[str, Dict]:
    try:
        data = json.loads(path.read_text(encoding='utf-8', errors='replace'))
        text = json.dumps(data, indent=2)

        truncated = False
        if len(text) > max_chars:
            text = text[:max_chars]
            truncated = True

        masked = mask_sensitive_text(text)
        if truncated:
            masked += "\n\n[TRUNCATED JSON CONTENT]"

        return masked, {"truncated": truncated}
    except Exception as e:
        return "", {"error": str(e)}

def extract_text_from_yaml(path: Path, max_chars: int = 100000) -> Tuple[str, Dict]:
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            data = yaml.safe_load(f)
        text = yaml.dump(data, default_flow_style=False)

        truncated = False
        if len(text) > max_chars:
            text = text[:max_chars]
            truncated = True

        masked = mask_sensitive_text(text)
        if truncated:
            masked += "\n\n[TRUNCATED YAML CONTENT]"

        return masked, {"truncated": truncated}
    except Exception as e:
        return "", {"error": str(e)}

def extract_text_from_document(path: Path) -> Tuple[str, Dict]:
    ext = path.suffix.lower()

    if ext == ".md":
        return extract_text_from_markdown(path)
    elif ext == ".txt":
        return extract_text_from_txt(path)
    elif ext == ".csv":
        return extract_text_from_csv(path)
    elif ext == ".json":
        return extract_text_from_json(path)
    elif ext in {".yaml", ".yml"}:
        return extract_text_from_yaml(path)

    return "", {"error": f"Unsupported extension: {ext}"}
