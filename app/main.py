from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def base():
    return {"result": "todo good"}
