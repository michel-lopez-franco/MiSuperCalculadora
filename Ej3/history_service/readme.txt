

# Version mas nueva
- fastapi dev main.py 

#Version anterior 
- uvicorn history_service:app

- http://127.0.0.1:8000/docs

- http://127.0.0.1:8000/history/1


// Post to /history
{
  "user_id": "1",
  "operation": "add",
  "operands": {"a":5,"b":6},
  "result": 11
}

curl -X 'POST' \
  'http://127.0.0.1:8000/history' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": "1",
  "operation": "add",
  "operands": {"a":5,"b":6},
  "result": 11
}'



- docker build -t operations_service:v1 .

- docker compose up --build

- docker compose up --build -d

- docker compose down