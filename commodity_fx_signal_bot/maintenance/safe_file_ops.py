"""Safe File Operations for offline maintenance."""
from pathlib import Path
import shutil
from typing import Dict

def validate_file_op_safety(path: Path, project_root: Path, allow_delete: bool = False, allow_move: bool = False) -> Dict:
    # Basic safety checks
    name = path.name
    if name in ["README.md", "ARCHITECTURE.md", "PHASE_LOG.md", ".env.example"]:
        return {"safe": False, "reason": "File is protected core documentation"}

    if path.suffix in [".py", ".yaml", ".toml"]:
        return {"safe": False, "reason": "File is protected source code or config"}

    if "tests" in path.parts:
        return {"safe": False, "reason": "File is within protected tests directory"}

    return {"safe": True, "reason": "Passed safety checks"}

def dry_run_delete_file(path: Path) -> Dict:
    return {"action": "delete", "path": str(path), "dry_run": True, "success": True}

def dry_run_move_to_archive(path: Path, archive_dir: Path) -> Dict:
    return {"action": "move_to_archive", "path": str(path), "target": str(archive_dir / path.name), "dry_run": True, "success": True}

def execute_delete_file(path: Path, project_root: Path, allow_delete: bool = False) -> Dict:
    if not allow_delete:
        return {"action": "delete", "path": str(path), "dry_run": False, "success": False, "reason": "allow_delete is False"}

    safety = validate_file_op_safety(path, project_root, allow_delete=True)
    if not safety["safe"]:
        return {"action": "delete", "path": str(path), "dry_run": False, "success": False, "reason": safety["reason"]}

    if path.exists() and path.is_file():
        path.unlink()
        return {"action": "delete", "path": str(path), "dry_run": False, "success": True}
    return {"action": "delete", "path": str(path), "dry_run": False, "success": False, "reason": "File not found"}

def execute_move_to_archive(path: Path, archive_dir: Path, project_root: Path, allow_move: bool = False) -> Dict:
    if not allow_move:
        return {"action": "move_to_archive", "path": str(path), "dry_run": False, "success": False, "reason": "allow_move is False"}

    safety = validate_file_op_safety(path, project_root, allow_move=True)
    if not safety["safe"]:
        return {"action": "move_to_archive", "path": str(path), "dry_run": False, "success": False, "reason": safety["reason"]}

    if path.exists() and path.is_file():
        archive_dir.mkdir(parents=True, exist_ok=True)
        target = archive_dir / path.name
        shutil.move(str(path), str(target))
        return {"action": "move_to_archive", "path": str(path), "target": str(target), "dry_run": False, "success": True}
    return {"action": "move_to_archive", "path": str(path), "dry_run": False, "success": False, "reason": "File not found"}
