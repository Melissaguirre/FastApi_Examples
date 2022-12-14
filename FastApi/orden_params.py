from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(*, 
    item_id: int = Path(title="The ID of the item to get" ,example="101", ge = 1),
    q: str, 
    size : float = Query(example = "2.5", gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results