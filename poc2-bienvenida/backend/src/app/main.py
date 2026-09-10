from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import bienvenida
from app.core.config import settings

app = FastAPI(
    title="PoC2 Backend",
    description="API de bienvenida para la PoC2",
    version="0.1.0"
)

# Configuración de CORS basada en la configuración centralizada
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar el router bajo el prefijo /api
app.include_router(bienvenida.router, prefix="/api", tags=["bienvenida"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8001, reload=True)
