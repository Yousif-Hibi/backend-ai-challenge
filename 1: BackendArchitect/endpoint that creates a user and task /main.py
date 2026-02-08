from flask import Flask, request
from sqlmodel import Field, Session, SQLModel, create_engine, Relationship, select


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    tasks: list["Task"] = Relationship(back_populates="user")

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    status: str = "pending"
    is_completed: bool = False
    user_id: int | None = Field(default=None, foreign_key="user.id")
    user: User | None = Relationship(back_populates="tasks")



engine = create_engine("sqlite:///database.db")


SQLModel.metadata.create_all(engine)

app = Flask(__name__)



@app.post("/task")
def post_tasks():
    """Challenge: Create a Task and a User in a single transaction."""
    data = request.get_json(silent=True) or {}
    
    with Session(engine) as session:
        try:
            
            new_user = User(name=data.get("username", "New programer"))
            session.add(new_user)
            session.flush() 
            new_task = Task(
                title=data.get("title", "playingTask"),
                status="active",
                is_completed=False,
                user_id=new_user.id
            )
            session.add(new_task)
            session.commit()
            return {"message": "Success!", "user": new_user.name, "task": new_task.title}, 201
        except Exception as e:
            session.rollback() 
            return {"error": str(e)}, 500

@app.get("/task")
def get_tasks():
    """Fetch tasks using the ORM instead of raw SQL."""
    with Session(engine) as session:
        statement = select(Task)
        results = session.exec(statement).all()
        tasks_list = [task.model_dump() for task in results]
        return {"tasks": tasks_list}, 200

if __name__ == "__main__":
    app.run(debug=True)