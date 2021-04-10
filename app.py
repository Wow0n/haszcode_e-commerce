from fastapi import FastAPI

import queries
import tags
import models

app = FastAPI(openapi_tags=tags.tags_metadata)


@app.get("/warehouse/select", status_code=200, tags=["Warehouse"])
def warehouse_storage():
    return queries.warehouse_select()


@app.post("/warehouse/insert", status_code=200, tags=["Warehouse"])
def warehouse_insert(item_insert: models.ItemInsert):
    return queries.warehouse_insert(item_insert)


@app.post("/warehouse/update", status_code=200, tags=["Warehouse"])
def warehouse_update(item_update: models.ItemUpdate):
    return queries.warehouse_update(item_update)


@app.delete("/warehouse/delete", status_code=200, tags=["Warehouse"])
def warehouse_delete(id: int):
    return queries.warehouse_delete(id)


@app.get("/client/select", status_code=200, tags=["Client"])
def client_product_list():
    return queries.client_select()
