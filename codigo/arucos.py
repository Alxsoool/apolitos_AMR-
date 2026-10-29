import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from ros2_aruco_interfaces.msg import ArucoMarkers  # Ajusta si usas otro paquete de ArUco
import math

class ArucoAligner(Node):
    def __init__(self):
        super().__init__('aruco_aligner')
        
        # Publicador de velocidad para mover el myAGV (cmd_vel)
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # Suscripción al tópico de detección de ArUco
        # (Cambia '/aruco_detections' si tu nodo publica en otro tópico)
        self.subscription = self.create_subscription(
            ArucoMarkers,
            '/aruco_detections',
            self.aruco_callback,
            10
        )
        
        self.get_logger().info('Buscando marcadores ArUco para alinear...')
        
        # ID del marcador ArUco al que te quieres alinear (cámbialo según tu ID)
        self.target_aruco_id = 0 
        
        # Distancia frontal objetivo en metros (ej. detenerse a 35 cm del marcador)
        self.target_distance = 0.35 

    def aruco_callback(self, msg):
        twist = Twist()
        found_target = False
        
        # Buscar el ID específico en la lista de marcadores detectados
        for i, marker_id in enumerate(msg.marker_ids):
            if marker_id == self.target_aruco_id:
                found_target = True
                
                # Obtener la pose del marcador respecto a la cámara
                pose = msg.poses[i]
                
                # Coordenadas cartesianas relativas a la cámara
                x = pose.position.x  # Izquierda (+) / Derecha (-)
                z = pose.position.z  # Distancia frontal en metros
                
                # Orientación (para calcular el ángulo de alineación)
                q = pose.orientation
                siny_cosp = 2.0 * (q.w * q.z + q.x * q.y)
                cosy_cosp = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
                yaw = math.atan2(siny_cosp, cosy_cosp)
                
                # --- CONTROL PROPORCIONAL DE ALINEACIÓN ---
                
                # 1. Control de giro (Angular Z): Centrar el robot frente al ArUco (x deber ser 0)
                angular_speed = -2.0 * x  
                
                # 2. Control de avance (Linear X): Acercarse o alejarse hasta la distancia objetivo
                distance_error = z - self.target_distance
                linear_speed = 0.8 * distance_error
                
                # Limitar velocidades máximas por seguridad del myAGV
                linear_speed = max(min(linear_speed, 0.15), -0.15)
                angular_speed = max(min(angular_speed, 0.5), -0.5)
                
                # Condición de parada (tolerancia muy baja)
                if abs(x) < 0.02 and abs(distance_error) < 0.02 and abs(yaw) < 0.05:
                    self.get_logger().info('¡Alineación completada con éxito!')
                    twist.linear.x = 0.0
                    twist.angular.z = 0.0
                    self.cmd_vel_pub.publish(twist)
                    return

                # Aplicar velocidades
                twist.linear.x = linear_speed
                twist.angular.z = angular_speed
                self.cmd_vel_pub.publish(twist)
                
                self.get_logger().info(
                    f'Alineándose -> Distancia (Z): {z:.2f}m | Desplazamiento (X): {x:.2f}m',
                    throttle_duration_sec=0.5
                )
                break
        
        # Si la cámara deja de ver el marcador temporalmente, el robot se detiene por seguridad
        if not found_target:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.cmd_vel_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = ArucoAligner()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
