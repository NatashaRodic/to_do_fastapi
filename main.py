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
@app.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {'todo': todo}
        else:
            return {'message': 'No todos found'}

#Create a todo
@app.post('/todos')
def create_todos(todo: Todo):
    todos.append(todo)
    return {'message': 'Todo has been added'}

#Update a todo
@app.put('/todos/{todo_id}')
def update_todo(todo_id: int, todo_object: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_object.item
            return {'todo': todo}
        else:
            return {'message': 'No todos found for update'}

#Delete a todo
@app.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {'message': 'To do has been DELETED'}
    return {'message': 'No todos found'}