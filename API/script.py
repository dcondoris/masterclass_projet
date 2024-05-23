from fastapi import FastAPI

app = FastAPI()

@app.get("/addition")
def addition(a: int, b: int):
    return a + b

@add.get("/soustraction")
def soustraction(a: int, b: int):
    return a - b