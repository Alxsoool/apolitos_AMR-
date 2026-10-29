# Lee la posición del robot respecto al MAPA (no a la odometría)
import math
import rclpy
from rclpy.node import Node
from rclpy.time import Time
from tf2_ros import Buffer, TransformListener, TransformException


class LectorCoordenadasMapa(Node):
    def __init__(self):
        super().__init__('lector_coordenadas_mapa_node')

        # Frames: 'map' lo publica AMCL (necesita el mapa .yaml cargado por Nav2)
        self.frame_mapa = 'map'
        self.frame_robot = 'base_link'  # en algunos robots es 'base_footprint'

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.timer = self.create_timer(0.5, self.leer_pose)
        self.get_logger().info('Esperando transformada map -> base_link...')

    def leer_pose(self):
        try:
            t = self.tf_buffer.lookup_transform(
                self.frame_mapa, self.frame_robot, Time())
        except TransformException as e:
            self.get_logger().warn(
                f'Aún no hay transformada map->{self.frame_robot}: {e}',
                throttle_duration_sec=2.0)
            return

        x = t.transform.translation.x
        y = t.transform.translation.y
        q = t.transform.rotation

        # Cuaternión -> yaw
        siny_cosp = 2.0 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        yaw = math.atan2(siny_cosp, cosy_cosp)

        self.get_logger().info(
            f'En el mapa -> X: {x:.2f} m | Y: {y:.2f} m | '
            f'Ángulo: {math.degrees(yaw):.1f}°')


def main():
    rclpy.init()
    nodo = LectorCoordenadasMapa()
    try:
        rclpy.spin(nodo)
    except KeyboardInterrupt:
        pass
    finally:
        nodo.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
