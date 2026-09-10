"""Tests para el módulo de línea de comandos."""

import argparse

import pytest

from senoide.cli import parsear_argumentos, validar_color, validar_positivo
from senoide.graficos import COLOR_DEFECTO
from senoide.senal import AMPLITUD_DEFECTO, FRECUENCIA_DEFECTO


def test_parsear_argumentos_por_defecto():
    """Comprueba que si no se pasan argumentos, se usan los de por defecto."""
    args = parsear_argumentos([])
    assert args.amplitud == AMPLITUD_DEFECTO
    assert args.frecuencia == FRECUENCIA_DEFECTO
    assert args.color == COLOR_DEFECTO


def test_parsear_argumentos_personalizados():
    """Comprueba el correcto parseo de argumentos válidos dados por el usuario."""
    args = parsear_argumentos(["--amplitud", "3.5", "--frecuencia", "2.0", "--color", "red"])
    assert args.amplitud == 3.5
    assert args.frecuencia == 2.0
    assert args.color == "red"


def test_validar_positivo_valido():
    """Comprueba que un número válido mayor a cero es convertido correctamente."""
    assert validar_positivo("2.5") == 2.5
    assert validar_positivo("10") == 10.0


def test_validar_positivo_invalido():
    """Comprueba que saltan errores si el valor no es válido o es <= 0."""
    with pytest.raises(argparse.ArgumentTypeError, match="debe ser mayor que cero"):
        validar_positivo("-1.0")

    with pytest.raises(argparse.ArgumentTypeError, match="debe ser mayor que cero"):
        validar_positivo("0")

    with pytest.raises(argparse.ArgumentTypeError, match="no es un número válido"):
        validar_positivo("texto")


def test_validar_color_invalido():
    """Comprueba que saltan errores si el color no existe en matplotlib."""
    with pytest.raises(argparse.ArgumentTypeError, match="no es un color válido"):
        validar_color("color_inventado")


def test_parsear_argumentos_errores_integracion():
    """Comprueba que parsear_argumentos aborta la ejecución con parámetros inválidos.

    argparse hace exit() cuando falla la validación desde línea de comandos,
    por lo que debemos atrapar la excepción SystemExit.
    """
    with pytest.raises(SystemExit):
        parsear_argumentos(["--amplitud", "-5"])
