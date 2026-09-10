# Backend PoC2 - Bienvenida

## Descripción
Este es el backend de la Prueba de Concepto 2 (PoC2). Es una API REST simple construida con FastAPI que proporciona un endpoint para generar saludos personalizados. El objetivo de este proyecto es demostrar cómo estructurar la comunicación entre un backend y un frontend de manera limpia y tipada, usando schemas de validación (contrato API first).

## Dependencias
El proyecto está construido usando **Python 3.11+** y emplea las siguientes librerías principales:
- **[FastAPI](https://fastapi.tiangolo.com/):** Framework web rápido para construir la API.
- **[Pydantic](https://docs.pydantic.dev/):** Para la validación de datos y el tipado estático (schemas).
- **[Uvicorn](https://www.uvicorn.org/):** Servidor ASGI de desarrollo y producción.
- **Dependencias de Desarrollo:** `pytest` y `httpx` (para los tests) y `ruff` (como linter rápido).

## Árbol de Carpetas y Ficheros
```text
backend/
├── pyproject.toml         # Configuración del proyecto y dependencias (hatchling)
├── .gitignore             # Archivos ignorados por Git
├── src/
│   └── app/
│       ├── __init__.py
│       ├── main.py            # Instancia de FastAPI y configuración CORS (Puerto: 8001)
│       ├── schemas.py         # Contrato de datos de la API (Request y Response)
│       ├── api/
│       │   └── bienvenida.py  # Router con el endpoint /api/bienvenida
│       └── core/
│           └── config.py      # Configuraciones globales de la app
└── tests/
    └── test_bienvenida.py # Tests unitarios y de integración (pytest)
```

## Enlaces de Referencia
- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de Pydantic V2](https://docs.pydantic.dev/)
- [Documentación de Ruff (Linter en Python)](https://docs.astral.sh/ruff/)
- [Documentación de Pytest](https://docs.pytest.org/)
