from sqlalchemy.orm import Session
from app.models.task import Task as TaskModel
from app.schemas.task import TaskCreate, TaskUpdate


def get_all_tasks(db: Session):
    """
    Retorna todas as tarefas no banco.
    """
    return db.query(TaskModel).all()


def create_task(db: Session, task: TaskCreate):
    """
    Cria uma nova tarefa com os dados de TaskCreate,
    salva no banco e retorna o objeto criado (TaskModel).
    """
    db_task = TaskModel(title=task.title, description=task.description, completed=False)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task: TaskUpdate):
    """
    Atualiza campos da tarefa (title, description ou completed).
    Se não encontrar a tarefa, retorna None.
    Caso encontre, aplica as alterações e retorna o objeto atualizado.
    """
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not db_task:
        return None

    if task.title is not None:
        db_task.title = task.title
    if task.description is not None:
        db_task.description = task.description
    if task.completed is not None:
        db_task.completed = task.completed

    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    """
    Deleta a tarefa com o ID especificado.
    Retorna True se deletou, False se não encontrou a tarefa.
    """
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not db_task:
        return False

    db.delete(db_task)
    db.commit()
    return True
