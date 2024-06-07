import time
import os
from picamera2 import Picamera2

def check_counter_frames():
    frames_path = os.path.join(os.getcwd(), "..", "frames")
    counter = 0
    while True:
        if f"frames_{count}.jpg" in os.listdir(frames_path):
            count += 1
        else:
            return counter

def take_photo(filename):
    camera = Picamera2()
    camera_config = camera.create_still_configuration(main={"size": (4608, 2592)})
    camera.configure(camera_config)
    camera.start()
    camera.capture_file(filename)  # Take the photo
    camera.close()  # Close the camera

def take_photos_interval(frames_path, filename_template, interval, num_photos, counter):
    for i in range(num_photos):
        filename = os.path.join(frames_path, filename_template.format(counter))
        take_photo(filename)
        time.sleep(interval)

def main():
    # Usage: 
    # 1)check the counter of the frames
    counter = check_counter_frames()
    # 2)take a photo every 20 seconds, for a total of 5 photos
    take_photos_interval('frames_{}.jpg', 20, 5)

main()
