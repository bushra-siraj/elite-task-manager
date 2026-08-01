# ⚡ Elite Task Control Center

---

## 🌟 Overview

**Elite Task Control Center** is a production-grade, full-stack task management system designed to showcase the architectural power of **FastAPI** paired with a modern, reactive **Streamlit** front-end. It features a bespoke dark-mode **glassmorphic design system**, micro-interactions, Lottie animations, and a dynamic 6-color rotating hover-glow workflow matrix.

**Check it out at**: https://elite-task.streamlit.app/
---

## ✨ Core Features

* **💎 Advanced Glassmorphism UI**: Custom CSS backdrop filters (`backdrop-blur`), soft shadows, and clean typography that mimics elite enterprise dashboard architecture.
* **🎨 6-Color Dynamic Task Matrix**: Tasks automatically cycle through six distinct neon hover-glow variants and status accent markers:
  1. **Crimson Red** (`#ef4444`)
  2. **Amber Gold** (`#f59e0b`)
  3. **Electric Blue** (`#3b82f6`)
  4. **Forest Green** (`#22c55e`)
  5. **Dark Pink** (`#ec4899`)
  6. **Deep Purple** (`#a855f7`)
* **⚡ Asynchronous FastAPI Backend**: Lightning-fast RESTful endpoints built with automatic data validation via Pydantic schemas.
* **🔄 Full CRUD Lifecycle**:
  * **Create**: Instantiate task pipelines dynamically.
  * **Read**: Fetch active items via clean metric cards and stream lists.
  * **Update**: Toggle completion status instantly or use the inline drawer to modify task specifications.
  * **Delete**: Secure record purging.
* **📊 Live System Telemetry**: Real-time health monitoring and metric counters tracking total, completed, and pending execution tasks.

---

## 🛠️ Tech Stack

* **Backend Core**: Python, FastAPI, Uvicorn, Pydantic
* **Frontend UI**: Streamlit, Streamlit-Lottie, Custom HTML/CSS Engine
* **Communication Layer**: HTTP Requests / REST API Architecture

---
## 📂 Folder Structure 

| File | Description |
| :--- | :--- |
| `app.py` | Streamlit dashboard UI, styling, and state controller |
| `main.py` | FastAPI server implementation & routing logic |
| `README.md` | Comprehensive project documentation |

---

## 🔷 How to run it
1. Install dependencies:
   \`\`\`bash
   pip install fastapi uvicorn
   \`\`\`
2. Run the server:
   \`\`\`bash
   uvicorn main:app --reload
   \`\`\`
3. Visit `http://localhost:8000/docs` for interactive Swagger UI.

## ◼ Endpoints

| Method | Path            | Description               |
|--------|-----------------|----------------------------|
| GET    | /               | API info                  |
| GET    | /health         | Health check               |
| GET    | /tasks          | List all tasks             |
| GET    | /tasks/{id}     | Get a single task          |
| POST   | /tasks          | Create a new task          |
| PUT    | /tasks/{id}     | Update a task               |
| DELETE | /tasks/{id}     | Delete a task               |

## Example request

HTTP/1.1 200 OK
date: Fri, 31 Jul 2026 18:39:56 GMT
server: uvicorn
content-length: 333
content-type: application/json

[
  {"id": 1, "title": "Buy milk", "done": false},
  {"id": 2, "title": "Walk the dog", "done": false},
  {"id": 3, "title": "Finish assignment", "done": true},
  {"id": 4, "title": "pay utility bills by Friday", "done": true},
  {"id": 5, "title": "Back up one important file to a cloud drive.", "done": false},
  {"id": 6, "title": "Drink 3 large sips of water.", "done": false}
]

---

## 👨‍💻 Author Information & Background

* **Name**: Student & Backend Engineering Specialist
* **Specialization**: Data Science, Artificial Intelligence, & Backend Architecture
* **Current Role**: Backend Engineering Intern at Flexible Flyrank AI
* **Linkedin**: www.linkedin.com/in/bushrasiraj
* **Email**: Bushrasiraj586@gmail.com

---

## 📷 Screenshot

<img width="960" height="420" alt="2026-07-31 20_29_37-FastAPI - Swagger UI" src="https://github.com/user-attachments/assets/25f4be79-232e-4f84-9101-761dfcf5bf0e" />
