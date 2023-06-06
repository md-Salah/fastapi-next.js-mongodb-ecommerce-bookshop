
from app.db.db_config import db
from app.schema.product import ProductSchema

collection = db.product

# async def fetch_one_todo(title):
#     document = await collection.find_one({"title": title})
#     return document

async def fetch_all_products():
    proudcts = []
    cursor = collection.find({})
    async for document in cursor:
        proudcts.append(ProductSchema(**document))
        
    return proudcts

# Create product
async def insert_product(product):
    document = product.dict()
    await collection.insert_one(document)



# async def update_todo(title, desc):
#     await collection.update_one({'title': title}, {'$set': {
#         'desc': desc
#     }})
    
#     document = await collection.find_one({'title': title})

# async def remove_todo(title):
#     await collection.delete_one({'title': title})
#     return True



