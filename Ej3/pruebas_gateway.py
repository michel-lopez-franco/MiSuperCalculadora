from fastapi import FastAPI
import json
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return "api gateway"


OPERATIONS_SERVICE_URL ="http://127.0.0.1:8003" #"http://operations-service:8000"
HISTORY_SERVICE_URL = "http://127.0.0.1:8002" #"http://history-service:8000"
AUTH_SERVICE_URL = "http://127.0.0.1:8001" #http://auth-service:8000"

@app.post("/calculate")
def calculate(operation: str, numbers: dict, token: str):
    # Verificar el token con el servicio de autenticación
    auth_response = requests.post(f"{AUTH_SERVICE_URL}/login", json= json.loads(token) )
    print( token)
    print( json.loads(token) )
    print( type(token))
    print( type(json.loads(token) ))
    print(f"{AUTH_SERVICE_URL}/login")
    print( operation )
    print( numbers )
    if auth_response.status_code != 200:
        return {"error": "Invalid token"}

    # Realizar la operación en el servicio de operaciones
    operation_url = f"{OPERATIONS_SERVICE_URL}/{operation}"
    operation_response = requests.post(operation_url, json=numbers)
    operation_data = operation_response.json()

    # Guardar la operación en el servicio de historial
    user_id = auth_response.json().get("user_id")
    history_data = {
        "user_id": user_id,
        "operation": operation,
        "operands": numbers,
        "result": operation_data.get("result", 0),
    }
    requests.post(f"{HISTORY_SERVICE_URL}/history", json=history_data)

    return operation_data

