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
│       └── save.py          # /save endpoint
├── .env                     # Env variables
├── .env.template            # Sample config
├── requirements.txt         # Dependencies
├── Dockerfile               # Docker image config
├── docker-compose.yml       # Run locally
└── README.md                # Documentation
```

---

## ⚙️ Environment Variables
Create a `.env` file using `.env.template`:

```env
MONGO_URI=your_mongo_connection_string
DB_NAME=ollama
COLLECTION_NAME=responses
```

---

## ▶️ Run Locally
```bash
# Build and start
docker-compose up --build
```

Service will be available at: [http://localhost:8001/save](http://localhost:8001/save)

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

## 🧠 Author
Built with ❤️ by Yanioconjota