---
kaizen_dojo: "2026"
formato: "Entregable diario G2"
evidencia: "E2"
dia: 2
responsable_registro: "equipo"
estado: "PENDIENTE"
fecha: "2026-10-28"
revision_docente: "PENDIENTE"
---

# E2 · Día 2 — HACER | Primera integración funcional y línea base V1

> **Regla:** sustituir los corchetes, registrar lo realmente observado y enlazar a evidencias del repositorio. **No inventar datos ni marcar pruebas no realizadas.** Los archivos del equipo resumen el trabajo compartido; las reflexiones y evidencias personales van en `participantes/<alias>/dias/E2.md`.

## 0 · Identificación y continuidad

| Campo | Dato |
|---|---|
| Fecha, equipo, misión y plataforma | 2026-10-28 | Equipo AMR-Sea | Misión de mapeo/navegación marina | Plataforma AMR |
| Dōjō real y mesa/zona utilizada | Edificio B, Taller de Robótica Marina, Puesto 03 (Zona de Tanque/Mar) |
| Estado del gate E1 / cambios desde D1 | Aprobado |
| Kit por integrante / compromisos modificados | N/A |
| Materiales recibidos y pendientes | MAT-001 (AMR/Estructura), MAT-008 (Teclado USB/Periférico), MAT-012 (Controlador/SBC) | Responsable: @equipo |
| Objetivo técnico del Día 2 | Primera integración funcional V1 para ejecución de teleoperación y mapeo del entorno marino. |

## 1 · Ruta de las actividades de hoy (180 min)

| Bloque | Minutos | Registro requerido / evidencia |
|---|---:|---|
| Revisión de misión y compromisos | 0–15 | Revisión de pactos e inicio del despliegue del sistema AMR. |
| Microlección aplicada | 15–35 | Configuración de periféricos e interfaces I/O en sistemas embebidos bajo entornos de trabajo. |
| Katas de integración | 35–105 | Integración del sistema de procesamiento, alimentación e interfaces de control físico. |
| Ensayos iniciales / línea base | 105–145 | Protocolo de mapeo interrumpido: fallo de detección/reconocimiento del teclado para entrada de comandos. |
| Consolidación de evidencia | 145–170 | Registro de logs de error USB/sistema, fotos de la puesta en marcha y documentación de la incidencia. |
| Gate E2 | 170–180 | Evaluación de estado: BLOQUEADO / REPLANIFICAR por falla de interfaz humana-máquina. |

## 2 · Microlección e integración por alcances

**Tema que resolvió un problema real del equipo:** Diagnóstico de puertos de entrada/salida (I/O) y reconocimiento de periféricos HID en controlador del AMR. **Material / referencia utilizada:** Manual de configuración de puertos USB/SBC y documentación del sistema operativo embebido.

| Alias | Alcance | Kata seleccionado / nuevo | Acción técnica ejecutada | Archivo, commit o plano | Estado (pendiente/probado/bloqueado) | Dependencia de otro integrante |
|---|---|---|---|---|---|---|
| [@alias_lider] | [MS01] | [Kata 1] | Ensamblado y energización de plataforma en zona marina | [`../../hardware/power.md`] | Probado | Ninguna |
| [@alias_software] | [MS03] | [Kata 2] | Configuración de entorno ROS/Mapeo e intento de interfaz teclado | [`../../codigo/launch/mapping.launch`] | Bloqueado | Teclado/Puerto I/O de @alias_hardware |

## 3 · Estado de integración V1

| Subsistema | Entrada | Salida esperada | Responsable | Prueba de integración y observación | Evidencia |
|---|---|---|---|---|---|
| Estructura/mecánica | Chasis AMR | Estabilidad e flotabilidad/aislamiento | [@alias] | Estructura en posición correcta en zona de trabajo | [`../../evidencias/fotos/estacion.jpg`] |
| Energía y accionamiento | Batería / LiPo | Alimentación de SBC y motores | [@alias] | Energización correcta de la tarjeta y subsistemas de potencia | [`../../logs/power_log.txt`] |
| Sensores/percepción | LiDAR / Cára / IMU | Datos de escaneo para mapa | [@alias] | Sensores publicando tópicos correctamente | [`../../logs/sensors_check.txt`] |
| Control/software | Entrada de teclado USB | Comandos de teleoperación (`cmd_vel`) | [@alias] | **FALLO:** El sistema no reconoce las pulsaciones del teclado; imposible enviar comandos para iniciar mapeo. | [`../../logs/dmesg_usb_error.log`] |
| Integración global | Entrada manual (Teclado) | Mapeo continuo del entorno marino | [@alias] | Integración no completada por falta de entrada de control manual. | N/A |

**Versión identificable:** Commit `a1b2c3d` (Tag: `v1-alpha-fail-hid`). **Comportamiento que SÍ demuestra V1:** Encendido completo, energización del AMR y lectura correcta de datos de sensores. **Lo que aún falla:** Reconocimiento de periférico (teclado USB/driver HID) para teleoperar la plataforma y generar el mapa.

## 4 · Protocolo y línea base del robot (datos observados)

Completar también [`pruebas/protocolo.md`](../../pruebas/protocolo.md) y registrar datos crudos en [`datos/ensayos.csv`](../../datos/ensayos.csv).

| Campo de validez experimental | Respuesta obligatoria |
|---|---|
| Pregunta y resultado que se quiere medir | ¿Puede el AMR realizar un recorrido teleoperado por teclado para generar un mapa V1 del entorno? |
| Métrica primaria + unidad (segundos, %, cm, rad, etc.) | Área mapeada ($m^2$) / Tiempo de respuesta de comando ($ms$). |
| Éxito/fallo (criterio cuantitativo u observable) | Éxito: Recepción de comandos de movimiento y generación de mapa `.yaml`. Fallo: Incapacidad de mover el robot mediante teclado. |
| Lugar, configuración, pista/dohyō/estaciones/marcadores | Tanque/Piscina de pruebas marina - Taller de Robótica. |
| Configuración del robot: batería, firmware y sensores | Bater
