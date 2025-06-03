import pytest
from app.models.task import Task as TaskModel
from app.schemas.task import TaskCreate, TaskUpdate
from app.services.task_service import (
    create_task,
    get_all_tasks,
    update_task,
    delete_task,
)


@pytest.mark.asyncio
async def test_create_task_service(async_session):
    task_data = TaskCreate(title="Service Task", description="Task Desc")
    task = await create_task(async_session, task_data)
    assert task.title == task_data.title
    assert task.description == task_data.description
    assert task.completed is False


@pytest.mark.asyncio
async def test_get_all_tasks_service(async_session):
    task_data = TaskCreate(title="Another Task", description="Another Desc")
    await create_task(async_session, task_data)

    tasks = await get_all_tasks(async_session)
    assert isinstance(tasks, list)
    assert len(tasks) >= 1


@pytest.mark.asyncio
async def test_update_task_found(async_session):
    task_data = TaskCreate(title="To Update", description="Update Desc")
    task = await create_task(async_session, task_data)

    update_data = TaskUpdate(title="Updated Title", completed=True)
    updated_task = await update_task(async_session, task.id, update_data)

    assert updated_task is not None
    assert updated_task.title == "Updated Title"
    assert updated_task.completed is True


@pytest.mark.asyncio
async def test_update_task_not_found(async_session):
    update_data = TaskUpdate(title="Should Fail")
    result = await update_task(async_session, 99999, update_data)  # ID inexistente
    assert result is None


@pytest.mark.asyncio
async def test_delete_task_found(async_session):
    task_data = TaskCreate(title="To Delete", description="Delete Desc")
    task = await create_task(async_session, task_data)

    result = await delete_task(async_session, task.id)
    assert result is True


@pytest.mark.asyncio
async def test_delete_task_not_found(async_session):
    result = await delete_task(async_session, 99999)  # ID inexistente
    assert result is False
