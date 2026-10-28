---
kaizen_dojo: "2026"
formato: "Entregable diario G2"
evidencia: "E3"
dia: 3
responsable_registro: "equipo"
estado: "PENDIENTE"
fecha: "2026-10-28"
revision_docente: "PENDIENTE"
---

# E3 · Día 3 — MEDIR Y APRENDER | Kaizen 1: ensayo, hipótesis y mejora

> **Regla:** sustituir los corchetes, registrar lo realmente observado y enlazar a evidencias del repositorio. **No inventar datos ni marcar pruebas no realizadas.** Los archivos del equipo resumen el trabajo compartido; las reflexiones y evidencias personales van en `participantes/<alias>/dias/E3.md`.

## 0 · Contexto de investigación de hoy

**Fecha/equipo/misión:** 2026-10-28 · Apolitos · M05 AMR ROS 2 (myAGV 2023 Pi Elephant Robotics)  
**Dōjō exacto:** Campus León, Edificio Choza, Taller Choza, Puesto: Pista  
**Versión de partida:** Commit SHA `e2a4b9f` (Tag: `v1-alpha-teleop-fail`)  
**Protocolo E2:** [`../../pruebas/protocolo.md`](../../pruebas/protocolo.md)

## 1 · Ruta del Día 3 (180 min)

| Actividad | Minutos | Evidencia a registrar |
|---|---:|---|
| Analizar un fallo real / demostración | 0–15 | Bloqueo E2: Impagación de movimiento por teclado en el robot myAGV al intentar mapear. |
| Diseño del experimento | 15–40 | Definición de hipótesis sobre conflicto de archivos en el workspace y prueba con nuevo nodo de teleop. |
| Diagnóstico del prototipo V1 | 40–80 | Inspección del paquete de teleoperación: se detectaron dos programas/scripts duplicados en la carpeta de teleop ejecutando rutas conflictivas. |
| Kaizen 1: cambio técnico | 80–125 | Limpieza del paquete de teleop, depuración de archivos redundantes y creación de un nuevo nodo personalizado de teleoperación (`custom_teleop_node.py`). |
| Reensayo equivalente | 125–160 | Pruebas de envío de comandos `cmd_vel` mediante el nuevo nodo y registro de respuesta del AMR en la pista. |
| Documentar, debatir, reflejar | 160–180 | Consolidación de logs de velocidad/movimiento, actualización de tabla comparativa y actualización de E3 personal. |

## 2 · Problema, hipótesis y trazabilidad

| Campo | Completar |
|---|---|
| Fallo / oportunidad de mejora observada (con evidencia) | El teclado no enviaba comandos `cmd_vel` al robot para iniciar el mapeo ([`../../logs/teleop_error.log`](../../logs/teleop_error.log)). Se identificó la presencia de dos scripts distintos en la carpeta de teleoperación, lo que generaba confusión en la ruta de ejecución de ROS 2. |
| Dónde se presenta y cuántas veces | Ocurrió en los 5 ensayos del Día 2 al intentar lanzar el nodo de teleoperación en la terminal de la Raspberry Pi. |
| Diagnóstico: causas alternativas que se consideraron | 1. Falla física/de puerto USB en el teclado.<br>2. Error de permisos en `/dev/input/`.<br>3. Duplicidad y conflicto de nombres de ejecutables en el entorno de ROS 2 / workspace (Causa confirmada). |
| Hipótesis contrastable: **si cambio X, espero que Y ocurra porque Z** | **Si** aislamos la carpeta de teleoperación eliminando el ejecutable duplicado y **creamos un nuevo nodo dedicado**, **esperamos que** las entradas del teclado sean leídas y convertidas correctamente en mensajes `geometry_msgs/msg/Twist`, **porque** se elimina la ambigüedad en el runtime de ROS 2 y se garantiza la publicación limpia en el tópico `/cmd_vel`. |
| Variable independiente que se modifica | Estructura del paquete de teleoperación (creación del nodo `custom_teleop_node.py` y eliminación de la duplicidad). |
| Métrica de resultado con unidad y criterio de mejora | Comandos de velocidad recibidos y ejecutados exitosamente por la base (conteo de respuestas $n$ de 5 corridas). Criterio de éxito: $\ge 4/5$ ejecuciones con movimiento físico responsivo. |
| Variables que se mantendrán iguales | Pista del dōjō Choza, nivel de carga de batería del myAGV, teclado USB de entrada, tasa de publicación de tópicos. |
| Ensayos requeridos y forma de muestreo | 5 corridas consecutivas de envío de comandos de dirección (`WASD` / flechas) en la pista. |
| Riesgo de sesgo/confusión y cómo se mitigará | Limpieza completa del workspace (`rm -rf build/ install/ log/`) y re-compilación con `colcon build` para evitar cachear ejecutables obsoletos. |
| Parada de seguridad / condición de aborto | Aborto inmediato por combinación `Ctrl+C` si el robot presenta movimientos erráticos o acelera sin control. |

## 3 · Colaboración y cambio técnico Kaizen 1

| Alias y alcance | Kata asociado (código o propio) | Qué cambió exactamente | Por qué | Código/CAD/commit y responsable de revisión | Validación de interfaz |
|---|---|---|---|---|---|
| @a00575141-bash | MS02 | K3 / Propio | Se eliminó el programa duplicado en la carpeta de teleop y se programó un nuevo nodo `custom_teleop_node.py` con mapeo explícito de teclas a `Twist`. | Para resolver el conflicto de ejecución en ROS 2 y asegurar la captura de eventos de teclado. | [`../../codigo/teleop/custom_teleop_node.py`](../../codigo/teleop/custom_teleop_node.py) (SHA: `f8c3d1e`) \| Rev: @a00574597 | Publicación correcta en `/cmd_vel` verificada mediante `ros2 topic echo`. |
| @a00574597 | MS01 | K2 | Actualización de los scripts de launch para direccionar al nuevo nodo de teleoperación. | Garantizar que el comando `ros2 launch` ejecute el nodo recién creado. | [`../../codigo/launch/mapping.launch.py`](../../codigo/launch/mapping.launch.py) \| Rev: @Ivanna0407 | Integración de lanzamiento probado. |
| @Ivanna0407 | AR10 | K1 | Mantenimiento y verificación del nodo de cámara durante las pruebas de movimiento. | Comprobar que la lectura de marcadores se mantenga estable con el robot en movimiento. | [`../../codigo/nodes/camera_reader.py`](../../codigo/nodes/camera_reader.py) \| Rev: @a00574830 | Transmisión de video continua. |
| @a00574830 | AR01 | K2 | Monitoreo y registro de tópicos de odometría (`/odom`) y LiDAR (`/scan`) durante el desplazamiento conducido. | Validar que los datos de la base se utilicen correctamente para el mapeo. | [`../../logs/kaizen1_topics.log`](../../logs/kaizen1_topics.log) \| Rev: @a00575141-bash | Tópicos respondiendo a frecuencia constante. |

**Identificador de versión K1:** Commit SHA `f8c3d1e` (Tag: `v1-kaizen1-teleop-fix`).  
**Otras modificaciones involuntarias o perturbaciones:** Ninguna; el entorno físico de la pista Choza y los componentes del robot mantuvieron la misma configuración que en E2.

## 4 · Ensayos comparables

**Enlace a datos crudos CSV:** [`../../datos/ensayos.csv`](../../datos/ensayos.csv) · **Protocolo:** [`../../pruebas/protocolo.md`](../../pruebas/protocolo.md).

| Prueba emparejada o bloque | Condición/escenario idéntico | V1, valor + unidad | K1, valor + unidad | Cambio / resultado | Incidencia o desviación |
|---:|---|---|---|---|---|
| 1 | Intento de avance rectilíneo (tecla 'W' / Avance) | 0 Comandos (Fallo) | 1 Respuesta (Éxito) | El robot avanzó a $0.2 \text{ m/s}$ | Ninguna. Respuesta inmediata al primer pulso. |
| 2 | Giro sobre su propio eje (tecla 'A' / Izquierda) | 0 Comandos (Fallo) | 1 Respuesta (Éxito) | El robot rotó a $0.5 \text{ rad/s}$ | Ligera latencia inicial por inicialización de buffer. |
| 3 | Giro sobre su propio eje (tecla 'D' / Derecha) | 0 Comandos (Fallo) | 1 Respuesta (Éxito) | El robot rotó a $-0.5 \text{ rad/s}$ | Rotación limpia sobre ruedas mecanum. |
| 4 | Reversa y parada de emergencia (tecla 'S' / Barra espaciadora) | 0 Comandos (Fallo) | 1 Respuesta (Éxito) | Detención inmediata ($0.0 \text{ m/s}$) | Parada segura validada. |
| 5 | Recorrido libre de prueba de mapeo en pista (2 min) | 0 Comandos (Fallo) | 1 Respuesta (Éxito) | Generación preliminar de mapa en RViz | Mapeo iniciado correctamente. |

**N válido V1 / K1:** $0/5$ (0% éxito) vs $5/5$ (100% éxito).  
**Resumen, variabilidad y tasa de éxito:** La tasa de éxito pasó de **0% en V1** a **100% en K1**. La eliminación del ejecutable duplicado y el despliegue del nuevo nodo `custom_teleop_node.py` restablecieron por completo la transmisibilidad de comandos hacia el motor del myAGV.  
**Incertidumbres/limitaciones:** Latencia de red imperceptible pero existente cuando se visualiza la transmisión de datos en RViz vía Wi-Fi.

## 5 · Interpretación y decisión

- **¿La evidencia respalda, contradice o no permite decidir la hipótesis?** Respalda totalmente la hipótesis. El problema no era de hardware o periféricos, sino de un conflicto en el runtime de ROS 2 causado por programas duplicados en la carpeta de teleoperación. El nuevo nodo responde de manera directa y estable a las entradas del teclado.
- **Si no hubo mejora, qué aprendimos:** N/A (hubo mejora sustancial). Aprendimos la importancia de mantener una estructura limpia de archivos en los paquetes de ROS 2 y re-compilar el workspace aislando executables obsoletos.
- **¿Qué riesgo o compromiso generó el cambio?** Ninguno. El nuevo nodo utiliza las estructuras estándar de ROS 2 (`geometry_msgs/msg/Twist`) sin alterar las interfaces del resto del equipo.
- **Decisión:** Conservar K1 con razón: Se recuperó el control de teleoperación al 100%, permitiendo desbloquear las tareas de mapeo e integración de la misión M05.
- **Siguiente pregunta para Kaizen 2:** ¿Qué tan preciso es el mapa 2D generado por el LiDAR mientras se realiza el recorrido conducido por la pista?

## 6 · Puerta de salida E3

- [x] V1 y K1 tienen identificadores o referencias inequívocas (`e2a4b9f` vs `f8c3d1e`).
- [x] La hipótesis está conectada con una medida y un problema diagnosticado (resolución de duplicidad y creación de nodo).
- [x] Se documentó una modificación técnica y su responsable (@a00575141-bash y equipo).
- [x] Ensayos y resultados mantienen condiciones comparables o exponen diferencias explícitamente.
- [x] La conclusión es honesta, incluso si el resultado es negativo (se confirmó el error previo de archivo redundante).
- [x] Cada estudiante registró su [E3 personal](../../participantes/_plantilla/dias/E3.md).

**Gate E3:** APROBADO.  
**Revisor:** Camilo Duque Becerra  
**Enlace a PR/commit:** [`https://github.com/Alxsoool/apolitos_AMR-/pull/3`](https://github.com/Alxsoool/apolitos_AMR-/pull/3)
