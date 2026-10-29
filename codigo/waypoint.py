import os
import signal
import subprocess
import time

RUTA_MAPA = os.path.expanduser('~/maps/map.yaml')   # <-- cambia esto


def main():
    if not os.path.isfile(RUTA_MAPA):
        print(f'[ERROR] No existe el mapa: {RUTA_MAPA}')
        return

    comando_nav2 = ['ros2', 'launch', 'nav2_bringup', 'bringup_launch.py',
                    f'map:={RUTA_MAPA}', 'use_sim_time:=false']
    comando_rviz = ['ros2', 'launch', 'nav2_bringup', 'rviz_launch.py']

    procesos = []
    try:
        procesos.append(subprocess.Popen(comando_nav2, start_new_session=True))
        time.sleep(3)
        procesos.append(subprocess.Popen(comando_rviz, start_new_session=True))
        print('Todo en marcha. Ctrl+C para cerrar.')
        while all(p.poll() is None for p in procesos):
            time.sleep(0.5)
    except KeyboardInterrupt:
        print('\nCerrando...')
    finally:
        for p in procesos:
            if p.poll() is None:
                os.killpg(os.getpgid(p.pid), signal.SIGINT)
        for p in procesos:
            try:
                p.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(os.getpgid(p.pid), signal.SIGKILL)


if __name__ == '__main__':
    main()
