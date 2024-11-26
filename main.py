from fastapi import FastAPI, HTTPException


app = FastAPI()

@app.get('/')
def root():
    return{'message': 'Hello World'}

#Get all todos

#Get single todo

#Create a todo

#Update a todo

#Delete a todo