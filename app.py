from fastapi import FastAPI

import queries
import tags
import models

app = FastAPI(openapi_tags=tags.tags_metadata)


@app.post("/warehouse/select/", status_code=200, tags=["Warehouse"])
def warehouse_storage():
    return queries.warehouse_select()


@app.post("/warehouse/insert/", status_code=200, tags=["Warehouse"])
def warehouse_insert(item: models.Item):
    return queries.warehouse_insert(item)


@app.post("/warehouse/delete/", status_code=200, tags=["Warehouse"])
def warehouse_delete(id: int):
    return queries.warehouse_delete(id)

@app.post("/client/select/", status_code=200, tags=["Client"])
def client_product_list():
    return queries.client_select()
