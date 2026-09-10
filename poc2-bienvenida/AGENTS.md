# AGENTS.md — PoC2: Monorepo FastAPI (backend) + Angular (frontend)

Guía de comportamiento para agentes generativos (Antigravity, Claude Code, etc.) en este
repositorio. Segunda PoC del taller de iniciación a la IA Generativa: introduce la
complejidad de coordinar un backend y un frontend que se comunican entre sí, dentro de un
único repositorio.

## 1. Contexto del proyecto

Monorepo con dos aplicaciones independientes que se comunican por HTTP:

- **Backend**: FastAPI con un único endpoint que recibe un texto (p. ej. un nombre) y
  devuelve un mensaje de bienvenida.
- **Frontend**: Angular con un formulario simple (un campo de texto y un botón) que llama al
  backend y muestra el resultado en pantalla.

Es intencionadamente sencillo a nivel funcional; el valor del ejercicio está en que el
agente estructure bien la comunicación cliente-servidor, el contrato de la API y el manejo
de errores/estados de carga en el frontend.

## 2. Rol del agente

Actúa como arquitecto full-stack: alguien que diseña primero el contrato de la API (qué
entra, qué sale, qué códigos de error) y después implementa cada lado de forma consistente
con ese contrato. No mezcles responsabilidades entre capas.

## 3. Estructura del monorepo

```
poc2-bienvenida/
├── AGENTS.md
├── README.md
├── backend/
│   ├── pyproject.toml
│   ├── src/
│   │   └── app/
│   │       ├── __init__.py
│   │       ├── main.py            # creación de la app FastAPI, CORS, routers
│   │       ├── api/
│   │       │   └── bienvenida.py  # router con el endpoint /api/bienvenida
│   │       ├── schemas.py         # modelos Pydantic (request/response)
│   │       └── core/
│   │           └── config.py      # settings (orígenes CORS permitidos, etc.)
│   └── tests/
│       └── test_bienvenida.py
└── frontend/
    ├── angular.json
    ├── package.json
    └── src/
        └── app/
            ├── app.config.ts
            ├── app.component.ts
            ├── core/
            │   └── services/
            │       └── bienvenida.service.ts   # llamada HTTP al backend
            └── features/
                └── bienvenida/
                    ├── bienvenida.component.ts
                    ├── bienvenida.component.html
                    ├── bienvenida.component.scss
                    └── bienvenida.component.spec.ts
```

## 4. Backend (FastAPI)

- Python 3.11+, FastAPI + Pydantic v2, `uvicorn` como servidor de desarrollo.
- **Contrato de la API primero**: define en `schemas.py` un `BienvenidaRequest` (campo
  `nombre: str`, con validación de longitud mínima) y un `BienvenidaResponse` (campo
  `mensaje: str`). El endpoint es `POST /api/bienvenida`.
- El router no contiene lógica de negocio si esta crece; para este caso tan simple, la
  construcción del mensaje puede vivir en el propio router o en una función pura separada
  (`construir_mensaje(nombre: str) -> str`) que sea fácil de testear de forma aislada.
- CORS configurado explícitamente en `core/config.py` para permitir el origen del frontend
  Angular en desarrollo (p. ej. `http://localhost:4200`); nunca uses `allow_origins=["*"]`
  en el ejemplo, aunque sea una PoC — es una oportunidad para enseñar buenas prácticas.
- Documenta el endpoint con `summary` y `description` en el decorador de FastAPI; esto genera
  Swagger/OpenAPI automáticamente, útil para que el agente y el usuario prueben el backend
  sin necesidad del frontend.
- Type hints en todo el código; docstrings en funciones no triviales.
- Tests con `pytest` + `httpx`/`TestClient` de FastAPI: al menos un test de caso feliz y uno
  de validación (nombre vacío → 422).

## 5. Frontend (Angular)

- Angular 18+ con **componentes standalone** (evita NgModules salvo que el usuario pida lo
  contrario) y `HttpClient` inyectado con `inject()`.
- Un servicio dedicado (`bienvenida.service.ts`) encapsula la llamada HTTP; el componente
  nunca llama a `HttpClient` directamente.
- Usa **signals** para el estado del componente (texto introducido, mensaje recibido, estado
  de carga, error) en vez de variables sueltas o `BehaviorSubject` manual, salvo que el
  usuario prefiera RxJS explícitamente.
- Maneja explícitamente tres estados en la vista: inicial, cargando y error (p. ej. backend
  no disponible) — no solo el camino feliz.
- Tipa la respuesta del backend con una interfaz TypeScript que refleje exactamente el
  `BienvenidaResponse` de Pydantic (mantén ambos contratos sincronizados).
- URL del backend configurable vía `environment.ts` / `environment.development.ts`, nunca
  hardcodeada dentro del componente o el servicio.
- Tests con Jasmine/Karma (o Jest si el proyecto ya está migrado): al menos un test del
  servicio (mockeando `HttpClient` con `HttpTestingController`) y uno del componente
  (comprobando que se muestra el mensaje tras una respuesta simulada).

## 6. Convenciones comunes a ambas capas

- Comentarios explican el *porqué*, no repiten el *qué* (mismo criterio que en la PoC1).
- Nombres de variables, endpoints y campos de la API en **español o inglés, pero
  consistentes** en todo el monorepo (elige uno al principio y avisa si detectas mezcla).
- Ningún secreto ni URL de producción hardcodeada en el código.
- Linting: `ruff` en el backend, ESLint + Prettier en el frontend. El agente debe dejar el
  código pasando ambos linters antes de darlo por terminado.

## 7. Qué NO debe hacer el agente

- No mezcles lógica de negocio del backend dentro del frontend (ni al revés).
- No generes autenticación, base de datos ni persistencia: el endpoint es sin estado.
- No uses `any` en TypeScript salvo justificación explícita en comentario.
- No dupliques la definición del contrato de datos sin dejar claro dónde vive la fuente de
  verdad (aquí: los schemas Pydantic del backend).

## 8. Al terminar cada tarea

Indica claramente:
1. Cómo levantar el backend (`uvicorn app.main:app --reload`, puerto por defecto).
2. Cómo levantar el frontend (`ng serve`, puerto por defecto) y que apunte al backend.
3. Cómo correr los tests de cada lado.
4. Si has tocado el contrato de la API, resáltalo para que el otro lado se actualice.
