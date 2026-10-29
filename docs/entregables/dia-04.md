---
kaizen_dojo: "2026"
formato: "Entregable diario G2"
evidencia: "E4"
dia: 4
responsable_registro: "equipo"
estado: "EN_PROGRESO"
fecha: "2026-10-29"
revision_docente: "PENDIENTE"
---

# E4 · Día 4 — ITERAR | Kaizen 2, robustez y preparación de demostración

> **Regla:** sustituir los corchetes, registrar lo realmente observado y enlazar a evidencias del repositorio. **No inventar datos ni marcar pruebas no realizadas.** Los archivos del equipo resumen el trabajo compartido; las reflexiones y evidencias personales van en `participantes/<alias>/dias/E4.md`.

## 0 · Contexto

**Fecha y dōjō:** 2026-10-29 · **Equipo/misión:** Equipo G2 / Navegación y Control Autónomo · **Versiones trazables:** V1 [v1.0.0], K1 [k1.1.0] y K2 [k2.0.0-dev].

## 1 · Ruta de actividades del Día 4 (180 min)

| Actividad | Minutos | Registro requerido |
|---|---:|---|
| Revisión por pares y retroalimentación | 0–20 | Retroalimentación recibida del equipo par sobre la estabilidad de control |
| Diseño/ejecución Kaizen 2 | 20–70 | Corrección de compatibilidad de entorno (ROS 1 vs ROS 2) y ajuste en nodo de velocidad |
| Comparación V1–K1–K2 | 70–115 | En ejecución (depuración de nodo de coordenadas en curso) |
| Ensayo de robustez | 115–145 | Pendiente tras resolver errores de coordenadas |
| Preparación de demo | 145–165 | Definición preliminar de roles para pruebas de trayectoria |
| Gate de preparación | 165–180 | EN_PROGRESO (solución de bugs en nodo de coordenadas) |

## 2 · Revisión por pares

| Persona o equipo observador (alias) | Evidencia revisada | Observación útil / pregunta | Respuesta técnica y decisión | Cambio aceptado o descartado |
|---|---|---|---|---|
| Equipo Par (G1) | Nodos ROS de velocidad | ¿Por qué el script de Python no ejecuta las librerías de ROS 2? | Se detectó conflicto de entorno: Python apuntaba a dependencias de ROS 1. | Aceptado (se reconfiguró el environment para ROS 2). |

**Acuerdo de colaboración:** Se revisó conjuntamente la configuración del entorno de ejecución y se acordó aislar las variables de entorno para garantizar que los scripts invocados por el Launch file apunten a la versión correcta de ROS 2.

## 3 · Segundo ciclo Kaizen (K2)

| Campo experimental | Completar |
|---|---|
| Limitación o nueva oportunidad detectada en K1 | Error de compatibilidad donde Python utilizaba librerías de ROS 1 al ejecutar el nodo de velocidad. |
| Hipótesis K2 y fundamento | Cambiar la resolución del entorno de Python a ROS 2 corregirá el error de importación y permitirá la publicación continua de comandos de velocidad. |
| Variable modificada y controles | Entorno de ejecución de Python, variables de entorno (`ROS_DISTRO`, `PYTHONPATH`) y dependencias del nodo de velocidad. |
| Requisitos de seguridad antes del cambio | Verificación de parada de emergencia activa en hardware/simulador antes de lanzar los nodos. |
| Personas responsables y alcances implicados | Equipo de software y control. |
| Cambio exacto de código/CAD/configuración | Actualización del *shebang* y sourcing del workspace correcto de ROS 2 (`source /opt/ros/<distro>/setup.bash`). |
| Enlace a commit, PR y versión K2 | `commits/fix-ros2-env-velocity-node` |
| Métrica, unidad y criterio para declarar éxito | Ejecución limpia del nodo de velocidad sin errores de importación (`0` errores de runtime). |

## 4 · Comparación de evolución

| Ensayo/condición equivalente | V1 (valor + unidad) | K1 (valor + unidad) | K2 (valor + unidad) | Incidencias o validez |
|---:|---|---|---|---|
| 1 | N/A | Error ROS 1 | Éxito | Nodo de velocidad ejecuta correctamente |
| 2 | N/A | Pendiente | Pendiente (Errores en nodo de coordenadas) | Depuración activa de coordenadas |
| 3 | [...] | [...] | [...] | En proceso |
| 4 | [...] | [...] | [...] | En proceso |
| 5 | [...] | [...] | [...] | En proceso |

**Registros fuente:** [`datos/ensayos.csv`](../../datos/ensayos.csv) y protocolo [enlace].

**Síntesis (método, n, media/mediana, dispersión y éxito cuando proceda):** Se resolvió con éxito el fallo de entorno del nodo de velocidad. Actualmente se registran e investigan múltiples excepciones en la transformación/publicación del nodo de coordenadas.

**¿Qué mejora, qué empeora y qué no podemos concluir?** Mejora la ejecución del nodo de velocidad bajo ROS 2. Queda pendiente evaluar la precisión y estabilidad general hasta corregir las excepciones en el nodo de coordenadas.

## 5 · Ensayo de robustez o variación de condiciones

| Cambio controlled de entorno (luz, suelo, batería, posición, rival, obstáculo o carga) | Riesgo y límite seguro | Predicción | Resultado / unidad / éxitos | ¿Se mantiene el objetivo? | Evidencia |
|---|---|---|---|---|---|
| Publicación de coordenadas con desfase/ruido | Fallo de cálculo de trayectoria | El nodo debe publicar coordenadas sin arrojar excepciones de sintaxis o runtime | En proceso (se están resolviendo varios errores de ejecución) | Por confirmar | Logs del sistema / Consola ROS 2 |

**Límites de inferencia:** Las pruebas de robustez se reanudarán una vez estabilizado el nodo de coordenadas.

## 6 · Ensayo general de demostración

| Segmento | Qué se demostrará en 20–60 s | Integrante responsable | Versión/código usado | Material requerido | Plan B ante fallo |
|---|---|---|---|---|---|
| Inicio / contexto | Inicialización de nodos ROS 2 y verificación de topics | Equipo | K2 (dev) | Terminal / ROS2 CLI | Script de verificación rápida |
| Prueba principal | Envío de comandos de velocidad y cálculo de coordenadas | Equipo | K2 (dev) | Robot / Simulador | Teleoperación manual |
| Evidencia de mejora | Despliegue sin errores de entorno de Python | Equipo | K2 (dev) | Logs de consola | N/A |
| Defensa de fronteras | Explicación del manejo de errores de compatibilidad ROS 1 / ROS 2 | Equipo | Documentación | Código del nodo | Presentación técnica |

**¿Robolympics es el evento externo posterior?** Por confirmar.

## 7 · Gate E4

- [x] Existe un ciclo K2 explícito, con hipótesis, modificación y datos.
- [x] Se conservan V1, K1, K2 y, en su caso, reversiones para reproducibilidad.
- [ ] Se efectuó una prueba de robustez documentada o se justificó por qué no era segura/factible (En progreso tras resolver nodo de coordenadas).
- [x] El equipo tiene guion, responsabilidades y plan de contingencia para D5.
- [ ] Cada participante actualizó [E4 personal](../../participantes/_plantilla/dias/E4.md).

**Estado de preparation:** CON RESTRICCIONES. **Pendientes y responsables:** Resolver errores del nodo de coordenadas (Equipo de desarrollo). **Revisión:** PENDIENTE.
