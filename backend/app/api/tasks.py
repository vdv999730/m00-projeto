from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.task import Task
from app.services.task_service import list_tasks, create_task, update_task, delete_task

router = APIRouter()

@router.get("/", response_model=List[Task])
async def get_tasks():
    return list_tasks()

@router.post("/", response_model=Task, status_code=201)
async def post_task(task: Task):
    return create_task(task)

@router.put("/{task_id}", response_model=Task)
async def put_task(task_id: int, task: Task):
    try:
        return update_task(task_id, task)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}", status_code=204)
async def del_task(task_id: int):
    try:
        delete_task(task_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")
