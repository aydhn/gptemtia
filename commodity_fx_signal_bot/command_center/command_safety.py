"""
Safety validations for the Command Center.
"""

from typing import Tuple, List, Dict
import pandas as pd
from command_center.command_models import SafeCommand

FORBIDDEN_COMMAND_TERMS = [
    "live",
    "broker",
    "order",
    "buy",
    "sell",
    "open_long",
    "open_short",
    "close_position",
    "position",
    "deploy",
    "production",
    "server",
    "daemon",
    "while true",
    "schedule live",
    "telegram live signal",
    "real trade",
    "exchange api key"
]

def detect_forbidden_command_terms(command: str) -> dict:
    found_terms = []
    # Simple check, ignoring context in a real-world scenario you'd want a more robust parser
    lower_command = command.lower()
    for term in FORBIDDEN_COMMAND_TERMS:
        if term in lower_command:
            # specifically check for things like "no live order"
            if f"no {term}" not in lower_command and f"not {term}" not in lower_command:
                found_terms.append(term)

    return {
        "forbidden_terms_found": len(found_terms) > 0,
        "found_terms": found_terms
    }

def classify_command_safety(command: str) -> str:
    terms = detect_forbidden_command_terms(command)
    if terms["forbidden_terms_found"]:
        # Naive classification based on the term
        if any(t in ["live", "real trade"] for t in terms["found_terms"]):
            return "blocked_live_command"
        elif any(t in ["broker", "order", "buy", "sell", "open_long", "open_short", "close_position", "position", "exchange api key"] for t in terms["found_terms"]):
            return "blocked_broker_command"
        elif any(t in ["deploy", "production"] for t in terms["found_terms"]):
            return "blocked_deploy_command"
        elif any(t in ["server", "daemon", "while true", "schedule live"] for t in terms["found_terms"]):
            return "blocked_daemon_command"
        return "unsafe_unknown_command"
    return "safe_offline_command"

def validate_safe_command(command: SafeCommand) -> dict:
    safety_label = classify_command_safety(command.command)
    if safety_label != "safe_offline_command":
        return {
            "valid": False,
            "warning": f"Command {command.command_name} is classified as {safety_label}"
        }
    if command.safety_label != "safe_offline_command":
        return {
            "valid": False,
            "warning": f"Command {command.command_name} has invalid safety label {command.safety_label}"
        }
    return {
        "valid": True,
        "warning": None
    }

def filter_safe_commands(commands: List[SafeCommand]) -> Tuple[List[SafeCommand], List[dict]]:
    safe = []
    blocked = []
    for cmd in commands:
        validation = validate_safe_command(cmd)
        if validation["valid"]:
            safe.append(cmd)
        else:
            blocked.append({
                "command_id": cmd.command_id,
                "command": cmd.command,
                "warning": validation["warning"]
            })
    return safe, blocked

def build_blocked_command_report(commands: List[str]) -> pd.DataFrame:
    data = []
    for cmd in commands:
        safety = classify_command_safety(cmd)
        data.append({
            "command": cmd,
            "safety_label": safety,
            "forbidden_terms": detect_forbidden_command_terms(cmd)["found_terms"]
        })
    return pd.DataFrame(data)
