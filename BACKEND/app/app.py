from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import users, products, auth


def init_app():
    app = FastAPI(
        title="FARM Stack Ecommerce",
        description="Ecommerce practice project with FastAPI, Nextjs, React, and MongoDB",
        version="1.0.0",
        contact={
            'name': "md salah",
            "email": 'mdsalah.connect@gmail.com'
        }
        
    )


    # CORS
    origins = ['http://localhost:3000']
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
    
    return app

app = init_app()

# Home
@app.get("/", tags=['HOME'])
async def home():
    return {"message": "Hello World"}   


# Users Router
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)


