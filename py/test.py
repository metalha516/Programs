import os 
from tkinter.filedialog import *
import shutil
path = askdirectory()
files = os.listdir(path)
for file in files:
    file_name,extention = os.path.splitext(file)
    extention = extention[1:]
if os.path.exists(path + '/'+extention):
    shutil.move(path + '/'+file, path+'/'+extention+'/'+file)
else:
    os.makedirs(path+'/'+extention)
    shutil.move(path+'/'+file, path+'/'+extention+'/'+file)
print("succesful")