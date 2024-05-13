
# Version mas nueva
- fastapi dev main.py 

#Version anterior 
- uvicorn operations_service:app


http://127.0.0.1:8000/docs


- docker build -t operations_service:v1 .


- docker run -d -p 8001:8000 operations_service:v1



- python -m uvicorn operations_service:app --reload

- python -m fastapi dev operations_service.py


- docker ps -n 4
- docker stop be62bda37892
- docker ps -l --size

- docker rm $(docker ps --filter status=exited -q)


docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname



docker tag operations_service:v1 michellopezfranco/operations_service:v1
docker push michellopezfranco/operations_service:v1 



- docker compose up --build

- docker compose up --build -d

- docker compose down




----------------------- kubernetes  -----------------------

- docker build -t operations_service:v1 .

- kubectl get apiservices
- kubectl get deployments
- kubectl get pods
- kubectl get services

- kubectl delete pod frontend-pod

kubectl apply -f frontend-pod.yaml
kubectl apply -f backend-pod.yaml


- kubectl apply -f frontend-pod.yaml
- kubectl apply -f frontend-service.yaml


----
- docker build -t operations_service:v1 .
- kubectl apply -f frontend-pod.yaml
- kubectl apply -f frontend-service.yaml