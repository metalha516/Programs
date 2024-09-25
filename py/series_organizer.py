import os 
import shutil
from tkinter.filedialog import *
video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf", ".mkv")
prefix = askdirectory()
address = input("Enter the series name : ").lower()
main_address = prefix+'/'+address
os.makedirs(main_address)
os.chdir(prefix)
def is_series(file):
    name,ext = os.path.splitext(file)
    name = name.lower()
    return (ext in video) and address in name
for file in os.listdir():
    if is_series(file):
        print(file)
        shutil.move(file, main_address)
