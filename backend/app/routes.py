from fastapi import APIRouter, HTTPException
from .models import Task

router = APIRouter()

tasks = []

@router.post("/tasks", response_model=Task)
def create_task(task: Task):
    for t in tasks:
        if t.id == task.id:
            raise HTTPException(status_code=400, detail="Task ID already exists.")
    tasks.append(task)
    return task

@router.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found.")

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found.")

@router.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": "Task deleted."}
