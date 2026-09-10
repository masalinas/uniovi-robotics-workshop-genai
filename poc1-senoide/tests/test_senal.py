"""Tests para el módulo senal."""

import numpy as np
import pytest

from senoide.senal import NUM_MUESTRAS, generar_senoide


def test_generar_senoide_shape():
    """Comprueba que los arrays devueltos tienen la forma esperada."""
    t, y = generar_senoide()
    assert t.shape == (NUM_MUESTRAS,)
    assert y.shape == (NUM_MUESTRAS,)


def test_generar_senoide_valores_conocidos():
    """Comprueba que la señal pasa por puntos conocidos matemáticamente."""
    t, y = generar_senoide(amplitud=1.0, frecuencia=1.0)

    # En t=0, sen(0) = 0
    assert np.isclose(y[0], 0.0)

    # En t=0.25 (un cuarto de ciclo para 1Hz), el valor debe ser la amplitud máxima
    idx_025 = np.argmin(np.abs(t - 0.25))
    assert np.isclose(y[idx_025], 1.0)

    # En t=0.5 (medio ciclo), el valor debe ser 0
    # Al usar 1000 muestras, t=0.5 exacto puede no existir, así que usamos una tolerancia mayor
    # o comparamos con el valor esperado para ese t específico.
    idx_05 = np.argmin(np.abs(t - 0.5))
    valor_esperado_05 = np.sin(2 * np.pi * t[idx_05])
    assert np.isclose(y[idx_05], valor_esperado_05)


def test_generar_senoide_parametros_invalidos():
    """Comprueba que se lanzan excepciones con parámetros inválidos."""
    with pytest.raises(ValueError, match="La amplitud debe ser mayor que cero"):
        generar_senoide(amplitud=0)

    with pytest.raises(ValueError, match="La frecuencia debe ser mayor que cero"):
        generar_senoide(frecuencia=-1.0)
