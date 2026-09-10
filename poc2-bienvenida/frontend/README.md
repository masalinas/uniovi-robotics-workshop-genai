# Frontend PoC2 - Bienvenida

## Descripción
Este es el frontend de la Prueba de Concepto 2 (PoC2), desarrollado en Angular. Consiste en un formulario que permite al usuario introducir su nombre, realizar una petición HTTP al backend y mostrar un mensaje de bienvenida. La aplicación ilustra el manejo de estados reactivos (cargando, éxito, error) utilizando Signals y componentes Standalone, sin utilizar la estructura clásica de NgModules.

## Dependencias
El proyecto utiliza **Node.js** y **Angular CLI** con las siguientes tecnologías principales:
- **[Angular 18+](https://angular.dev/):** Framework web, utilizando las funcionalidades más modernas (Standalone Components y Signals).
- **[RxJS](https://rxjs.dev/):** Utilizado de forma interna por el `HttpClient` de Angular para las llamadas asíncronas HTTP.
- **[SCSS](https://sass-lang.com/):** Preprocesador de CSS utilizado para los estilos locales del componente de bienvenida.
- **Dependencias de Desarrollo:** `Jasmine` y `Karma` para los tests unitarios, además de `ESLint` y `Prettier` para asegurar la consistencia y formato automático del código.

## Árbol de Carpetas y Ficheros
A continuación se muestra el árbol de archivos relevantes (sin contar configuraciones base generadas por Angular):
```text
frontend/
├── angular.json           # Configuración del workspace de Angular CLI
├── package.json           # Dependencias y scripts de Node
├── tsconfig.json          # Configuración de TypeScript
└── src/
    ├── main.ts            # Punto de entrada de la aplicación
    ├── environments/      # Variables de entorno (apuntan a http://127.0.0.1:8001/api)
    │   ├── environment.ts
    │   └── environment.development.ts
    └── app/
        ├── app.config.ts  # Proveedores globales (ej. provideHttpClient)
        ├── app.component.ts   # Componente raíz de la app
        ├── core/
        │   ├── models/    # Interfaces TypeScript (contrato de datos)
        │   └── services/  # Lógica de comunicación con el Backend (bienvenida.service.ts)
        └── features/
            └── bienvenida/# Componente visual del formulario de saludo (.ts, .html, .scss)
```

## Enlaces de Referencia
- [Angular.dev (Nueva Documentación Oficial)](https://angular.dev/)
- [Angular Signals Guide](https://angular.dev/guide/signals)
- [Guía del HttpClient en Angular](https://angular.dev/guide/http)
- [Documentación de SCSS/Sass](https://sass-lang.com/documentation/)
