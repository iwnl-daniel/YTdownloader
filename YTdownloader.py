# daniel gregorio
# 10.31.23
# YTdownloader app

import os
import tkinter

import customtkinter
from pytube import YouTube


# function to download video
def download_video():
    try:
        ytLink = url.get()
        fromYT = YouTube(ytLink)
        video = fromYT.streams.get_highest_resolution()
        video.download(output_path='YTD_videos')
        video_title.configure(text=f'{fromYT.title} Downloaded', text_color="green")
    except:
        video_title.configure(text="Downloading Error", text_color="red")

# function to download audio
def download_audio():
    try:
        ytLink = url.get()
        fromYT = YouTube(ytLink)
        audio = fromYT.streams.get_audio_only()
        outaudio = audio.download(output_path="YTD_Audios")
        base, ext = os.path.splitext(outaudio)
        new_file = base + ".mp3"
        os.rename(outaudio, new_file)
        video_title.configure(text=f'{fromYT.title} Downloaded', text_color="green")
    except:
        video_title.configure(text="Downloading Error", text_color="red")
    
# Settings for the app
app = customtkinter.CTk()
app.geometry("600x400")
app.title("YTdownloader")

title = customtkinter.CTkLabel(app, text="Enter YouTube Link")
title.pack(padx=10,pady=10)

video_url = tkinter.StringVar()
url = customtkinter.CTkEntry(app, placeholder_text="Enter YouTube Link", width=300,height=40, textvariable=video_url)
url.pack()

video_title = customtkinter.CTkLabel(app, text="")
video_title.pack(padx=10,pady=10)

audio_download = customtkinter.CTkButton(app, text="Download MP3", command=download_audio)
audio_download.pack(padx=10,pady=10)

video_download = customtkinter.CTkButton(app, text="Download MP4", command=download_video)
video_download.pack(padx=10,pady=10)

app.mainloop()