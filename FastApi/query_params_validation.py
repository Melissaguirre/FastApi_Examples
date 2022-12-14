from typing import List, Union
from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()

@app.get("/items2/")
async def read_items(
    q: Union[str, None] = Query(
        default=None, min_length=3, max_length=50, regex="^fixedquery$"
    )
):
    results = {"items2": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#ingresar y traer varios items
@app.get("/items/")
async def read_items(q: Union[List[str], None] = Query(default = None)):
    query_items = {"q": q}
    return query_items

#Valor que se ingresó en q, siendo menor de 50 caracter
@app.get("/itemss/")
async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#si la persona no ingresa nada al campo q, por default se ingresa "fixedquery"
@app.get("/items3/")
async def read_items(q: str = Query(default="fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#por medio de Query q es obligatoria
@app.get("/items_required/")
async def read_items(q: str = Query(min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#los tres puntos también indica que es obligatorio
@app.get("/items-required2/")
async def read_items(q: str = Query(default=..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#obligatorio con la librería Required
@app.get("/items/")
async def read_items(q: str = Query(default=Required, min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results