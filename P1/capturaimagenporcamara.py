import cv2
import os

def capture_photos_manual(output_dir, num_photos=10):
    # Verifica si el directorio de salida existe, si no, lo crea
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Inicia la captura de video desde la cámara
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("No se pudo acceder a la cámara.")
        return

    photo_count = 0

    print(f"Presiona 's' para capturar una foto, 'q' para salir.")
    
    while True:
        ret, frame = cap.read()

        if not ret:
            print("No se pudo capturar la imagen.")
            break

        # Muestra la imagen en una ventana
        cv2.putText(frame, f"Fotos capturadas: {photo_count}/{num_photos}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Capture Photo', frame)

        key = cv2.waitKey(1) & 0xFF

        # Presiona 's' para capturar una foto
        if key == ord('s'):
            if photo_count < num_photos:
                photo_filename = os.path.join(output_dir, f"photo_{photo_count + 1}.jpg")
                cv2.imwrite(photo_filename, frame)
                print(f"Foto {photo_count + 1} guardada en {photo_filename}")
                photo_count += 1
            else:
                print("Se ha alcanzado el número máximo de fotos.")

        # Presiona 'q' para salir
        if key == ord('q'):
            print("Saliendo del modo de captura.")
            break

        # Detiene cuando se capturan todas las fotos
        if photo_count >= num_photos:
            print("Se han capturado todas las fotos.")
            break

    # Libera la cámara y cierra las ventanas
    cap.release()
    cv2.destroyAllWindows()

# Directorio donde se guardarán las fotos
output_directory = "fotos_capturadas_manual"

# Llama a la función para capturar 10 fotos manualmente
capture_photos_manual(output_directory)
