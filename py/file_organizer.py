import os
import shutil
import pyttsx3 as pt
from tkinter.filedialog import *


path = askdirectory()
files = os.listdir(path) #to get the list of file name

for file in files:
    filename, extension = os.path.splitext(file) #split file type 
    extension = extension[1:] #remove . from file extension

    if os.path.exists(path + '/' +extension):
        shutil.move(path + '/' + file, path+ '/' +extension +'/'+file)
    else:
        os.makedirs(path+ '/' + extension)
        shutil.move(path + '/' + file, path+ '/' +extension +'/'+file)

    