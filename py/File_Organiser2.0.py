import os
import shutil
download_directory = 'C:/Users/talha/Downloads'
audio_dir = 'C:/Users/talha/Downloads/Audio'
video_dir = 'C:/Users/talha/Downloads/Video'
image_dir = 'C:/Users/talha/Downloads/Images'
exe_dir = 'C:/Users/talha/Downloads/Exe'
pdf_dir = 'C:/Users/talha/Downloads/pdf'
zip_dir = 'C:/Users/talha/Downloads/zip'
html_dir = 'C:/Users/talha/Downloads/HTML'
py_dir = 'C:/Users/talha/Downloads/python'
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf", ".mkv")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

def is_audio(file):
    ext = os.path.splitext(file)[1]
    return ext in audio
def is_video(file):
    ext = os.path.splitext(file)[1]
    return ext in video
def is_img(file):
    ext = os.path.splitext(file)[1]
    return ext in img
def is_exe(file):
    ext = os.path.splitext(file)[1]
    return ext==".exe"
def is_pdf(file):
    ext = os.path.splitext(file)[1]
    return ext==".pdf"
def is_zip(file):
    ext = os.path.splitext(file)[1]
    return ext==".zip"
def is_html(file):
    ext = os.path.splitext(file)[1]
    return ext==".html"
def is_py(file):
    ext = os.path.splitext(file)[1]
    return ext==".py"
def folder_fix(directory):
        os.chdir(directory)
        files = os.listdir()
        for file in files:
            if is_audio(file):
                shutil.move(file, audio_dir)
            elif is_video(file):
                shutil.move(file, video_dir)
            elif is_img(file):
                shutil.move(file, image_dir)
            elif is_exe(file):
                shutil.move(file, exe_dir)
            elif is_pdf(file):
                shutil.move(file, pdf_dir)
            elif is_zip(file):
                shutil.move(file, zip_dir)
            elif is_html(file):
                shutil.move(file, html_dir)
            elif is_py(file):
                shutil.move(file, py_dir)
folder_fix(download_directory)
        

