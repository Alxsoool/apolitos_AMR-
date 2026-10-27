---
kaizen_dojo: "2026"
formato: "Entregable diario G2"
evidencia: "E1"
dia: 1
responsable_registro: "equipo"
estado: "PENDIENTE"
fecha: "2026-10-26"
revision_docente: "PENDIENTE"
---

# E1 · Día 1 — ATREVERSE | Contrato de misión, inventario y dōjō

> **Regla:** sustituir los corchetes, registrar lo realmente observado y enlazar a evidencias del repositorio. **No inventar datos ni marcar pruebas no realizadas.** Los archivos del equipo resumen el trabajo compartido; las reflexiones y evidencias personales van en `participantes/<alias>/dias/E1.md`.

## 0 · Identificación, equipo y logística del dōjō

| Campo obligatorio | Dato |
|---|---|
| Fecha y horario de esta sesión | [2026-10-26; 9:00–12:00, 180 min] |
| Nombre / alias del equipo | [Apolitos] |
| Misión / plataforma | [M05 AMR ROS 2] |
| Objetivo verificable del robot (una frase) | [El robot se debe mover de manera controlada, utilizando sus sensores haciendo una ruta predefinifa e identificando marcadores con la cámara] |
| **Dōjō asignado — campus, edificio y sala/taller exactos** | **[Campus _León__ / Edificio _Choza__ / Sala o taller __Choza_ / Nº de laboratorio _Choza__]** |
| Puesto o zona dentro del dōjō | [Pista] |
| Horario / reserva confirmada | [9:00-12:00] |
| Responsable del espacio y contacto institucional | [Camilo Duque Becerra Camilo.duque@tec.mx] |
| Acceso, aforo y ajustes de accesibilidad | Revisar llaves del lugar para poder acceder |
| Salidas, botiquín, extintor y punto de reunión | [CTA] |
| Zonas segregadas por riesgo | [Tránsito AMR / ensayo de pista] |
| Ubicación de materiales y resguardo nocturno | [LNA] |
| Plan de sustitución si falla el espacio | [Pista Alternativa] |
| Instructor o supervisor presente en la sesión | [Camilo Duque Becerra Camilo.duque@tec.mx] |

> ⛔ **No se permite avanzar a pruebas físicas sin dōjō concreto y autorización del responsable.** No inventar salón, número de laboratorio ni recursos que no hayan sido confirmados.

## 1 · Integrantes, responsabilidades, accesibilidad y decisiones (0–15 min)

| Alias GitHub | Rol inicial | Carta y frontera (D/S/E; F1–F4) | Alcances ID (1–3) | Kit personal (archivo) | Necesidad de apoyo o accesibilidad acordada |
|---|---|---|---|---|---|
| [@Ivanna0407] | [Pruebas] | [D · F1 · D1] | [NA] | [`../../participantes/alias/compromiso.md`](https://github.com/Alxsoool/apolitos_AMR-/blob/main/participantes/_plantilla/Compromiso_Ivanna_Mart%C3%ADnez_de_Alba.md) |
| [@a00575141-hash] | [seguridad] | [NA] | [participantes/compromiso-kaizen-miranda-garcia-marquez (1).md] 
| [@a00574597] | [Integración] | [NA] | [AR01 AR10] | 
[participantes/_plantilla/compromiso-kaizen-massimo-orozco-ocampo.md]
| [@a00574830] | [Pruebas] | [D · F1 · D1] | [NA] | [https://github.com/Alxsoool/apolitos_AMR-/blob/eda5562445bbc56c55a8c4221a3195d3783b9335/participantes/_plantilla/compromiso-kaizen-alexa-marisol-rodriguez-barajas.md] 

**Acuerdo de colaboración:** [Siempre nos comunicamos entre nosotros de que es lo que estamos haciendo y lo que necesitamos, nos apoyamos como compañeros en caso de tener dudas o no estar seguros de algo. Si hay algun conflicto se habla de manera calmada ente los miembros y en caso de ser necesario se puede pedir apoyo al profesor, todos colaboramos en las actividades que hacemos, sin dejar a nadie atrás o solo]]

## 2 · Demostración de la plataforma y seguridad (15–35 min)

| Elemento | Observación directa | Evidencia / vínculo |
|---|---|---|
| Plataforma base inspeccionada (estado, modelo, ID inventario) | [AGV 2023 PI Elephant Robotics ] | [https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjgpcDlm9iXAxXvEkQIHRT-HpIQFnoECBIQAQ&url=https%3A%2F%2Fwww.3dmarket.mx%2Fp%2Fmyagv-2023-pi-elephant-robotics%2F%3Fsrsltid%3DAYCX9vK4FhiuGFzijKWIhrng3SFxqYSygYlzRH496652_yk4boD6jYFO&usg=AOvVaw0lSb-53SOPrEij7BO0_YVS&opi=89978449] |
| Funciones existentes y límites comprobados | [Autónomo, RC, LiDAR ] | [NA] |
| Paro de emergencia / desconexión segura ensayados | [ SHUT DOWN] | [enlace / tutor responsable] |
| Restricciones de competición o exhibición verificadas | [ Mantenerse dentro del área de mapeo , no uso del brazo robótico] | [fuente / por verificar] |
| Riesgos vistos y medidas activas | [Se puede quemar y desconfigurar ] | [NA] |

**Normas específicas según misión:**
- **M01:** protecciones de alimentación; desarmar motores antes de tocar ruedas; dohyō delimitado, rival de referencia y bordes seguros.
- **M03:** pista despejada, altura/posición de sensores controlada, baterías y ruedas comprobadas.
- **M04:** espacio interior autorizado, observador humano, altura y desplazamientos limitados, baterías y aterrizaje inmediato; *verificar modelo real de Tello*.
- **M05:** ROS 2 y TF/navegación listos; límites de velocidad, sensor de obstáculos, paro seguro y zona de tránsito marcada.

## 3 · Diagnóstico práctico colectivo (35–65 min)

**Condición inicial V0 de la plataforma:** [Robot completo]

| Prueba diagnóstica | Condición y procedimiento | Resultado observado / unidad | Problema / causa probable | Evidencia |
|---|---|---|---|---|
| [1: movimiento o comunicación] | [Batería] | [Movimiento] | [Mapeo incorrecto] | [enlace] |
| [2: lectura de sensor] | [Cámara] | [Transmisión] | [Mala calibración] | [enlace] |


**Capacidades ya disponibles y dependencias:** [qué módulos se pueden reutilizar, y qué necesita cada alcance de otro integrante.]

## 4 · Integración de Mission Forge C2 y pacto de alcances (65–100 min)

Cada participante debe colocar el archivo **Markdown original generado por la web** en:

`participantes/<alias>/compromiso.md`

Se conserva íntegro (incluido el frontmatter y la lista de katas). Los nuevos alcances/katas diseñados por el participante quedan claramente marcados como *propuesta propia* y requieren aprobación técnica.

**Catálogo de referencia:** [Google Sheets C2](https://docs.google.com/spreadsheets/d/1FKxFzoyu9KJb3RlOwB609vliS5hAtmwWFu2G2zG3Ky4/edit) · **Configurador Mission Forge:** [`herramientas/mission-forge-c2.html`](../../herramientas/mission-forge-c2.html) (descárgalo y ábrelo en el navegador; funciona sin Internet).

| Alias | Kit enlazado | Alcance principal | Complementos | Katas elegidos o nuevos | Horas mín.–máx. | Evidencia final esperada | Negociación aprobada |
|---|---|---|---|---|---|---|---|
| ivanna0407 | [https://github.com/Alxsoool/apolitos_AMR-/blob/main/participantes/_plantilla/Compromiso_Ivanna_Mart%C3%ADnez_de_Alba.md] | [AR10] | [MS05] | [K1 Y propio] | [6–8 h] | Prueba del robot | [Sí / Pendiente; revisor] |
| [A00575141-Bash] | [participantes/compromiso-kaizen-miranda-garcia-marquez (1).md]  | [MS02,MS011] | [MS02 / los tres] | [K1, K3 / propio] | [6–8 h] | [Mapeo-prueba] | [Sí / Pendiente; revisor] |
| [@a00574597] | [compromiso-kaizen-massimo-orozco-ocampo.md] | [MS01] | [MS02 / ninguno] | [K1, K3] | [6–8 h] | [Prueba] | [Sí] |
| [@a00574830] | [compromiso-kaizen-alexa-marisol-rodriguez-barajas.md] | [AR01, AR10] | [MS02 / MS10] | [K1, K2, K3 ] | [6–8 h] | [prueba] | [Sí; revisor] |

**Resultado de negociación grupal:** [Puntos de integración; interfaces entre códigos/firmware/sensores/estructura; prioridad si no hay tiempo.]

## 5 · Inventario exhaustivo y especificación de materiales (obligatorio)

### 5.1 Inventario maestro del equipo

Completar **cada recurso requerido**: estructura, electrónica, actuadores, sensores, herramientas, consumibles, instrumentos, software, datos, red, espacios de ensayo y elementos de seguridad. Añadir filas sin límite.

| ID | Categoría | Material o recurso (especificación exacta: modelo, medida, versión o característica) | Cantidad requerida + unidad | Cantidad confirmada | Fuente/proveedor o dueño | Ubicación física o ruta digital | Responsable | Estado (disponible/reservado/falta) | Alternativa compatible | Día requerido |
|---|---|---|---|---|---|---|---|---|---|---|
| MAT-001 | [AMR] | [myAGV2023, accesorios] | [1ud.] | [1] | [LNA] | [EIC] | [@CamiloDuque] | [DIsponible] | [Arismendi] | [D2] |
| MAT-002 | [Zona de pruebas] | [Pista; dimensiones y configuración] | [1ud.] | [1] | [LNA] | [EIC] | [Camilo René Duque Becerra] | [Disponible] | [Arismendi] | [D2] |

También disponible el archivo [`datos/inventario_materiales.csv`](../../datos/inventario_materiales.csv) para registrar muchos materiales sin agrandar esta tabla.

### 5.2 Lista de cotejo específica por plataforma (elegir solo la misión asignada)

| Misión | Revisar y especificar (marca/modelo/cantidad reales) |
|---|---|
| M01 · AMR ROS 2 | Base AMR y baterías/cargador, computador y distribución ROS 2/paquetes, workspace y repositorio base, sensores (p. ej. lidar/odometría), mapa y TF/localización, RViz/Nav2 si aplica, red de comunicación, estaciones/marcadores, área de navegación acordonada, instrumento de medida y paro seguro. |

**Enlaces a fichas técnicas / instrucciones de conexión, fabricación y seguridad:** https://docs.elephantrobotics.com/docs/myagv_jn23_en/1-ProductIntroduction/

### 5.3 Riesgos de recursos y abastecimiento

| Bloqueante | A qué alcance afecta | Solución prevista / fecha y responsable | Impacto si no se resuelve |
|---|---|---|---|
| [Teclado] | [Simulación y programación] | [Obtener un repuesto - Miranda - 27/10/2026] | [Simulación y compilación fallida] |

**Materiales completos para ejecutar el Día 2:**   Parcial  **Confirmado por:** [docente y responsable equipo] a [fecha/hora].

## 6 · Kata 0 — exploración técnica de arranque (100–160 min)

| Integrante/alcance | Pregunta técnica | Mini-prueba o prototipo de exploración | Resultado o error observado | Evidencia enlazada | Acción necesaria antes de D2 |
|---|---|---|---|---|---|
| ivanna0407 | Que necesita el robot para alinearse a un punto | revisar que sensores tiene y como leerlos |Pude ver imagenes de la cámara y tomar distancias de los marcadores |  |
| [@a00575141-bash] | [Por qué la cámara no detecta los arucos] | [Calibrar cámara] | [Detecta algunos] |
| [@A00574830] | [Conexión al AMR] | [Investigación técnica] | [Documentación] | [Descargar software] |
| [@A00574597] | [Conexión al AMR] | [Investigación técnica] | [Documentación] | [NA]| [Descargar software] |

**Integración entre subequipos:** [Qué interfaz se dejó validada: alimentación, dimensiones, tópicos, salida sensorial, etc.]

## 7 · Cierre: contrato técnico y puerta de salida E1 (160–180 min)

- [si] El objetivo colectivo tiene condición de éxito verificable.
- [si] Cada estudiante depositó **su kit Markdown original** en `participantes/<alias>/compromiso.md`.
- [si] Cada estudiante completó [E1 personal](../../participantes/_plantilla/dias/E1.md) y definió frontera, evidencia y alcance negociado.
- [si] El inventario está **completo** y cada recurso indica cantidad, especificación, disponibilidad y responsable.
- [si] Se asignó **dōjō específico** con edificio, salón/taller, horarios, supervisión y autorización.
- [si] Se inspeccionaron riesgos, paro y condiciones de seguridad de la plataforma.
- [si] Se identificaron dependencias y bloqueos del Día 2; están bajo control o se ajustó la misión.
- [si] El profesor aprobó el alcance y la seguridad, o registró observaciones y una alternativa viable.

**Estado del gate:** [APROBADO].

**Condiciones, responsables, fecha y próxima decisión:** [ 27/10/2026]

**Revisor docente:** [ ... ] · **Enlace a commit/PR:** [ ... ]

**Criterio mínimo E1:** existe un contrato de misión y frontera individual, hay evidencia del punto de partida, un inventario verificable y un espacio de trabajo autorizado. La ausencia de algún material crítico NO debe esconderse.


