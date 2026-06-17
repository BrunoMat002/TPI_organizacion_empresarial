# TPI_organizacion_empresarial
Este proyecto consiste en la automatización del proceso de solicitud y gestión de licencias anuales ordinarias (vacaciones) para el personal técnico y administrativo de **FO-NET S.A.** (empresa dedicada al despliegue y mantenimiento de redes de fibra óptica). 

La solución implementa una interfaz conversacional por línea de comandos (CLI) desarrollada en Python, totalmente alineada con un modelado formal de procesos de negocio bajo el estándar **BPMN 2.0**.

## 📌 Características Principales

- **Arquitectura Modular:** Desarrollo estructurado basado en funciones específicas para la carga de datos, persistencia e interfaz de usuario.
- **Máquina de Estados:** Control estricto del flujo conversacional mediante estados secuenciales (`ESPERANDO_LEGAJO`, `ESPERANDO_DIAS`, `ESPERANDO_FECHA`).
- **Validación y Robustez (Camino Infeliz):** Captura controlada de excepciones (`try-except`) ante formatos de fecha inválidos, datos no numéricos o ingresos erróneos, evitando caídas catastróficas.
- **Validación de Reglas de Negocio:** Verificación en tiempo real del saldo disponible del empleado antes de procesar cualquier solicitud.
- **Persistencia en CSV:** Actualización automática y segura de los registros en un archivo plano externo (`empleados.csv`) al concluir exitosamente el trámite.

## 🗺️ Modelado del Proceso (BPMN 2.0)

El flujo conversacional está estructurado formalmente dividiendo las responsabilidades en dos carriles (*Lanes*) principales dentro del contenedor de la organización:
1. **USUARIO:** Técnico de campo o empleado que interactúa ingresando sus requerimientos.
2. **BOT:** Asistente virtual encargado de validar la identidad, consultar saldos, verificar fechas y actualizar el sistema.

---
