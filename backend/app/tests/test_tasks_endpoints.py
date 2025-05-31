# tests/test_tasks_endpoints.py

# Testes CRUD para /tasks/

def test_get_all_tasks_empty(client):
    response = client.get("/tasks/")
    # Pode retornar 200 com lista vazia ou 404, dependendo da implementação
    assert response.status_code in (200, 404)

def test_create_task(client):
    payload = {"title": "Nova Tarefa", "description": "Descrição de teste"}
    response = client.post("/tasks/", json=payload)
    assert response.status_code in (200, 201)
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["completed"] is False
    assert "id" in data

def test_get_all_tasks_non_empty(client):
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_get_task_by_id(client):
    # Cria uma nova tarefa para garantir existe um ID
    payload = {"title": "Tarefa para GET", "description": "Desc GET"}
    create_resp = client.post("/tasks/", json=payload)
    task_id = create_resp.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == payload["title"]

def test_update_task(client):
    # Cria uma nova tarefa
    payload = {"title": "Tarefa PUT", "description": "Desc PUT"}
    create_resp = client.post("/tasks/", json=payload)
    task_id = create_resp.json()["id"]

    update_payload = {"title": "Atualizado", "completed": True}
    response = client.put(f"/tasks/{task_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Atualizado"
    assert data["completed"] is True

def test_delete_task(client):
    # Cria uma nova tarefa
    payload = {"title": "Tarefa DELETE", "description": "Desc DELETE"}
    create_resp = client.post("/tasks/", json=payload)
    task_id = create_resp.json()["id"]

    # Deleta a tarefa
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code in (200, 204)

    # Verifica que GET /tasks/{id} agora retorna 404
    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 404
