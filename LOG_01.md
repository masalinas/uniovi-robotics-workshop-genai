# Descripción
Prompts utilizados a la hora de configurar los casos de uso para poder ser implementado de forma agentica por el agente antigravity de Google.

## Prompts
**Prompt_01**:

Tengo antigravity instalado y quiero generar un AGENTS.md para que los agentes me generen buen codigo en python y angular con buenas practicas, testeable y con buenos comentarios en todo momento. Este AGENTS.md sera utilizado para generar tres Pruebas de concepto en un taller sobre inicializacion a la programación generativa y el uso de la misma para codificar:

- Primera PoC: prueba de concepto en python que dibuje una senoide con su precuencia, amplitud y color por defecto. Despues le pedire al agente que mejore el script para que pueda meter la amplitud, frecuencia y color por consola como parámetro.

- Segunda PoC: prueba de concepto para que me haga un backend en fastapi con un solo endpoint que me de un mensaje de bienvenida pasándole un texto, mi nombre por ejemplo y un frontend en angular en donde pueda meter este texto, se conecte con el backend y me de el resultado en una vista. Este caso un poco mas complejo por tener front y back lo quiero implementar como un monorepo para el back y front.

- Tercer PoC: prueba de concepto para que pueda interactuar con matlab, en este caso quiero que me genere el mismo ejemplo de la senoide pero utizando matlab para pintarlo.

***Resultado**

Los tres AGENTS.md para cada proyecto.

**Prompt_02**:

Ok en mi caso voy a crear un repo comun llamado uniovi-robotics-workshop-genai y dentro de el tres subcarpertas cada una de ellas con el AGENTS.md creado por ti.

poc1-senoide
poc2-bienvenida
poc3-senoide-matlab

Para generar el codigo con antigravity tengo que abrir antigravity subcarpeta a subcarpeta o puedo abrirlo en la carpeta principal  uniovi-robotics-workshop-genai e ir generando codigo proyecto a proyecto. ¿Que opcion es mejor?

***Resultado**

Creo un repo comun llamado uniovi-robotics-workshop-genai y dentro de el las tres pruebas de concepto y copio el AGENTS.md de cada uno en su carpeta. Le pido al agente que lo revise todo.

**Prompt_03**:

Ok con estos PoC que te he pedido y has creado un AGENTS.md para cada uno de ellos que configuracion settings.json seria buena para cada uno de ellos. Algun skill que se pueda instalar, algun subagente que pueda ser util, alguna configuracion especial que sea util. date cuenta que estos proyectos van  aser publicados para que los alumnos puedan recuperarlos y es bueno que puedan ver como configura el agente, si hay alguna skill o subagente seria interesante si de puede aplicar en alguna de las tres PoCs, ¿que opinas?

***Resultado**

Ahora quiero ir un poco mas haya y le digo al agente que me cree una configuración del agente para cada prueba de concepto asi como un skill que el considera util para los tests. No hace nada para subagentes

**Prompt_04**:

Al final mi repo con todos los PoC creadas y fichero de memoria y configuracion quedan como ves, es correcto?

***Resultado**
Le pido finalmente que revide y o corija todas las configuraciones agenticas si fuera preciso. 

## Notas

- Este es el punto de partida a la hora de desarrollar todos los casod de uso con el agente antigravity localizado en la rama **master** del repo. Ha la hora de implementar los casos de uso se crea una nueva rama llamada **final-solution** en donde se utiliza la memoria, configuración y skills en cada caso de uso. 

- La memoria AGENTS.md es muy precisa y descriptiva al estilo SDD. Realmente SDD lo que hace es implementar esta memoria de forma desagregada en varios ficheros util en proyectos grandes y complejos donde toda la descripcion no puede estar en un nsolo fichero, en nuestro caso varias PoC es suficiente.