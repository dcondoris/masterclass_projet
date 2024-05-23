from fastapi import FastAPI

app = FastAPI()

@app.get("/addition")
def addition(a: int, b: int):
    return a**3 + b**3