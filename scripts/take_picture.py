import time
from picamera2 import Picamera2

def take_photo(filename):
    picam2 = Picamera2()
    camera_config = picam2.create_still_configuration(main={"size": (4608, 2592)})
    picam2.configure(camera_config)
    picam2.start()
    picam2.capture_file(filename)  # Take the photo
    picam2.close()  # Close the camera

def take_photos_interval(filename_template, interval, num_photos):
    for i in range(num_photos):
        filename = filename_template.format(i)
        take_photo(filename)
        time.sleep(interval)

# Usage: take a photo every 20 seconds, for a total of 5 photos
take_photos_interval('frame_{}.jpg', 20, 5)
