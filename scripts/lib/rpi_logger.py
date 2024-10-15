import os,time,csv
from datetime import datetime
'''
This class is used to log data to a csv file, it creates a new csv file 
for each flight and logs the objects along with the timestamp of the detection.
'''
class rpi_logger:
    '''
    The init creates a new csv file with a progressive numbering and the header of the csv file.
    '''
    def __init__(self):
        self.log_path = os.path.join(os.getcwd(), "..", "log")
        if not os.path.isdir(self.log_path):
            os.mkdir(self.log_path)
        self.list=[]
        count = 0
        while True:
            if f"flight_{count}.csv" in os.listdir(self.log_path):
                count += 1
            else:
                self.counter=count
                head=("detection","date","time")
                with open(os.path.join(self.log_path, f"flight_{self.counter}.csv"), "w") as log_file:
                    csv_writer = csv.writer(log_file)
                    csv_writer.writerow(head)
                break
    '''
    This function is used to log data to the previously created csv file, it accepts as argument
    the name of the object that was detected.
    '''
    def log_data(self, obj_name:str):
        with open(os.path.join(self.log_path, f"flight_{self.counter}.csv"), "a") as log_file:
            csv_writer = csv.writer(log_file)
            current_time= datetime.fromtimestamp(time.time())
            date=current_time.strftime('%Y-%m-%d')
            time_str=current_time.strftime('%H-%M-%S')
            csv_writer.writerow((obj_name,date,time_str))
            self.list.append((obj_name,date,time_str))
