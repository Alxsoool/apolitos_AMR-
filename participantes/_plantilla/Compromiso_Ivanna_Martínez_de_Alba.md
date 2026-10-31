---
kit: "Kaizen Dōjō 2026 — Compromiso de misión"
version_catalogo: "C2 / 1.1"
participante: "Ivanna Martínez"
equipo: "Apollo10.9"
mision: "M05"
plataforma: "AMR con ROS 2"
territorio_personal: "D · DOMINAR"
frontera_personal: "F1 · INTEGRAR"
validacion_docente: "PENDIENTE"
---

# Mi compromiso Kaizen · 2026

> **Mi desafío:** Entender que es lo que hace moverse al robot y hacer un algoritmo para que el robot tome decisiones de a donde debe moverse

## 1. Mi misión y mi frontera

- **Participante:** Ivanna Martínez
- **Equipo:** Apollo10.9
- **Plataforma:** M05 · AMR con ROS 2
- **Territorio personal:** D · DOMINAR
- **Frontera personal:** F1 · INTEGRAR

**Hoy todavía no puedo:**

Hoy todavía no comprendo completamente como funciona la cámara del robot y como poder hacer que siga una ruta autonoma

**Al finalizar Kaizen Dōjō demostraré que puedo:**

Entender que es lo que toma la cámara y hacer un algoritmo para que el robot tome decisiones

**La evidencia o indicador que utilizaré:**

Lo voy a comprobar con vídeos del robot ejecutando los algoritmos

**Mi motivación:**

_No especificada_

## 2. Alcances y katas seleccionados

Esta es mi propuesta individual dentro de una misión colaborativa. Cada alcance requiere evidencia de contribución propia y negociación de viabilidad.

### 1. AR04 · Enviar y supervisar meta de navegación

- **Tipo:** Preestablecido · catálogo C2
- **Territorio sugerido:** DOMINAR
- **Frontera sugerida:** F2 · DECIDIR
- **Carta:** D1 · AUTONOMOUS SYSTEM
- **Duración estimada:** 3–4 h
- **Resultado esperado / aceptación:** Programa que asigne una meta y confirme éxito/fallo usando la interfaz disponible.
- **Recursos o prerequisitos:** Pila de navegación y localización estables.

**Katas elegidos**

- [ ] Probar objetivo cercano con herramienta de navegación.
- [ ] Codificar envío de meta y lectura de estado.
- [ ] Ensayar llegada y fallo controlado documentando resultado.

**Mi evidencia final:** Vídeo del robot funcionando

**Enlaces a código/CAD/pruebas:** _Agregar enlaces relativos al repositorio_

### 2. AR10 · Incorporar decisión condicionada por percepción

- **Tipo:** Preestablecido · catálogo C2
- **Territorio sugerido:** EXPLORAR
- **Frontera sugerida:** F4 · TRANSFERIR
- **Carta:** E2 · INTELLIGENCE LAB
- **Duración estimada:** 4–5 h
- **Resultado esperado / aceptación:** Robot que decide continuar o cambiar acción usando dato de sensor disponible.
- **Recursos o prerequisitos:** Sensor real o tópico de señal validado y misión base.

**Katas elegidos**

- [ ] Definir evento de percepción y umbral interpretable.
- [ ] Utilizar la cámara y Lidar para identificar arucos y guiar la decisión del robot _(propuesta propia)

**Mi evidencia final:** _Completar al avanzar el proyecto_

**Enlaces a código/CAD/pruebas:** _Agregar enlaces relativos al repositorio_

## 3. Planeación y viabilidad

- **Alcances:** 2 de un máximo de 3
- **Katas:** 5
- **Esfuerzo técnico estimado:** 7–9 horas
- **Disponibilidad orientativa:** 8–10 horas de trabajo técnico dentro de las 15 horas presenciales.
- **Estado:** PENDIENTE DE VALIDACIÓN DOCENTE

## 4. Mi bitácora Kaizen (cinco sesiones)

| Día | Evidencia que registraré | Estado |
|---|---|---|
| D1 · Atreverse | Diagnóstico y pacto de frontera | [ ] |
| D2 · Hacer | Prototipo / primera integración V1 | [ ] |
| D3 · Medir | Ensayo base y ciclo Kaizen 1 | [ ] |
| D4 · Iterar | Ciclo Kaizen 2 y comparación V1–Vn | [ ] |
| D5 · Demostrar | Desafío, evidencia y reflexión | [ ] |

## 5. Mi protocolo de mejora

### Ciclo Kaizen 1

- **Hipótesis:** Un nodo debe ser diferente entre mandar solo velocidades y generar rutas
- **Cambio implementado:** Tipo de nodo y utilización de librerías 
- **Métrica base:** Puntos o que tan correcta es la ruta
- **Resultado:** Nodos con algunos problemas pero llegando a la meta de navegación

### Ciclo Kaizen 2

- **Hipótesis:** La navegación por puntos debe ser más eficiente que manualmente
- **Cambio implementado:** método de navegación
- **Comparación con V1:** Rutinas autónomas pequeñas
- **Aprendizaje:** Es importante asegurar que los puntos no estén demasiado cerca entre ellos o paredes

## 6. Cierre y reflexión

**Antes no podía:** Diagnosticar y comprender completamente la navegación autónoma

**Ahora puedo:** Diagnosticar errores básicos y hacer rutinas de navegación 

**Cómo lo demostré:** haciendo pruebas de rutinas autónomas simples con seguimiento de coordenadas

**Qué intentaría mejorar después:** Aprender más y comprender más del sistema de ROS 

---

_Documento generado localmente con el configurador Kaizen Dōjō 2026 · catálogo C2. El estudiante debe revisar y acordar con el profesor los alcances y condiciones de seguridad antes de operar robots físicos._

**Fuente de catálogo:** https://docs.google.com/spreadsheets/d/1FKxFzoyu9KJb3RlOwB609vliS5hAtmwWFu2G2zG3Ky4/edit
