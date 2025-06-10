from fastapi import APIRouter
from app.models.task_model import Task
from app.services.task_service import TaskService

router = APIRouter()
task_service = TaskService()

@router.get("/tasks")
async def get_tasks():
    return await task_service.get_all_tasks()

@router.post("/tasks")
async def create_task(task: Task):
    return await task_service.create_task(task)

@router.put("/tasks/{task_id}")
async def complete_task(task_id: str):
    return await task_service.complete_task(task_id)

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    return await task_service.delete_task(task_id)
