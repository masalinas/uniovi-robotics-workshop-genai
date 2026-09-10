---
name: matlab-bridge-safety
description: Guía para integrar Python con MATLAB de forma segura y testeable (vía matlab.engine o subprocess). Úsala al crear o modificar puente_matlab.py, al llamar a funciones .m desde Python, o al decidir cómo testear código que depende de MATLAB.
---

# Integración Python ↔ MATLAB, de forma segura y testeable

## Cuándo usar esta skill

- Al escribir o modificar `puente_matlab.py` (o cualquier módulo que importe
  `matlab.engine` o lance `subprocess` contra el ejecutable de `matlab`).
- Al decidir si un test necesita MATLAB instalado o puede mockearse.
- Al depurar un error que viene de MATLAB y llega a Python como una excepción opaca.

## Reglas

1. **Un único punto de entrada a MATLAB.** Todo el código que hable con MATLAB (arrancar el
   engine, invocar la función `.m`, cerrarlo) vive en un módulo dedicado. Ningún otro módulo
   importa `matlab.engine` directamente.
2. **Nunca lances el engine de MATLAB dentro de un bucle o de cada llamada a la función.**
   Arrancarlo cuesta varios segundos; documenta y reutiliza una única instancia por ejecución
   del script.
3. **Valida los parámetros en Python antes de llamar a MATLAB.** No dejes que un valor
   inválido (amplitud negativa, color no reconocido) llegue a MATLAB para que falle allí;
   MATLAB debe recibir siempre entradas ya validadas.
4. **Traduce los errores.** Envuelve las llamadas al engine en un `try/except` que capture
   las excepciones de MATLAB y las relance como una excepción Python propia y descriptiva
   (p. ej. `MatlabExecutionError`), nunca dejes pasar el traceback crudo de MATLAB sin
   contexto de qué operación estaba en curso.
5. **Comandos peligrosos requieren confirmación.** Lanzar el ejecutable de MATLAB por
   `subprocess` es una operación cara y con efectos secundarios (puede escribir ficheros,
   tarda en arrancar); no lo marques como comando "Allow" automático en la configuración de
   permisos del agente, déjalo en "Ask".

## Testing

- Los tests de la validación de parámetros (`parametros.py`) nunca necesitan MATLAB.
- Los tests del módulo puente **mockean** el engine (`unittest.mock.patch`) para comprobar
  que se llama a la función `.m` con los argumentos correctos — no arrancan MATLAB de
  verdad.
- Si añades un test de integración real con MATLAB, márcalo con `@pytest.mark.matlab` y
  regístralo en `pyproject.toml`/`pytest.ini` para poder excluirlo por defecto
  (`pytest -m "not matlab"`), tal y como está configurado en este proyecto.

## Ejemplo del patrón de mock

```python
from unittest.mock import MagicMock, patch


@patch("senoide_matlab.puente_matlab._arrancar_engine")
def test_llama_a_generar_senoide_con_los_parametros_correctos(mock_arrancar):
    mock_engine = MagicMock()
    mock_arrancar.return_value = mock_engine

    from senoide_matlab.puente_matlab import generar_senoide_via_matlab
    generar_senoide_via_matlab(amplitud=2.0, frecuencia=1.0, color="r")

    mock_engine.generar_senoide.assert_called_once_with(2.0, 1.0, "r", False, nargout=2)
```
