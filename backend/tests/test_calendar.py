import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.routes import schedules  # schedules 가져오기

client = TestClient(app)

# 임시 일정 데이터
sample_event = {
    "id": 1,
    "title": "Test Event",
    "start": "2024-12-01T10:00:00",
    "end": "2024-12-01T11:00:00"
}

updated_event = {
    "id": 1,
    "title": "Updated Event",
    "start": "2024-12-01T12:00:00",
    "end": "2024-12-01T13:00:00"
}

@pytest.fixture(autouse=True)
def clear_schedules():
    """테스트 시작 전에 일정 초기화"""
    schedules.clear()  # schedules 초기화
    schedules.extend([])  # 기본 데이터를 비우기

def test_get_schedules_empty():
    """초기 일정 목록이 비어 있는지 확인"""
    response = client.get("/api/schedules")
    assert response.status_code == 200
    assert response.json() == []

def test_create_schedule():
    """새로운 일정 추가 테스트"""
    response = client.post("/api/schedules", json=sample_event)
    assert response.status_code == 200
    assert response.json()["message"] == "Schedule added!"
    assert response.json()["schedule"] == sample_event

def test_get_schedules_after_creation():
    """일정 추가 후 목록에 추가되었는지 확인"""
    response = client.post("/api/schedules", json=sample_event)
    assert response.status_code == 200
    response = client.get("/api/schedules")
    assert response.status_code == 200
    schedules = response.json()
    assert len(schedules) == 1
    assert schedules[0]["title"] == "Test Event"

def test_update_schedule():
    """기존 일정 업데이트 테스트"""
    client.post("/api/schedules", json=sample_event)
    response = client.put(f"/api/schedules/{sample_event['id']}", json=updated_event)
    assert response.status_code == 200
    assert response.json()["message"] == "Schedule updated!"
    assert response.json()["schedule"]["title"] == "Updated Event"

def test_get_schedules_after_update():
    """업데이트 후 일정 내용이 반영되었는지 확인"""
    client.post("/api/schedules", json=sample_event)
    client.put(f"/api/schedules/{sample_event['id']}", json=updated_event)
    response = client.get("/api/schedules")
    assert response.status_code == 200
    schedules = response.json()
    assert schedules[0]["title"] == "Updated Event"

def test_delete_schedule():
    """일정 삭제 테스트"""
    client.post("/api/schedules", json=sample_event)
    response = client.delete(f"/api/schedules/{sample_event['id']}")
    assert response.status_code == 200
    assert response.json()["message"] == "Schedule deleted!"

def test_get_schedules_after_deletion():
    """삭제 후 일정 목록이 비어 있는지 확인"""
    client.post("/api/schedules", json=sample_event)
    client.delete(f"/api/schedules/{sample_event['id']}")
    response = client.get("/api/schedules")
    assert response.status_code == 200
    assert response.json() == []

def test_cors_settings():
    """CORS 설정 확인"""
    response = client.options("/api/schedules")
    assert response.status_code == 200
    assert "access-control-allow-origin" in response.headers
    assert response.headers["access-control-allow-origin"] == "*"
