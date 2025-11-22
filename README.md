# 🧩 RICK AND MORTY API

Servicio desarrollado con **FastAPI** para gestionar capitulos de Rick y Morty.  

---

## 🚀 Tecnologías principales

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Python 3.13+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker-Compose](https://docs.docker.com/compose/)
- [logging](https://docs.python.org/3/library/logging.html)

---

## 💾 Esquema SQL

Se adjunta un archivo **schema.sql** que permite visualizar la estructura SQL de SQLite

---

## ⚙️ Variables de entorno

Las variables de entorno se cargan mediante el archivo `env.sh` **(Mac)**.  
Ejemplo de contenido:

```bash
export NAMESPACE=management-information
export RESOURCE=tv
export URL_DATABASE="sqlite:///rickandmortyapi.db"
```

Para cargarlas en tu entorno local **(Mac)**:

```bash
source env.sh
```

## ⚙️ Variables de entorno del contenedor levantado con docker-compose

Las variables de entorno que se utilizarán para el contenedor deben estar en un archivo `.env`.  
Ejemplo de contenido:

```bash
NAMESPACE=management-information
RESOURCE=tv
URL_DATABASE="sqlite:///rickandmortyapi.db"
```

---

## 🐳 Ejecución con Docker y/o Podman

### 1️⃣ Construir la imagen

```bash
docker build -t rickmortyapi-image:1.0.0 .
podman build -t rickmortyapi-image:1.0.0 .
```

### 2️⃣ Ejecutar el contenedor

```bash
docker run -d -p 8000:8000 --name rickmortyapi-container --env-file ./.env rickmortyapi-image:1.0.0
podman run -d -p 8000:8000 --name rickmortyapi-container --env-file ./.env rickmortyapi-image:1.0.0
```

> ⚠️ Nota: asegúrate de que el archivo `.env` esté en el mismo directorio donde ejecutas el comando `docker run`.

> **⚠️ Nota: se recomienda utilizar docker-compose**


### 3️⃣ Ejecución del docker-compose [All In One]

```bash
docker compose up -d --build [Levantar procesos]
podman compose up -d --build [Levantar procesos]

docker compose down -v [Kill procesos]
podman compose down -v [Kill procesos]
```

---

## ▶️ Ejecución local **(Mac)**

Crea un entorno virtual y activa las variables. Asegurate de tener python 3.13+:

```bash
python3.13.+ -m venv .venv
source .venv/bin/activate **usa .venv/bin/activate con powershell**
source env.sh
pip install -r requirements.txt
```

Ejecuta el servidor:

```bash
python src/main.py
```

---

## 📂 Estructura general del proyecto

```bash
rickandmortyapi/
├── src/
│   ├── application/
│   │   ├── services/
│   │   ├── usecases/
│   ├── domain/
│   │   ├── dao/
│   │   ├── dto/
│   │   ├── exceptions/
│   │   ├── models/
│   │   ├── settings.py
│   ├── infrastructure/
│   │   ├── database/
│   │   ├── repositories/
│   │   ├── routes/
│   ├── log/
│   ├── container.py
│   ├── main.py
├── .env
├── env.sh
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── schema.sql
└── README.md
```

---

## 🧠 Endpoints REST

| Método | Ruta | Descripción |
|--------|------|--------------|
| `GET`  | `/management-information/api/v1/tv/liveness` | Verifica si el servicio esta arriba |
| `GET` | `/management-information/api/v1/tv/episodes` | Obtiene los detalles de todos los episodios |
| `POST`  | `/management-information/api/v1/tv/episodes` | Crea un nuevo episodio |
| `GET`  | `/management-information/api/v1/tv/episodes/{id}` | Obtiene los detalles de un episodio |
| `DELETE`  | `/management-information/api/v1/tv/episodes/{id}` | Elimina un episodio por id |
| `PATCH`  | `/management-information/api/v1/tv/episodes/{id}/favorite` | Realiza la operación de marcar como favorito un episodio |

---

## 📜 Swagger del servicio

### Docs Endpoints REST

```bash
http://localhost:8000/docs
```

---

## 🧾 Logging

El proyecto usa un logger JSON personalizado que incluye detalles de un proceso en ejecución.  
Ejemplo de salida:

```json
{
  "timestamp": "2025-11-14T14:03:32.529368+00:00",
  "level": "INFO",
  "logger": "RickAndMortyAPI",
  "path": "/rickandmortyapi/rickandmortyapi/src/application/usecases/create_episode.py",
  "message": "episode created with success",
  "details": "extra info ..."
}
```

---

## ✨ Autor

**Kevin Espejel**  
📦 Proyecto interno: *🧩 RICK AND MORTY API*
