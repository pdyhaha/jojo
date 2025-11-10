from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/")
def read_root(item: Item):
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("01:app", host="127.0.0.1", port=8000, reload=True)