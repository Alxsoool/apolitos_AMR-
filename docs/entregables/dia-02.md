---
kaizen_dojo: "2026"
formato: "Entregable diario G2"
evidencia: "E2"
dia: 2
responsable_registro: "equipo"
estado: "PENDIENTE"
fecha: "2026-10-27"
revision_docente: "PENDIENTE"
---

# E2 · Día 2 — HACER | Primera integración funcional y línea base V1

> **Regla:** sustituir los corchetes, registrar lo realmente observado y enlazar a evidencias del repositorio. **No inventar datos ni marcar pruebas no realizadas.** Los archivos del equipo resumen el trabajo compartido; las reflexiones y evidencias personales van en `participantes/<alias>/dias/E2.md`.

## 0 · Identificación y continuidad

| Campo | Dato |
|---|---|
| Fecha, equipo, misión y plataforma | 2026-10-27 \| Apolitos \| M05 AMR ROS 2 \| myAGV 2023 Pi Elephant Robotics |
| Dōjō real y mesa/zona utilizada | Campus León, Edificio Choza, Taller Choza, Puesto: Pista |
| Estado del gate E1 / cambios desde D1 | Aprobado (Obtención de repuesto de teclado pendiente desde el 26/10/2026 por @a00575141-bash) |
| Kit por integrante / compromisos modificados | Sin modificaciones de compromiso; se mantiene estructura de E1 |
| Materiales recibidos y pendientes | MAT-001 (myAGV2023 base), MAT-002 (Pista); Pendiente/Bloqueado: Teclado USB de repuesto (Responsable: @a00575141-bash) |
| Objetivo técnico del Día 2 | Primera integración V1 para teleoperación básica, lectura de LiDAR/cámara e inicio de mapeo del entorno |

## 1 · Ruta de las actividades de hoy (180 min)

| Bloque | Minutos | Registro requerido / evidencia |
|---|---:|---|
| Revisión de misión y compromisos | 0–15 | Revisión de pactos; evaluación del bloqueo con el periférico de entrada (teclado) |
| Microlección aplicada | 15–35 | Configuración de nodos de teleoperación ROS 2 (`teleop_twist_keyboard`) e interfaces HID en Linux/SBC |
| Katas de integración | 35–105 | Puesta en marcha de la base myAGV, verificación de topics ROS 2 para LiDAR y cámara |
| Ensayos iniciales / línea base | 105–145 | Intento de mapeo interrumpido: imposibilidad de conectar/mapear entrada de teclado para direccionar el AMR |
| Consolidación de evidencia | 145–170 | Extracción de logs de ROS 2, registro de comandos no reconocidos y captura de estado de terminal |
| Gate E2 | 170–180 | Evaluación del gate: REPLANIFICAR / CONDICIONADO por bloqueo en interfaz de control |

## 2 · Microlección e integración por alcances

**Tema que resolvió un problema real del equipo:** Mapeo de puertos de entrada y comunicación por teclado en entornos ROS 2 / Raspberry Pi.  
**Material / referencia utilizada:** Documentación oficial Elephant Robotics myAGV ROS 2 & package `teleop_twist_keyboard`.

| Alias | Alcance | Kata seleccionado / nuevo | Acción técnica ejecutada | Archivo, commit o plano | Estado (pendiente/probado/bloqueado) | Dependencia de otro integrante |
|---|---|---|---|---|---|---|
| @a00574597 | MS01 | K1, K2 | Energización de la base myAGV y verificación de comunicación base | `../../codigo/launch/base_bringup.launch.py` | Probado | Ninguna |
| @a00575141-bash | MS02 | K1, K3 | Intento de conexión de teclado y configuración de nodo de mapeo | `../../codigo/launch/mapping.launch.py` | Bloqueado | Falta de reconocimiento del teclado |
| @Ivanna0407 | AR10 | K1 | Captura de transmisión de video y prueba de lectura de marcadores Aruco | `../../codigo/nodes/camera_reader.py` | Probado | Lectura correcta de cámara |
| @a00574830 | AR01 | K1, K2 | Verificación de tópicos de odometría y sensores LiDAR | `../../logs/sensor_topics.txt` | Probado | Módulo de sensores |

## 3 · Estado de integración V1

| Subsistema | Entrada | Salida esperada | Responsable | Prueba de integración y observación | Evidencia |
|---|---|---|---|---|---|
| Estructura/mecánica | Chasis myAGV 2023 | Estabilidad y desplazamiento omnidireccional | @a00574597 | La estructura y ruedas mecanum responden físicamente en encendido | `../../evidencias/fotos/myagv_encendido.jpg` |
| Energía y accionamiento | Batería integrada myAGV | Alimentación a Pi, motores y LiDAR | @a00574597 | Encendido nominal del sistema completo y arranque de ROS 2 | `../../logs/power_check.log` |
| Sensores/percepción | LiDAR / Cámara integrados | Tópicos `/scan` y `/camera/image_raw` | @Ivanna0407 / @a00574830 | Transmisión de imagen y escaneo de distancia funcionando correctamente | `../../evidencias/rviz_sensors.png` |
| Control/software | Pulsaciones de teclado USB | Comandos `geometry_msgs/msg/Twist` (`cmd_vel`) | @a00575141-bash | **FALLA:** El teclado no es reconocido por la interfaz/sistema para mapear las teclas a comandos de movimiento | `../../logs/teleop_error.log` |
| Integración global | Control por teclado | Mapeo 2D del entorno en tiempo real | Equipo | **INCOMPLETO:** No se puede desplazar el robot de forma controlada para construir el mapa | `../../logs/mapping_attempt.log` |

**Versión identificable:** Commit SHA `e2a4b9f` (Tag: `v1-alpha
