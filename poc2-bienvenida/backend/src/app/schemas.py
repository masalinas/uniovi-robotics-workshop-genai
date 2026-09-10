from pydantic import BaseModel, Field


class BienvenidaRequest(BaseModel):
    """
    Contrato de la petición para el endpoint de bienvenida.
    """
    nombre: str = Field(
        ...,
        min_length=1,
        description="El nombre del usuario al que se va a saludar."
    )

class BienvenidaResponse(BaseModel):
    """
    Contrato de la respuesta para el endpoint de bienvenida.
    """
    mensaje: str = Field(
        ...,
        description="El mensaje de bienvenida generado."
    )
