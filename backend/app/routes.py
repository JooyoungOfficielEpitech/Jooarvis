from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

router = APIRouter()

# 일정 데이터 모델
class Schedule(BaseModel):
    id: int
    title: str
    start: str
    end: str

# 임시 일정 데이터
schedules = [
    {"id": 1, "title": "Meeting", "start": "2024-11-29", "end": "2024-11-29"},
    {"id": 2, "title": "Workshop", "start": "2024-11-30", "end": "2024-11-30"},
]

# OPTIONS 요청 처리
@router.options("/{path:path}")
def handle_options():
    return JSONResponse(content="OPTIONS request received.", headers={
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "*"
    })

# GET /api/schedules - 모든 일정 가져오기
@router.get("/schedules")
def get_schedules():
    return schedules

# POST /api/schedules - 새로운 일정 추가
@router.post("/schedules")
def create_schedule(schedule: Schedule):
    schedules.append(schedule.dict())
    return {"message": "Schedule added!", "schedule": schedule}

# PUT /api/schedules/{id} - 일정 수정
@router.put("/schedules/{id}")
def update_schedule(id: int, schedule: Schedule):
    for i, s in enumerate(schedules):
        if s["id"] == id:
            schedules[i] = schedule.dict()
            return {"message": "Schedule updated!", "schedule": schedule}
    return {"error": "Schedule not found!"}

# DELETE /api/schedules/{id} - 일정 삭제
@router.delete("/schedules/{id}")
def delete_schedule(id: int):
    global schedules
    schedules = [s for s in schedules if s["id"] != id]
    return {"message": "Schedule deleted!"}
