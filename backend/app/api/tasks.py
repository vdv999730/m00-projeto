from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.models.task import Task as TaskModel
from app.services.task_service import (
    get_all_tasks,
    create_task,
    update_task,
    delete_task,
)

router = APIRouter()


@router.get("/", response_model=List[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return get_all_tasks(db)


@router.post("/", response_model=TaskResponse)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)


# 🚀 AQUI: ROTA DE GET POR ID (QUE FALTAVA!)
@router.get("/{task_id}", response_model=TaskResponse)
def read_task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task não encontrada"
        )
    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_existing_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    updated = update_task(db, task_id, task)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task não encontrada"
        )
    return updated


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    success = delete_task(db, task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task não encontrada"
        )
    return
