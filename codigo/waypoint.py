# Herramienta para OBTENER waypoints en el mapa (ROS 2 Galactic).
#
# Dos formas de capturar un punto:
#   1) Enter  -> guarda la pose ACTUAL del robot en el mapa (x, y, yaw).
#                Mueve el robot (teleop) al lugar y presiona Enter.
#   2) Clic   -> con la herramienta "Publish Point" de RViz, haz clic en el
#                mapa. Guarda x, y (yaw queda en 0.0, editalo si lo necesitas).
#
# Comandos en la terminal:
#   Enter = capturar pose del robot | u = deshacer ultimo | l = listar
#   g = guardar en archivo          | q = salir (guarda automaticamente)
import math
import os
import threading

import rclpy
from geometry_msgs.msg import PointStamped
from rclpy.node import Node
from rclpy.time import Time
from tf2_ros import Buffer, TransformListener, TransformException

# ============================================================
# CONFIGURACION
# ============================================================
FRAME_MAPA = 'map'
FRAME_ROBOT = 'base_link'   # si no funciona, prueba 'base_footprint'
ARCHIVO_SALIDA = os.path.expanduser('~/waypoints_capturados.py')
# ============================================================


class CapturadorWaypoints(Node):
    def __init__(self):
        super().__init__('capturador_waypoints')
        self.puntos = []
        self.salir = False

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        # Herramienta "Publish Point" de RViz
        self.create_subscription(
            PointStamped, '/clicked_point', self.clic_callback, 10)

    # ---------- captura ----------
    def clic_callback(self, msg):
        if msg.header.frame_id != FRAME_MAPA:
            self.get_logger().warn(
                f'El clic viene en frame "{msg.header.frame_id}", no "{FRAME_MAPA}". '
                f'Pon el Fixed Frame de RViz en "{FRAME_MAPA}".')
            return
        self.agregar(msg.point.x, msg.point.y, 0.0, origen='clic')

    def capturar_pose_robot(self):
        try:
            t = self.tf_buffer.lookup_transform(FRAME_MAPA, FRAME_ROBOT, Time())
        except TransformException as e:
            print(f'[ERROR] No hay transformada {FRAME_MAPA}->{FRAME_ROBOT}. '
                  f'¿Nav2/AMCL activos y pose inicial puesta? ({e})')
            return
        q = t.transform.rotation
        yaw = math.atan2(2.0 * (q.w * q.z + q.x * q.y),
                         1.0 - 2.0 * (q.y * q.y + q.z * q.z))
        self.agregar(t.transform.translation.x, t.transform.translation.y,
                     math.degrees(yaw), origen='robot')

    def agregar(self, x, y, yaw_deg, origen):
        self.puntos.append({'x': round(x, 2), 'y': round(y, 2),
                            'yaw_deg': round(yaw_deg, 1)})
        n = len(self.puntos)
        p = self.puntos[-1]
        print(f'[P{n} ({origen})] x={p["x"]}  y={p["y"]}  yaw={p["yaw_deg"]}°')

    # ---------- salida ----------
    def formato_lista(self):
        lineas = ['WAYPOINTS_CONFIG = [']
        for i, p in enumerate(self.puntos, start=1):
            lineas.append(
                f'    {{"x": {p["x"]:.2f}, "y": {p["y"]:.2f}, '
                f'"yaw_deg": {p["yaw_deg"]:.1f}}},   # P{i}')
        lineas.append(']')
        return '\n'.join(lineas)

    def guardar(self):
        with open(ARCHIVO_SALIDA, 'w') as f:
            f.write(self.formato_lista() + '\n')
        print(f'[GUARDADO] {ARCHIVO_SALIDA}')

    # ---------- interfaz de teclado (hilo aparte) ----------
    def bucle_teclado(self):
        print(__doc__)
        while not self.salir:
            try:
                cmd = input().strip().lower()
            except EOFError:
                break
            if cmd == '':
                self.capturar_pose_robot()
            elif cmd == 'u':
                if self.puntos:
                    print(f'[DESHECHO] {self.puntos.pop()}')
            elif cmd == 'l':
                print(self.formato_lista())
            elif cmd == 'g':
                self.guardar()
            elif cmd == 'q':
                break
            else:
                print('Comando no valido (Enter, u, l, g, q).')
        self.salir = True


def main():
    rclpy.init()
    nodo = CapturadorWaypoints()

    hilo = threading.Thread(target=nodo.bucle_teclado, daemon=True)
    hilo.start()

    try:
        while rclpy.ok() and not nodo.salir:
            rclpy.spin_once(nodo, timeout_sec=0.1)
    except KeyboardInterrupt:
        pass
    finally:
        if nodo.puntos:
            print('\n' + nodo.formato_lista())
            nodo.guardar()
        nodo.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
