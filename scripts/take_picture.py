import time
from picamera2 import Picamera2, Preview

def scatta_foto(filename):
    camera = Picamera2()
    #camera.resolution = (1024, 768)  # Imposta la risoluzione
    camera_config = camera.create_preview_configuration()
    camera.configure(camera_config)
    camera.start_preview(Preview.NULL)
    camera.start()
    #camera.start_preview()  # Avvia l'anteprima
    time.sleep(2)  # Attendi un paio di secondi per permettere alla fotocamera di regolare le impostazioni
    camera.capture_file(filename)  # Scatta la foto
    #camera.stop_preview()  # Ferma l'anteprima
    camera.close()  # Chiudi la fotocamera

# Utilizzo
scatta_foto('foto.jpg')
