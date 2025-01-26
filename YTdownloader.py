# daniel gregorio
# 10.31.23
# YTdownloader app

# Updated 01.25.25

import os
import tkinter
from yt_dlp import YoutubeDL
import customtkinter

# function to download audio
def download_audio():
    ytLink = url.get()
    try:
        options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'YTD_Audios/%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],  # Attach progress hook
        }
        with YoutubeDL(options) as ydl:
            info_dict = ydl.extract_info(ytLink, download=True)
            video_title.configure(text=f"{info_dict['title']} Downloaded", text_color="green")
    except Exception as e:
        video_title.configure(text=f"Downloading Error: {e}", text_color="red")
    url.delete(0, 'end')
    url.insert(0, "")

# function to download video
def download_video():
    ytLink = url.get()
    try:
        options = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': 'YTD_videos/%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],  # Attach progress hook
        }
        with YoutubeDL(options) as ydl:
            info_dict = ydl.extract_info(ytLink, download=True)
            video_title.configure(text=f"{info_dict['title']} Downloaded", text_color="green")
    except Exception as e:
        video_title.configure(text=f"Downloading Error: {e}", text_color="red")
    url.delete(0, 'end')
    url.insert(0, "")

# progress hook function
def progress_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes', d.get('total_bytes_estimate', 0))
        downloaded_bytes = d.get('downloaded_bytes', 0)
        if total_bytes > 0:
            percentage = downloaded_bytes / total_bytes * 100
            prog_percent.configure(text=f"{int(percentage)}%")
            prog_bar.set(percentage / 100)
            prog_percent.update()

# Settings for the app
customtkinter.set_appearance_mode("system")
app = customtkinter.CTk()
app.geometry("600x400")
app.title("YTdownloader")

# title with the name of the app
title = customtkinter.CTkLabel(app, text="YTdownloader",
                               font=('Helvetica', 18, 'bold'))
title.pack(padx=10, pady=5)

# header letting the user know to enter a link in the textbox
header = customtkinter.CTkLabel(app, text="Enter YouTube Link")
header.pack(padx=10, pady=10)

# textbox that allows the user to enter a link to a YouTube video
video_url = tkinter.StringVar()
url = customtkinter.CTkEntry(app, width=450, height=40,
                             textvariable=video_url)
url.pack(padx=10, pady=10)

# will display the title of the video from the user's link
video_title = customtkinter.CTkLabel(app, text="")
video_title.pack(padx=10, pady=10)

# progress percentage
prog_percent = customtkinter.CTkLabel(app, text="0%")
prog_percent.pack(padx=10, pady=10)

# progress bar
prog_bar = customtkinter.CTkProgressBar(app, width=400)
prog_bar.set(0)
prog_bar.pack(padx=10, pady=10)

# button to download as MP3
audio_download = customtkinter.CTkButton(app, text="Download MP3",
                                         command=download_audio, fg_color="blue",
                                         text_color="white")
audio_download.pack(padx=10, pady=10)

# button to download as MP4
video_download = customtkinter.CTkButton(app, text="Download MP4",
                                         command=download_video, fg_color="red",
                                         text_color="white")
video_download.pack(padx=10, pady=10)

# run the app
app.mainloop()