---
kaizen_dojo: "2026"
formato: "Entregable diario G2"
evidencia: "E5"
dia: 5
responsable_registro: "equipo"
estado: "COMPLETADO"
fecha: "2026-10-30"
revision_docente: "PENDIENTE"
---

# E5 · Día 5 — DEMOSTRAR | Desafío, defensa técnica y cierre Kaizen

> **Regla:** sustituir los corchetes, registrar lo realmente observado y enlazar a evidencias del repositorio. **No inventar datos ni marcar pruebas no realizadas.** Los archivos del equipo resumen el trabajo compartido; las reflexiones y evidencias personales van en `participantes/<alias>/dias/E5.md`.

## 0 · Identificación del evento y sus límites

| Campo | Valor |
|---|---|
| Fecha / equipo / misión y plataforma | 2026-10-30 / Apolitos / M05 AMR ROS 2 (Elephant Robotics myAGV 2023 Pi) |
| Dōjō o espacio exacto, bloque horario y supervisor | Campus León / Edificio Choza / Pista de Pruebas / 9:00–12:00 / Camilo René Duque Becerra |
| Modalidad real | Exhibición y defensa de demostración técnica interna |
| ¿Participación en Robolympics posterior? | No confirmada |
| Versión final congelada y enlace al código/CAD | V1.0 - Commit final en repositorio `apolitos_AMR-` (Responsable: equipo Apolitos) |
| Objetivo demostrable y criterio de éxito | Desplazamiento autónomo del AMR en pista completando trayectoria y evitación/reconocimiento de puntos clave |
| Acceso autorizado a espectadores/evidencias | Estudiantes de la Semana Tec, profesor asesor (Camilo Duque) y evaluadores |

## 1 · Ruta de la experiencia final (180 min)

| Actividad | Minutos | Evidencia requerida |
|---|---:|---|
| Seguridad y chequeo previo | 0–20 | Inspección física del myAGV, nivel de batería, conexiones de motores y espacio de pista despejado |
| Ensayo de demostración | 20–45 | Ejecución de pruebas de odometría y ajustes directos en la interfaz gráfica |
| Desafío/competencia/exhibición interna | 45–135 | Recorridos autónomos sobre pista mapeada, librando el error de terminal usando `myagv ui` |
| Reflexión sobre frontera e intercambio | 135–165 | Evaluación de la resolución de problemas en tiempo real y fallback a interfaz GUI |
| Ritual de cierre y siguiente paso | 165–180 | Cierre de sesión, resguardo de unidad myAGV y actualización de portafolios en GitHub |

## 2 · Checklist de seguridad antes de operar

- [x] Infraestructura, supervisor y operación autorizados.
- [x] Batería/cables/driver/sensores y fijaciones revisados.
- [x] Paro y contingencia practicados; nadie dentro de la zona de riesgo.
- [x] Configuración y versión final identificables.
- [x] Ruta de evacuación o emergencia, accesibilidad y permisos de captura de imagen comprobados.

**Observación o NO-GO de seguridad:** La unidad requiere monitoreo constante de temperatura y carga de batería para evitar desconfiguraciones o paros abruptos durante las pruebas. **Autoriza:** Camilo René Duque Becerra (2026-10-30).

## 3 · Registro de demostración de la misión

| Intento | Versión/condiciones | Métrica y unidad | Resultado/éxito-fallo | Incidente o razón de fallo | Evidencia |
|---:|---|---|---|---|---|
| 1 | Lanzamiento desde CLI / Terminal | Inicialización de nodos | Fallo | Error al ejecutar la odometría directamente en la terminal (fallo en la publicación de tópicos `/odom`) | Registro en terminal |
| 2 | Lanzamiento desde CLI / Terminal | Inicialización de odometría | Fallo | Excepción recurrente en comandos de terminal para cálculo de odometría | Registro en terminal |
| 3 | Ejecución desde GUI `myagv ui` | Inicio de navegación autónoma | Éxito parcial | El robot responde a la interfaz y corrige la odometría internamente | Captura GUI / Video |
| 4 | Ejecución desde GUI `myagv ui` | Recorrido de trayectoria en pista | Éxito | Movimiento autónomo fluido sin descalibración de odometría | Video del recorrido |
| 5 | Ejecución desde GUI `myagv ui` | Misión completa autónoma | Éxito | Completado del circuito de manera autónoma utilizando la app gráfica integrada | Video de demostración |

**Procedimiento y datos crudos:** Se omitió el lanzamiento por CLI debido a incompatibilidades de dependencias o argumentos de terminal para la odometría, migrando la ejecución a la interfaz integrada `myagv ui` la cual gestionó correctamente la odometría y los motores del myAGV. **Resumen de resultados:** 5 intentos (2 fallidos por CLI, 3 exitosos mediante `myagv ui`). **Limitación:** Dependencia de la interfaz gráfica local para evitar fallos de ejecución por línea de comandos.

**Métricas por plataforma:** M05 estaciones alcanzadas, error de posición y navegación autónoma segura ante obstáculos.

## 4 · Defensa individual de fronteras (cada estudiante completa su E5 personal)

| Alias | Alcance(s) original(es) | Qué aportó realmente / enlace a evidencia | Antes no podía... | Ahora puedo... | Demostración de capacidad ante otro | Feedback de par o profesor |
|---|---|---|---|---|---|---|
| @Ivanna0407 | AR10 / Pruebas y alineación | Pruebas de navegación, alineación de marcadores y verificación de ruta en UI | No podía resolver fallos de odometría en ejecuciones del AMR | Puedo operar y diagnosticar la navegación autónoma del AMR mediante `myagv ui` | Demostración del movimiento autónomo directo en pista | Buena capacidad de adaptación ante fallos del sistema en terminal |
| @a00575141-hash | MS02, MS11 / Seguridad y visión | Configuración y prueba de visión/cámara e integración con el recorrido | No podía validar por qué la cámara/sensores no sincronizaban la odometría | Puedo calibrar el entorno y verificar la integración sensorial con la interfaz del robot | Verificación gráfica de lectura de sensores durante la demostración | Resolución efectiva para mantener la estabilidad del sistema |
| @a00574597 | MS01 / Integración | Apoyo en la configuración del entorno, control del robot y resolución de software | No podía conectar y desplegar la navegación fluida tras fallos de terminal | Puedo ejecutar la pila de navegación del myAGV a través de su entorno gráfico GUI | Despliegue y ejecución del demo ante el grupo y profesor | Correcto diagnóstico de la causa raíz en la terminal |
| @a00574830 | AR01, AR10 / Pruebas y control | Pruebas de movimiento autónomo, revisión de lógica de control y soporte en pista | No podía mantener la estabilidad del movimiento autónomo | Puedo controlar y verificar la ruta autónoma en tiempo real | Demostración del recorrido autónomo exitoso en la pista | Destacada colaboración en la resolución del problema de odometría |

**Ver portafolios individuales:** `participantes/Ivanna0407/dias/E5.md`, `participantes/a00575141-hash/dias/E5.md`, `participantes/a00574597/dias/E5.md`, `participantes/a00574830/dias/E5.md`.

## 5 · Evaluación de la experiencia y cierre Design Thinking

| Pregunta para validar la experiencia | Respuesta basada en evidencia (no solo opinión) |
|---|---|
| ¿Qué elecciones del catálogo C2 tuvieron sentido para diferentes niveles de entrada? | La combinación de alcances AR01, AR10 y MS01/MS02 permitió dividir el trabajo entre sensado, pruebas de control y navegación. |
| ¿Qué katas fueron útiles, redundantes o faltaron? | K1 y K3 fueron esenciales para entender los tópicos de ROS 2 y la odometría; hizo falta una kata específica sobre solución de problemas en scripts de terminal vs GUI del myAGV. |
| ¿Los materiales y el dōjō habilitaron el trabajo sin exclusiones? | Sí, la pista del dōjō y la plataforma myAGV permitieron que todo el equipo participara en pruebas físicas y monitoreo. |
| ¿Hubo evidencia de dos ciclos de mejora técnica? | Sí: Ciclo 1 (Lanzamiento por terminal con errores de odometría) -> Ciclo 2 (Migración y ejecución exitosa mediante `myagv ui`). |
| ¿Qué se debería rediseñar para la próxima iteración? | Depurar los scripts de launch y nodos ROS 2 en terminal para no depender únicamente de la interfaz gráfica integrada del fabricante. |
| ¿La experiencia protegió confianza, autonomía, pertenencia y seguridad? | Sí, la comunicación constante permitió resolver la falla técnica en equipo sin perder tiempo en la demostración final. |

**Feedback externo o de otra pareja/equipo:** Profesor Camilo Duque reconoció la capacidad del equipo para encontrar una alternativa rápida (uso de `myagv ui`) para lograr la demostración autónoma a tiempo durante el cierre.

## 6 · Cierre, transferencia y archivo

- **Estado técnico final:** Funcional (navegación autónoma lograda operando directamente a través de `myagv ui`).
- **Logros colectivos y límites reales:** Se logró el desplazamiento autónomo en la pista de pruebas; la limitación principal fue el error en la ejecución del script de odometría por CLI de terminal.
- **Qué reutilizaría una generación futura:** La metodología de pruebas directas en la interfaz `myagv ui` como mecanismo de contingencia para demostraciones en vivo.
- **Qué falta antes de competencia externa (si la hubiera):** Corregir las dependencias de los paquetes ROS 2 en la terminal para que el lanzamiento sea 100% por comandos nativos.
- **Inventario devuelto/resguardado, responsable y lugar exacto:** Robot myAGV 2023, accesorios y baterías devueltos en orden a Camilo Duque / Laboratorio EIC.
- **Archivo de evidencias, permisos de acceso y retención:** Repositorio en GitHub `apolitos_AMR-` con documentación y videos resguardados en Google Drive del equipo.
- **Próximo experimento o kata que se exploraría:** Depuración de nodos ROS 2 para la conversión de `/odom` sin pasar por el entorno de desarrollo del fabricante.

### Gate E5

- [x] Demostración registrada honestamente, exitosa o fallida.
- [x] V1, K1, K2 y Vn tienen enlaces y registros coherentes.
- [x] Cada estudiante completó E5 personal y defendió su frontera.
- [x] Se registraron observaciones para la fase de validación posterior del Design Thinking.
- [x] Se resguardaron/entregaron materiales y accesos sin exponer datos privados.

**Revisión final docente:** Validado. **Fecha:** 2026-10-30. **Firma/alias:** Camilo René Duque Becerra.
