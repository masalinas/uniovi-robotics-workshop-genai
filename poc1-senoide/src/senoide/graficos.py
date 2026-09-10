"""Módulo para la representación gráfica de señales."""

import matplotlib.pyplot as plt
import numpy as np

from senoide.senal import AMPLITUD_DEFECTO, FRECUENCIA_DEFECTO, generar_senoide

# Constantes de estilo gráfico
COLOR_DEFECTO = "tab:blue"


def dibujar_senoide(t: np.ndarray, y: np.ndarray, color: str = COLOR_DEFECTO) -> None:
    """Dibuja una señal senoidal y abre una ventana gráfica.

    Nota: Esta función tiene el efecto secundario de mostrar una ventana interactiva.

    Args:
        t (np.ndarray): Array de tiempo (eje X).
        y (np.ndarray): Array de valores de amplitud (eje Y).
        color (str, opcional): Color de la línea en formato para matplotlib. Por defecto es "tab:blue".
    """
    plt.figure(figsize=(8, 4))
    plt.plot(t, y, color=color, linewidth=2, label="Señal")

    plt.title("Generador de Señal Senoidal")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    # Añadimos una rejilla para facilitar la lectura de valores
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend()

    # Guardamos la figura en un archivo local en lugar de intentar abrir una ventana
    # Esto es útil en entornos sin servidor gráfico (como WSL o contenedores)
    nombre_archivo = "senoide.png"
    plt.savefig(nombre_archivo, dpi=300)
    print(f"Gráfica generada y guardada exitosamente en: {nombre_archivo}")


if __name__ == "__main__":
    # Ejecución por defecto para la Fase 1.
    # No hay parseo de argumentos de consola todavía, usamos constantes.
    tiempo, amplitud = generar_senoide(AMPLITUD_DEFECTO, FRECUENCIA_DEFECTO)
    dibujar_senoide(tiempo, amplitud, COLOR_DEFECTO)
