# ⚡ Elite Task Control Center

---

## 🌟 Overview

**Elite Task Control Center** is a production-grade, full-stack task management system designed to showcase the architectural power of **FastAPI** paired with a modern, reactive **Streamlit** front-end. It features a bespoke dark-mode **glassmorphic design system**, micro-interactions, Lottie animations, and a dynamic 6-color rotating hover-glow workflow matrix.

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

## 📂 Project Directory Structure

```text
elite-task-manager/
│
├── main.py          # FastAPI server implementation & routing logic
├── app.py           # Streamlit dashboard UI, styling, and state controller
└── README.md        # Comprehensive project documentation

