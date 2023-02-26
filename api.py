from typing import Union
from modules.connection import serching
from fastapi import FastAPI
#  uvicorn api:app --reload
app = FastAPI()


@app.get("/")
def read_root(request:str):
    results = serching(request)
    return {"data": results }
