# daniel gregorio
# 10.31.23
# YTdownloader app

import os
import tkinter

import customtkinter
from pytube import YouTube


def downloadVideo():
    try:
        fromYT = YouTube(url=url.get())
        videoTitle.configure(text=fromYT.title)
        video = fromYT.streams.get_highest_resolution()
        video.download(output_path='YTD_videos')
    except:
        videoTitle.configure(text="Downloading Error") 
        
# Settings for the app
app = customtkinter.CTk()
app.geometry("600x400")
app.title("YTdownloader")

title = customtkinter.CTkLabel(app, text="Enter YouTube Link")
title.pack(padx=10,pady=10)

videoURL = tkinter.StringVar()
url = customtkinter.CTkEntry(app, width=300,height=40,textvariable=videoURL)
url.pack()

videoTitle = customtkinter.CTkLabel(app, text="")
videoTitle.pack()

finishedDownload = customtkinter.CTkLabel(app, text="")
finishedDownload.pack()


download = customtkinter.CTkButton(app, text="Download", command=downloadVideo)
download.pack(padx=10,pady=10)

app.mainloop()

# Downloading Logic (will change once UI is compleate)
# while True:
#     toDownload = str(input("Enter the YouTube link\n➜ "))
#     print("Would you like to download MP3 or MP4?")
#     print("Enter [1] for MP3 (Audio Only)")
#     print("Enter [2] for MP4 (Video + Audio)")
#     userInput = int(input("➜ "))
#     fromYT = YouTube(url=toDownload)
#     if userInput == 1:
#         audio = fromYT.streams.get_audio_only()
#         outaudio = audio.download(output_path="YTD_Audios")
#         base, ext = os.path.splitext(outaudio)
#         new_file = base + ".mp3"
#         os.rename(outaudio, new_file)
#     if userInput == 2:
#         video = fromYT.streams.get_highest_resolution()
#         video.download(output_path='YTD_videos')
#     end = str(input("Would you like to download again? (Y/n)"))
#     if end in ['n','N']:
#         break