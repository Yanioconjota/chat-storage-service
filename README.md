# 📦 Ollama Storage Service

A microservice built with FastAPI that receives prompts and responses from another API and stores them in MongoDB (hosted on Railway).

---

## 🚀 Features
- FastAPI-based microservice
- MongoDB integration using PyMongo
- Clean structure ready for Docker & scaling
- `.env` support for easy configuration

---

## 📁 Structure
```
ollama-storage-service/
├── app/
│   ├── main.py              # FastAPI app
│   ├── models.py            # Pydantic models
│   ├── database.py          # MongoDB connection
│   └── routes/
│       └── save.py          # /save and /health endpoints
├── .env                     # Env variables (local/dev)
├── .env.template            # Sample config
├── .env.prod.template       # Sample prod config
├── requirements.txt         # Dependencies
├── Dockerfile               # Docker image config
├── docker-compose.yml       # For development
├── docker-compose.prod.yml  # For production
└── README.md                # Documentation
```

---

## ⚙️ Environment Variables
Create a `.env` or `.env.prod` file using the templates:

```env
MONGO_URI=mongodb+srv://your_user:your_pass@your_cluster.mongodb.net/?retryWrites=true&w=majority
DB_NAME=ollama
COLLECTION_NAME=responses
```

To use the **local MongoDB container** (via Docker):
```env
MONGO_URI=mongodb://mongo:27017
DB_NAME=ollama
COLLECTION_NAME=responses
```

---

## ▶️ Run Locally (Development)
```bash
docker-compose up --build
```

## 🚀 Run in Production
```bash
docker-compose -f docker-compose.prod.yml up --build -d
```

Service will be available at: [http://localhost:8001](http://localhost:8001)

---

## 📬 POST /save
**Body:**
```json
{
  "prompt": "Why is the sky blue?",
  "response": "Because of Rayleigh scattering..."
}
```

**Response:**
```json
{
  "status": "success",
  "inserted_id": "<mongo_id>"
}
```

---

## 🔍 GET /health
Checks DB connectivity:
```json
{
  "status": "ok",
  "documents": 42
}
```

---

## ✅ TO-DO
- [ ] Integrate this API with the Ollama microservice (`POST /save`)
- [ ] Add test suite with Pytest and Mongo mocking
- [ ] Add Makefile or Taskfile for common dev commands

---

## 🧠 Author
Built with ❤️ by Janio