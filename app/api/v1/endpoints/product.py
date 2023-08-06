from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder
from app.schemas.product import Product, ProductUpdate
from app.crud.product import (create_product, get_single_product,
                              get_all_products, update, delete)
router = APIRouter()

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED,
             response_description="New product created!")
async def create_product_(
    *,
    product_in: Product
):
    """
    Creates a new product
    """
    product = jsonable_encoder(product_in)
    new_product = await create_product(product_data=product)
    return new_product

@router.get("/{product_id}", response_model=Product, status_code=status.HTTP_200_OK,
            )
async def get_product(
    *,
    product_id: str
):
    """
    Searches for a product based on its ID
    """
    product = await get_single_product(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found!"
        )
    return product

@router.get("/", response_model=Product, status_code=status.HTTP_200_OK)
async def get_products():
    """
    Searches for all products
    """
    products = await get_all_products()
    if not products:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Products not found"
        )
    return products

@router.put("/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
async def update_product(
    *,
    product_id: str,
    update_in: ProductUpdate
):
    """
    updates a product
    """
    product = await get_single_product(id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with given ID was not found."
        )
    print("passed")
    updated = await update(id=id, product_data=update_in)
    return updated
    
    
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    *,
    product_id: str
):
    """
    deletes a product
    """
    product = await get_single_product(id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with given ID was not found"
        )
    await delete(id=product_id)
    return
    