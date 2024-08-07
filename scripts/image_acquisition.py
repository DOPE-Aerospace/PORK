import time
import os
from picamera2 import Picamera2
from libcamera import controls

def check_counter_frames(frames_path):
    count = 0
    while True:
        # check if the frames_{counter}.jpg exists inside frames directory
        if f"frames_{count}.jpg" in os.listdir(frames_path):
            count += 1
        else:
            return count

def take_photos_interval(frames_path, filename_template, interval, num_photos, counter):
    camera = Picamera2()
    camera_config = camera.create_still_configuration(main={"size": (4608, 2592)})
    camera.configure(camera_config)
    camera.start()
    print(f"Starting frames acquisition...")
    for i in range(num_photos):
        camera.set_controls({"AfMode" : controls.AfModeEnum.Auto})
        print(f"Starting autofocus cycle...")
        camera.autofocus_cycle()
        filename = os.path.join(frames_path, filename_template.format(counter))
        camera.capture_file(filename) # Take the photo
        print(f"frames_{counter}.jpg taken")
        counter += 1
        time.sleep(interval)
    print(f"Acquisition of {num_photos} frames done!")
    camera.close()

def main():
    # Usage:
    # 1) set variables
    interval = 6 # number of seconds between frames
    num_photos = 100 # number of total frames taken 
    # 2) check the counter of the frames
    frames_path = os.path.join(os.getcwd(), "..", "frames")
    count = check_counter_frames(frames_path)
    # 3) take a photo every 20 seconds, for a total of 5 photos
    take_photos_interval(frames_path, 'frames_{}.jpg', interval, num_photos, count)

main()
