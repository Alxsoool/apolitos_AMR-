import cv2
import cv2.aruco as aruco
import numpy as np

# 1. Pipeline de GStreamer para la cámara CSI del myAGV (extraído de la guía)
def gstreamer_pipeline(
    sensor_id=0,
    capture_width=3264,
    capture_height=2464,
    display_width=960,
    display_height=540,
    framerate=21,
    flip_method=0
):
    return (
        f"nvarguscamerasrc sensor-id={sensor_id} ! "
        f"video/x-raw(memory: NVMM), width=(int){capture_width}, height=(int){capture_height}, framerate=(fraction){framerate}/1 ! "
        f"nvvidconv flip-method={flip_method} ! "
        f"video/x-raw, width=(int){display_width}, height=(int){display_height}, format=(string)BGR ! "
        f"videoconvert ! video/x-raw, format=(string)BGR ! "
        f"appsink drop=True max-buffers=1 emit-signals=True"
    )

def main():
    # Abrir la cámara correctamente con GStreamer
    cam = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    assert cam.isOpened(), "Error: La cámara del myAGV falló al abrirse"
    
    # Matriz de calibración y coeficientes provistos en la guía para resolución 960x540[cite: 3]
    camera_matrix = np.array([
        [785.855437, 0.0, 451.670922],
        [0.0, 584.820336, 259.056856],
        [0.0, 0.0, 1.0]
    ])
    dist_coeffs = np.array([0.095135, -0.109279, -0.002513, -0.002418, 0.0])
    
    marker_length = 0.05  # Tamaño real del lado del marcador en metros (cámbialo al tamaño impreso)[cite: 3]
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters()

    print("Iniciando detección de ArUco. Presiona la tecla 'q' en la ventana de video para salir.")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("No se pudo recibir fotograma de la cámara.")
            break
            
        # Mejorar contraste en iluminación irregular (recomendado en la guía)[cite: 3]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        
        corners, ids, rejected = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        
        if ids is not None:
            # Dibujar los marcadores detectados sobre la imagen
            aruco.drawDetectedMarkers(frame, corners, ids)
            
            # Estimar la pose 3D (distancia Z y desplazamiento X/Y)[cite: 3]
            rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, marker_length, camera_matrix, dist_coeffs)
            
            for i, mid in enumerate(ids.flatten()):
                # tvec[i][0] nos da [X, Y, Z] en metros respecto a la cámara[cite: 3]
                x_cm = tvecs[i][0][0] * 100
                y_cm = tvecs[i][0][1] * 100
                z_cm = tvecs[i][0][2] * 100
                
                # Imprimir en consola los datos métricos exactos
                print(f"ID ArUco: {mid} | Distancia frontal (Z): {z_cm:.1f} cm | Offset horizontal (X): {x_cm:.1f} cm")

        cv2.imshow("myAGV ArUco Detection", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
