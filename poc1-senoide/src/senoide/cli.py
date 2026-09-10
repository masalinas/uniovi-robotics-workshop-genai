"""Módulo de interfaz de línea de comandos (CLI) para la generación de señales."""

import argparse

from matplotlib import colors as mcolors

from senoide.graficos import COLOR_DEFECTO, dibujar_senoide
from senoide.senal import AMPLITUD_DEFECTO, FRECUENCIA_DEFECTO, generar_senoide


def validar_positivo(valor_str: str) -> float:
    """Valida que un argumento sea un número float mayor que cero.

    Args:
        valor_str (str): El valor pasado por consola como cadena.

    Returns:
        float: El valor convertido a float.

    Raises:
        argparse.ArgumentTypeError: Si no es un número o es menor o igual a cero.
    """
    try:
        valor = float(valor_str)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{valor_str}' no es un número válido.")

    if valor <= 0:
        raise argparse.ArgumentTypeError(f"El valor debe ser mayor que cero, se recibió {valor}.")
    return valor


def validar_color(color_str: str) -> str:
    """Valida que un string represente un color válido en matplotlib.

    Args:
        color_str (str): El nombre del color a validar.

    Returns:
        str: El mismo string si es válido.

    Raises:
        argparse.ArgumentTypeError: Si el color no es reconocido por matplotlib.
    """
    # is_color_like comprueba de forma robusta si matplotlib sabe interpretar este string
    if not mcolors.is_color_like(color_str):
        raise argparse.ArgumentTypeError(
            f"'{color_str}' no es un color válido reconocido por matplotlib."
        )
    return color_str


def parsear_argumentos(args: list[str] | None = None) -> argparse.Namespace:
    """Configura y parsea los argumentos de línea de comandos.

    Args:
        args (list[str] | None): Lista de argumentos. Si es None, usa sys.argv.

    Returns:
        argparse.Namespace: Un objeto con los argumentos parseados.
    """
    parser = argparse.ArgumentParser(
        description="Genera y guarda una gráfica de una señal senoidal."
    )

    parser.add_argument(
        "--amplitud",
        type=validar_positivo,
        default=AMPLITUD_DEFECTO,
        help=f"Amplitud de la señal senoidal (por defecto: {AMPLITUD_DEFECTO})",
    )

    parser.add_argument(
        "--frecuencia",
        type=validar_positivo,
        default=FRECUENCIA_DEFECTO,
        help=f"Frecuencia de la señal en Hz (por defecto: {FRECUENCIA_DEFECTO})",
    )

    parser.add_argument(
        "--color",
        type=validar_color,
        default=COLOR_DEFECTO,
        help=f"Color de la línea en matplotlib (por defecto: '{COLOR_DEFECTO}')",
    )

    return parser.parse_args(args)


def main() -> None:
    """Punto de entrada principal de la aplicación CLI."""
    argumentos = parsear_argumentos()

    # 1. Generamos la matemática (sin efectos secundarios gráficos)
    t, y = generar_senoide(amplitud=argumentos.amplitud, frecuencia=argumentos.frecuencia)

    # 2. Dibujamos y guardamos la gráfica
    dibujar_senoide(t, y, color=argumentos.color)


if __name__ == "__main__":
    main()
