# Mi primer Microservicio 
Realizado por: Romel Gualoto 
Microservicio REST desarrollado con **FastAPI** y **MongoDB** para la gestión de tareas. Permite crear, listar, marcar como completada y eliminar tareas de forma eficiente.

---
## Funcionalidades presentadas 

- Crear nuevas tareas
- Ver todas las tareas
- Marcar tareas como completadas
- Eliminar tareas por ID
- Conectado a MongoDB 
- Documentación interactiva con Swagger

---


---

##  Instalación local (sin Docker)

### 1. Clonar el repositorio

git clone https://github.com/Romelg18/task-manager-api.git
cd task-manager-api

## 2. Crear y activar el entorno virtual 
python -m venv venv
.\venv\Scripts\activate

## 3. Instalar dependencias
pip install -r requirements.txt

## 4. Configurar archivo .env (MUY IMPORTANTE)
Crear un archivo .env en la carpeta raiz  que contenga: 
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=taskdb

## 5. Ejecutar el servidor 
uvicorn app.main:app --reload
## 6. Visualizar el microservicio 
 http://127.0.0.1:8000/docs


## EJECUCION OPCIONAL
-Adicionalmente se hizo un dockerfile en caso de querer ejecutar con docker para eso tendriamos que cambiar el.env
MONGO_URI=mongodb://host.docker.internal:27017
DATABASE_NAME=taskdb
-Construir la imagen 
docker build -t task-manager-api .
-Y ejecutar el contenedor 
docker run -d -p 8000:8000 --env-file .env task-manager-api
