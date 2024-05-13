
# Version mas nueva
- fastapi dev main.py 

#Version anterior 
- uvicorn auth_service:app

- http://127.0.0.1:8000/docs

- http://127.0.0.1:8000/history/1


- docker build -t auth_service:v1 .

curl -X 'POST' \
  'http://127.0.0.1:8000/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "admin",
  "password": "admin"
}'

- docker build -t auth_service:v1 .

- docker compose up --build

- docker compose up --build -d

- docker compose down