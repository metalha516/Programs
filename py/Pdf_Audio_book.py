import PyPDF2
from tkinter.filedialog import *
import pyttsx3
import keyboard

speaker = pyttsx3.init()
path = askopenfilename()
initial = int(input("Enter number of starting page"))
book = open(path, 'rb')
reader = PyPDF2.PdfReader(book)
for i in range(initial, len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
    
