# auth_service.py
from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return "login service"

users = {
    "user1": "password1",
    "user2": "password2",
    "admin": "admin"
}

user_id= {
    "user1": "1",
    "user2": "2",
    "admin": "3"
}
class User(BaseModel):
    username: str
    password: str

def authenticate_user(user: User):
    if user.username in users and users[user.username] == user.password:
        return True
    return False

@app.post("/login")
def login(user: User):
    if authenticate_user(user):
        return {"token": f"valid_token_for_{user.username}",
                "user_id": user_id[user.username]}
    return {"error": "Invalid credentials"}