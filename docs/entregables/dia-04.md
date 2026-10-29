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

**Fecha y dōjō:** 2026-10-29 · Campus León, Edificio Choza, Sala/Pista Choza · **Equipo/misión:** Apolitos · M05 AMR ROS 2 (myAGV 2023 PI Elephant Robotics) · **Versiones trazables:** V1 [v1.0.0], K1 [k1.1.0] y K2 [k2.0.0-dev].

## 1 · Ruta de actividades del Día 4 (180 min)

| Actividad | Minutos | Registro requerido |
|---|---:|---|
| Revisión por pares y retroalimentación | 0–20 | Retroalimentación del equipo par sobre la ejecución de nodos Python en el entorno |
| Diseño/ejecución Kaizen 2 | 20–70 | Corrección de conflicto de entorno (Python tomaba ROS 1 en lugar de ROS 2) en nodo de velocidad |
| Comparación V1–K1–K2 | 70–115 | En desarrollo (depuración activa de errores en nodo de coordenadas) |
| Ensayo de robustez | 115–145 | Pendiente hasta estabilizar la publicación de coordenadas |
| Preparación de demo | 145–165 | Organización de roles y pruebas del recorrido en la pista |
| Gate de preparación | 165–180 | EN_PROGRESO (trabajando en la resolución de excepciones de coordenadas) |

## 2 · Revisión por pares

| Persona o equipo observador (alias) | Evidencia revisada | Observación útil / pregunta | Respuesta técnica y decisión | Cambio aceptado o descartado |
|---|---|---|---|---|
| Equipo Par / Camilo Duque Becerra | Nodos ROS de velocidad | ¿Por qué el script de Python marca error de versión/librería al ejecutar? | Se identificó que Python estaba apuntando al entorno/variables de ROS 1 en lugar de ROS 2. | Aceptado (se reconfiguró el entorno para forzar ROS 2). |

**Acuerdo de colaboración:** Nos comunicamos constantemente sobre el estado del código. Tras el fallo de compatibilidad de entorno, reconfiguramos las variables del sistema para garantizar el uso exclusivo de ROS 2 en los nodos de ejecución.

## 3 · Segundo ciclo Kaizen (K2)

| Campo experimental | Completar |
|---|---|
| Limitación o nueva oportunidad detectada en K1 | El nodo de velocidad arrojaba error al ejecutarse debido a que Python utilizaba dependencias de ROS 1. |
| Hipótesis K2 y fundamento | Corregir las variables de entorno (`PYTHONPATH`, `ROS_DISTRO`) y apuntar a ROS 2 permitirá ejecutar el nodo de velocidad sin fallos de importación. |
| Variable modificada y controles | Variables de entorno de Python y configuración del workspace de ROS 2 en el myAGV. |
| Requisitos de seguridad antes del cambio | Paro de emergencia verificado y robot levantado del suelo antes de publicar comandos de velocidad. |
| Personas responsables y alcances implicados | Apolitos (@Ivanna0407, @a00575141-hash, @a00574597, @a00574830). |
| Cambio exacto de código/CAD/configuración | Ajuste de entorno/shebang y sourcing directo del workspace de ROS 2 (`source /opt/ros/<distro>/setup.bash`). |
| Enlace a commit, PR y versión K2 | `https://github.com/Alxsoool/apolitos_AMR-/commits/main` |
| Métrica, unidad y criterio para declarar éxito | Ejecución limpia del nodo de velocidad sin excepciones ni errores de versión (`0` errores de entorno). |

## 4 · Comparación de evolución

| Ensayo/condición equivalente | V1 (valor + unidad) | K1 (valor + unidad) | K2 (valor + unidad) | Incidencias o validez |
|---:|---|---|---|---|
| 1 | Error de mapeo / conexión | Error ROS 1 en velocidad | Éxito en nodo velocidad | Nodo de velocidad ejecuta correctamente bajo ROS 2 |
| 2 | N/A | Pendiente | Errores en nodo coordenadas | Depuración activa de excepciones en el nodo de coordenadas |
| 3 | [...] | [...] | En proceso | Pendiente de validación |
| 4 | [...] | [...] | En proceso | Pendiente de validación |
| 5 | [...] | [...] | En proceso | Pendiente de validación |

**Registros fuente:** [`datos/ensayos.csv`](../../datos/ensayos.csv) y repositorio del equipo [Apolitos AMR](https://github.com/Alxsoool/apolitos_AMR-).

**Síntesis (método, n, media/mediana, dispersión y éxito cuando proceda):** Se resolvió el conflicto de entorno en el nodo de velocidad, logrando su correcta ejecución en ROS 2. Al avanzar con el nodo de coordenadas se presentaron varios errores de ejecución que el equipo continúa resolviendo.

**¿Qué mejora, qué empeora y qué no podemos concluir?** Mejora la estabilidad del entorno de ejecución Python/ROS 2 para velocidad. No podemos concluir la precisión de trayectoria hasta solucionar los errores en el nodo de coordenadas.

## 5 · Ensayo de robustez o variación de condiciones

| Cambio controlado de entorno (luz, suelo, batería, posición, rival, obstáculo o carga) | Riesgo y límite seguro | Predicción | Resultado / unidad / éxitos | ¿Se mantiene el objetivo? | Evidencia |
|---|---|---|---|---|---|
| Cálculo y publicación en tiempo real desde nodo de coordenadas | Pérdida de localización o desvío en pista | El nodo debe procesar coordenadas sin lanzar excepciones de runtime | En proceso (resolviendo varios errores de código/publicación) | Por confirmar | Logs en terminal de ROS 2 |

**Límites de inferencia:** Las pruebas de robustez en pista se completarán una vez corregidos los errores del nodo de coordenadas.

## 6 · Ensayo general de demostración

| Segmento | Qué se demostrará en 20–60 s | Integrante responsable | Versión/código usado | Material requerido | Plan B ante fallo |
|---|---|---|---|---|---|
| Inicio / contexto | Inicialización de nodos y verificación del entorno ROS 2 en myAGV | Apolitos | K2 | myAGV 2023 PI, Terminal | Script de verificación de entorno |
| Prueba principal | Envío de velocidades y lectura de coordenadas en ruta | Apolitos | K2 | Robot, Pista Choza | Control manual / ajuste de parámetros |
| Evidencia de mejora | Ejecución directa del nodo de velocidad sin conflictos ROS 1/ROS 2 | Apolitos | K2 | Terminal / Logs | N/A |
| Defensa de fronteras | Explicación del flujo de navegación y corrección del entorno | Apolitos | K2 / Docs | Repositorio | Explicación técnica del script |

**¿Robolympics es el evento externo posterior?** Por confirmar. D5 documenta la demostración interna en el dōjō Choza.

## 7 · Gate E4

- [x] Existe un ciclo K2 explícito, con hipótesis, modificación y datos.
- [x] Se conservan V1, K1, K2 y, en su caso, reversiones para reproducibilidad.
- [ ] Se efectuó una prueba de robustez documentada o se justificó por qué no era segura/factible (En progreso tras resolver nodo de coordenadas).
- [x] El equipo tiene guion, responsabilidades y plan de contingencia para D5.
- [x] Cada participante actualizó [E4 personal](../../participantes/_plantilla/dias/E4.md).

**Estado de preparación:** CON RESTRICCIONES. **Pendientes y responsables:** Resolver los errores del nodo de coordenadas (@Ivanna0407, @a00575141-hash, @a00574597, @a00574830). **Revisor:** Camilo Duque Becerra.
