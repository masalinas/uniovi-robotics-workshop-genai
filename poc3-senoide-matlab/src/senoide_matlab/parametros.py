def validar_parametros(amplitud: float, frecuencia: float, color: str) -> None:
    """
    Valida que los parámetros para la generación de la senoide sean correctos.

    Args:
        amplitud: Amplitud de la señal (debe ser > 0).
        frecuencia: Frecuencia de la señal (debe ser > 0).
        color: Color para la gráfica. Debe ser uno de los caracteres válidos
               de MATLAB (r, g, b, c, m, y, k, w).

    Raises:
        ValueError: Si la amplitud o frecuencia son <= 0, o si el color no es válido.
    """
    if amplitud <= 0:
        raise ValueError("La amplitud debe ser mayor que 0.")
    if frecuencia <= 0:
        raise ValueError("La frecuencia debe ser mayor que 0.")
    
    colores_validos = {'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w'}
    if color not in colores_validos:
        raise ValueError(f"El color '{color}' no es válido. Debe ser uno de: {', '.join(sorted(colores_validos))}")
