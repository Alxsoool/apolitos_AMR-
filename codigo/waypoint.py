# Abre Nav2 (map_server + AMCL) con TU mapa y RViz, todo con un solo comando:
#   ros2 launch mapa_y_rviz.launch.py
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

# ============================================================
# CONFIGURACION: escribe aqui la ruta de tu mapa
# ============================================================
RUTA_MAPA = os.path.expanduser('~/maps/map.yaml')   # <-- cambia esto

# (Opcional) archivo de parametros de Nav2 propio del myAGV.
# Dejalo en None para usar el que trae nav2_bringup por defecto.
RUTA_PARAMS = None
# ============================================================


def generate_launch_description():
    nav2_dir = get_package_share_directory('nav2_bringup')
    launch_dir = os.path.join(nav2_dir, 'launch')

    argumentos_nav2 = {
        'map': RUTA_MAPA,
        'use_sim_time': 'false',
    }
    if RUTA_PARAMS:
        argumentos_nav2['params_file'] = RUTA_PARAMS

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_dir, 'bringup_launch.py')),
        launch_arguments=argumentos_nav2.items())

    rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_dir, 'rviz_launch.py')))

    return LaunchDescription([nav2, rviz])


if __name__ == '__main__':
    main()
