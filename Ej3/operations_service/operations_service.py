# operations_service.py
from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/sum")
def sum_numbers(numbers: dict):
    a = numbers.get("a", 0)
    b = numbers.get("b", 0)
    return {"result": a + b}

@app.post("/subtract")
def subtract_numbers(numbers: dict):
    a = numbers.get("a", 0)
    b = numbers.get("b", 0)
    return {"result": a - b}

@app.post("/multiply")
def multiply_numbers(numbers: dict):
    a = numbers.get("a", 0)
    b = numbers.get("b", 0)
    return {"result": a * b}

@app.post("/divide")
def divide_numbers(numbers: dict):
    a = numbers.get("a", 0)
    b = numbers.get("b", 0)
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": a / b}

@app.post("/all")
def all_numbers(numbers: dict):
    a = numbers.get("a", 0)
    b = numbers.get("b", 0)
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"sum": a + b, "subtract": a - b,"multiply": a * b,"divide": a / b}


        