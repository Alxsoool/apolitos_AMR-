# Protocolo de pruebas del equipo

**Alcance y versión:** [...]  
**Métrica primaria (unidad):** [...]  
**Definición de éxito/fallo:** [...]  
**Condiciones controladas:** pista 1, batería cargada, conectado al monitor para ver que es lo que hace
**Procedimiento:** Verificar batería del robot, prender odometría y lidar 
**Número de ensayos:** de 2 a 3 
**Variable modificada:** Velocidad, método de navegación, mapa
**Criterio de seguridad y aborto:** En caso de que los movimientos no sean predecibles utilizar ctrl+c en el teclado

## Dos ciclos Kaizen
### Ciclo 1 · Día 3
- Línea base: Poder ejecutar un primer nodo de navegación de velocidad continua
- Hipótesis: El robot debe poder navegar de manera más eficiente autónomamente que manualmente
- Cambio: Método de navegación
- Resultados comparables: Qué tan rápido o eficiente fue en sus rutas
- Conclusión: Debemos revisar los nodos que se ejecutan y sis errores 

### Ciclo 2 · Día 4
- Nueva línea base: Navegar a base de puntos
- Hipótesis:Si al robot le damos un número de puntos, debe poder navegar de manera autonoma y sin intervención de nosotros
- Cambio:Número y ubicación de los puntos (si es necesario)
- Resultados comparables:Cuántos puntos pudo alcanzar el robot 
- Conclusión:debemos revisar la ubicación de los puntos y que tanto se puede acercar el robot a las paredes 

Registra observaciones en `datos/ensayos.csv`; no inventar resultados ni eliminar corridas desfavorables.
