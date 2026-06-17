# TPI_organizacion_empresarial
Este proyecto consiste en la automatización del proceso de solicitud y gestión de licencias anuales ordinarias (vacaciones) para el personal técnico y administrativo de **FO-NET S.A.** (empresa dedicada al despliegue y mantenimiento de redes de fibra óptica). 

La solución implementa una interfaz conversacional por línea de comandos (CLI) desarrollada en Python, totalmente alineada con un modelado formal de procesos de negocio bajo el estándar **BPMN 2.0**.

##  Características Principales

- **Arquitectura Modular:** Desarrollo estructurado basado en funciones específicas para la carga de datos, persistencia e interfaz de usuario.
- **Máquina de Estados:** Control estricto del flujo conversacional mediante estados secuenciales (`ESPERANDO_LEGAJO`, `ESPERANDO_DIAS`, `ESPERANDO_FECHA`).
- **Validación y Robustez (Camino Infeliz):** Captura controlada de excepciones (`try-except`) ante formatos de fecha inválidos, datos no numéricos o ingresos erróneos, evitando caídas catastróficas.
- **Validación de Reglas de Negocio:** Verificación en tiempo real del saldo disponible del empleado antes de procesar cualquier solicitud.
- **Persistencia en CSV:** Actualización automática y segura de los registros en un archivo plano externo (`empleados.csv`) al concluir exitosamente el trámite.

## Modelado del Proceso (BPMN 2.0)

El flujo conversacional está estructurado formalmente dividiendo las responsabilidades en dos carriles (*Lanes*) principales dentro del contenedor de la organización:
1. **USUARIO:** Técnico de campo o empleado que interactúa ingresando sus requerimientos.
2. **BOT:** Asistente virtual encargado de validar la identidad, consultar saldos, verificar fechas y actualizar el sistema.

## Modo de Uso y Guía de Interacción

El programa simula el comportamiento de un chatbot corporativo a través de la consola de comandos. A continuación, se detalla cómo interactuar con el sistema paso a paso y qué esperar en cada etapa del flujo de trabajo:

### Paso 1: Inicio y Autenticación
Al iniciar el script, el sistema te dará la bienvenida y te solicitará tu identificación:
* **Qué hacer:** Ingresá un número de legajo válido que exista en el archivo `empleados.csv` (por ejemplo: `1001`).
* **Control de errores:** Si ingresás texto o un legajo que no existe, el sistema te mostrará un mensaje de error y te pedirá que lo intentes de nuevo sin romper el programa.

### Paso 2: Consulta de Saldo y Solicitud de Días
Una vez que el bot valide tu legajo, te saludará de forma personalizada con tu nombre y sector, informándote cuántos días de vacaciones tenés disponibles. Luego, te preguntará cuántos querés tomarte.
* **Qué hacer:** Ingresá la cantidad de días deseados como un número entero (por ejemplo: `5`).
* **Control de errores:** 
  - Si ingresás un número menor o igual a `0`, el bot te indicará que la cantidad debe ser válida.
  - Si solicitás más días de los que tenés disponibles, el bot rechazará la solicitud por saldo insuficiente y finalizará la sesión de forma segura.

### Paso 3: Definición de la Fecha de Inicio
Si tenés saldo suficiente, el bot pasará al último estado y te pedirá la fecha en la que querés arrancar tus vacaciones.
* **Qué hacer:** Escribí la fecha respetando estrictamente el formato de barras `DD/MM/AAAA` (por ejemplo: `15/10/2026`).
* **Control de errores:** Si errás el formato o ponés un mes inexistente (ej: formato con guiones o texto), el sistema te advertirá del error para que la ingreses correctamente.

### Paso 4: Procesamiento y Persistencia (Fin del Flujo)
Una vez ingresada la fecha correcta, el bot procesará la transacción automáticamente:
1. Restará los días solicitados de tu saldo en memoria.
2. Impactará el nuevo valor directamente reescribiendo el archivo `empleados.csv`.
3. Te mostrará en pantalla un resumen completo del trámite con el estado: **APROBADO AUTOMÁTICAMENTE**.

---
