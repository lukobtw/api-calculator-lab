from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal


app = FastAPI(
    title="API Calculator",
    description="Учебный API-калькулятор",
    version="1.0.0"
)


class CalculationRequest(BaseModel):
    operation: Literal["add", "subtract", "multiply", "divide"]
    a: float
    b: float


@app.get("/")
def root():
    return {
        "message": "API Calculator is running"
    }


@app.post("/calculate")
def calculate(data: CalculationRequest):

    if data.operation == "add":
        result = data.a + data.b

    elif data.operation == "subtract":
        result = data.a - data.b

    elif data.operation == "multiply":
        result = data.a * data.b

    elif data.operation == "divide":

        if data.b == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed"
            )

        result = data.a / data.b

    return {
        "operation": data.operation,
        "a": data.a,
        "b": data.b,
        "result": result
    }