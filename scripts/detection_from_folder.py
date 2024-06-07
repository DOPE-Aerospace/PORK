from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath("./models/tiny-yolov3.pt")
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "./input/drone1.jpeg"), output_image_path=os.path.join(execution_path , "./output/drone1_output.jpg"), minimum_percentage_probability=1)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
    print("--------------------------------")