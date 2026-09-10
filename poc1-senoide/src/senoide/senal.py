"""Módulo para la generación matemática de la señal senoidal."""

import numpy as np

# Valores por defecto de la señal
AMPLITUD_DEFECTO = 1.0
FRECUENCIA_DEFECTO = 1.0
NUM_MUESTRAS = 1000
TIEMPO_INICIO = 0.0
TIEMPO_FIN = 1.0


def generar_senoide(
    amplitud: float = AMPLITUD_DEFECTO, frecuencia: float = FRECUENCIA_DEFECTO
) -> tuple[np.ndarray, np.ndarray]:
    """Genera una señal senoidal en un intervalo de tiempo fijo.

    Args:
        amplitud (float, opcional): La amplitud pico de la señal. Por defecto es 1.0.
        frecuencia (float, opcional): La frecuencia de la señal en Hz. Por defecto es 1.0.

    Returns:
        tuple[np.ndarray, np.ndarray]: Una tupla que contiene:
            - Un array de numpy con los valores de tiempo (eje X).
            - Un array de numpy con los valores de amplitud (eje Y).

    Raises:
        ValueError: Si la amplitud o la frecuencia son menores o iguales a cero.
    """
    if amplitud <= 0:
        raise ValueError("La amplitud debe ser mayor que cero.")
    if frecuencia <= 0:
        raise ValueError("La frecuencia debe ser mayor que cero.")

    # Usamos linspace en lugar de arange para garantizar un número exacto y controlado
    # de muestras en el intervalo cerrado [TIEMPO_INICIO, TIEMPO_FIN].
    t = np.linspace(TIEMPO_INICIO, TIEMPO_FIN, NUM_MUESTRAS)
    y = amplitud * np.sin(2 * np.pi * frecuencia * t)

    return t, y
