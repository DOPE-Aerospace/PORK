import time
from picamera import PiCamera

def scatta_foto(filename):
    camera = PiCamera()
    camera.resolution = (1024, 768)  # Imposta la risoluzione
    #camera.start_preview()  # Avvia l'anteprima
    time.sleep(2)  # Attendi un paio di secondi per permettere alla fotocamera di regolare le impostazioni
    camera.capture(filename)  # Scatta la foto
    #camera.stop_preview()  # Ferma l'anteprima
    camera.close()  # Chiudi la fotocamera

# Utilizzo
scatta_foto('foto.jpg')
