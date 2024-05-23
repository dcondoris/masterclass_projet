"""
First script
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/addition")
def addition(a: int, b: int):
    """
    Performs an addition
    """
    return a + b

@app.get("/soustraction")
def soustraction(a: int, b: int):
    """
    Performs a subsraction
    """
    return a - b
