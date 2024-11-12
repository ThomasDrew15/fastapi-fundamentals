from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    """return a welcome message"""
    return {'message': "Welcome to the Car Sharing service!"}

@app.get("/date")
def welcome():
    """return the current date and time"""
    return {'date': datetime.now()}