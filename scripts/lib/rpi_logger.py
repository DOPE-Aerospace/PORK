import os,time,csv
from datetime import datetime


log_path = ""
counter = 0


#function that initializes log file for current flight session
def log_init():
    global log_path,counter
    log_path = os.path.join(os.getcwd(), "..", "log")
    counter = 1
    while True:
        if f"flight_{counter}.csv" in os.listdir(log_path):
            counter += 1
        else: 
            attributes=["detection","time"]
            with open(os.path.join(log_path, f"flight_{counter}.csv"), "w") as log_file:
                csv_writer = csv.writer(log_file)
                csv_writer.writerow(attributes)
                break


#function that logs object detection to current flight session log file
def log_data():
    global log_path
    with open(os.path.join(log_path, f"flight_{counter}.csv"), "a") as log_file:
        csv_writer = csv.writer(log_file)
        #converting time to readable format
        current_time= datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d  %H:%M:%S')
        csv_writer.writerow(["object", current_time])        