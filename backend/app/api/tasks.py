from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from typing import List

from app.core.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.models.task import Task as TaskModel
from app.services.task_service import (
    create_task,
    update_task,
    delete_task,
)
from app.services.audit_service import log_event  # <-- Só adicionei essa linha aqui.

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task_by_id(task_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TaskModel).where(TaskModel.id == task_id))
    task = result.scalars().first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task não encontrada"
        )
    return task


@router.post("/", response_model=TaskResponse)
async def create_new_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    task_created = await create_task(db, task)
    await log_event(
        db, user_id=None, action="TASK_CREATED", details=f"Task ID {task_created.id}"
    )
    return task_created


@router.get("/", response_model=List[TaskResponse])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TaskModel))
    tasks = result.scalars().all()
    return tasks
