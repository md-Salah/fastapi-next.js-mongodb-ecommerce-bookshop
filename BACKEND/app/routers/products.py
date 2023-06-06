from fastapi import APIRouter, Depends, HTTPException, status

from app.schema.product import ProductSchema
from app.controller.product import insert_product, fetch_all_products

router = APIRouter(
    prefix="/products",
    tags=["PRODUCTS"],
    responses={404: {"description": "Not found"}},
)


# Get All Products
@router.get("/")
async def get_products():
    products = await fetch_all_products()
    return products

# Get Product by id
# @router.get("/{product_id}")
# async def get_product_by_id(product_id: int):
#     for product in products:
#         if product['id'] == product_id:
#             return product
#     raise HTTPException(status_code=404, detail="Product not found")

# Create Product
@router.post("/")
async def create_product(product: ProductSchema):
    p = await insert_product(product)
    return p

# # Update Product
# @router.put("/{product_id}")
# async def update_product(product_id: int, product: ProductSchema):
#     for p in products:
#         if p['id'] == product_id:
#             p['title'] = product.title
#             p['description'] = product.description
#             p['price'] = product.price
#             return p
#     raise HTTPException(status_code=404, detail="Product not found")


# # Delete Product
# @router.delete('/{product_id}')
# async def delete_product(product_id: int):
#     global products
#     products = [d for d in products if d['id'] != product_id]
#     return {'msg': 'Product removed'}


