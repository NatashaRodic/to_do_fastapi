from fastapi import FastAPI, HTTPException


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

#Update a todo

#Delete a todo