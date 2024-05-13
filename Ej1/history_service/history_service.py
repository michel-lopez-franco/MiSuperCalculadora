# history_service.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Operation(BaseModel):
    user_id: str
    operation: str
    operands: dict
    result: float

operations = []

@app.post("/history")
def save_operation(operation: Operation):
    operations.append(operation.dict())
    return {"message": "Operation saved successfully"}

@app.get("/history/{user_id}")
def get_user_history(user_id: str):
    user_operations = [op for op in operations if op["user_id"] == user_id]
    return user_operations

