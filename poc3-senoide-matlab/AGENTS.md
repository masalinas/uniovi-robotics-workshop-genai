# AGENTS.md — PoC3: Python interactuando con MATLAB (señal senoidal)

Guía de comportamiento para agentes generativos en este repositorio. Tercera PoC del taller:
repite el ejercicio de la señal senoidal de la PoC1, pero delegando el cálculo y/o el dibujo
en MATLAB desde Python, para mostrar cómo un agente puede orquestar herramientas externas.

## 1. Contexto del proyecto

Script Python que genera los parámetros de una señal senoidal (amplitud, frecuencia, color)
y utiliza MATLAB como motor de cálculo y/o de representación gráfica, en vez de matplotlib.
El objetivo didáctico es distinto al de la PoC1: aquí el agente debe razonar sobre la
integración entre dos entornos distintos, no solo sobre Python puro.

## 2. Antes de generar nada: aclarar el mecanismo de integración

Existen varias formas legítimas de conectar Python con MATLAB; **el agente debe preguntar o
detectar cuál aplica antes de escribir código**, en vez de asumir una por defecto, porque
cada una cambia por completo la estructura del proyecto:

1. **MATLAB Engine API for Python** (`matlab.engine`): requiere una instalación de MATLAB
   local con el paquete `matlabengine` instalado vía pip, y la versión de MATLAB debe ser
   compatible con la versión de Python usada. Es la opción más directa para llamar funciones
   `.m` desde Python en el mismo proceso.
2. **Invocación por línea de comandos**: Python lanza `matlab -batch "script"` con
   `subprocess`, y MATLAB escribe resultados a fichero (p. ej. `.mat`, `.csv`, imagen `.png`)
   que Python lee después. Útil si no se quiere/puede instalar `matlabengine`.
3. **MATLAB Compiler / MATLAB Runtime**: para producción, fuera del alcance de una PoC de
   taller salvo que el usuario lo pida explícitamente.

Si el usuario no lo ha especificado, el agente debe preguntarlo explícitamente o, si no
puede preguntar, documentar en el README la opción elegida y por qué, y dejar claro cómo
cambiar a otra estrategia.

## 3. Estructura de carpetas esperada (asumiendo opción 1, Engine API)

```
poc3-senoide-matlab/
├── AGENTS.md
├── README.md
├── pyproject.toml
├── matlab/
│   └── generar_senoide.m       # función MATLAB: parámetros → vectores t, y (+ plot)
├── src/
│   └── senoide_matlab/
│       ├── __init__.py
│       ├── parametros.py       # validación de amplitud/frecuencia/color en Python
│       └── puente_matlab.py    # capa de integración: arranca engine, llama a la función .m
└── tests/
    ├── test_parametros.py
    └── test_puente_matlab.py   # tests que MOCKEAN el engine de MATLAB
```

## 4. Reglas de código — lado Python

- Type hints y docstrings igual que en la PoC1.
- **Aísla la dependencia de MATLAB en un único módulo** (`puente_matlab.py`). El resto del
  código Python no debe importar `matlab.engine` directamente; así el proyecto sigue siendo
  testeable sin MATLAB instalado.
- La validación de parámetros (amplitud > 0, frecuencia > 0, color válido) vive en Python
  puro (`parametros.py`), no dentro de la función `.m`, para poder testearla sin arrancar
  MATLAB.
- Gestiona explícitamente el ciclo de vida del engine de MATLAB (arranque y cierre), y
  documenta que arrancarlo es lento (varios segundos) — no lo hagas en cada llamada si el
  script va a invocar la función varias veces.
- Captura y traduce los errores de MATLAB a excepciones Python claras (no dejes que un error
  de MATLAB se propague como un traceback críptico sin contexto).

## 5. Reglas de código — lado MATLAB

- La función `.m` debe ser pura en la medida de lo posible: recibe amplitud, frecuencia y
  color, devuelve los vectores `t` e `y`, y opcionalmente dibuja si se le pasa un flag
  (`generar_senoide(amplitud, frecuencia, color, mostrarGrafico)`).
- Comentarios en cabecera de la función `.m` describiendo entradas, salidas y un ejemplo de
  uso (convención estándar de ayuda de MATLAB, accesible con `help`).
- Nombres de variables en MATLAB siguiendo camelCase (convención habitual de MATLAB),
  aunque el resto del proyecto use snake_case en Python — no fuerces un único estilo entre
  ambos lenguajes, respeta la convención idiomática de cada uno.

## 6. Testing

- Los tests Python de `parametros.py` no requieren MATLAB y deben poder correr en CI sin
  problema.
- Los tests de `puente_matlab.py` **mockean** el engine de MATLAB (p. ej. con
  `unittest.mock`) para comprobar que se llama a la función `.m` con los argumentos
  correctos, sin necesitar una instalación real de MATLAB en la máquina que ejecuta los
  tests.
- Si se dispone de MATLAB en la máquina de desarrollo, añade un test de integración aparte,
  marcado explícitamente (p. ej. `@pytest.mark.matlab`) y excluido por defecto de la
  ejecución normal de `pytest`.

## 7. Qué NO debe hacer el agente

- No asumas que MATLAB está instalado en el entorno donde se ejecutan los tests por defecto.
- No mezcles lógica de validación de parámetros dentro del código `.m` si ya existe en
  Python (evita duplicar la misma regla en dos lenguajes).
- No generes rutas absolutas al ejecutable de MATLAB hardcodeadas; usa configuración
  (variable de entorno o fichero de configuración) para la ruta si hace falta.
- No optes silenciosamente por la opción "invocación por línea de comandos" sin dejar
  constancia de por qué, si el usuario no la pidió expresamente.

## 8. Al terminar cada tarea

Indica: qué opción de integración con MATLAB se ha usado, qué hay que instalar para
reproducirlo (MATLAB + toolbox si aplica, `matlabengine` vía pip), cómo correr el script y
cómo correr los tests que no requieren MATLAB.
