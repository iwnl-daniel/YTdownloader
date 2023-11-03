# daniel gregorio
# 10.31.23
# YTdownloader app

import os
import tkinter

import customtkinter
from pytube import YouTube


# function to download audio
def download_audio():
    try:
        ytLink = url.get()
        fromYT = YouTube(ytLink, on_progress_callback=on_progress)
        audio = fromYT.streams.get_audio_only()
        # outaudio = audio.download(output_path="../../../YTD_Audios")    # For MAC
        outaudio = audio.download(output_path="YTD_Audios")               # For Windows and Local RUN
        base, ext = os.path.splitext(outaudio)
        new_file = base + ".mp3"
        os.rename(outaudio, new_file)
        video_title.configure(text=f'{fromYT.title} Downloaded', text_color="green")
    except:
        video_title.configure(text="Downloading Error", text_color="red")
    url.delete(0, 'end')
    url.insert(0, "")

# function to download video
def download_video():
    try:
        ytLink = url.get()
        fromYT = YouTube(ytLink, on_progress_callback=on_progress)
        video = fromYT.streams.get_highest_resolution()
        # video.download(output_path="../../../YTD_videos")   # For MAC
        video.download(output_path="YTD_videos")              # For Windows and Local RUN
        video_title.configure(text=f'{fromYT.title} Downloaded', text_color="green")
    except:
        video_title.configure(text="Downloading Error", text_color="red")
    url.delete(0, 'end')
    url.insert(0, "")

# function for the progress bar and progress percent
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compleation = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compleation))
    prog_percent.configure(text=f'{per}%')
    prog_percent.update()
    prog_bar.set(float(percentage_of_compleation) / 100)

# Settings for the app
customtkinter.set_appearance_mode("system")
app = customtkinter.CTk()
app.geometry("600x400")
app.title("YTdownloader")

# title with the name of the app
title = customtkinter.CTkLabel(app, text="YTdownloader",
                               font=('Helvetica', 18, 'bold'))
title.pack(padx=10,pady=5)

# header letting the user know to enter a link in the textbox
header = customtkinter.CTkLabel(app, text="Enter YouTube Link")
header.pack(padx=10,pady=10)

# textbox that allows the user to enter a link to a YouTube video
video_url = tkinter.StringVar()
url = customtkinter.CTkEntry(app, width=450,height=40,
                             textvariable=video_url)
url.pack(padx=10,pady=10)

# will display the title of the video from the user's link
video_title = customtkinter.CTkLabel(app, text="")
video_title.pack(padx=10,pady=10)

# progress percentage
prog_percent = customtkinter.CTkLabel(app, text="0%")
prog_percent.pack(padx=10,pady=10)

# progress bar
prog_bar = customtkinter.CTkProgressBar(app, width=400)
prog_bar.set(0)
prog_bar.pack(padx=10,pady=10)

# button to download as MP3
audio_download = customtkinter.CTkButton(app, text="Download MP3",
                                         command=download_audio, fg_color="blue",
                                         text_color="white")
audio_download.pack(padx=10,pady=10)

# button to download as MP4
video_download = customtkinter.CTkButton(app, text="Download MP4",
                                         command=download_video, fg_color="red",
                                         text_color="white")
video_download.pack(padx=10,pady=10)

# run the app
app.mainloop()