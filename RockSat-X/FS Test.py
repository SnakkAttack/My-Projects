
### Libraries ###
import os
from datetime import datetime

class FileStructure:
    
    highest_id = 0
    highest_id_path = {}

    def __init__(self, data_path, folders, subfolders):
        self.data_path = data_path
        self.folders = folders
        self.subfolders = subfolders
        self.ID = 1
        self.current_time = datetime.now().strftime("%m-%d-%Y_%Hhr-%Mmin-%Ssec")

    def create_folders(self):
        os.makedirs(self.data_path, exist_ok=True)
        for folder in self.folders:
            path = os.path.join(self.data_path, folder)
            os.makedirs(path, exist_ok=True)
            if folder in self.subfolders:
                for subfolder in self.subfolders[folder]:
                    subpath = os.path.join(path, subfolder)
                    os.makedirs(subpath, exist_ok=True)
        
        find_highest_id(data_path)

    def write_to_folder(self, folder_name, subfolder_name, data):
        while True:
            file_path = os.path.join(self.data_path, folder_name, subfolder_name, f"{self.ID} {fs.current_time}.txt")
            folder_path = os.path.join(self.data_path, folder_name, subfolder_name)
            if [file for file in os.listdir(folder_path) if file.split(stop_char)[0] == str(self.ID)]:
                print(f"File with ID {self.ID} already exists.")
                self.ID += 1
            else:
                with open(file_path, 'w') as file:
                    file.write(data)
                if fs.highest_id < self.ID:
                    fs.highest_id = self.ID
                    fs.highest_id_path[folder_path] = file_path
                self.ID = 1
                break
        
        find_highest_id(data_path)

### Functions ###
def find_highest_id(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            find_highest_id(item_path)
        else:
            # Check if the file name starts with an ID
            id = item.split(" ")[0]
            if id.isdigit():
                if fs.ID > fs.highest_id:
                    fs.highest_id_path[path] = item_path


### Variables ###
data_path = r"C:\Users\Gage\Desktop\Data"
stop_char = ' '
folders = ["BME680", "9DOF", "MLX90640", "PTC08", "Geiger_Counter", "Flight_Log", "VL53L1X"]
subfolders = {
    "BME680": ["Gas", "Humidity", "Pressure", "Temperature"],
    "9DOF": ["Accelerometer", "Magnetometer", "Gyroscope"]
}
fs = FileStructure(data_path, folders, subfolders)



# Create the folders
fs.create_folders()
fs.write_to_folder('Flight_Log', '', 'Folders have been created\n')

# Creating files and writing the FIRST LINE of data
test_number = str(20)
test_flog = 'Testing'
fs.write_to_folder("BME680", "Temperature", test_number) #Write to a subfolder
fs.write_to_folder('MLX90640', '', test_number) #Write to a folder

#Writing to the file with the highest ID in a given folder
folder_path = os.path.join(data_path, "Flight_Log")
file_path = fs.highest_id_path[folder_path]
with open(file_path, 'a') as file:
    file.write("\nAdditional data")