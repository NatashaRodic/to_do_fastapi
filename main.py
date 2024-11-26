from fastapi import FastAPI, HTTPException
from models import Todo


app = FastAPI()

@app.get('/')
def root():
    return{'message': 'Hello World'}

todos = []

#Get all todos
@app.get('/todos')
def all_todos():
    return {'todos': todos}

#Get single todo

#Create a todo
@app.post('/todos')
def create_todos(todo: Todo):
    todos.append(todo)
    return {'message': 'Todo has been added'}

#Update a todo

#Delete a todo