
# Version mas nueva
- fastapi dev main.py 

#Version anterior 
- uvicorn operations_service:app


http://127.0.0.1:8000/docs


//Todo hacer una cola de rabbitQM para escuchar la peticion de la suma, y guardar el valor
sin modificar este archivo de operaciones. 


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