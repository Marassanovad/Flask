from fastapi import APIRouter
from HW_6.db import products, database
from HW_6.models.product import Product, ProductIn

router = APIRouter()


@router.post("/fake_products/{count}")
async def create_fake_products(count: int):
    for i in range(count):
        query = products.insert().values(name=f'name{i}',
                                      description=f'description{i}',
                                      price=i * 1000)
        await database.execute(query)
    return {'message': f'{count} fake products create'}


@router.post("/products", response_model=ProductIn)
async def create_product(new_product: ProductIn):
    query = products.insert().values(name=new_product.name,
                                  description=new_product.description, price=new_product.price)
    last_record_id = await database.execute(query)
    return {**new_product.dict(), "id": last_record_id}


@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


@router.get("/all_products/")
async def read_all_product():
    query = products.select()
    return await database.fetch_all(query)


@router.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': 'Product deleted'}