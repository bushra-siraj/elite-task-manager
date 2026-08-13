from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

def get_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row  
    return conn

def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
    """)
    # seed only if empty
    count = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    if count == 0:
        conn.executemany(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            [("Buy milk", 0), ("Walk the dog", 0), ("Finish assignment", 1)]
        )
        conn.commit()
    conn.close()

init_db()

app = FastAPI()

tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Walk the dog", "done": False},
    {"id": 3, "title": "Finish assignment", "done": True},
]

class TaskCreate(BaseModel):
    title: str

@app.get("/")
def read_root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/tasks", description="List all tasks")
def get_tasks():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/tasks/{task_id}", description="Get a single task by id")
def get_task(task_id: int):
    conn = get_connection()
    row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return dict(row)

@app.post("/tasks", status_code=201, description="Create a new task")
def create_task(new_task: TaskCreate):
    if not new_task.title.strip():
        raise HTTPException(status_code=400, detail="Title is required")

    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (new_task.title, 0)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return {"id": new_id, "title": new_task.title, "done": False}

class TaskUpdate(BaseModel):
    title: str
    done: bool

@app.put("/tasks/{task_id}", description="Update a task")
def update_task(task_id: int, updated: TaskUpdate):
    if not updated.title.strip():
        raise HTTPException(status_code=400, detail="Title is required")

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated.title
            task["done"] = updated.done
            return task

    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@app.delete("/tasks/{task_id}", status_code=204, description="Delete a task")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return

    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")