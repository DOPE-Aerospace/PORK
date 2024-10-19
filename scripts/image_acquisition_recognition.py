## Libraries ##

# Default libraries
import os
import cv2
from PIL import Image

# Custom libraries
from lib import rpi_logger as rpi

# Raspberry pi and AI libraries
from picamera2 import Picamera2
from libcamera import controls
from imageai.Detection import ObjectDetection

################################################

## Const Variables ##

# Inizializza il detector
def startDetector():
    detector = ObjectDetection()
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath("../models/tiny-yolov3.pt")
    detector.loadModel()
    return detector

# Inizializza la camera
def startPICamera():
    camera = Picamera2()
    camera_config = camera.create_still_configuration(main={"size": (4608, 2592)})
    camera.configure(camera_config)
    camera.start() 
    camera.set_controls({"AfMode": controls.AfModeEnum.Continuous, "AfSpeed": controls.AfSpeedEnum.Fast})   
    return camera

# Inizializza il sistema di log
def startLogger():
    return rpi.rpi_logger()

# Recupera il numero corrente di elementi nella directory "frames"
def currentCounterInDirectory():
    framesPath = os.path.join(os.getcwd(), "..", "frames")
    count = 0
    while True:
        if f"frames_{count}.jpg" in framesPath:
            count += 1
        else:
            return count
        

def main ():
    detector = startDetector()
    camera = startPICamera()
    logger = startLogger()
    counter = currentCounterInDirectory()

    while True:
        photo = Image.fromarray(camera.capture_array())

        print("Photo acquired")

        print("Starting detection")
        
        detections = detector.detectObjectsFromImage(input_image = photo, minimum_percentage_probability=5)

        print("Starting to show objects in picture")

        for eachObject in detections:
            name = eachObject["name"]
            percentage_probability = eachObject["percentage_probability"]
            box_points = eachObject["box_points"]
            print(name, ":", percentage_probability, ":", box_points)
            logger.log_data(name)
        
        cv2.rectangle(photo, (box_points[0], box_points[1]), (box_points[2], box_points[3]), (255, 0, 0), 2)
        cv2.putText(photo, name, (box_points[0], box_points[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        cv2.imshow("Object Detection PI", photo)
        cv2.imwrite(f"frame_{counter}.jpg", photo)

        print("New image in output folder")

        counter += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


main()
