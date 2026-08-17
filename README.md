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

## Why SQLite
Zero setup, single file, no separate server to install — perfect for a small project like this, and it means the app's data survives a restart, unlike the in-memory version from Week 2.

---

## Docker

This app is containerized. To run it:

\`\`\`bash
docker compose up
\`\`\`

That's it — no manual setup, no installing Python or dependencies on your machine. `tasks.db` is mounted as a volume, so your data survives even if you remove the container.

To stop:
\`\`\`bash
docker compose down
\`\`\`

### Why containerize?
It guarantees the app runs identically on any machine — no "works on my machine" issues, no manually installing Python versions or dependencies. Same idea as the SQLite persistence lesson from Week 2, just one level up: now the whole *app* is portable, not just the data.

---

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

---

## Example request
\`\`\`bash
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'
\`\`\`

---

## Example SQL query (Stage 4)
\`\`\`sql
UPDATE tasks SET done = 1;
\`\`\`
Marked every task as completed directly in DB Browser — the change showed up instantly through the API with no restart, since both read the same file.

---

## 📂 Folder Structure 

| File | Description |
| :--- | :--- |
| `app.py` | Streamlit dashboard UI, styling, and state controller |
| `main.py` | FastAPI server implementation & routing logic |
| `README.md` | Comprehensive project documentation |

---

## 👨‍💻 Author Information & Background

* **Name**: Bushra Siraj
* **Specialization**: Data Science, Artificial Intelligence, & Backend Architecture
* **Current Role**: Backend AI Engineering Intern at Flyrank AI
* **Linkedin**: www.linkedin.com/in/bushrasiraj
* **Email**: Bushrasiraj586@gmail.com

---

## 📷 Screenshorts

<img width="960" height="420" alt="2026-07-31 20_29_37-FastAPI - Swagger UI" src="https://github.com/user-attachments/assets/25f4be79-232e-4f84-9101-761dfcf5bf0e" />

<img width="960" height="505" alt="2026-08-13 21_57_13-" src="https://github.com/user-attachments/assets/7bf573ba-8d8f-477e-bb0b-7af7edba90e2" />