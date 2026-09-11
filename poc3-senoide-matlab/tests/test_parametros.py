import pytest
from senoide_matlab.parametros import validar_parametros

def test_validar_parametros_validos():
    # No debería lanzar excepción
    validar_parametros(amplitud=1.0, frecuencia=2.0, color='r')

def test_amplitud_invalida():
    with pytest.raises(ValueError, match="La amplitud debe ser mayor que 0"):
        validar_parametros(amplitud=0.0, frecuencia=2.0, color='b')

def test_frecuencia_invalida():
    with pytest.raises(ValueError, match="La frecuencia debe ser mayor que 0"):
        validar_parametros(amplitud=1.5, frecuencia=-1.0, color='g')

def test_color_invalido():
    with pytest.raises(ValueError, match="El color 'x' no es válido"):
        validar_parametros(amplitud=1.5, frecuencia=2.0, color='x')
