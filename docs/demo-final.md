# Demostración Kaizen — Día 5

**Plataforma:** M05 AMR ROS 2 (Elephant Robotics myAGV 2023 Pi)  
**Objetivo técnico de la demostración:** Demostrar el movimiento autónomo del robot myAGV en la pista de pruebas, asegurando la correcta lectura de odometría y navegación.  
**Versión candidata:** V1.0 - Commit final en el repositorio `apolitos_AMR-`

---

## Guion de 90 segundos por estudiante

### @Ivanna0407 (Pruebas y alineación)
1. **Al llegar, yo todavía no podía…** Resolver los fallos de odometría en la ejecución directa del AMR desde la terminal.
2. **Mi alcance y mi principal dificultad fueron…** Alcanzar la meta AR10 (Pruebas del robot y alineación de marcadores); la principal dificultad fue que el robot perdía la odometría al lanzarse por comandos de consola.
3. **Cambié o construí…** Ayudé a reestructurar la estrategia de ejecución migrando las pruebas directas hacia la interfaz gráfica integrada `myagv ui`.
4. **Las pruebas muestran…** Que el AMR logra realizar sus recorridos autónomos sobre la pista manteniendo la estabilidad de sus sensores.
5. **Ahora puedo…** Operar, diagnosticar y verificar el movimiento autónomo de un AMR combinando la lectura de marcadores y la gestión del robot desde su entorno gráfico.

### @a00575141-hash (Seguridad y visión)
1. **Al llegar, yo todavía no podía…** Garantizar que la cámara y los sensores mantuvieran la sincronización con la localización durante el movimiento.
2. **Mi alcance y mi principal dificultad fueron…** Desarrollar MS02/MS11 (Visión y calibración); la dificultad radicaba en los errores de publicación de tópicos de odometría que afectaban las lecturas.
3. **Cambié o construí…** Calibré la cámara, configuré la integración de sensores y validé los límites de seguridad en la pista.
4. **Las pruebas muestran…** Que el sistema detecta el entorno y navega de forma autónoma sin salirse del margen de seguridad establecido.
5. **Ahora puedo…** Calibrar sensores de visión e integrar la cámara con la pila de navegación de un AMR en escenarios reales.

### @a00574597 (Integración)
1. **Al llegar, yo todavía no podía…** Desplegar la pila de navegación sin tropezar con excepciones en la terminal de ROS 2.
2. **Mi alcance y mi principal dificultad fueron…** Cumplir con MS01 (Integración de software); el mayor reto fue aislar el fallo del comando de odometría en la terminal.
3. **Cambié o construí…** Implementé la alternativa de contingencia lanzando y gestionando el sistema a través del backend de `myagv ui`.
4. **Las pruebas muestran…** Un flujo de ejecución continuo y sin bloqueos de software que permite al AMR completar su circuito.
5. **Ahora puedo…** Integrar componentes de software en ROS 2 y aplicar estrategias de *fallback* funcional cuando la CLI presenta errores de entorno.

### @a005748
