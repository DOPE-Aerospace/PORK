from imageai.Detection import ObjectDetection
from lib import rpi_logger as rpi
import os
import cv2

execution_path = os.getcwd()
logger = rpi.rpi_logger()

# Inizializza il detector
detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath("../models/tiny-yolov3.pt")
detector.loadModel()

# Avvia la cattura video dalla webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Legge un frame dalla webcam
    ret, frame = video_capture.read()
    if not ret:
        break

    # Rileva gli oggetti nel frame
    detections = detector.detectObjectsFromImage(input_image=frame, minimum_percentage_probability=5)

    # Disegna i box intorno agli oggetti rilevati
    for eachObject in detections:
        name = eachObject["name"]
        percentage_probability = eachObject["percentage_probability"]
        box_points = eachObject["box_points"]
        print(name, ":", percentage_probability, ":", box_points)
        logger.log_data(name)

        # Disegna il box intorno all'oggetto
        cv2.rectangle(frame, (box_points[0], box_points[1]), (box_points[2], box_points[3]), (255, 0, 0), 2)
        cv2.putText(frame, name, (box_points[0], box_points[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Mostra il frame con i box intorno agli oggetti rilevati
    cv2.imshow('Object Detection', frame)

    # Interrompe il loop se viene premuto 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilascia le risorse
video_capture.release()
cv2.destroyAllWindows()
"""
"""
from imageai.Detection import ObjectDetection
from lib import rpi_logger as rpi
import os
import cv2

execution_path = os.getcwd()
logger = rpi.rpi_logger()

# Inizializza il detector
detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath("../models/tiny-yolov3.pt")
detector.loadModel()

# Avvia la cattura video dalla webcam
video_capture = cv2.VideoCapture(0)

# Dizionario per tenere traccia delle persone già rilevate e dei loro identificativi
identified_persons = {}

while True:
    # Legge un frame dalla webcam
    ret, frame = video_capture.read()
    if not ret:
        break

    # Rileva gli oggetti nel frame
    detections = detector.detectObjectsFromImage(input_image=frame, minimum_percentage_probability=5)

    # Disegna i box intorno agli oggetti rilevati
    for eachObject in detections:
        name = eachObject["name"]
        percentage_probability = eachObject["percentage_probability"]
        box_points = eachObject["box_points"]
        
        # Verifica se l'oggetto rilevato è una persona
        if name == "person":
            # Calcola un identificativo unico per la persona
            person_id = hash(tuple(box_points))

            # Controlla se questa persona è stata già identificata
            if person_id in identified_persons:
                # Se la persona è già stata identificata, usa il suo identificativo precedente
                name = identified_persons[person_id]
            else:
                # Se la persona è nuova, genera un nuovo identificativo e memorizzalo
                name = f"person_{len(identified_persons) + 1}"
                identified_persons[person_id] = name
                
        print(name, ":", percentage_probability, ":", box_points)
        logger.log_data(name)

        # Disegna il box intorno all'oggetto
        cv2.rectangle(frame, (box_points[0], box_points[1]), (box_points[2], box_points[3]), (255, 0, 0), 2)
        cv2.putText(frame, name, (box_points[0], box_points[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Mostra il frame con i box intorno agli oggetti rilevati
    cv2.imshow('Object Detection', frame)

    # Interrompe il loop se viene premuto 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilascia le risorse
video_capture.release()
cv2.destroyAllWindows()












