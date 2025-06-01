import pytest

# Testes CRUD para /tasks/


@pytest.mark.asyncio
async def test_get_all_tasks_empty(async_client):
    response = await async_client.get("/tasks/")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio
async def test_create_task(async_client):
    payload = {"title": "Nova Tarefa", "description": "Descrição de teste"}
    response = await async_client.post("/tasks/", json=payload)
    assert response.status_code in (200, 201)
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["completed"] is False
    assert "id" in data


@pytest.mark.asyncio
async def test_get_all_tasks_non_empty(async_client):
    response = await async_client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


@pytest.mark.asyncio
async def test_get_task_by_id(async_client):
    # Cria uma nova tarefa para garantir que existe um ID
    payload = {"title": "Tarefa para GET", "description": "Desc GET"}
    create_resp = await async_client.post("/tasks/", json=payload)
    task_id = create_resp.json()["id"]

    response = await async_client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == payload["title"]


@pytest.mark.asyncio
async def test_update_task(async_client):
    # Cria uma nova tarefa
    payload = {"title": "Tarefa PUT", "description": "Desc PUT"}
    create_resp = await async_client.post("/tasks/", json=payload)
    task_id = create_resp.json()["id"]

    update_payload = {"title": "Atualizado", "completed": True}
    response = await async_client.put(f"/tasks/{task_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Atualizado"
    assert data["completed"] is True


@pytest.mark.asyncio
async def test_delete_task(async_client):
    # Cria uma nova tarefa
    payload = {"title": "Tarefa DELETE", "description": "Desc DELETE"}
    create_resp = await async_client.post("/tasks/", json=payload)
    task_id = create_resp.json()["id"]

    # Deleta a tarefa
    response = await async_client.delete(f"/tasks/{task_id}")
    assert response.status_code in (200, 204)

    # Verifica que GET /tasks/{id} agora retorna 404
    get_resp = await async_client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 404
