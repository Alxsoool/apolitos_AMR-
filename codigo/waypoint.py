import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
import math

class AmclCoordinatesLogger(Node):
    def __init__(self):
        super().__init__('amcl_coordinates_logger')
        
        # Suscripción directa al tópico de pose de AMCL (basado en el mapa .yaml)
        self.subscription = self.create_subscription(
            PoseWithCovarianceStamped,
            '/amcl_pose',
            self.pose_callback,
            10
        )
        self.get_logger().info('Escuchando /amcl_pose. Mueve el myAGV en el mapa...')

    def pose_callback(self, msg):
        # Posición cartesiana en metros respecto al origen del archivo .yaml
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        
        # Conversión del cuaternión de orientación a ángulo Yaw (grados)
        q = msg.pose.pose.orientation
        siny_cosp = 2.0 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        yaw_rad = math.atan2(siny_cosp, cosy_cosp)
        yaw_deg = math.degrees(yaw_rad)
        
        # Imprimir coordenadas en consola
        self.get_logger().info(
            f'Posición (Mapa) -> X: {x:.3f} m | Y: {y:.3f} m | Yaw: {yaw_deg:.2f}°'
        )

def main(args=None):
    rclpy.init(args=args)
    node = AmclCoordinatesLogger()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
