# imports
import math
import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult

# ============================================================
# CONFIGURACIÓN: edita aquí tus coordenadas (frame 'map')
# ============================================================
META_X = 2.0      # metros
META_Y = 1.5      # metros
META_YAW = 1.57   # radianes (1.57 ≈ 90°)

# Pose inicial del robot en el mapa (para no usar "2D Pose Estimate" en RViz)
USAR_POSE_INICIAL = True
INICIO_X = 0.0
INICIO_Y = 0.0
INICIO_YAW = 0.0
# ============================================================


def crear_pose(navigator, x, y, yaw):
    """Crea un PoseStamped en el frame 'map' a partir de x, y y yaw (rad)."""
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()
    pose.pose.position.x = x
    pose.pose.position.y = y
    # Yaw -> cuaternión (solo rotación en Z)
    pose.pose.orientation.z = math.sin(yaw / 2.0)
    pose.pose.orientation.w = math.cos(yaw / 2.0)
    return pose


def main():
    rclpy.init()
    navigator = BasicNavigator()

    if USAR_POSE_INICIAL:
        navigator.setInitialPose(
            crear_pose(navigator, INICIO_X, INICIO_Y, INICIO_YAW))

    # Espera a que AMCL y Nav2 estén listos
    navigator.waitUntilNav2Active()

    meta = crear_pose(navigator, META_X, META_Y, META_YAW)
    navigator.get_logger().info(
        f'Yendo a x={META_X}, y={META_Y}, yaw={META_YAW}')
    navigator.goToPose(meta)

    # Mientras navega, mostrar la distancia restante
    while not navigator.isTaskComplete():
        feedback = navigator.getFeedback()
        if feedback:
            navigator.get_logger().info(
                f'Distancia restante: {feedback.distance_remaining:.2f} m',
                throttle_duration_sec=1.0)

    resultado = navigator.getResult()
    if resultado == TaskResult.SUCCEEDED:
        navigator.get_logger().info('¡Llegó a la meta!')
    elif resultado == TaskResult.CANCELED:
        navigator.get_logger().warn('Navegación cancelada')
    else:
        navigator.get_logger().error('Falló la navegación')

    navigator.lifecycleShutdown()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
