---
name: pytest-conventions
description: Guía para escribir tests con pytest de funciones numéricas puras (generación de señales, cálculos con numpy). Úsala al crear o revisar tests en este proyecto, especialmente en tests/test_senal.py.
---

# Convenciones de testing para código numérico con pytest

## Cuándo usar esta skill

- Al añadir una función nueva a `senal.py` (o similar) que haya que testear.
- Al revisar si los tests existentes cubren casos límite (parámetros inválidos, valores
  extremos).

## Cómo escribir los tests

1. **Un test por comportamiento, no por función.** Si `generar_senoide` tiene tres
   comportamientos relevantes (forma del array, valor en `t=0`, validación de amplitud
   negativa), son tres tests, no uno con múltiples asserts sin relación.
2. **Usa `pytest.mark.parametrize`** para cubrir varias combinaciones de amplitud/frecuencia
   sin duplicar código de test.
3. **Comparaciones numéricas con `pytest.approx` o `numpy.testing.assert_allclose`**, nunca
   `==` directo sobre floats.
4. **Nombres de test descriptivos**: `test_amplitud_negativa_lanza_valueerror`, no
   `test_caso_2`.
5. **Los tests no deben abrir ventanas gráficas.** Si una función importa `matplotlib`,
   verifica que el test solo comprueba los datos devueltos, no el render.

## Ejemplo mínimo

```python
import numpy as np
import pytest

from senoide.senal import generar_senoide


@pytest.mark.parametrize("amplitud,frecuencia", [(1.0, 1.0), (2.5, 3.0)])
def test_amplitud_maxima_coincide_con_parametro(amplitud, frecuencia):
    t, y = generar_senoide(amplitud=amplitud, frecuencia=frecuencia)
    assert np.max(y) == pytest.approx(amplitud, rel=1e-6)


def test_amplitud_negativa_lanza_valueerror():
    with pytest.raises(ValueError):
        generar_senoide(amplitud=-1.0, frecuencia=1.0)
```

## Qué evitar

- Tests que dependan del orden de ejecución de otros tests.
- Fixtures compartidas innecesarias para un módulo tan pequeño: mejor argumentos directos.
