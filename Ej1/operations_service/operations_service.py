# operations_service.py
from fastapi import FastAPI

app = FastAPI()

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

