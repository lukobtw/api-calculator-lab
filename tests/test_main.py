import sys
from pathlib import Path

from fastapi.testclient import TestClient


# Добавляем корневую папку проекта в путь Python
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "API Calculator is running"
    }


def test_add():
    response = client.post(
        "/calculate",
        json={
            "operation": "add",
            "a": 10,
            "b": 5
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 15


def test_subtract():
    response = client.post(
        "/calculate",
        json={
            "operation": "subtract",
            "a": 20,
            "b": 5
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 15


def test_multiply():
    response = client.post(
        "/calculate",
        json={
            "operation": "multiply",
            "a": 6,
            "b": 7
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 42


def test_divide():
    response = client.post(
        "/calculate",
        json={
            "operation": "divide",
            "a": 20,
            "b": 4
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_division_by_zero():
    response = client.post(
        "/calculate",
        json={
            "operation": "divide",
            "a": 20,
            "b": 0
        }
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Division by zero is not allowed"
    }


def test_invalid_operation():
    response = client.post(
        "/calculate",
        json={
            "operation": "hack",
            "a": 10,
            "b": 5
        }
    )

    assert response.status_code == 422