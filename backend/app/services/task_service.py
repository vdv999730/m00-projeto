from typing import List
from app.schemas.task import Task

# _fake_db armazena tasks em memória
_fake_db: List[Task] = []
_next_id = 1

def list_tasks() -> List[Task]:
    return _fake_db

def create_task(task: Task) -> Task:
    global _next_id
    task.id = _next_id
    _next_id += 1
    _fake_db.append(task)
    return task

def update_task(task_id: int, task_data: Task) -> Task:
    for idx, t in enumerate(_fake_db):
        if t.id == task_id:
            updated = task_data.copy(update={"id": task_id})
            _fake_db[idx] = updated
            return updated
    raise ValueError("Task not found")

def delete_task(task_id: int) -> None:
    global _fake_db
    _fake_db = [t for t in _fake_db if t.id != task_id]
