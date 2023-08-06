import motor.motor_asyncio
from app.core.settings import settings
from motor.motor_asyncio import (
    AsyncIOMotorCollection, AsyncIOMotorDatabase, AsyncIOMotorClient)

client: AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URL)
db: AsyncIOMotorDatabase = client.virtual_market
product_collection: AsyncIOMotorCollection = db.products
