from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
from db import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo, update_todo,
    remove_todo
)

app = FastAPI()

origins = ['http://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return {"msg": "Welcome to fast api"}


@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_id(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no Todo item with title '{title}' was found")


@app.post("/api/todo", response_model=Todo)
async def post_todo_by_id(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response, 200
    raise HTTPException(400, "Something Went wrong")


@app.put("/api/todo/{title}", response_model=Todo)
async def update_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response, 200
    raise HTTPException(404, f"There is no Todo item with title '{title}' was found")


@app.delete("/api/todo/{title}", response_model=Todo)
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return {"msg": "todo was deleted successfully"}, 200
    raise HTTPException(404, f"There is no Todo item with title '{title}' was found")
