---
name: api-contract-sync
description: Mantiene sincronizado el contrato de datos entre los schemas Pydantic del backend FastAPI y las interfaces TypeScript del frontend Angular. Úsala siempre que se cree o modifique un endpoint, un modelo Pydantic, o una interfaz TypeScript que represente una petición/respuesta de la API en este monorepo.
---

# Sincronización del contrato Backend (Pydantic) ↔ Frontend (TypeScript)

## Cuándo usar esta skill

- Al crear un endpoint nuevo en `backend/src/app/api/`.
- Al modificar cualquier `BaseModel` de Pydantic en `backend/src/app/schemas.py`.
- Al tocar cualquier interfaz TypeScript en `frontend/src/app/**` que represente el body de
  una petición o el shape de una respuesta HTTP.

## Regla de oro

**La fuente de verdad del contrato son los schemas Pydantic del backend.** Cualquier cambio
ahí debe reflejarse en la interfaz TypeScript correspondiente, y viceversa nunca: no cambies
primero el TypeScript "porque es más rápido" y luego el backend.

## Procedimiento

1. Antes de tocar un endpoint, localiza el schema Pydantic (`Request`/`Response`) y la
   interfaz TypeScript equivalente en el `service` del frontend.
2. Si cambias un campo en el schema Pydantic (nombre, tipo, opcionalidad):
   - Actualiza la interfaz TypeScript con el mismo nombre y tipo equivalente
     (`str` → `string`, `int`/`float` → `number`, `bool` → `boolean`,
     `Optional[X]` → `X | undefined` o `?: X`).
   - Revisa el `.spec.ts` del componente/servicio afectado y actualiza los mocks de
     respuesta si hace falta.
   - Revisa el test de FastAPI (`test_bienvenida.py`) y actualiza el payload esperado.
3. Si el cambio es incompatible (p. ej. renombrar un campo), indícalo explícitamente al
   usuario al terminar la tarea: "he cambiado el contrato de la API, revisa ambos lados".
4. Nunca dupliques la definición de validación (p. ej. longitud mínima de un string) en el
   frontend Y en el backend con valores distintos; si hace falta validarlo en ambos sitios
   por UX, deja el mismo valor en los dos y coméntalo.

## Señal de alarma

Si al terminar una tarea el nombre de un campo en `schemas.py` no coincide con el nombre
usado en la interfaz TypeScript del frontend, la tarea no está completa.
