from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.task import Task as TaskModel
from app.schemas.task import TaskCreate, TaskUpdate


async def get_all_tasks(db: AsyncSession):
    """
    Retorna todas as tarefas no banco.
    """
    result = await db.execute(select(TaskModel))
    tasks = result.scalars().all()
    return tasks


async def create_task(db: AsyncSession, task: TaskCreate):
    """
    Cria uma nova tarefa com os dados de TaskCreate,
    salva no banco e retorna o objeto criado (TaskModel).
    """
    db_task = TaskModel(title=task.title, description=task.description, completed=False)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task


async def update_task(db: AsyncSession, task_id: int, task: TaskUpdate):
    """
    Atualiza campos da tarefa (title, description ou completed).
    Se não encontrar a tarefa, retorna None.
    Caso encontre, aplica as alterações e retorna o objeto atualizado.
    """
    result = await db.execute(select(TaskModel).where(TaskModel.id == task_id))
    db_task = result.scalars().first()
    if not db_task:
        return None

    if task.title is not None:
        db_task.title = task.title
    if task.description is not None:
        db_task.description = task.description
    if task.completed is not None:
        db_task.completed = task.completed

    await db.commit()
    await db.refresh(db_task)
    return db_task


async def delete_task(db: AsyncSession, task_id: int):
    """
    Deleta a tarefa com o ID especificado.
    Retorna True se deletou, False se não encontrou a tarefa.
    """
    result = await db.execute(select(TaskModel).where(TaskModel.id == task_id))
    db_task = result.scalars().first()
    if not db_task:
        return False

    await db.delete(db_task)
    await db.commit()
    return True
