from dotenv import dotenv_values
from motor.motor_asyncio import AsyncIOMotorClient
from pathlib import Path

settings = dotenv_values(dotenv_path=f"{Path(__file__).parent}/../.env")

db_url = settings.get('DB_URL')
if not db_url:
    raise Exception("DB_URL")
mongo_client = AsyncIOMotorClient(db_url)

db_name = settings.get('DB_NAME')
if not db_name:
    raise Exception("DB_NAME")
database = mongo_client.db_name

tasks_collection = database.get_collection(name="tasks_collection")

async def retrieve_tasks():
    tasks = []
    async for task in tasks_collection.find():
        tasks.append(task)
    return tasks

async def create_item(task_data: dict):
    task = await tasks_collection.insert_one(task_data)
    new_task = await tasks_collection.find_one(filter={"_id": task.inserted_id})
    return new_task

async def retrieve_item(task_id: str):
    new_task = await tasks_collection.find_one(filter={"_id": task_id})
    if not new_task:
        return {"msg": "not found"}
    return new_task
    
async def update_item(task_id: str, data: dict) -> bool:
    item = await tasks_collection.find_one(filter={"_id": task_id})
    if not item:
        return False
    
    updated_item = await tasks_collection.update_one(
        filter={"_id": task_id},
        update={"$set": data}
    )
    
    if not updated_item:
        return False
    
    return True

async def delete_item(task_id: str) -> bool:
    item = await tasks_collection.find_one(filter={"_id": task_id})
    if not item:
        return False
    await tasks_collection.delete_one(filter={"_id": task_id})
    return True

async def delete_all_items() -> bool:
    await tasks_collection.delete_many(filter={"_id": {"$regex": ".*"}})
    return True