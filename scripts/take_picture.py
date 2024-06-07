import time
import os
from picamera2 import Picamera2

# Define the directory to save the frames
frames_dir = os.path.join("..", "frames")

# Create the directory if it doesn't exist
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

def take_photo(filename):
    camera = Picamera2()
    camera_config = camera.create_still_configuration(main={"size": (4608, 2592)})
    camera.configure(camera_config)
    camera.start()
    camera.capture_file(filename)  # Take the photo
    camera.close()  # Close the camera

def take_photos_interval(filename_template, interval, num_photos):
    for i in range(num_photos):
        filename = os.path.join(frames_dir, filename_template.format(i))
        take_photo(filename)
        time.sleep(interval)

# Usage: take a photo every 20 seconds, for a total of 5 photos
take_photos_interval('frames_{}.jpg', 20, 5)
