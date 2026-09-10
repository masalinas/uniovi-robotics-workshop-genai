from fastapi.testclient import TestClient

from app.api.bienvenida import construir_mensaje
from app.main import app

client = TestClient(app)

def test_construir_mensaje():
    """
    Test unitario de la función pura que genera el mensaje.
    """
    resultado = construir_mensaje("Miguel")
    assert resultado == "¡Hola, Miguel! Bienvenido a la PoC2."

def test_bienvenida_endpoint_exitoso():
    """
    Test de integración del caso feliz del endpoint POST /api/bienvenida.
    """
    response = client.post("/api/bienvenida", json={"nombre": "Miguel"})
    assert response.status_code == 200
    data = response.json()
    assert "mensaje" in data
    assert data["mensaje"] == "¡Hola, Miguel! Bienvenido a la PoC2."

def test_bienvenida_endpoint_nombre_vacio():
    """
    Test de validación cuando el nombre está vacío.
    """
    response = client.post("/api/bienvenida", json={"nombre": ""})
    # Pydantic debe devolver 422 Unprocessable Entity debido a min_length=1
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data

def test_bienvenida_endpoint_faltan_datos():
    """
    Test de validación cuando falta el campo requerido.
    """
    response = client.post("/api/bienvenida", json={})
    assert response.status_code == 422
