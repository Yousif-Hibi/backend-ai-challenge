from flask import Flask ,request 
import requests

app = Flask(__name__)

tasks_db = [
    {"id": 1, "title": "Setup Project", "status": "completed", "priority": "high"},
    {"id": 2, "title": "Design API Endpoints", "status": "in-progress", "priority": "medium"},
    {"id": 3, "title": "Write Documentation", "status": "pending", "priority": "low"},
    {"id": 4, "title": "Refactor Database Logic", "status": "pending", "priority": "high"},
    {"id": 5, "title": "Deploy to Production", "status": "pending", "priority": "medium"}
]


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/task")
def get_tasks():
    return tasks_db

@app.get("/task/<int:id>")
def get_task_by_id(id):
    for  task in tasks_db :
        if str(task["id"]) == str(id) : 
            return task
    return 'id does not exist'
@app.get("/task/search")
def get_task_by_status():
    task_search=[]
    for  task in tasks_db :
        if str(task["status"]) == str("pending") : 
            task_search.append(task)
    if len(task_search) > 0 :
        return task_search
    return 'no pending tasks'

@app.post("/task")
def post_tasks():
    # silent=True returns None instead of a 400 error if JSON is missing/broken
    new_data = request.get_json(silent=True)
    
    
    if new_data is None:
        return {"error": "Invalid or missing JSON body"}, 400
    
    if "title" not in new_data:
        return {"error": "Key 'title' is required"}, 400

    new_task = {
        "id": len(tasks_db) + 1,
        "title": new_data["title"],
        "status": new_data.get("status", "pending"),
        "priority": new_data.get("priority", "low")
    }
    
    tasks_db.append(new_task)
    return new_task, 201

@app.delete("/task/<int:id>")
def delete_task(id):
    for  task in tasks_db :
        if str(task["id"]) == str(id) : 
            tasks_db.remove(task)
            return f'task {id} was deleted'
    return "id does not exist"
