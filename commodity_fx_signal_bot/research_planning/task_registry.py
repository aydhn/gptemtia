import pandas as pd
from pathlib import Path
from research_planning.planning_models import ResearchTask, research_task_to_dict

class ResearchTaskRegistry:
    def __init__(self, registry_dir: Path):
        self.registry_dir = registry_dir
        self.registry_dir.mkdir(parents=True, exist_ok=True)
        self.tasks: dict[str, ResearchTask] = {}

    def add_task(self, task: ResearchTask) -> Path:
        self.tasks[task.task_id] = task
        # In a real system, we might append to a JSONL here
        return self.registry_dir / f"{task.task_id}.json"

    def load_tasks(self) -> pd.DataFrame:
        if not self.tasks:
            return pd.DataFrame()
        return tasks_to_dataframe(list(self.tasks.values()))

    def get_task(self, task_id: str) -> dict | None:
        if task_id in self.tasks:
            return research_task_to_dict(self.tasks[task_id])
        return None

    def update_task_status(self, task_id: str, status: str, notes: str | None = None) -> dict:
        if task_id in self.tasks:
            self.tasks[task_id].status = status
            if notes:
                self.tasks[task_id].warnings.append(notes)
            return research_task_to_dict(self.tasks[task_id])
        return {}

    def list_by_priority(self, priority_label: str) -> pd.DataFrame:
        df = self.load_tasks()
        if not df.empty and "priority_label" in df.columns:
            return df[df["priority_label"] == priority_label]
        return pd.DataFrame()

    def list_by_type(self, task_type: str) -> pd.DataFrame:
        df = self.load_tasks()
        if not df.empty and "task_type" in df.columns:
            return df[df["task_type"] == task_type]
        return pd.DataFrame()

    def summarize(self) -> dict:
        return {
            "total_tasks": len(self.tasks)
        }

def deduplicate_tasks(tasks: list[ResearchTask]) -> list[ResearchTask]:
    seen = {}
    for task in tasks:
        if task.task_id not in seen:
            seen[task.task_id] = task
        else:
            seen[task.task_id].warnings.append("Duplicate merged")
    return list(seen.values())

def tasks_to_dataframe(tasks: list[ResearchTask]) -> pd.DataFrame:
    if not tasks:
        return pd.DataFrame()
    return pd.DataFrame([research_task_to_dict(t) for t in tasks])
