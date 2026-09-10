from pydantic import BaseModel


class Settings(BaseModel):
    """
    Configuración principal de la aplicación.
    Mantiene los orígenes permitidos para la configuración de CORS.
    """
    cors_origins: list[str] = ["http://localhost:4200"]

settings = Settings()
