from pydantic import BaseModel
from typing import Optional


# ------------------------------------------------------
# Esquema base para criar/atualizar tarefas
# ------------------------------------------------------
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None


# ------------------------------------------------------
# Modelo usado ao criar nova tarefa (POST /tasks/)
# ------------------------------------------------------
class TaskCreate(TaskBase):
    completed: bool = False


# ------------------------------------------------------
# Modelo usado ao atualizar tarefa (PUT /tasks/{id})
# Todos os campos são opcionais aqui
# ------------------------------------------------------
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


# ------------------------------------------------------
# Resposta enviada pelo backend (Task + campos adicionais)
# ------------------------------------------------------
class TaskResponse(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
