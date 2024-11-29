from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_create_task():
    task_data = {"id": 1, "title": "Test Task", "description": "This is a test task", "completed": False}
    response = client.post("/api/tasks", json=task_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_get_tasks():
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_task():
    task_id = 1
    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 200

def test_update_task():
    updated_task = {"id": 1, "title": "Updated Task", "description": "Updated description", "completed": True}
    response = client.put("/api/tasks/1", json=updated_task)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"

def test_delete_task():
    response = client.delete("/api/tasks/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted."}
