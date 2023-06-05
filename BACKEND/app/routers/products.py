from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/products",
    tags=["PRODUCTS"],
    responses={404: {"description": "Not found"}},
)

products = [
    {"id": 1, "title": "Monitor", "description": "Good product", "price": 120},
    {"id": 2, "title": "Mouse", "description": "Good product", "price": 130},
    {"id": 3, "title": "Keyboard", "description": "Good product", "price": 500},
]

class ProductSchema(BaseModel):
    id: int
    title: str
    description: str
    price: str
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Graphics Card",
                "description": "good product",
                "price": 1000
            }
        }
    
    
# Get All Products
@router.get("/")
async def get_products():
    return products

# Get Product by id
@router.get("/{product_id}")
async def get_product_by_id(product_id: int):
    for product in products:
        if product['id'] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# Create Product
@router.post("/")
async def create_product(product: ProductSchema):
    products.append(product.dict())
    return products[-1]

# Update Product
@router.put("/{product_id}")
async def update_product(product_id: int, product: ProductSchema):
    for p in products:
        if p['id'] == product_id:
            p['title'] = product.title
            p['description'] = product.description
            p['price'] = product.price
            return p
    raise HTTPException(status_code=404, detail="Product not found")


# Delete Product
@router.delete('/{product_id}')
async def delete_product(product_id: int):
    global products
    products = [d for d in products if d['id'] != product_id]
    return {'msg': 'Product removed'}


