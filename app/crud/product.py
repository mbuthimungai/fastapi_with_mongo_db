from bson.objectid import ObjectId
from app.api.deps import product_collection

async def get_all_products():
    products = []
    async for product in product_collection.find():
        products.append(product)
    return products
        
async def get_single_product(id: str):
    product = await product_collection.find_one({"_id": ObjectId(id)})
    return product

async def create_product(product_data: dict) -> dict:
    product = await product_collection.insert_one(product_data)
    new_product = await product_collection.find_one({"_id": product.inserted_id}) 
    return new_product

async def update(id: str, product_data: dict) -> dict:
    updated = await product_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": product_data}
    )
    return updated
    
async def delete(id: str):
    await product_collection.delete_one({"_id": ObjectId(id)})
