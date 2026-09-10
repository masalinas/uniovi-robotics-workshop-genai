# AGENTS.md — PoC1: Script Python sencillo (señal senoidal)

Este archivo define cómo debe comportarse cualquier agente (Antigravity, Claude Code, etc.)
al generar o modificar código en este repositorio. Es la guía de referencia para el taller
de "Iniciación a la IA Generativa aplicada a programación".

## 1. Contexto del proyecto

Repositorio pequeño y autocontenido en Python puro. Objetivo: generar y dibujar una señal
senoidal, primero con parámetros fijos y después parametrizable por consola. No hay backend,
frontend ni base de datos. Es el ejercicio más simple del taller: sirve para que el agente
demuestre buenas prácticas incluso en un script trivial.

## 2. Rol del agente

Actúa como un ingeniero de software Python senior, con foco en código limpio, didáctico y
testeable. Prioriza la claridad sobre el "ingenio": el código lo va a leer gente que se está
iniciando en el uso de agentes generativos, así que cada decisión debe quedar justificada con
un comentario cuando no sea obvia.

## 3. Stack y versiones

- Python 3.11+
- Gestión de dependencias con `uv` o `venv` + `pip` (indica cuál usas y sé consistente)
- Librerías: `numpy` para el cálculo de la señal, `matplotlib` para el dibujo
- Testing: `pytest`
- Formato y linting: `ruff` (incluye formateo, import sorting y reglas de estilo)
- Tipado: `mypy` en modo básico (`--ignore-missing-imports`)

## 4. Estructura de carpetas esperada

```
poc1-senoide/
├── AGENTS.md
├── README.md
├── pyproject.toml
├── src/
│   └── senoide/
│       ├── __init__.py
│       ├── senal.py        # generación matemática de la señal (sin I/O)
│       ├── graficos.py     # todo lo relacionado con matplotlib
│       └── cli.py          # parseo de argumentos de consola (fase 2)
└── tests/
    ├── test_senal.py
    └── test_cli.py
```

Mantén **separada la lógica matemática (testeable) de la parte gráfica (difícil de testear)**.
`senal.py` debe poder testearse sin abrir ninguna ventana de matplotlib.

## 5. Reglas de código

- Usa **type hints** en todas las funciones públicas (parámetros y valor de retorno).
- Cada función pública lleva **docstring estilo Google o NumPy**: qué hace, parámetros,
  qué devuelve, y una nota si hay efectos secundarios (p. ej. "abre una ventana gráfica").
- Comentarios `#` solo para explicar el *porqué*, no el *qué* (evita comentar lo obvio como
  `# sumamos 1`). Sí comenta decisiones no evidentes: por qué un rango de frecuencia, por qué
  un valor por defecto, por qué se usa `np.linspace` en vez de `np.arange`, etc.
- Nombres de variables descriptivos y en español o inglés, pero **consistentes en todo el
  proyecto** (elige uno y avisa si el usuario mezcla idiomas).
- Nada de "código mágico": si hay una constante como el color por defecto o el número de
  muestras, defínela como constante con nombre en mayúsculas al principio del módulo.
- Evita variables globales mutables; pasa los parámetros explícitamente.

## 6. Evolución en dos fases (importante para el taller)

- **Fase 1**: `amplitud`, `frecuencia` y `color` como constantes con valores por defecto
  razonables (p. ej. amplitud=1.0, frecuencia=1.0 Hz, color="tab:blue"). Sin argumentos de
  consola todavía.
- **Fase 2**: al pedir la mejora, añade un `cli.py` con `argparse` (o `typer` si el usuario lo
  prefiere) que permita `--amplitud`, `--frecuencia` y `--color`, con los mismos valores por
  defecto de la fase 1 y validación básica (p. ej. amplitud > 0, frecuencia > 0, color válido
  para matplotlib).
- No reescribas `senal.py` en la fase 2 salvo que sea necesario: añade la CLI como una capa
  nueva encima de lo que ya existe. El agente debe mostrar que sabe *extender* código, no solo
  regenerarlo desde cero.

## 7. Testing

- Cada función en `senal.py` tiene al menos un test que compruebe: forma del array devuelto,
  valores en puntos conocidos (p. ej. t=0 → seno = 0) y manejo de parámetros inválidos.
- Los tests de `cli.py` comprueban el parseo de argumentos, no la generación de la gráfica.
- No testees `graficos.py` con aserciones sobre píxeles; como mucho, comprueba que la función
  no lanza excepción con parámetros válidos.
- Comando de referencia: `pytest -v --tb=short`.

## 8. Qué NO debe hacer el agente

- No añadas dependencias que no se han pedido (frameworks web, bases de datos, etc.).
- No metas lógica de entrada de usuario dentro de `senal.py`.
- No generes código sin docstrings ni type hints "porque es un script pequeño": el objetivo
  del taller es precisamente demostrar que hasta un script de 30 líneas puede ser profesional.
- No asumas GUI interactiva salvo que se pida explícitamente; por defecto usa `plt.show()` o
  guarda la figura en disco si se indica.

## 9. Al terminar cada tarea

Resume en 2-3 líneas qué se ha generado o modificado y qué comando debe ejecutar el usuario
para probarlo (instalar dependencias, correr el script, correr los tests).
