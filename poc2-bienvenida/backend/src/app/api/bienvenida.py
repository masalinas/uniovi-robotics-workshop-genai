from fastapi import APIRouter

from app.schemas import BienvenidaRequest, BienvenidaResponse

router = APIRouter()

def construir_mensaje(nombre: str) -> str:
    """
    Construye el mensaje de bienvenida.
    Función pura aislada de la lógica HTTP para facilitar el testing.

    Args:
        nombre (str): Nombre de la persona a saludar.

    Returns:
        str: Mensaje de saludo.
    """
    return f"¡Hola, {nombre}! Bienvenido a la PoC2."

@router.post(
    "/bienvenida",
    response_model=BienvenidaResponse,
    summary="Genera un mensaje de bienvenida",
    description="Recibe un nombre de usuario y devuelve un mensaje de saludo personalizado."
)
async def saludar(request: BienvenidaRequest) -> BienvenidaResponse:
    """
    Endpoint para saludar al usuario.
    """
    mensaje = construir_mensaje(request.nombre)
    return BienvenidaResponse(mensaje=mensaje)
