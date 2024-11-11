from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    """return a welcome message"""
    return {'message': "Welcome to the Car Sharing service!"}