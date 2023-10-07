import uvicorn
from fastapi import FastAPI
from HW_6.db import database
from HW_6.routers import user, product, order

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(user.router, tags=["users"])
app.include_router(product.router, tags=["goods"])
app.include_router(order.router, tags=["order"])

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)