import cv2
import numpy as np

# se carga la imagen 
image = cv2.imread("img3.jpeg", 0)
# cargamos el video
video = cv2.VideoCapture("video.mp4")

# obtener el número total de Fotogramas del video, devuelve un numero
TotalFotogramas = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
# Obtener la velocidad de fotogramas
fps = int(video.get(cv2.CAP_PROP_FPS))

# Contador para llevar el registro del segundo actual
contador = 0
limite = 0.8
def buscar_imagen_recursivo(video, image, contador, limite, fps):
    ret, fotograma = video.read()
    if not ret:
        return
    # Convertir el fotograma a escala de grises
    gray = cv2.cvtColor(fotograma, cv2.COLOR_BGR2GRAY)
    # Buscar la imagen en el fotograma
    res = cv2.matchTemplate(gray, image, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= limite)
    print("Buscando en el Frame " + str(contador))
    if len(loc[0]) > 0:
        print("\nEncontrado en el Frame "+str(contador))
        if contador > fps*60:#si es mayor al numero de fotogramas por minuto
            aux = contador // fps
            print("La imagen se encontró en el minuto "+str(int(aux//60)) +" segundo " + str(aux % 60))
        else:
            print("La imagen se encontró en el segundo "+str(int(contador//fps)))
        return
    else:
        buscar_imagen_recursivo(video, image, contador+1, limite, fps)


buscar_imagen_recursivo(video, image, contador, limite, fps)
# Si no se encontró la imagen
if contador == TotalFotogramas:
    print("La imagen no se encontró en el video")

# Liberar el video
video.release()