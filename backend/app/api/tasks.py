from fastapi import APIRouter, Depends, Body  # <- IMPORTANTE adicionar Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.models.audit import AuditLog
from app.schemas.tasks import TaskCreate, TaskUpdate, TaskResponse
from app.crud.tasks import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task,
)
from app.services.audit_log import log_event

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskResponse)
async def create_new_task(
    task: TaskCreate = Body(...), db: AsyncSession = Depends(get_db)
):
    task_created = await create_task(db, task)
    await log_event(
        db, user_id=None, action="TASK_CREATED", details=f"Task ID {task_created.id}"
    )
    return task_created


@router.get("/", response_model=list[TaskResponse])
async def read_tasks(db: AsyncSession = Depends(get_db)):
    tasks = await get_all_tasks(db)
    return tasks


@router.get("/{task_id}", response_model=TaskResponse)
async def read_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await get_task_by_id(db, task_id)
    return task


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task_endpoint(
    task_id: int,
    task_update: TaskUpdate = Body(...),
    db: AsyncSession = Depends(get_db),
):
    updated_task = await update_task(db, task_id, task_update)
    await log_event(
        db,
        user_id=None,
        action="TASK_UPDATED",
        details=f"Task ID {updated_task.id} updated",
    )
    return updated_task


@router.delete("/{task_id}", status_code=204)
async def delete_task_endpoint(task_id: int, db: AsyncSession = Depends(get_db)):
    await delete_task(db, task_id)
    await log_event(
        db, user_id=None, action="TASK_DELETED", details=f"Task ID {task_id} deleted"
    )
    return {"message": "Task deleted successfully"}
