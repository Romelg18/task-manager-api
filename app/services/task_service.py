from app.db.mongo_client import db
from app.models.task_model import Task
from bson import ObjectId

class TaskService:
    def __init__(self):
        self.collection = db["tasks"]

    async def get_all_tasks(self):
        tasks = await self.collection.find().to_list(100)
        formatted_tasks = []

        for task in tasks:
            task["id"] = str(task["_id"])  
            del task["_id"]                
            formatted_tasks.append(task)

        return formatted_tasks

    async def create_task(self, task: Task):
        result = await self.collection.insert_one(task.dict(exclude={"id"}))
        return str(result.inserted_id)

    async def complete_task(self, task_id: str):
        result = await self.collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"completed": True}}
        )
        return result.modified_count

    async def delete_task(self, task_id: str):
        result = await self.collection.delete_one({"_id": ObjectId(task_id)})
        return result.deleted_count
