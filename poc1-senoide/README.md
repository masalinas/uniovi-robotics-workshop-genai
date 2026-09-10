# PoC1: Generador de Señal Senoidal

## Resumen del proyecto
Este es un proyecto autocontenido en Python puro desarrollado como parte del taller "Iniciación a la IA Generativa aplicada a programación". El objetivo principal del script es generar y visualizar una señal senoidal, permitiendo parametrizar características como la amplitud, la frecuencia y el color a través de la línea de comandos.

El enfoque del código es puramente didáctico y orientado a buenas prácticas: promueve un código limpio, testeable, tipado y con una clara separación entre la lógica matemática pura y la lógica de interfaz de usuario y gráfica.

## Dependencias
El proyecto requiere **Python 3.11 o superior**. Utiliza las siguientes librerías:

**Dependencias principales:**
- `numpy`: Para el cálculo eficiente y la generación matemática de la señal.
- `matplotlib`: Para el dibujado y representación gráfica de los datos.

**Dependencias de desarrollo:**
- `pytest`: Para realizar pruebas unitarias (testing).
- `ruff`: Para el linting, formateo y revisión de estilo del código.
- `mypy`: Para la comprobación estática de tipos.

Las dependencias están definidas dentro del archivo `pyproject.toml`.

## Estructura de carpetas y ficheros

```text
poc1-senoide/
├── AGENTS.md          # Instrucciones para el comportamiento de agentes de IA en el repositorio.
├── README.md          # Documentación del proyecto (este archivo).
├── pyproject.toml     # Definición de dependencias, meta-información y configuración de herramientas.
├── src/
│   └── senoide/
│       ├── __init__.py
│       ├── senal.py   # Lógica matemática (pura) para generar los datos de la señal.
│       ├── graficos.py# Funciones para generar la ventana gráfica con matplotlib.
│       └── cli.py     # Parseo de argumentos de línea de comandos (argparse) y punto de entrada.
└── tests/
    ├── test_senal.py  # Tests unitarios para la función de generación de la señal matemática.
    └── test_cli.py    # Tests unitarios para comprobar el comportamiento del parseo de comandos.
```

## Links de interés
- [Documentación Oficial de Python](https://docs.python.org/3/)
- [Documentación de NumPy](https://numpy.org/doc/stable/)
- [Documentación de Matplotlib](https://matplotlib.org/stable/index.html)
- [Documentación de pytest](https://docs.pytest.org/)
- [Documentación de Ruff](https://docs.astral.sh/ruff/)
- [Documentación de Mypy](https://mypy.readthedocs.io/en/stable/)
