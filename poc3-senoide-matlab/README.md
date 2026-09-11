# PoC3: Python interactuando con MATLAB (señal senoidal)

Este proyecto muestra cómo generar y visualizar los parámetros de una señal senoidal utilizando Python para la lógica/validación y MATLAB como motor de cálculo y representación gráfica.

## Estrategia de Integración

Se ha optado por utilizar la **Opción 1: MATLAB Engine API for Python** (`matlabengine`).

### ¿Por qué?
Esta opción permite llamar directamente a funciones `.m` desde Python en el mismo proceso, facilitando el paso de parámetros y la obtención de resultados sin tener que recurrir a la escritura/lectura de archivos intermedios, que sería necesario utilizando `subprocess`.

### Requisitos

Para que este proyecto funcione, necesitas:
1. Tener **MATLAB** instalado localmente.
2. Tener instalado el paquete `matlabengine` a través de `pip`, cuidando de que la versión del paquete coincida con la de tu instalación local de MATLAB (ej. `25.2.x` para R2025b).

## Estructura del Código

- **`matlab/generar_senoide.m`**: Función pura en MATLAB encargada del cálculo de la senoide y opcionalmente del dibujado.
- **`src/senoide_matlab/parametros.py`**: Validación de parámetros en Python puro (independiente de MATLAB).
- **`src/senoide_matlab/puente_matlab.py`**: Capa de integración donde se instancia el engine de MATLAB de forma perezosa (lazy) y se delega la ejecución, transformando además posibles errores.
- **`tests/`**: Suite de tests dividida entre los que no requieren MATLAB y los que simulan (mockean) o utilizan (integración) el engine.

## Uso

Para instalar el entorno y las dependencias (asumiendo que estás en un entorno virtual):

```bash
pip install -e .[dev]
```

*Nota: Hemos fijado en el `pyproject.toml` la versión de `matlabengine` a `>=25.2.0,<25.3.0` para que sea compatible con MATLAB R2025b.*

### Ejecutar Tests

Los tests unitarios principales mockean la dependencia de MATLAB o no la necesitan:

```bash
pytest -m "not matlab"
```

Si deseas correr el test de integración real (que sí arrancará MATLAB en background, tomando algunos segundos adicionales), ejecuta:

```bash
pytest -m "matlab"
```
