import motor.motor_asyncio
from motor.motor_asyncio import (
    AsyncIOMotorCollection, AsyncIOMotorDatabase, AsyncIOMotorClient)
from bson import ObjectId
from app.core.settings import settings
client: AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URL)
db: AsyncIOMotorDatabase = client.virtual_market
product_collection: AsyncIOMotorCollection = db.products

async def is_valid_objectID(id: str) -> bool:
    return ObjectId.is_valid(id)